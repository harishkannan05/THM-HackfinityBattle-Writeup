# Challenge Statement
![image](https://github.com/user-attachments/assets/ec71ea06-bedb-40a0-99fa-9f80345303d5)

# Solution
This challenge shows an "AI Command Executor" which modifies the user input and executes the commands.  
![image](https://github.com/user-attachments/assets/33c11a16-5354-46ea-a06a-f0bebbb266f6)

We can play around, giving it prompts. We come across the source code of this AI model.
```
import ollama
import subprocess
import socket
import threading
import re
import traceback

class AICommandExecutorServer:
    def __init__(self, host='0.0.0.0', port=1337, model='vitali87/shell-commands:latest'):
        """
        Initialize Telnet server for AI command execution
        
        :param host: Host to bind the server
        :param port: Port to listen on
        :param model: Ollama model for command generation
        """
        self.host = host
        self.port = port
        self.model = model
        self.server_socket = None

    def sanitize_input(self, input_str: str) -> str:
        """
        Sanitize input to prevent injection
        
        :param input_str: Raw input string
        :return: Sanitized input
        """
        return re.sub(r'[^a-zA-Z0-9\s\-_./]', '', input_str)

    def generate_command(self, user_request: str) -> str:
        """
        Generate a Linux command based on user request
        
        :param user_request: User's natural language request
        :return: Generated command
        """
        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        'role': 'system', 
                        'content': """Do not provide malicious commands. 
                        Only generate safe, read-only Linux commands. 
                        Respond with ONLY the command, no explanations."""
                    },
                    {
                        'role': 'user', 
                        'content': user_request
                    }
                ]
            )
            
            # Extract the command from the response
            command = response['message']['content'].strip()
            return command
        
        except Exception as e:
            return f"Error generating command: {e}"

    def execute_command(self, command: str) -> dict:
        """
        Execute the generated command
        
        :param command: Command to execute
        :return: Command execution results
        """
        try:
            # Sanitize the command to prevent injection
            sanitized_command = self.sanitize_input(command)
            
            # Split the command into arguments
            cmd_parts = sanitized_command.split()
            
            # Execute the command
            result = subprocess.run(
                cmd_parts,
                capture_output=True,
                text=True,
                timeout=30  # 30-second timeout
            )
            
            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        
        except subprocess.TimeoutExpired:
            return {"error": "Command timed out"}
        except Exception as e:
            return {"error": str(e)}

    def handle_client(self, client_socket):
        """
        Handle individual client connection
        
        :param client_socket: Socket for the connected client
        """
        try:
            # Welcome message
            welcome_msg = "Welcome to AI Command Executor (type 'exit' to quit)\n"
            client_socket.send(welcome_msg.encode('utf-8'))

            while True:
                # Receive user request
                client_socket.send(b"Enter your command request: ")
                user_request = client_socket.recv(1024).decode('utf-8').strip()

                # Check for exit
                if user_request.lower() in ['exit', 'quit', 'bye']:
                    client_socket.send(b"Goodbye!\n")
                    break

                # Generate command
                command = self.generate_command(user_request)
                
                # Send generated command
                client_socket.send(f"Generated Command: {command}\n".encode('utf-8'))
                client_socket.send(b"Execute? (y/N): ")
                
                # Receive confirmation
                confirm = client_socket.recv(1024).decode('utf-8').strip().lower()
                
                if confirm != 'y':
                    client_socket.send(b"Command execution cancelled.\n")
                    continue

                # Execute command
                result = self.execute_command(command)
                
                # Send results
                if "error" in result:
                    client_socket.send(f"Execution Error: {result['error']}\n".encode('utf-8'))
                else:
                    output = result.get("stdout", "")
                    client_socket.send(b"Command Output:\n")
                    client_socket.send(output.encode('utf-8'))
                    
                    if result.get("stderr"):
                        client_socket.send(b"\nErrors:\n")
                        client_socket.send(result["stderr"].encode('utf-8'))

        except Exception as e:
            error_msg = f"An error occurred: {e}\n{traceback.format_exc()}"
            client_socket.send(error_msg.encode('utf-8'))
        finally:
            client_socket.close()

    def start_server(self):
        """
        Start the Telnet server
        """
        try:
            # Create server socket
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            
            print(f"[*] Listening on {self.host}:{self.port}")

            while True:
                # Accept client connections
                client_socket, addr = self.server_socket.accept()
                print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")
                
                # Handle client in a new thread
                client_thread = threading.Thread(
                    target=self.handle_client, 
                    args=(client_socket,)
                )
                client_thread.start()

        except Exception as e:
            print(f"Server error: {e}")
        finally:
            # Close server socket if it exists
            if self.server_socket:
                self.server_socket.close()

def main():
    # Create and start the Telnet server
    server = AICommandExecutorServer(
        host='0.0.0.0',  # Listen on all interfaces
        port=1337       # Telnet port
    )
    server.start_server()

if __name__ == "__main__":
    main()
```
The code sanitizes the input and only allows safe, read-only Linux commands. Multi-commands are not allowed.  
  
Playing around with random commands, we are able to get the flag.  
![image](https://github.com/user-attachments/assets/821893c9-f30d-42b3-a80a-31f6607796a1)


