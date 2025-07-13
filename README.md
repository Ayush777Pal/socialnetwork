# Visit the Site Here 
->https://ayush7171.pythonanywhere.com/
# Network
The implementation of a social network that allows users to make posts, follow other users, and “like” posts using Python framework Django, JavaScript, HTML, and CSS.This web application consist of different section such as create post, view all post, user profile, follow page, log in and log out page.
## All Post
Default page of web app is all post page this page shows the post made by all user that consist of like and dislike button and edit button for current user. When ever user clicks on edit button a pop up box will come along with edit option in the page when clicked on save changes it will change the content inside the post of current login user. Each post consist of its creater name on clicking on user name it will take to user Profile Page

<img width="1360" height="768" alt="image" src="https://github.com/user-attachments/assets/ed1a05a7-e6ab-4e63-96fa-4052ef03c128" />


### after clicking on user name inside post

<img width="1360" height="768" alt="image" src="https://github.com/user-attachments/assets/fe2dec1c-7252-4ba1-8de6-eef7e8474285" />

## Profile page
On clicking of user name in post it will take us to user profile page where we can see the information of user such as its all posts , its followers, its following, and a center icon just to look good(further modification can be done even to add image by applying Django image field)

<img width="1360" height="768" alt="image" src="https://github.com/user-attachments/assets/98d4f10c-c751-4a3a-a96b-7b91f402946c" />

## Follow Page
This page consist of all post by the other user that had been followed by the current user.

<img width="1360" height="768" alt="image" src="https://github.com/user-attachments/assets/70af7bc9-5f33-47a4-b78c-df8163847a06" />

## Create Post 
This post consist of a textbox form and a submit button that allows current user to post something on website

<img width="1360" height="768" alt="image" src="https://github.com/user-attachments/assets/3ba797dd-a3a5-48c0-bbd2-b609b9f6c949" />

## Login Page 
This page makes user to login into its own account

<img width="1360" height="768" alt="image" src="https://github.com/user-attachments/assets/a34624d3-9a6b-4fb6-8368-77bf6e857316" />

## Register Page
This page makes the user to create new account

<img width="1360" height="768" alt="image" src="https://github.com/user-attachments/assets/b66e402e-bc8d-456a-99d7-20b3b378c6eb" />

## Note
1)Webiste also shows pagination that is user that move to next post and even can go back to previous post 

<img width="1360" height="768" alt="image" src="https://github.com/user-attachments/assets/becc4f9d-d9f6-4fe7-8bf3-13cbcfe58d77" />

2)When the current user checks the profile of other user then he/she has option to choose to follow or unfollow other users

<img width="1360" height="768" alt="image" src="https://github.com/user-attachments/assets/1fbdcb0c-daa9-47de-aa8d-a4561391bedb" />

<img width="1360" height="768" alt="image" src="https://github.com/user-attachments/assets/5c9e60be-09d2-4d3f-b61e-e30dd21048cc" />

3)When the user has not logged in to the website the he can only see the all post, profile page, login and register page

<img width="1360" height="768" alt="image" src="https://github.com/user-attachments/assets/9c40fb78-3611-4182-a8ae-b99ec8b618db" />

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
