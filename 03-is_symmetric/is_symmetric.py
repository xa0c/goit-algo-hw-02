from typing import Any


class Stack:
    """Class for Stack storage."""

    def __init__(self) -> None:
        self.data = []

    def push(self, val: Any) -> None:
        self.data.append(val)

    def pop(self) -> Any:
        return self.data.pop()

    def is_empty(self) -> bool:
        return not self.data


def is_symmetric(text: str) -> bool:
    """Check if provided text value is symmetric.

    Args:
        text (str): Source text.

    Returns:
        bool: True if symmetric. False otherwise.
    """
    stack = Stack()
    for ch in text:
        try:
            match ch:
                case '(' | '[' | '{':
                    stack.push(ch)
                case ')':
                    if stack.pop() != '(':
                        return False
                case ']':
                    if stack.pop() != '[':
                        return False
                case '}':
                    if stack.pop() != '{':
                        return False
        except IndexError:
            # Stack is empty when closing brace appears before opening brace
            return False
    if not stack.is_empty():
        return False
    return True


if __name__ == "__main__":
    texts = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }",
        ")(",
    ]
    for text in texts:
        print(f"{text.ljust(40)} {": SYMMETRIC" if is_symmetric(text) else ": NOT SYMMETRIC"}")
