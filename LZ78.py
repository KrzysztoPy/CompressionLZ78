import binascii

x = bin(int.from_bytes('aa'.encode(), 'big'))

print(x[2:])
