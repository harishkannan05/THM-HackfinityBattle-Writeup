# Challenge Statement

![image](https://github.com/user-attachments/assets/96b011c0-c60a-4f1a-92ec-f65abb4e9b5a)

# Solution
In the given VM, we are greeted with a ransomware asking for the decryption key.  
![image](https://github.com/user-attachments/assets/ba69a24d-b503-4a46-a8c5-03de336b4657)

We have been given the clue that the "ransomware saves data to the tmp directory."  
Checking the `/tmp` directory, we find a file called `public_key.txt`.  
![image](https://github.com/user-attachments/assets/06fbdf21-52bf-4d7f-9e83-e4ae7ee72550)

Now that we know `e` and `n`, we can use this [decoder](https://www.dcode.fr/rsa-cipher) to find d.  
![image](https://github.com/user-attachments/assets/d13ae307-d83e-413a-8ff2-abc968e14989)

Entering the value of `d` in the decryption key field in the ransomware, we are able to decrypt the files.  
![image](https://github.com/user-attachments/assets/38a98483-5daf-40e7-9e12-c6f6570bc24d)

We can now open and view the files on the Desktop. The `student_grades.docx` holds the flag.  
![image](https://github.com/user-attachments/assets/7f06ad29-256a-42f5-9f6d-32002c364ad0)

Flag: THM{d0nt_l34k_y0ur_w34k_m0dulu5}
