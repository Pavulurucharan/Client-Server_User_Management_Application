import socket

import mysql.connector

PASSPHRASE = "2580"


def register_user(username, password, email):
    try:
        # Establish connection to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="charan123",
            database="python"
        )

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute SQL query to insert user data into the database
        sql = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        val = (username, password, email)
        mycursor.execute(sql, val)

        # Commit changes to the database
        mydb.commit()

        # Close cursor and database connection
        mycursor.close()
        mydb.close()

        return True  # Registration successful
    except mysql.connector.Error as err:
        print("Error:", err)
        return False  # Registration failed


def main():
    print("Welcome to Charan Company")
    server_socket = socket.socket()
    server_socket.bind(('localhost', 9993))
    server_socket.listen(5)
    print("Waiting for Connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        try:
            print("Connected with", client_address, "-", client_socket.recv(1024).decode())
            received_data = client_socket.recv(1024).decode()
            username, passphrase = received_data.split(":")
            if passphrase == PASSPHRASE:
                client_socket.send(bytes("Authentication successful. Welcome!", 'utf-8'))

                # Assuming received_data contains registration details in the format "username:password:email"
                register_data = received_data.split(":")
                if len(register_data) == 3:
                    username, password, email = register_data
                    if register_user(username, password, email):
                        client_socket.send(bytes("User registration successful!", 'utf-8'))
                    else:
                        client_socket.send(bytes("User registration failed!", 'utf-8'))
                else:
                    client_socket.send(bytes("Invalid registration data format!", 'utf-8'))
            else:
                client_socket.send(bytes("Authentication failed. Connection refused.", 'utf-8'))
        except Exception as e:
            print("Error:", e)
        finally:
            client_socket.close()


if __name__ == "__main__":
    main()
