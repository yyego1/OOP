class Stack(object):
    '''Simple stack realisation class using python list'''

    def __init__(self, dlugosc):
        '''Creates new list wich we will be using as stack'''
        self.stack = []
        self.dlugosc = dlugosc


    def push(self, item):
        '''Push(insert) new item on the top of the stack'''
        if len(self.stack) < self.dlugosc:
          self.stack.insert(0,item)
        else:
          raise Exception("Przekroczyles dlugosc stosu")

    def pop(self):
        '''Pop (delete) item on the top of the list'''
        self.stack.pop()

    def multipop(self, k):
      if len(self.stack) != 0:
        while k != 0:
          self.stack.pop()
          k -= 1

    def top(self):
        '''Return the top item'''
        return self.stack[0]

    def wyszukiwanie(self, el):
      x = Stack.top(self)
      while len(self.stack) != 0:
        if el == x:
          return f"Element {el} jest w stosie"
        else:
          return Stack.pop(self)
        return wyszukiwanie()

    def isEmpty(self):
        '''Return True if stack is empty, otherwise False'''
        return len(self.stack)==0

    def __str__(self):
      return f"Twoj stos: {self.stack}"

stack1 = Stack(5)
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
print(f"Stos: {stack1}")
print(f"Top element stosu: {stack1.top()}")
