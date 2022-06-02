from stacksandqueues.stack import Stack

def main():
    #todo: make unit tests
    stack = Stack()

    stack.peek()
    stack.push("Hello")
    stack.push("World")
    stack.push("!")
    print("Value at top after three pushes:", stack._list[0])

    stack.pop()
    print("Value at top after one pop:", stack._list[0])

    print("Is stack full with two values:", stack.isFull())

    stack.pop()
    stack.pop()
    print("Stack is empty after removing all values:", stack.isEmpty())

if __name__ == "__main__":
    main()