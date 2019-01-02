import CeaserCipherLib 

topRow = StringToList('abcdefghijklmnopqrstuvwxyz1234567890!@£$%^&*()_ ')
bottomRow = StringToList(' qwertyuiopasdfghjklzxcvbnm')

M = input('Message')


C = encode(M, topRow, bottomRow)
print(C)

DecodedM = decode(C, topRow, bottomRow)
print(DecodedM)
