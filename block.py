import binascii

def encrypt(K, P):
    K_0 = K[0:16]
    K_1 = K[16:32]
    K_0_dec = int(K_0, 16)
    K_1_dec = int(K_1, 16)
    C = ( (P ^ K_0_dec) + K_1_dec) % (2**64)
    return hex(C)[2:]

def decrypt(K, C):
    K_0 = K[0:16]
    K_1 = K[16:32]
    K_0_dec = int(K_0, 16)
    K_1_dec = int(K_1, 16)
    D = ((C - K_1_dec) ^ K_0_dec) % (2**64)
    return hex(D)[2:] 

def main ():
    # Given Key
    key_hex= "78FB0C23AE7B3C4D97B26FD59C27AF17"

    # Take in an input from user and encode it into hexadecimal
    secret_message = input("Please enter your secret message(in string format): ")      
    plaintext_hex = secret_message.encode("utf-8").hex()
    print(f'plaintext(hexadecimal): {plaintext_hex}\n')
    # First make sure the plaintext is divided into equal 64 bits since our key is 128 bits
    n = 16 # chunk length
    partitions = [plaintext_hex[i:i+n] for i in range(0, len(plaintext_hex), n)]

    # Check if the last element in the list is 64 bits, if not, append zeros until it is 64 bits
    if len(partitions[-1]) < 16:
            addZeros = 16 - len(partitions[-1])
            i = 0
            while i < addZeros:
                partitions[-1] += "0"
                i += 1

    # Alter each part of the list into decimals in order to properly mod it
    i = 0
    for element in partitions:
        partitions[i] = int(element, 16)
        i += 1

    # Run encryption on each partition of the plaintext
    Cipher_list = []
    Ciphertext = ""
    i = 0
    for element in partitions:
        Cipher_list.append(encrypt(key_hex, element))
        Ciphertext += Cipher_list[i]
        i += 1
    print(f'Ciphertext: {Ciphertext} \n')
    # Run decryption on each partition of the plaintext and output original message
    Decrypted_Message = ""
    i = 0
    for element in Cipher_list:
        Decrypted_Message = Decrypted_Message + bytes.fromhex(decrypt(key_hex, int(Cipher_list[i], 16))).decode('utf-8')
        i += 1
    print(f'Decrypted message: {Decrypted_Message}')

if __name__ == "__main__":
    main()    



