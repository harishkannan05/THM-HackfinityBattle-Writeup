# Challenge Statement

![image](https://github.com/user-attachments/assets/52d4d546-6a0d-4cd4-a863-9947ce50cf55)

# Solution
Opening the link and logging in with the given credentials, we see that there's an email asking for a "Detailed Report".  
I tried attaching a `txt file` and sending it, I was prompted to attach a `docx or docm` file.  
![image](https://github.com/user-attachments/assets/1b380eb1-f9bb-466e-b876-e4c2a667afde)

This suggests that we are supposed to upload a **Macro-enabled Document file (docm)**  
We can use Metasploit for creating the Docm file which would create a Reverse Shell.  
![image](https://github.com/user-attachments/assets/4c8e5af3-d331-41e2-8b3c-5a2573f099cc)

Now, before sending the file, we need to set up a listener using Metasploit.  
![image](https://github.com/user-attachments/assets/4b1db480-3814-427d-876e-f4e7434398fa)

Now, we can send the file. It takes a couple of minutes and we should be able to get a reverse shell access.  
![image](https://github.com/user-attachments/assets/c6d1d3e3-fea2-4b5f-9e28-63df1ad6eb2a)

Traversing through the system, we are able to locate the flag.  
![image](https://github.com/user-attachments/assets/8cf26c41-9a96-4859-8033-b6415c446463)
