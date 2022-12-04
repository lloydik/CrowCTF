from  binascii                import                                                                                   hexlify

flag                          =                                                                           "##################"
key                           =                                                                                    "ThisIsKey"
cipher                        =                                                                                             ""
i                             =                                                                                              0
j                             =                                                                                              0

while len( flag ) - len(key)  > len(key): key    += key                                                               ;
while len( flag ) - len(key)  > 0       : key    += key[i]                                                            ; i += 1
while len(cipher) - len(key)  < 0       : cipher += chr((~ord(flag[j]) | ~ord(key[j])) & (ord(flag[j]) | ord(key[j]))); j += 1
print    (hexlify      (                  cipher    .encode()                                                      ).decode())