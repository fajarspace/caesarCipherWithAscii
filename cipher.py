print('Nama : Fajar Agung Nugroho')
print('NIM : 312010448')
print('')

plaintext = str(input('Plain Text: '))
ciphertext = []
ascii_code = []
print('') 

geser = int(input('mau geser brp?: '))

#encrypt
print('ENCRYPT :')
for i in plaintext:
    temp = ord(i) + geser
    ciphertext.append(chr(temp))
print('Cipher Text:', ''.join(ciphertext))
#ascii
for i in ciphertext[::-1]:  
    ascii_code.append(ord(i))
print('ASCII code:', ascii_code)
print ("geser : ",geser,'\n')

#Decrypt
print('DECRYPT :')
key = ascii_code
decrypt_ascii = []  
decrypt_ciphertext = []  
for i in key[::-1]: 
    decrypt_ascii.append(i)
print('ASCII code:', decrypt_ascii)
for i in decrypt_ascii:
    temp = i - geser
    decrypt_ciphertext.append(chr(temp))
print('Plain Text:', ''.join(decrypt_ciphertext))
print ("geser : ",geser)

