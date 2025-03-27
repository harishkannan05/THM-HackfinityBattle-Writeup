# Challenge Statement
![image](https://github.com/user-attachments/assets/d1c09fa7-9694-4a49-b2b1-1ff3afad1c95)

Attachment: [pwn1.c](https://github.com/harishkannan05/THM-HackfinityBattle-Writeup/blob/main/Attachments/pwn1.c)

# Solution
Analyzing the given code, we see that the `login()` function calls the `print_flag()` function upon successful login.  
The two local buffers are - `char password[100] = "";` and `char username[100] = "";`  

The `login()` function reads the username input using `gets(username)`, which is vulnerable to buffer overflow.  

We also have the credentials given in the code:
![image](https://github.com/user-attachments/assets/486242da-eee2-4267-84a9-bc4639fdfcca)

So, all we have to do is find the memory layout and overflow the **username** buffer, which can be used to overwrite the **password** buffer.  
To do this, we can compile the code and build a local executable.  
```
gcc -fno-stack-protector -z execstack -o challenge pwn1.c
```

Now, we can disassemble the file using the command:
```
objdump -d challenge > disassembly.txt
```
![image](https://github.com/user-attachments/assets/3c0fc1fc-26b9-4672-a75a-ac3e4cd2a9b7)

From the Assembly Code, we can see that a single buffer is used for both the username and the password.  
The username part is from `-0xe0` to `-0x70` and from `-0x70` is the password.  
![image](https://github.com/user-attachments/assets/d55e77e2-a582-4ec3-8f59-a6824677359d)

Thus, the username occupies 0xe0 - 0x70 = 0x70 bytes --> 112 bytes. 
So the payload will be: 
```
python3 -c "print('bytereaper' + '\x00' + 'A'*101 + '5up3rP4zz123Byte')" | nc 10.10.160.254 1337
```
![image](https://github.com/user-attachments/assets/d43219ab-8efe-4fed-9868-e43d0da100b6)
