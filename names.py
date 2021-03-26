from functools import cache
import socket

FILE = "D:\Scripts\ip.txt"

with open(FILE) as file:
    ADDRESSES = file.read().splitlines()

with open(r"D:\\Scripts\\resolve_list.txt", "w") as file:
    for address in ADDRESSES:
        try:
            name = socket.gethostbyaddr(address)
            file.writelines(str(name) + "\n")
        except:
            file.writelines(address + "  " + "not found" + "\n")
