import socket
import sys

res = socket.getaddrinfo("192.168.0.5", 10006, socket.AF_UNSPEC, socket.SOCK_STREAM)
# print(res)
af, socktype, proto, canonname, sa = res[0]
# print(proto)
s = socket.socket(af, socktype, proto)
# s = socket.socket()
s.settimeout(1)
s.connect(sa)
# s.send(b"\x02\x00\x01\x04\x38\x3F")
# out = b"\x02\x00" + b"\x02" + b"\x06" + b"\x00" + b"\x0A"
# out = b"\x02\x00\x02\x04\x21\x29"
# out = b"\x02\x00\x02\x04\x20\x28"
out = b"\x02\x00\x01\x06\x00\x09"
for x in out:
  print(x)
print(out)
s.send(out)
test = s.recv(50)
print(test)
for x in test:
  print(x)
sys.exit()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("192.168.0.5", 10006))
sock.send(b"getversion")

test = sock.recv(500)
