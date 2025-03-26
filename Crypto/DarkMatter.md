# Challenge Statement

![image](https://github.com/user-attachments/assets/96b011c0-c60a-4f1a-92ec-f65abb4e9b5a)

# Solution
In the given VM, we are greeted with a ransomware asking for the decryption key.  
![image](https://github.com/user-attachments/assets/ba69a24d-b503-4a46-a8c5-03de336b4657)

We have been given the clue that the "ransomware saves data to the tmp directory."  
Checking the `/tmp` directory, we find a file called `public_key.txt`.  
![image](https://github.com/user-attachments/assets/06fbdf21-52bf-4d7f-9e83-e4ae7ee72550)

Now that we know `e` and `n`, we can use this [decoder](https://www.dcode.fr/rsa-cipher) to find d.  
![image](https://github.com/user-attachments/assets/2fcc0e0e-ee06-4c2b-af78-11217dbc29a8)

Entering the value of `d` in the decryption key field in the ransomware, we are able to decrypt the files.  
![image](https://github.com/user-attachments/assets/38a98483-5daf-40e7-9e12-c6f6570bc24d)

We can now open and view the files on the Desktop. The `student_grades.docx` holds the flag.  
![image](https://github.com/user-attachments/assets/917f8a69-3a97-479e-80f7-32b97c580f67)
