from django.test import TestCase

# Create your tests here.
def hello():
    print('Hello World!')

test = hello
hello()
test()

def my_deco(function):
    def wrap():
        print('---------------------')
        function()
        print('---------------------')
    
    return wrap

func = my_deco(hello)
func()    # wrat()

def hello2():
    print("Hello")

func2 = my_deco(hello2)
func2()

@my_deco
def test1():
    print('test1')

test1()

@my_deco
def test2():
    print('test2')

test2()



# 매개변수가 있는 함수
def my_deco2(function):
    def wrap(name):    # decorator를 붙일 함수가 매개변수가 있는 경우 wrap함수에 붙인다.
        print('---------------------')
        function(name)
        print('---------------------')
    
    return wrap


@my_deco2
def greeting(name):
    print('Hi', name+'!')

greeting('은우')

