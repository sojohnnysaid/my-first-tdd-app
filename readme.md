# My First TDD app

The purpose of this exercise is to write a test before writing any application code. The web app will have the following:

## homepage
A page containing the list of "mini apps" links

## mini apps

### string reverse
Returns the user's submitted string in reverse

### guess
Guess a number from 1-10. See if your number matches the randomly generated number

### guestbook
Sign into the guestbook and join the list of other guests who are probably just you

# Installation
- clone the repo
- cd into the repo
- python3 -m venv env
- source env/bin/activate
- pip install --upgrade pip
- pip install -r requirements.txt
- python manage.py runserver
- PROFIT!

## If you are interested in running the tests
You can run the unit tests without any issues with the command `pytest */tests/unit_*`


**caution** 

If you want to run the functional tests you are going to need the chrome driver
for selenium. The short story is you will have to download the executable file, copy that into
your /bin directory and add the full path to your $PATH variable. For mac I downloaded chromedriver
then `mv chromedriver /usr/local/bin` and finally `export PATH=/usr/local/bin/chromedriver:$PATH`.

The command `pytest` will run all the tests


Your milage may vary. Happy testing!
