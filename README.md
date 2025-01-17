# Network
The implementation of a social network that allows users to make posts, follow other users, and “like” posts using Python framework Django, JavaScript, HTML, and CSS.This web application consist of different section such as create post, view all post, user profile, follow page, log in and log out page.
## All Post
Default page of web app is all post page this page shows the post made by all user that consist of like and dislike button and edit button for current user. When ever user clicks on edit button a pop up box will come along with edit option in the page when clicked on save changes it will change the content inside the post of current login user. Each post consist of its creater name on clicking on user name it will take to user Profile Page

![image](https://github.com/user-attachments/assets/0fd6fff1-596d-4874-9d7e-e9c38b860398)

### after clicking on user name inside post

![image](https://github.com/user-attachments/assets/491b3423-dd9e-4737-aa0c-d75f0927e841)
## Profile page
On clicking of user name in post it will take us to user profile page where we can see the information of user such as its all posts , its followers, its following, and a center icon just to look good(further modification can be done even to add image by applying Django image field)

![image](https://github.com/user-attachments/assets/b3d0ec29-5c88-4f94-a69f-97477f00e0ff)
## Follow Page
This page consist of all post by the other user that had been followed by the current user.

![image](https://github.com/user-attachments/assets/9fa69db7-55ac-42fb-a6e4-01c1065f0836)

## Create Post 
This post consist of a textbox form and a submit button that allows current user to post something on website

![image](https://github.com/user-attachments/assets/a518f141-a243-482c-ab16-c0966113348c)

## Login Page 
This page makes user to login into its own account

![image](https://github.com/user-attachments/assets/7e8c5289-9f13-4b13-a654-38f441486bb2)
## Register Page
This page makes the user to create new account

![image](https://github.com/user-attachments/assets/3018d679-e9f8-410f-aa1b-febc622f73c4)
## Note
1)Webiste also shows pagination that is user that move to next post and even can go back to previous post 

![pag](https://github.com/user-attachments/assets/731591ea-1cb5-4465-9888-6019a35bc873)
2)When the current user checks the profile of other user then he/she has option to choose to follow or unfollow other users

![Untitled](https://github.com/user-attachments/assets/81a3a25e-1b4f-4218-a5e0-128dc68a6e42)

![hu](https://github.com/user-attachments/assets/e79f6cd4-530e-4c28-8bdf-3d13f1dc25f8)
3)When the user has not logged in to the website the he can only see the all post, profile page, login and register page

![image](https://github.com/user-attachments/assets/e1808843-2d28-4abf-8980-b51e8ce7c845)

## Database info
The backend data base is show in form of django development server that consist of different django model that is use to store information. These data models name include Followers,Like,Post, user
![image](https://github.com/user-attachments/assets/5e8c4233-ba2a-47ee-8f70-3460d5c6cc04)
### User model
store information about username, password , date of login etc
![image](https://github.com/user-attachments/assets/35476e0e-d774-48e8-a30f-c56dad99179e)
### Follows model
this consist information about who is following whom
![image](https://github.com/user-attachments/assets/f4b3e040-aaeb-4cf4-bfb0-f2c97b8fd165)
### Like model
this consist of information about who had liked whose post
![image](https://github.com/user-attachments/assets/3c7677a2-ecab-40f7-9497-c3990040a79b)
### Post
information about post done by all user
![image](https://github.com/user-attachments/assets/9be88d19-1af1-4a4c-9c40-834f11754878)

### Thank You 😊
