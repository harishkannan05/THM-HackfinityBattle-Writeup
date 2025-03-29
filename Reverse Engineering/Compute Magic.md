# Challenge Statement
![image](https://github.com/user-attachments/assets/ad207280-576d-4826-bd60-870d7c080147)

Attachment: [computemagic](https://github.com/harishkannan05/THM-HackfinityBattle-Writeup/blob/main/Attachments/computemagic)

# Solution
First, we check the file type.  
```
file computemagic
```
![image](https://github.com/user-attachments/assets/9a09e9d3-76cc-4d46-8be3-21974c829882)  

Since this is an non stripped ELF 64-bit PIE executable, the symbol and function names are visible.  
We can now disassemble the binary and view the assembly code.  
```
objdump -d computemagic > disassembly.txt
```

We find a long switch statement, where each function calls a different function - `magic_fail()`, `read_flag()`, `check_other()`.
We also find that the `func_24` is the only function that calls the `read_flag` function correctly.  
So, the answer would be to trigger `func_24`, which can be done when **"X"** is the input.

![image](https://github.com/user-attachments/assets/d1a58893-3797-4722-9aa4-181e08773b49)
