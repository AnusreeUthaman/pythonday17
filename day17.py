#Decorators
#decorators was using @ keyword first

#syntax
'''
def decorator(function):
    def wrap()
    print("****")
    function()
    print("****")
    return wrap
@ decorator
def greet():
    print("hello)
'''

def decorator(function):
    def wrap():
        print("****")
        function()
        print("****")
    return wrap
@ decorator
def greet():
    print("hello")
greet()

****
hello
****
