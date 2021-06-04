# FinalProject

To deploy my web application, the directory should have flask environment installed in it for the application to run successfully.
If you are already inside the directory where you want to run your flask environment, then using the following command you can install flask 
environment in your directory.

python3 -m venv venv

Note: The above command will store your environment in a folder called venv. So, feel free to change the second 'venv' to any name you like.

So, once the environment is setup our project is ready to go. Just to run it, get to the directory in which the project folder is installed and open either CMD or Window PowerShell to run our code.
Once inside the directory, write the following command on CMD or Window PowerShell to run the program:

python app.py


Description of various files in the project: 

app.py is my main file which need to run every time we want to test our web application.

The main Python files inside webpages folder are:
__init__.py – This file creates the flask app and the generic file extending to almost every file in the project. We create the database and our tables in this file.
auth.py – This file has all the views related to authentication. So, the main views are login, logout and sign up. This file also manages login session and all necessary part of login and logout of the customer and manager.
home.py – This file has all other views related to the project and almost all the views are extended from the home view as for very view the top part remains the same which is Home and Logout for all the users in our database.
table.py – This table deals with creation of all the tables in our database. This file describes the schema of various tables ranging from what columns and what constraints they have ranging from Primary key to foreign key.

The templates folder has all the HTML files required for our project and they all are being called in their respective views.
So, the project run in flask virtual environment. So, all you need is one programming language editor for me I personally used Sublime to code and then used Windows PowerShell to run my project. Then, I just ran the localhost:5000 on my Google Chrome browser. So, basically, I will recommend using Chrome or Firefox to run the project for web application part of the project.
Once, you run app.py and run localhost:5000 on a browser. It will take you to the Home window where it will ask you to login or signup. So, if you have an account, you can login and if you do not you can create one.
