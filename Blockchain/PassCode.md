# Challenge Statement
![image](https://github.com/user-attachments/assets/176e130a-fd33-49ff-bfd4-70de1ee74848)

# Solution
Heading over to the site, we can view the contract's source code.  
![image](https://github.com/user-attachments/assets/327b0589-bd99-40e2-9a47-21c05a7c8bbd)

The contract’s logic is straightforward, it only unlocks if you provide the correct number via the `unlock function`.  
The flag is stored in the `secret variable` and is only revealed by the `getFlag function` once `unlock_flag` is set to true.  
The `unlock function` takes an input and compares it to the stored variable `code`. If they match, it sets unlock_flag to true.  
We can try to read `code` from the contract's storage.  
![image](https://github.com/user-attachments/assets/bf27c338-eca1-4295-9a48-df80a2044e1c)

Now, we can send a transaction to call `unlock`
![image](https://github.com/user-attachments/assets/3ec3d61d-e297-4721-89cc-cb60bbb4c4f9)

Now, we can call the `getFlag()` function to reveal the flag.
![image](https://github.com/user-attachments/assets/7dc1b466-ddb5-4a8d-8b7f-c7aefaaf848c)
