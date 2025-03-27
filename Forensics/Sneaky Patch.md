# Challenge Statement
![image](https://github.com/user-attachments/assets/a3bbb96d-113c-48ef-b3f4-2b019340aacb)

# Solution
Since the challenge talks about a kernel level backdoor, we can run lsmod to check for any unexpected kernel modules.  
![image](https://github.com/user-attachments/assets/6303c5a4-bd6a-4850-a671-5c77b4c48238)

We find this suspicious module `spatch`. We can analyse the module file.  
![image](https://github.com/user-attachments/assets/72bb32f5-cf4e-4c3d-81ff-1f0eeedde50b)

This leads us to another file `/lib/modules/6.8.0-1016-aws/kernel/drivers/misc/spatch.ko`.
![image](https://github.com/user-attachments/assets/19c6f299-f122-41b7-9358-a8b0bcebc018)

We find this string, which seems to be the flag in hex.  
![image](https://github.com/user-attachments/assets/8af61b3b-b041-4878-ac98-91ebff423b71)
