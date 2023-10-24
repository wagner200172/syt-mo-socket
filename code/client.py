import socket
from uttlv import TLV


def client_program():
    host = socket.gethostname()  # as both code is running on the same PC
    port = 9979  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    while True:
        temperature = float(input("Enter temperature: "))  # Get temperature from the user
        humidity = float(input("Enter humidity: "))  # Get humidity from the user

        t = TLV()
        t[0x01] = int(temperature)
        t[0x02] = int(humidity)

        tlv_data = bytes([0x01, 0x02])
        

        client_socket.send(tlv_data)  
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data)  # show in the terminal


if __name__ == '__main__':
    client_program()
