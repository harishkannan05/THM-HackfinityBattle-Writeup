# Challenge Statement
![image](https://github.com/user-attachments/assets/9d8418d1-4bd1-47d5-a836-62f888b15133)

# Solution
Going throught the code, we can see that it shifts each character of the plaintext by its position in the message. 
The function adjusts alphabetic characters, while non-alphabetic ones stay the same.

To decrypt the message, we just need to reverse the process, by shifting the characters backwords by their position in the message. 
I wrote the following Python code for the decryption process.
```
def decrypt(ciphertext):
    result = []
    for i, c in enumerate(ciphertext):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c) - base - i) % 26 + base))
        else:
            result.append(c)
    return "".join(result)

ciphertext = "a_up4qr_kaiaf0_bujktaz_qm_su4ux_cpbq_ETZ_rhrudm"

decoded_message = decrypt(ciphertext)
flag = f"THM{{{decoded_message}}}"
print("Flag:", flag)
```

Flag: THM{a_sm4ll_crypt0_message_to_st4rt_with_THM_cracks}
