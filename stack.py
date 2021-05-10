from typing import Any

class Stack(object):

    def __init__(self) -> None:
        self.stack = []
    
    def push(self, data) -> None:
        self.stack.append(data)

    def pop(self) -> Any:
        if self.stack:
            return self.stack.pop()

if __name__ == '__main__':
    stack = Stack()
    print(stack.stack)
    stack.push(1)
    print(stack.stack)
    stack.push(2)
    print(stack.stack)
    stack.pop()
    print(stack.stack)





def validate_format(chars: str) -> bool:
    lookup = {'{': '}', '[':']', '(':')'}
    stack = []
    for char in chars:
        if char in lookup.keys():
            stack.append(lookup[char])
        if char in lookup.values():
            if not stack:
                return False
            if char != stack.pop():
                return False
    if stack:
        return False
    
    return True


if __name__ == '__main__':
    j = "{'key1': 'value1', 'key2': [1, 2, 3], 'key3': (1, 2, 3)}"
    print(validate_format(j))
