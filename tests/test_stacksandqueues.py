import re
from stacksandqueues.stack import Stack

def getteststack():
    stack = Stack()
    stack.push("Hello")
    stack.push("World")
    stack.push("!")

    return stack


def test_valueontop_is_lastpushedvalue():
    stack = getteststack()
    stack.push("Hello")
    stack.push("World")
    stack.push("!")

    assert stack.peek() == "!"