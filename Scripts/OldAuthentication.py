# Building the Key
key = bytearray([0x41] * 16) # 16 byte key
key[2] = 0x03   # To get 'Q'
key[13] = 0x66  # To get '4'
for i in range(4, 8):
    key[i] = 0x10 ^ 0x52
key[8] = 0x10 ^ 0x52
for i in range(9, 11):
    key[i] = 0x14 ^ 0x52
key[11] = 0x18 ^ 0x52
key[14] = 0x43
key[15] = 0x45

# Building the Username
username = "".join(chr(ord(c) - 2) for c in "elb4rt0pwn")

# Output
print(key.decode('latin1', errors='replace'))
print(username)
