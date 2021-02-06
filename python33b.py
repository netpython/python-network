import getpass
import telnetlib

HOST = "192.168.1.92"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user.encode('ascii') + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password.encode('ascii') + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")

for n in range (50,60):
    tn.write("vlan " + str(n).encode('ascii') + "\n")
    tn.write("name Python_VLAN_" + str(n).encode('ascii') + "\n")

tn.write("end\n")
tn.write("wr\n")
tn.write("exit\n")

print(tn.read_all().decode('ascii'))
