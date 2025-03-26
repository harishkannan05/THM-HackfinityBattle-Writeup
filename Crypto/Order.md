# Challenge Statement
![image](https://github.com/user-attachments/assets/49d3be63-0bc3-45e7-9ea5-34faa19cc942)

# Solution
It's been given that the encryption is done using a repeating-key XOR cipher and that the message always starts with "ORDER".  
Using this information, we can decrypt the message. I've written a script. 

```
import binascii

ciphertext = "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f63731a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60" 

ciphertext_bytes = binascii.unhexlify(ciphertext) # Convert the hex string into bytes

known_plaintext = b"ORDER:" 

# Derive the encryption key by XORing the ciphertext bytes with the known plaintext bytes
key = bytes(ciphertext_bytes[i] ^ known_plaintext[i] for i in range(len(known_plaintext)))

# Decrypt the entire ciphertext by XORing with the derived key repeatedly
plaintext = bytes(ciphertext_bytes[i] ^ key[i % len(key)] for i in range(len(ciphertext_bytes)))

print(plaintext)
```

![image](https://github.com/user-attachments/assets/4bd9a970-0513-49f9-b449-d093bdb85734)
