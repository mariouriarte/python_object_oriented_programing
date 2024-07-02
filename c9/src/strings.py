dec = '9.26'
print(dec.isdecimal())

dec2 = 9.26
# exception
# print(dec2.isdecimal())

dec3 = '9\u066026'
print(dec3.isdecimal())

dec4 = float('45\u06602')
print(type(dec4))

print(bytes([137, 80, 78, 71, 13, 10, 26, 10]))
print(bytes([64, 97]))
print("----------------------")
# Decoding bytes to text
characters = b'\x63\x6c\x69\x63\x68\xc3\xa9'
print(characters)
print(characters.decode("UTF-8"))

character_e = b'\xc3\xa9'
print(character_e)
print(character_e.decode("UTF-8"))
print("----------------------")

character_e = 'é'
print(character_e.encode('UTF-8'))

# Encoding text to bytes
characters = "cliché"
print(characters.encode("UTF-8"))
print(characters.encode("latin-1"))
print(characters.encode("cp1252"))
print(characters.encode("CP437"))

# print(characters.encode("ascii")) # raise error

print("----------------------")
# Mutable byte strings
ba = bytearray(b"abcdefgh")
ba[4:6] = b"\x15\xa3"
print(ba)
