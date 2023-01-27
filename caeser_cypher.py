

def encrypt(value, k=3):
    ref = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for i in value:
        p = ref.find(i)
        location = (p + k)%26
        found_value = ref[location]
        encrypted_text += found_value
    
    return(encrypted_text)


def decrypt(value, k=3):
    ref = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_text = ''
    for i in value:
        p = ref.find(i)
        location = (p - k)%26
        found_value = ref[location]
        decrypted_text += found_value
    
    return(decrypted_text)

flag = True

while flag:
    cmd = input("E for encypt, D for decrypt: ").lower()
    if cmd == 'e':
        aa = input("Enter the text to encrypt: ")
        print(encrypt(aa))
    elif cmd == 'd':
        aa = input("Enter text to decrypt: ")
        print(decrypt(aa))
    else:
        flag = False

