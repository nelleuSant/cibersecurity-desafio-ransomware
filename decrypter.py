import os
import pyaes

# Abrindo o arquivo encriptografado

file_name = 'teste.txt.encryptFile'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Chave para descriptografar
key = b'key_decrypt_file'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Remover arquivo criptografado
os.remove(file_name)

# Criando um novo arquivo descriptografado
new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()

