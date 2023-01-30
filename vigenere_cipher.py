ref = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plain_text, key):
    cipher_text = ''
    count = 0

    for i in plain_text:
        p = ref.find(i)
        k = ref.find(key[count])
        pos = (p + k)%26
        cipher_text += ref[pos]
        count += 1
    
    return cipher_text


'''
while True:

    plain_text = input("Enter plain text:")
    key = input("Enter key: ")

    if len(plain_text) == len(key):
        break
    else:
        print("length of plaintext and key should be same")'''



plain_text = input("Enter plain text:")
key = input("Enter key: ")

if len(key) == len(plain_text):
    pass
else:
    key = key * len(plain_text)
    key = key[0:len(plain_text)]
print(encrypt(plain_text, key))

