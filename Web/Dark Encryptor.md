#Challenge Statement
![image](https://github.com/user-attachments/assets/ea48e5f0-8b6a-4849-8408-f522ae894af9)

# Solution
The web app appears to be a simple PGP encryption tool designed for encrypting messages using one of several recipients’ public keys. 
I tried various inputs and found that the web app is vulnerable to `OS command injection`. We can simply cat the flag.  
```
;cat flag.txt
```
![image](https://github.com/user-attachments/assets/4e8f406e-2464-4ad3-864a-bece6f3e62a5)
