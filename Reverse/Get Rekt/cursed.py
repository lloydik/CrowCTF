from binascii import hexlify

flag = "\x11\x10\x19\x36\x3f\x1a\x30\x22\x18\x39\x05\x08\x2c\x0d\x12\x32\x16\x04"
key = "ThisIsKey"
cipher = ""
i = 0
j = 0

while len(flag) - len(key) > len(key):
    key += key

while len(flag) - len(key) > 0:
    key += key[i]
    i += 1

while len(cipher) - len(key) < 0:
    cipher += chr((~ord(flag[j]) | ~ord(key[j])) & (ord(flag[j]) | ord(key[j])))
    j += 1

print(cipher)
