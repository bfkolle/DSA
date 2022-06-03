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

def test_valueontop_is_lastpushedvalue():
    stack = getteststack()
    stack.push("Hello")
    stack.push("World")
    stack.push("!")

    assert stack.peek() == "!"