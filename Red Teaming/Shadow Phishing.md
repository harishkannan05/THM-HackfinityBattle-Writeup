# Challenge Statement
![image](https://github.com/user-attachments/assets/6df7acb7-a8b7-4c9a-bdb7-61258d13daeb)

# Solution
This one is similar to the [Ghost Phishing Challenge](https://github.com/harishkannan05/THM-HackfinityBattle-Writeup/blob/main/Red%20Teaming/Ghost%20Phishing.md), but this time we have to attach a Windows Executable.  
![image](https://github.com/user-attachments/assets/d84091ae-1479-4867-a4da-913de5658742)

We can use msfvenom to generate the executable file.  
![image](https://github.com/user-attachments/assets/cbadb445-da8d-4396-abd0-df257d12b4ef)

Now, we have to set up the Metasploit Reverse TCP listener.  
![image](https://github.com/user-attachments/assets/e36e158d-2d9a-4bfb-abfa-a0e21cb7af5a)

Now, we can send the email and within a few minutes we should be able to get a Meterpreter shell into the machine.  
We can then traverse the system and locate the flag.  
![image](https://github.com/user-attachments/assets/01448655-95cd-4dc0-b82d-c9e4b8efad46)
