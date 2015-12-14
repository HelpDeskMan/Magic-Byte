#!/usr/bin/env python2.7

import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
to = ('sb1.cyberskyline.com', 3050)

for line in open('PrimeNumList.txt'):
    m = '\x78'
    m += struct.pack('>I', int(line))
    m += '\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA'
    m += '\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA'
    print line
    s.sendto(m, to)

print 'receive'
data = s.recv(25)
print data
print 'done'

s.close()
