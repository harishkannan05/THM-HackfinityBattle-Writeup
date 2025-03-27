# Challenge Statement
![image](https://github.com/user-attachments/assets/b0a901be-70ca-4f88-8d35-ea8f17bab803)

Attachment: [Dump.docx](https://github.com/harishkannan05/THM-HackfinityBattle-Writeup/blob/main/Attachments/%23%23Dump%23%23.docx)

# Solution
We are provided with a **Local Security Authority Subsystem Service (LSASS)** dump, which contains all the hashes of all the users.  
We can do a nmap scan of the target, to see what services are running.  
![image](https://github.com/user-attachments/assets/2c6bc196-3db5-423c-98ac-a93c82373cf6)

Now, we know that **Windows Remote Management (WinRM)** is running on port 5985.  
We can use **`Evil-WinRM`** with the dump information to get a Reverse shell.  
![image](https://github.com/user-attachments/assets/e91b0aec-0aac-4ce6-8fc1-44f0716b0ecf)

Now, we can just traverse through the system and obtain the flag.  
![image](https://github.com/user-attachments/assets/1c82951c-53be-4589-9b52-1c91f53139d2)
