import getpass
import telnetlib

HOST = "192.168.1.71"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
        tn.write(b"show interface status\n")
        tn.write(b"exit\n")

        print(tn.read_all().decode('ascii'))
