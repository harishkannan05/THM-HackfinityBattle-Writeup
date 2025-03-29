# Challenge Statement
![image](https://github.com/user-attachments/assets/e40ba862-a725-4598-8ae8-1740132003b2)

# Solution
We see that we need to get a score of 999999 to get the flag.  
We need to analyse the code and try to find the function which checks the score and reads out the flag.  
I used Binary Ninja to analyze the code.  
![image](https://github.com/user-attachments/assets/1d71c544-75b9-4279-9261-fb570a257ccb)

Now, we just need to find the function, change it from "999999" to "1" and recompile into an .exe file.  
Play the game and we can now easily get the flag.  

![image](https://github.com/user-attachments/assets/0d68066e-1ed9-48d6-b3d6-47bef10a13d7)
