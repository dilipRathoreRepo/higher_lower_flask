from random import randint
from flask import Flask

app = Flask(__name__)


def decorator_too_low(func):
    def wrapper_func():
        return f'<h2 style="color:red"><b>{func()}</b><h2>' \
               f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    return wrapper_func


def decorator_too_high(func):
    def wrapper_func():
        return f'<h2 style="color:blue"><b>{func()}</b><h2>' \
               f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    return wrapper_func


def decorator_correct_guess(func):
    def wrapper_func():
        return f'<h2 style="color:black"><b>{func()}</b><h2>' \
               f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    return wrapper_func


@app.route('/')
def home():
    return f'<h1><b> guess a number between 0 to 5 </b></h1>' \
           f'<br>' \
           f'<br>' \
           f'<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@decorator_too_low
def return_low_output():
    return 'Too low'


@decorator_too_high
def return_high_output():
    return 'Too high'


@decorator_correct_guess
def return_equal_output():
    return 'You got it right!'


@app.route("/<int:number>")
def user_input(number):
    actual_number = randint(0, 5)
    print(f'actual_number is {actual_number}')
    if number < actual_number:
        return return_low_output()
    elif number > actual_number:
        return return_high_output()
    else:
        return return_equal_output()


if __name__ == "__main__":
    app.run()
