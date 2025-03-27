# Challenge Statement
![image](https://github.com/user-attachments/assets/d6895792-f14e-4728-bb2f-2d325b79c454)

Attachment: [pwn21.c](https://github.com/harishkannan05/THM-HackfinityBattle-Writeup/blob/main/Attachments/pwn21.c)

# Solution
Analysing the code, we find that it is has a **format string bug** in the printf(username) call.  
Instead of using a safe call like `printf("%s", username);`, the code simple calls `printf(username)`. We can include format specifiers and try to print variables from the stack.  
![image](https://github.com/user-attachments/assets/719b4002-fb1b-4525-99e6-f7c27b5e912d)
