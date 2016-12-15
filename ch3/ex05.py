# Problem: You have a byte string and need to unpack it into an integer value

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))

x = 94522842520747284487117727783387188

print(x.to_bytes(16, 'big'))
