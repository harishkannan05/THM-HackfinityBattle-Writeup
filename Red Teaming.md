# Challenge Statement


# Solution
Opening the link and logging in with the given credentials, we see that there's an email asking for a "Detailed Report". 
I tried attaching a `txt file` and sending it, I was prompted to attach a `docx or docm` file.
![image](https://github.com/user-attachments/assets/1b380eb1-f9bb-466e-b876-e4c2a667afde)

This suggests that we are supposed to upload a **Macro-enabled Document file (docm)**  
We can use Metasploit for creating the Docm file which would create a Reverse Shell.  
![image](https://github.com/user-attachments/assets/4c8e5af3-d331-41e2-8b3c-5a2573f099cc)

Now, before sending the file, we need to set up a listener.  
We can do that using Metasploit.  
![image](https://github.com/user-attachments/assets/4b1db480-3814-427d-876e-f4e7434398fa)


