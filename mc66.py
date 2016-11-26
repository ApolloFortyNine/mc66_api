import socket


class MC66:
  def __init__(self):
    self.fr = b"\x02\x00"
    
  def all_on(self):
    cmd = self.fr + b"\x01\x04\x38\x3F"
    self.send_cmd(cmd)
    return 0

  def all_off(self):
    cmd = self.fr + b"\x01\x04\x39\x40"
    self.send_cmd(cmd)
    return 0

  def power_on(self, zone_number):
    cmd = self.fr + self.conv_zone(zone_number)
    cmd += b"\x04\x20"
    cmd += self.checksum(cmd)
    self.send_cmd(cmd)
    return 0

  def power_off(self, zone_number):
    cmd = self.fr + self.conv_zone(zone_number)
    cmd += b"\x04\x21"
    cmd += self.checksum(cmd)
    self.send_cmd(cmd)
    return 0

  def volume_up(self, zone_number):
    cmd = self.fr + self.conv_zone(zone_number)
    cmd += b"\x04\x09"
    cmd += self.checksum(cmd)
    self.send_cmd(cmd)
    return 0

  def volume_down(self, zone_number):
    cmd = self.fr + self.conv_zone(zone_number)
    cmd += b"\x04\x0A"
    cmd += self.checksum(cmd)
    self.send_cmd(cmd)
    return 0

  def set_input(self, zone_number, chan_number):
    cmd = self.fr + self.conv_zone(zone_number)
    cmd += b"\x04"
    cmd += bytes(chr(chan_number + 2), 'utf-8')
    cmd += self.checksum(cmd)
    self.send_cmd(cmd)
    return 0

  def conv_zone(self, zone_number):
    tmp = bytes(chr(zone_number), 'utf-8')
    return tmp

  def checksum(self, cmd):
    tmp = 0
    for x in cmd:
      tmp += x
    return bytes(chr(tmp), 'utf-8')

  def send_cmd(self, cmd):
    res = socket.getaddrinfo("192.168.0.5", 10006, socket.AF_UNSPEC, socket.SOCK_STREAM)
    af, socktype, proto, canonname, sa = res[0]
    s = socket.socket(af, socktype, proto)
    s.settimeout(1)
    s.connect(sa)
    print(cmd)
    s.send(cmd)
    s.recv(256)
    s.close()

