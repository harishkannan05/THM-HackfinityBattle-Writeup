# Challenge Statement 
![image](https://github.com/user-attachments/assets/42c29c83-324a-470f-a210-acc66eb06267)

Attachment: [OldAuth](https://github.com/harishkannan05/THM-HackfinityBattle-Writeup/blob/main/Attachments/oldauth)
# Solution
Same as before, we can first get the assembly code from the executable. (Or use Ghidra)
```
objdump -d oldauth > disassembly.txt
```

We see that we need to input a key and a username, but both are altered before being compared with the stored values.  
For the key, the checks are -  
![image](https://github.com/user-attachments/assets/e580aae4-61ef-45b9-a384-abae8bfaeb0b)

The key is also getting XOR'd with 0x52 beofre the checks are applied. Here's the script to build the key.
```
key = bytearray([0x41] * 16) # 16 byte key
key[2] = 0x03   # To get 'Q'
key[13] = 0x66  # To get '4'
for i in range(4, 8):
    key[i] = 0x10 ^ 0x52
key[8] = 0x10 ^ 0x52
for i in range(9, 11):
    key[i] = 0x14 ^ 0x52
key[11] = 0x18 ^ 0x52
key[14] = 0x43
key[15] = 0x45
```

Going through the code, we see that for the username, it checks if after 2 to each byte of the input, it matches with 'elb4rt0pwn’ or not.   
Thus, the correct input for the username would be to subtract 2 byte from each byte. Here's a simple code for this.  
```
username = "".join(chr(ord(c) - 2) for c in "elb4rt0pwn")
print("username:", username)
```

Running the code, we are able to get the flag!  
![image](https://github.com/user-attachments/assets/2c61216d-6ec0-4971-900d-26066963955a)
