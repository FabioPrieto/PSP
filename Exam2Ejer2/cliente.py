import socket
import time

class SocketClient:
    def __init__(self, initial_host="10.10.30.50", initial_port=2000):
        self.initial_host = initial_host
        self.initial_port = initial_port
        self.next_host = None
        self.next_port = None

    def send_receive(self, host, port, message, buffer_size=1024, ignore_initial=False):
        try:
            # Create socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Connect to server
                s.connect((host, port))

                if ignore_initial:
                    # Receive the initial message and ignore it
                    initial = s.recv(buffer_size).decode()
                    print(f"Initial server message (ignored): {initial}")

                # Send message
                s.send(message.encode())

                # Receive response
                response = s.recv(buffer_size).decode()
                return response
        except Exception as e:
            print(f"Error in communication: {e}")
            return None

    def process_first_response(self, response):
        try:
            parts = response.strip().split('#')
            if len(parts) >= 4 and parts[1] == 'OK':
                self.next_host = parts[2]
                self.next_port = int(parts[3])
                print(f"Next server will be: {self.next_host}:{self.next_port}")
                return True
            return False
        except Exception as e:
            print(f"Error processing first response: {e}")
            return False

    def process_second_response(self, response):
        try:
            parts = response.strip().split('#')
            if len(parts) >= 3 and parts[1] == 'OK':
                return parts[2]
            return None
        except:
            return None

    def execute_protocol(self, nombre, id_value, dni):
        # First server communication
        first_message = f"#PET#{nombre}#{id_value}#"
        print(f"Sending to first server: {first_message}")

        response1 = self.send_receive(self.initial_host, self.initial_port, first_message, ignore_initial=True)
        if not response1:
            return "Failed to communicate with first server"

        print(f"First server response: {response1}")

        if not self.process_first_response(response1):
            return "Invalid response from first server"

        # Add a small delay between requests
        time.sleep(1)

        # Second server communication - also needs to ignore initial message
        second_message = f"#OBT#{nombre}#{dni}#"
        print(f"Sending to second server: {second_message}")

        response2 = self.send_receive(self.next_host, self.next_port, second_message, ignore_initial=True)
        if not response2:
            return "Failed to communicate with second server"

        print(f"Second server response: {response2}")

        codigo = self.process_second_response(response2)
        if codigo is None:
            return "Invalid response from second server"

        return codigo

def main():
    client = SocketClient()

    # Your values
    nombre = "Fabio"
    id_value = "DAM222"
    dni = "44664504E"  # Using the DNI from your output

    result = client.execute_protocol(nombre, id_value, dni)
    print(f"Final result: {result}")

if __name__ == "__main__":
    main()