# Challenge Statement
![image](https://github.com/user-attachments/assets/db3a2032-45b5-4dab-9745-7dc77be4d8db)

# Solution
First, let's start with a nmap scan of the network.  
![image](https://github.com/user-attachments/assets/7130903e-37a5-4e25-98f1-4f43085434f8)

We find that there is a D-link Router. We can try logging into the admin portal.  
![image](https://github.com/user-attachments/assets/12dd4237-1585-49b2-812d-bc6aaac686d6)

Looking around for CVEs for this version of D-Link Routers, we come across this [blog post](https://tomorrowisnew.com/posts/hacking-the-dlink-dir-615-for-fun-and-no-profit-part-3-cve-2020-10213/).  
It highlights a `Command Injection` vulnerability in the POST parameter of the `/set_sta_enrollee_pin.cgi` page.  

We can try to visit `/set_sta_enrollee_pin.cgi` (which leads to an infinity loop), intercept the request and send to the BurpSuite repeater.  
Now, we can modify the request to look like this.  
![image](https://github.com/user-attachments/assets/ffdc4bed-2dd7-464d-8079-3d91fd5bdf72)  

Make sure to set up a netcat listener before sending the request.  
![image](https://github.com/user-attachments/assets/4163982d-50b4-4c89-afb4-2bd35126abe0)
