# Challenge Statement
![image](https://github.com/user-attachments/assets/63fdfcec-b457-4b68-8d25-83f64f5005aa)

# Solution
We have a `.pcapng` which shows us the packets transmitted when the NFS server was infiltrated.  
We can use the filter `nfs.data`.  
![image](https://github.com/user-attachments/assets/2a0207e6-3fd0-45dd-ac68-de855cf213b5)

We then follow the TCP Stream to view the contents of the packet. We find that there is a `md5 hash` of an "Archive" Password.  
![image](https://github.com/user-attachments/assets/5a52a807-7263-429f-a31b-1c9d38428248)

We can use any tool to crack the md5 hash and get the password. I've used [this site.](https://crackstation.net/)
![image](https://github.com/user-attachments/assets/06128ad2-8afe-4e95-8ed6-44f89fae26b2)

The password is: avengers

To retrieve the "Archive" file, we can change the data type to `RAW` and save it as a zip file.  
Then, we just have to unzip the file and enter the password that we had retrieved. 
![image](https://github.com/user-attachments/assets/25cfd7b5-c8f9-4798-8ac0-f6adaa4221fb)

We get a QR code, which gives us the flag when scanned.  
![image](https://github.com/user-attachments/assets/e47d78bb-540c-4708-a46b-bdc55a4badab)

Flag: THM{n0t_s3cur3_f1l3_sh4r1ng}
