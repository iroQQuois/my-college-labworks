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


def hooks_balanced(word):
    stack = Stack()
    list_word = list(word)
    right_hook_counter = 0
    left_hook_counter = 0
    for hook in list_word:
        if hook == ')' or hook == '>' or hook == '}' or hook == ']':
            stack.push(hook)
            left_hook_counter += 1
        if hook == '(' or hook == '<' or hook == '{' or hook == '[':
            stack.push(hook)
            right_hook_counter += 1
    if right_hook_counter == left_hook_counter:
        return True
    else:
        return False


print(hooks_balanced('(<((())>)})'))
