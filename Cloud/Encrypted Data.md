# Challenge Statment
![image](https://github.com/user-attachments/assets/80a9a2fb-8d3b-43bb-b17f-fd3504136e4f)

# Solution
Firstly, we configure our AWS CLI.  
![image](https://github.com/user-attachments/assets/f07f65be-60a5-42fb-a87d-ab8ae6f7a224)

Then we can check the given S3 bucket. It contains a file, which we can download and view.  
![image](https://github.com/user-attachments/assets/6bdf636b-6da8-4fd3-84f0-d3aaade9a1d0)

Now, we have a ciphertext, a key ID, and an algorithm type, but we do not have the permissions to decrypt it.  
Looking at other IAM roles, we find this role called `crypto-master`.  
![image](https://github.com/user-attachments/assets/7b43d20a-1668-4ae9-a672-7a5df6314471)

We can try to assume the role temporarily using AWS STS.  
![image](https://github.com/user-attachments/assets/2e2a721c-a395-4eda-b9e8-61a4231f14b8)

Now, we can use the AccessKeyId, SecretAccessKey, and SessionToken to configure the AWS CLI.  
We can now use AWS KMS to decrypt the CipherText.
![image](https://github.com/user-attachments/assets/4859635a-7d7e-4bb5-991a-e54b68a67a7b)
