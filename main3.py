#Using functions
def yell(text):
    return text.upper() + '!'

yell('hello')

shout = yell
shout('get out from here')

def greet(func):
    greeting = func('Hello, I am a Python program')
    print(greeting)