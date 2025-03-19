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

We find that the `main function (0x1b90)` calls the function `checkSpell (0x193d)`, which subtracts 0x41 (ASCII for 'A') from the first character of the input and uses it to call the `func_xxxx`.  
We also find that the `func_24` is the only function that calls the `read_flag` function.  
So, the answer would be to trigger `func_24`, which can be done when **"X"** is the input.

![image](https://github.com/user-attachments/assets/cf49bf34-dffa-4bec-991b-8aa0b9eeb4d6)


Flag: THM{s0m3_mag1c_that_can_b3_computed}
