# Challenge Statement
![image](https://github.com/user-attachments/assets/2cff37dd-1b51-4c1f-81cf-0307bdbcd4f0)

# Solution
Going through the given `.pcapng` file, we can see that they have some sort of Blind SQL injection and the requests are URL encoded.
![image](https://github.com/user-attachments/assets/d4714b8e-1aa7-49e9-9754-860beb9f4a16)

We can write a Python script to iterate the relevated packet captures and output the exfiltrated data. 
```
import re
from collections import defaultdict
from scapy.all import rdpcap, IP, TCP, Raw
from urllib.parse import unquote, parse_qs
from scapy.layers.http import HTTPRequest, HTTPResponse

# Configuration variables
PCAP_PATH = "challenge.pcapng"
ALLOW_ONLY_PRINTABLE = True

# Regex patterns for parsing SQL-like queries in HTTP payloads
pattern_mid = re.compile(r"ORD\(MID\(\(SELECT.*?\),(\d+),1\)\)", re.IGNORECASE)
pattern_select = re.compile(r"SELECT\s+(.*?)\s+FROM", re.IGNORECASE)
pattern_limit = re.compile(r"LIMIT\s+(\d+),1", re.IGNORECASE)
pattern_field = re.compile(r"CAST\(`?([a-zA-Z_]+)`?\s+AS\s+NCHAR", re.IGNORECASE)


def read_packets(file_path):
    """Load packets from the specified PCAP file."""
    return rdpcap(file_path)


def match_request_response(packets):
    """
    Process packets to match HTTP requests with corresponding responses.
    A session key (combination of IP addresses, ports, and TCP parameters) is used.
    """
    sessions = {}
    for pkt in packets:
        if pkt.haslayer(HTTPRequest):
            try:
                req_path = pkt[HTTPRequest].Path.decode()
                params = parse_qs(unquote(req_path.split("?", 1)[1]))
                sql_query = params.get("query", [None])[0]
                if not sql_query or ">" not in sql_query:
                    continue
                # Split condition and comparison value
                condition_part, cmp_value_str = sql_query.rsplit(">", 1)
                pos_index = int(pattern_mid.search(condition_part).group(1))
                cmp_value = int(cmp_value_str)
            except Exception:
                continue

            key = (
                pkt[IP].src, pkt[IP].dst, pkt[TCP].sport, pkt[TCP].dport, pkt[TCP].ack
            )
            sessions[key] = {
                "condition": condition_part,
                "position": pos_index,
                "cmp_value": cmp_value,
            }
        elif pkt.haslayer(HTTPResponse) and pkt.haslayer(Raw):
            key = (
                pkt[IP].dst, pkt[IP].src, pkt[TCP].dport, pkt[TCP].sport, pkt[TCP].seq
            )
            if key in sessions:
                payload = pkt[Raw].load
                sessions[key]["result_found"] = b"No results found" not in payload
    return sessions


def decode_characters(sessions):
    """
    Build a mapping of SQL expression and character positions to their ASCII range,
    based on query success/failure.
    """
    char_ranges = defaultdict(dict)
    for session in sessions.values():
        if "result_found" not in session:
            continue

        condition_text = session["condition"]
        value = session["cmp_value"]
        pos = session["position"]

        select_match = pattern_select.search(condition_text)
        expression = select_match.group(1).strip() if select_match else condition_text.split("ORD")[0].strip()
        if any(keyword in expression.lower() for keyword in ["char_length", "count"]):
            continue

        limit_match = pattern_limit.search(condition_text)
        key = f"{expression} [LIMIT {limit_match.group(1)},1]" if limit_match else expression

        if pos not in char_ranges[key]:
            # Set initial ASCII range as [0, 255]
            char_ranges[key][pos] = [0, 255]

        if session["result_found"]:
            char_ranges[key][pos][0] = max(char_ranges[key][pos][0], value)
        else:
            char_ranges[key][pos][1] = min(char_ranges[key][pos][1], value)
    return char_ranges


def reconstruct_table(char_ranges):
    """
    Rebuild the table by ordering characters based on their position.
    Row and column identifiers are extracted from the SQL expression.
    """
    table = defaultdict(dict)
    for header, pos_info in char_ranges.items():
        reconstructed = ""
        for _, (min_val, max_val) in sorted(pos_info.items()):
            ascii_char = chr(max_val)
            if ALLOW_ONLY_PRINTABLE and not (32 <= max_val <= 126):
                continue
            reconstructed += ascii_char
        reconstructed = reconstructed.strip()

        limit_info = pattern_limit.search(header)
        field_info = pattern_field.search(header)
        if not limit_info or not field_info:
            continue
        row_id = limit_info.group(1)
        col_name = field_info.group(1)
        table[row_id][col_name] = reconstructed
    return table


def display_table(table):
    """
    Display the reconstructed table in a formatted tabular view.
    Rows are sorted by row number, and columns are shown with headers.
    """
    headers = ["id", "name", "description"]
    # Print a header row
    header_row = f"{'Row':<5}" + "".join(f"{col.capitalize():<20}" for col in headers)
    separator = "-" * len(header_row)
    print("Reconstructed Table:")
    print(separator)
    print(header_row)
    print(separator)
    # Print each row
    for row_key in sorted(table.keys(), key=int):
        row_data = table[row_key]
        row_text = f"{row_key:<5}" + "".join(f"{row_data.get(col, '[missing]'):<20}" for col in headers)
        print(row_text)
    print(separator)


if __name__ == "__main__":
    packets = read_packets(PCAP_PATH)
    sessions = match_request_response(packets)
    ascii_data = decode_characters(sessions)
    reconstructed_table = reconstruct_table(ascii_data)
    display_table(reconstructed_table)
```

Running the code, we obtain the flag.  
![image](https://github.com/user-attachments/assets/526bcb49-4622-476b-9238-245b184c7e0b)


