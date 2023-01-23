#INCLUINDO A BIBLIOTECA DA CRIPTOGRAFIA TRIPLE DES
#IMPORTANDO UM GERADOR DE CHAVE ALEATORIA

from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

#INCLUINDO A UM LOOP, SE TRUE, GERAR UMA CHAVE ALEATORIA DE 24 BYTES (3 CHAVES DIFERENTES)
#ASSIM QUE A CHAVER FOR GERADA COM SUCESSO QUEBRAMOS O LOOP, CASO CONTRÁRIO VAI TENTAR GERAR UMA CHAVE NOVAMENTE

while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        pass

#DEFININDO O METODO DE CRIPTOGRAFIA, PARA PEGAR UM TEXTO COMO PARAMETRO E RETORNAR CRIPTOGRAFADO

def encrypt(msg):   # -----> VAI RECEBER A MENSAGEM
    cipher = DES3.new(key, DES3.MODE_EAX)   # -----> OBJETO CIFRADO
    nonce = cipher.nonce 
    ciphertext = cipher.encrypt(msg.encode('ascii'))  
    return nonce, ciphertext  # -----> RETORNANDO TEXTO CRIPTOGRAFADO

#DEFININDO O METODO PARA DECRIPTAR A MENSAGEM

def decrypt(nonce, ciphertext):
    cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)  # -----> OBTENDO O TEXTO
    return plaintext.decode('ascii')

#CÓDIGO PARA RECEBER A ENTRADA DE CRIPTOGRAFIA E DESCRIPTOGRAFIA
#CHAMANDO OS RETURN

nonce, ciphertext = encrypt(input('Digite uma mensagem: ')) # -----> RECEBER MENSAGEM A SER CRIPTOGRAFADA
plaintext = decrypt(nonce, ciphertext)
print(f'Cipher text: {ciphertext}') # -----> MENSAGEM GRIPTOGRAFADA
print(f'Plain text: {plaintext}') # -----> MENSAGEM DESCRIPTOGRAFADA