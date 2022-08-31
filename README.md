# FizzBuzz_API
This application displays endpoints for CRUD(Create, Retrieve, Update, Delete) using Django & Django Rest Framework .Please take the time to install your virtual environment with this command. If you have python install with in your system.  
```
python3 -m venv env
```
If not go to https://www.python.org/ and download the version of python for you system. Then you can run the command in your bash or command line.
Then you will need to install all the requirements in requirements.txt. You could do so by typing this into the bash or command window after downloading FizzBuzz_API. Enter into your directory where you created the env and type ```source env/bin/activate``` or if you are using windows ```.env\Scripts\activate```. Once you seee the indicator in your left side of the directory prompt. Cd into the folder where you download the FizzBuzz_API. Then you can enter this code into the bash or command window. ```pip install -r requirements.txt``` Now you should see the indication of the packages being downloaded, once it is finished you can then go to the command or bash window and type ``` python3 manage.py migrate```. This will get your tables in Django up and ready for the capability of viewing this application on your browser. Next there is a step that comes into play populating the database with some fixtures. This will require you to use this command to get some data into you tables after the migrations. Here is the command ```python manage.py loaddata fixtures/fizzbuzz.json```. Now you have your table with date we could go head and run the next command here ```python3 manage.py runserver```.
This will allow you to go your browser of your choice and run 127.0.0.1:8000. Here are you endpoints for the application if you would like to use something like POSTMAN to do you calls to the REST endpoint.
Go to 127.0.0.1:8000/redoc 
Now you can create a superuser and use the drf(Django Rest Framework) to make calls to the API and use it as you see fit. 
 Thank You For Your Time.

