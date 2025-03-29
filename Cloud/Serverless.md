# Challenge Statement
![image](https://github.com/user-attachments/assets/c2ba964f-cf0e-46cc-ab68-77bbe4afcd9d)

# Solution
Firstly, let's configure our AWS CLI.  
![image](https://github.com/user-attachments/assets/997c64e3-3b8c-48b9-b6c9-9252d3197e73)

Now, we can check for any S3 buckets.  
![image](https://github.com/user-attachments/assets/bc3dac39-8c87-4b77-80b0-f899bca3d1c7)

Trying to view the contents of the S3 bucket doesn't work since we don't have the permissions.  
Let's try to check the bucket policies.  
![image](https://github.com/user-attachments/assets/17b8427c-0405-413f-afc7-cb60a2dacc13)

We see that the bucket policy allows anyone to get objects from the bucket.  
We can try to check the object versions in the bucket.  
![image](https://github.com/user-attachments/assets/4a1b63d5-88dd-430a-bcc7-bebe074e0619)

Now, we can view the object names and can check each version by using the `get-object` command.  
![image](https://github.com/user-attachments/assets/3e0c2cbc-9bc7-4565-935d-8f0e35d577f7)  

Here, we have our **first flag!**
![image](https://github.com/user-attachments/assets/11683489-4395-44f8-8187-df87b258c87c)

Viewing this page source code, we see this weird piece of code.  
![image](https://github.com/user-attachments/assets/9ee02a65-cd6c-41a0-a413-1308a7fe8332)

This performs a **POST** request to a Lambda function without any input validation. We can try to exploit this with some injection (SSRF).  
Playing around with the directory, we are able to find the **second flag.**  
![image](https://github.com/user-attachments/assets/fe4d5e94-024c-4977-8c3a-8698caea75cb)

We can then check for other files in the system. One interesting file is the `\proc\self\environ`.  
![image](https://github.com/user-attachments/assets/18c048a1-29ff-4ce9-b37a-d025482a3f55)

Trying to use the new AWS keys to get access to the new user.  
![image](https://github.com/user-attachments/assets/f41b182b-9582-4721-8d86-2ce14137d4a4)

We now have access to the user - "redteamapp-lambda". We can try to assume the dev role since we have permissions to do so.  
![image](https://github.com/user-attachments/assets/30d11f06-07ec-4a36-9162-64ab15758938)  
![image](https://github.com/user-attachments/assets/9acd5c5c-da8f-42c7-a7ba-fe3c0487f717)  

Now, remember the website mentioned a DB. This could mean the DynamoDB.  
![image](https://github.com/user-attachments/assets/facd8445-7f2c-47ba-be52-e4423da894c3)  

We can check for the contents of the database and we get our **third flag!**  
![image](https://github.com/user-attachments/assets/16e732d5-4d32-4ca4-ab3f-be81beec8518)




