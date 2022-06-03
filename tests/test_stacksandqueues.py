import re
from stacksandqueues.stack import Stack

def getemptyteststack():
    return Stack()

def getteststack():
    stack = Stack()
    stack.push("Hello")
    stack.push("World")
    stack.push("!")

    return stack

def test_when_stackempty_peek_returnsnone():
    stack = getemptyteststack()
    assert stack.peek() == None

def test_peek_returns_topstackvalue():
    stack = getteststack()
    assert stack._list[0] == stack.peek()

def test_push_adds_valuetostack():
    stack = getemptyteststack()
    stack.push("Hello")
    assert stack.peek() == "Hello"

def test_push_adds_valuetotopofstack():
    stack = getteststack()
    assert stack.peek() == "!"

def test_pop_removes_topofstack():
    stack = getteststack()
    stack.pop()
    assert stack.peek() == "World"

def test_pop_returns_topofstack():
    stack = getteststack()
    assert stack.pop() == "!"