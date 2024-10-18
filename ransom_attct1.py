

'''

import random
msg = (ksdfij)
print
encrypted_level = 128 // 8
char_poll = ''

for i in range(0,255):
    char_poll += chr(i)

key = ''
for i in range(encrypted_level):
   key += random.choice(char_poll)

key_index = 0
max_key_index = encrypted_level-1
encrypted_msg =''

for i in msg:
    encrypted_char = ord(i)^ord(key[key_index])
    encrypted_msg += chr(encrypted_char)
    encrypted_msg = ''
 if key_index == max_key_index
  key_index = 0

 else :
     key_index +=1
print(f'Encrypted message {encrypetd_smg}')

key_index = 0
decrypted_msg = ''

for i in decrypted_msg:
   decrypted_char = ord(i)ord^chr(key[key_index])
   decrypted_msg += chr(decrypted_char)
   decrypted_msg = ''

if key_index == max_key_index
 key_index=0

else:
    key_index +=1

print(f'Decrypted msg{decrypted_msg}')     


'''

import random

msg = "Hello, this is a secret message!"  # Encrypt করার জন্য একটি মেসেজ
print(f"Original msg: {msg}")

# এনক্রিপশন লেভেল নির্ধারণ করা
encryption_level = 128 // 8  # 128-bit encryption
char_poll = ""

# প্রতিটি চরিত্রের জন্য সম্ভাব্য ASCII মানের সীমা নির্ধারণ করা
for i in range(0, 256):
    char_poll += chr(i)

# কী জেনারেট করা
key = ''
for i in range(encryption_level):
    key += random.choice(char_poll)

print(f"Key: {key}")

# এনক্রিপশন প্রক্রিয়া
key_index = 0
max_key_index = encryption_level - 1
encrypted_msg = ''

for i in msg:
    encryption_char = ord(i) ^ ord(key[key_index])  # XOR অপারেশন
    encrypted_msg += chr(encryption_char)
    
    if key_index == max_key_index:
        key_index = 0
    else:
        key_index += 1

print(f'Encrypted message: {encrypted_msg}')

# ডিক্রিপশন প্রক্রিয়া
key_index = 0
decrypted_msg = ''

for i in encrypted_msg:
    decrypted_char = ord(i) ^ ord(key[key_index])  # XOR অপারেশন
    decrypted_msg += chr(decrypted_char)
    
    if key_index == max_key_index:
        key_index = 0
    else:
        key_index += 1

print(f"Decrypted message: {decrypted_msg}")






