from CeaserCipherLib import *

topRow = StringToList('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.!?')
bottomRow = StringToList(' qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0987654321?!.')

M = input('Message')


C = encode(M, topRow, bottomRow)
print(C)

    
