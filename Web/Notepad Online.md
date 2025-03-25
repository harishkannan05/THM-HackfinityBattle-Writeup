# Challenge Statement
![image](https://github.com/user-attachments/assets/a5104795-3ab7-4fce-b729-de7bd1c8bcf2)

# Solution
Go to the site and login with the given credentials.
We see this screen with the URL: http://10.10.10.15/note.php?note_id=1
![image](https://github.com/user-attachments/assets/57d4cd7b-2d5c-4ca8-a43a-f9cefc000a86)

Clue here is that “the note will only be visible to you”. So we try to view others’ notes by changing the note id.  
Changing the URL to: http://10.10.252.73/note.php?note_id=0 
![image](https://github.com/user-attachments/assets/dae89f3b-9d5f-4ed6-ade7-7fb4960a85fb)

**Flag:** THM{i_can_see_your_notes}
