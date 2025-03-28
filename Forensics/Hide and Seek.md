# Challenge Statement
![image](https://github.com/user-attachments/assets/b64fbcc7-9ed4-4ed9-97b5-f10de1d75fff)

# Solution
Firstly, we can assume **ROOT** since we can do `sudo su`.  

➜ The **First Clue** - "Time is on my side, always running like clockwork.", suggests something related to cronjobs in Linux.  
We can check all the current cron jobs using `crontab -l`.  
![image](https://github.com/user-attachments/assets/ab4b2f85-1aa1-4415-abaa-e9dc5a97f9db)

We can decode this to find the 1st part of the flag.  
![image](https://github.com/user-attachments/assets/a08cc4e3-bdc9-424b-9552-9f74c8801d96)

➜ The **Second Clue** - "A secret handshake gets me in every time.", suggests something related to the SSH.  
We can check the `.ssh` folder on all of our accounts.  
![image](https://github.com/user-attachments/assets/e1b93c52-aacd-464c-bf5b-3a04bf92614c)

We find a strange string after the sha2 key. Let's try to decode it.  
![image](https://github.com/user-attachments/assets/55e23cc7-609e-45ed-88db-7b931d3f801f)

➜ The **Third Clue** - "Whenever you set the stage, I make my entrance.", refers to something that runs when a user logs in.  
Let's check the `.bashrc` files.  
![image](https://github.com/user-attachments/assets/fd5252f6-09fe-4adb-8e18-3ef1a4abba97)

Decoding it we can get our 3rd part of the flag.  
![image](https://github.com/user-attachments/assets/97c4ef48-0f10-4bef-bea5-0c1e7f091e51)

➜ The **Fourth Clue** - "I run with the big dogs, booting up alongside the system.", suggests some service which runs when the system is booted.
Let's check for the any suspicious services -
```
systemctl list-unit-file --type=service | grep enabled
```   
We find this file called cipher.service, let's investigate further.  
![image](https://github.com/user-attachments/assets/8f6d4267-9bae-4746-b915-f3d10db1df6a)

Decoding this string, we get our 4th flag.  
![image](https://github.com/user-attachments/assets/2fd973f7-891c-4f81-987d-9ed0f71c56ae)

➜ The **Fifth Clue** - "I love welcome messages.", refers to the message of the day (MOTD), which is sent when the user logs in.  
Checking out the `/etc/update-motd.d` folder, we can find this string.
![image](https://github.com/user-attachments/assets/fe43062e-fab5-4598-8417-b94d6472e1af)

Decoding it, we get out final flag.  
![image](https://github.com/user-attachments/assets/5c488015-34b1-4be5-a737-ab858087bace)

➜ Combining all the flags, we can submit our complete flag. 

