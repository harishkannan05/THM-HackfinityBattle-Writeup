# Challenge Statement


# Solution
Once again, we visit the site and view the Solidity source code.  
![image](https://github.com/user-attachments/assets/a45376e0-1afe-4bae-bb7a-3a80f432d350)

The goal here is to drain the contract's wallet, which would cause `isSolved()` function to return true.  
![image](https://github.com/user-attachments/assets/336e6291-48d0-43b4-ae7c-c5bf0dab357e)

One vulnerability is that anyone can call the `changeOwnership()` function to become the new owner, after which we can call `withdraw()` to transfer all funds from the wallet.  
![image](https://github.com/user-attachments/assets/4950cfb5-60f4-4342-b925-0e91f5ed9d42)

Now, we can go back to the webpage and get the flag.  
![Screenshot 2025-03-27 014200](https://github.com/user-attachments/assets/17ac3b81-46a8-4908-8b15-b611c698e230)
