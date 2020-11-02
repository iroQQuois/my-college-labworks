class Stack:
    def __init__(self):
        self.item = []

    def push(self, value):
        self.item.insert(0, value)

    def pop(self):
        array = self.item
        array.remove(array[0])

    def top(self):
        first_number = self.item[0]
        return first_number

    def empty(self):
        if self.item:
            return True
        else:
            return False

    def size(self):
        return len(self.item)

    def clear(self):
        """очистить массив"""
        self.item.clear()


operators_dict = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
            }


def parse(string: str) -> int:
  """доп задания  2, 3, 4 доделаю позже"""
  number_stack = Stack()
  operator_stack = Stack()

  for char in string:
    if char != ')':
      if char.isdigit() == True:
        number_stack.push(int(char))
      elif char in list(operators_dict.keys()):
        operator_stack.push(char)
    else:
      if number_stack.size() > 1 and operator_stack.size() > 0:
        remove_current_and_push(number_stack, operator_stack)

  return number_stack.top()



def count_up(operator, number1, number2):
  """
  функция вычисляет и возвращает результат примера из двух чисел
  """
  result = operators_dict[operator](number2, number1)
  return result  

def remove_current_and_push(number_stack, operator_stack):
  """
  выстаскивает числа, вызывает функцию подсчёта и пушит результат в стек
  """
  number2 = number_stack.top()
  number_stack.pop()

  number1 = number_stack.top()
  number_stack.pop()

  result = count_up(operator_stack.top(), number2, number1)
  operator_stack.pop()

  number_stack.push(result)

print(int(parse('( ( 2 + 3 ) * ( 4 * 5 ) )')))