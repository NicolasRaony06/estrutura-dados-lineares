class Item:
    def __init__(self, value, prev):
        self.value = value
        self.prev = prev

    def __str__(self) -> str:
        return f"{self.value}"

class Stack:
    def __init__(self):
        self.__top = None

    def top(self):
        if self.__top is not None:
            return self.__top.value

    def push(self, value):
        item = Item(value, self.__top)
        self.__top = item 
                
    def pop(self):
        if self.__top is not None:
            item_prev_top = self.__top
            self.__top = self.__top.prev
            return item_prev_top.value

if __name__ == '__main__':
    stack = Stack()
    stack.push(2)
    top_prev = stack.pop()
    print(top_prev)
    print(stack.top())