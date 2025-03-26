# Challenge Statement
![image](https://github.com/user-attachments/assets/03fb3182-51ab-40fa-81bf-1695163f327c)

# Solution
Opening the website, we are met with a tool which seems to be take any text file and encrypt using the respective pgp keys.
![image](https://github.com/user-attachments/assets/d28eabbe-f808-4568-aa6f-21450d7dc60f)

Opening BurpSuite Repeater and playing around with different inputs, we find that the website is vulnerable to command injection in the `recipient` field.  
We can setup a netcat listener to receive the exfiltrated data.  The payload I used is: 
![image](https://github.com/user-attachments/assets/669bd677-2e70-48e9-9d97-c0d7529aba94)

![image](https://github.com/user-attachments/assets/585f9885-bcec-4fb2-9165-4b2dbea2e068)
