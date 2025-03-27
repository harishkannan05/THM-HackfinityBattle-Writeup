# Challenge Statement
![image](https://github.com/user-attachments/assets/8098ac69-d3c2-44fe-b20a-e1b537969d91)

# Solution
Since the challenge talks about a web application vulnerability, we can directly head to the website's directory to look for suspicious files.  
![image](https://github.com/user-attachments/assets/95ba540f-08f5-49dc-98a6-b394e58ee867)

Going through all the files and folders, we see that there is an `images.php` file, which s PHP web shell.  
![image](https://github.com/user-attachments/assets/eff5bce4-28ea-4520-aabe-f62a9e968199)

The web shell allows us to execute commands on the server by passing them as a base64-encoded query parameter.  
Now, we cannot do anything with this information, but we can look at the logs to see the attacker's actions.  

Command I used: 
```
cat other_vhosts_access.log.1 | grep images.php?query=
```

![image](https://github.com/user-attachments/assets/8c22bf95-7fe3-4ac3-a2e5-c120eab56c8f)

From these, we can decode the base64 strings and obtain the flag.
![image](https://github.com/user-attachments/assets/ee1c418d-f9ba-4027-bd04-3f03d69d5e94)
