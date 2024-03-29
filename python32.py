import getpass
import telnetlib

HOST = "192.168.1.92"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

    tn.write(b"conf t\n")
    tn.write(b"vlan 31\n")
    tn.write(b"name Python_VLAN_31\n")
    tn.write(b"vlan 32\n")
    tn.write(b"name Python_VLAN_32\n")
    tn.write(b"vlan 33\n")
    tn.write(b"name Python_VLAN_33\n")
    tn.write(b"vlan 34\n")
    tn.write(b"name Python_VLAN_34\n")
    tn.write(b"vlan 35\n")
    tn.write(b"name Python_VLAN_35\n")
    tn.write(b"vlan 36\n")
    tn.write(b"name Python_VLAN_36\n")
    tn.write(b"vlan 37\n")
    tn.write(b"name Python_VLAN_37\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode("ascii"))
