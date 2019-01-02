from rsaLib import encodeMessage, StringToList
#Asks for publicKey 
Public = input('PublicKey?')
#Asks for message to encode
Message = input('Message?')
#CreatesCipher
cList = encodeMessage(Message, StringToList(Public))
#Prints Cipher to decode in decode file
print('Cipher: {0}'.format(cList))


