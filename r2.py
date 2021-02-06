import getpass
import telnetlib

HOST = input("Enter the IP Address of Device: ")
user = input("Enter your GNS3 account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"terminal len 0\n")
tn.write(b"show run\n")
tn.write(b"exit\n")


print(tn.read_all().decode('ascii'))
