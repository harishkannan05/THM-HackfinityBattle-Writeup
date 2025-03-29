# Challenge Statement
![image](https://github.com/user-attachments/assets/e40ba862-a725-4598-8ae8-1740132003b2)

# Solution
We see that we need to get a score of 999999 to get the flag.  
We need to analyse the code and try to find the function which checks the score and reads out the flag.  
I used Binary Ninja to analyze the code.  
![image](https://github.com/user-attachments/assets/fafd9ce3-a1c7-4007-b236-8b722ad4d2b9)

Now, we just need to find the function, change it from "999999" to "1" and recompile into an .exe file.  
Play the game and we can now easily get the flag.  

![image](https://github.com/user-attachments/assets/8ee75260-caf9-4eb4-b67d-ccce29e4fef8)
