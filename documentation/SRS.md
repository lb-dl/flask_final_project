# easy-learn flask app

### Vision
Easy-learn web application is based on Flask for backend and Vue for frontend. It provides
users with functionality which helps learning a foreign language. The current version is for
the Czech language learners only. However, the application might be developed to add more languages.
As a user you can sign up, sign in and see a profile page, where you can edit your personal information,
create, update and delete your own lessons. There is 1 activity which helps memorizing new words. 
More activities could be added in the future developing the application.

### Intended Audience
This project is a web application which provides users with activity which helps learning the Czech language. 
Users can easily create a new lesson adding the words or phrases they want to learn. Each lesson can be modified
or deleted. Users can create as many lessons as they want. After creating a lesson there is an activity that may help 
the user to memorize the words and phrases from a current lesson.
The application would be useful for the Check language learners and for teachers as well.

### The project should provide:
- Create or delete users accounts
- Store the account information of all the users in a database
- Create lessons and stored them  in the database
- Display a list of all created lessons
- Update the list of lessons (adding or removing them)
- Update a specific lesson (adding or deleting words/phrases)
- Store new word/phrases in the database to show users a hint
- Using an activity based on the specific lesson


###  Entity–relationship model 
The major features of database system is shown in below entity–relationship model (ER model)

- here should be the img of DB

1. Users
   <br>
   <br>
    1.1 User account control  
<br>
    The application allows multiple, unrelated users to use the same project. That is why, each user should have
   a private login account for the system. 
<br>

- Application displays "Sing Up" form for registration;
- User enters username, email, password, password conformation and presses “Register Account” button;
- If any data is entered incorrectly, incorrect data message is displayed;
- If the user with the email has already existed, then error message is displayed;
- If entered data is valid, then the email and password are adding to database;
- Then the application displays "Sign in" form;
- User enters the username and password and presses "Sign in" button;
- If entered data is valid, the page with "profile" is shown;
- If any data is entered incorrectly, incorrect data message is displayed.  
    <br>
    1.2 Managing user's personal information
  <br>
  <br>
   On the "Home" page, authorized users can manage their personal information, such as email, username and password.
  <br>
- The application shows some input boxes in order to change personal information;
- User enters a nickname or password in order to change them;
- When a new nickname is entered, user presses "Change Nickname" button;
- The message "Nickname has changed successfully" is shown;
- To change a password three input boxes must be filled;
- When "Old password", "New password and "New password-confirmation" fields are filled, 
  user presses "Change Password" button;
- If any data is entered incorrectly, incorrect data message is displayed.
- If the entered data is valid, "Login" form is shown;
- Users can sing out by pressing "Sing out" button;
- When the "Sign out" button is pressed, the "Home" page without "Profile" and "Log in" form is shown.

2. Lessons application
   <br>
   <br>
    2.1 Lessons control  
<br>
    The application allows users to create, update or delete lessons and view a list of created lessons.
<br>

- When a user presses the "Lessons" button on the navbar, the list of the lessons is shown
- The application also shows a button 'Create a new lesson'
- If the 'Create a new lesson' button is pressed the pop-up window is shown where user can enter new words or phrases
- If users want to add more than five words/phrases, they should press the button 'Add a new line'
- If 'Add a new line' button is pressed, a new line is added to the list where new words/phrases could be typed
- If users want to finish they press 'Save a lesson' button
- The saved lesson is stored in the table 'Lesson' which is related to the current user only
- All the words and phrases from the saved lesson are stored into the table 'Dictionary'
- If users want to go back to the previous page to see a list of lessons, "Go back" button must be pressed

  <br>
  <br>
    2.2 Use a lesson to memorise words/phrases
  <br>
  <br>
   On the "Lessons" page, users can choose a lesson to start 'playing' with the words to remember them.
  <br>
  <br>
- To start a 'game' the button 'Start learning' should be pressed
- All words/phrases from the chosen lesson are shuffled and shown 1 by 1 to help the user memorise them 
- When all words/phrases are shown the statistic of the correct/incorrect answers is shown
- If the user wants to 'play' again, the 'Repeat a lesson' button should be pressed
- If the user wants to go back to the previous page to see a list of lessons, "Go back" button must be pressed

  <br>
  <br>
    2.3 Leave a comment and rate a lesson
  <br>
  <br>
   On the "Lessons" page, a user can leave a comment and rate a lesson.
  <br>
  <br>
- To rate a lesson users chose a number in a range from 1 to 5 and press "Rate" button
- A message with the chosen rate is shown
- If a user has already rated the lesson, they cannot rate it again
- To leave a comment, users fill the text input field and press the "Add Comment" button
- When "Rate" or/and "Add Comment" button is pressed the input data is saved in the database

