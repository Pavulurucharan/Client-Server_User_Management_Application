import socket


def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 9993))
        name = input("Enter Your Name: ")
        passphrase = input("Enter passphrase: ")
        name_passphrase = f"{name}:{passphrase}"
        client_socket.send(bytes(name_passphrase, 'utf-8'))
        response = client_socket.recv(1024).decode()
        print(response)  # Print authentication response

        # Handle response for user registration
        registration_response = client_socket.recv(1024).decode()
        print(registration_response)

    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()


if __name__ == "__main__":
    main()
