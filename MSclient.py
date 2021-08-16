import socket
import subprocess
import os


def server_program():
    # get the hostname
    host = "bravo.cs.uwindsor.ca"
    port = 8080  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)

    hostname = socket.gethostname()
    print("Server Side Host:")
    print(socket.gethostbyname(hostname))

    print("")
    print("")
    print("||-------Client Server Socket Programming-------||")
    print("socket is listening")  # accept new connection
    print("Bravo - Charlie Connection Established")
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    print("")
    print("|---Bravo Server---|")
    print("Command Log")
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break

        if data.lower() == "bye":
            print("Server Disconnecting")
            break

        print("#" + data)
        print("")
        res = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        conn.send(res.stdout.read().encode())  # send data to the client
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()