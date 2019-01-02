from CeaserCipherLib import *

topRow = StringToList('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.!?')
bottomRow = StringToList(' qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0987654321?!.')

C = input('Cipher')

DecodedM = decode(C, topRow, bottomRow)
print(DecodedM)
