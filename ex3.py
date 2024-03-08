class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

def parse_expression(expression):
    tokens = expression.split()
    stack = []
    root = None

    for token in tokens:
        if token.isdigit():
            node = Node(token)
            stack.append(node)
        elif token in operators:
            right = stack.pop()
            left = stack.pop()
            node = Node(token)
            node.left = left
            node.right = right
            left.parent = node
            right.parent = node
            stack.append(node)
    root = stack.pop()
    return root

def evaluate_expression(root):
    if root is None:
        return 0

    if root.data.isdigit():
        return int(root.data)

    left_value = evaluate_expression(root.left)
    right_value = evaluate_expression(root.right)

    if root.data == '+':
        return left_value + right_value
    elif root.data == '-':
        return left_value - right_value
    elif root.data == '*':
        return left_value * right_value
    elif root.data == '/':
        if right_value == 0:
            raise ValueError("Division by zero")
        return left_value / right_value

operators = ('+', '-', '/', '*')
expression = input("Enter Expression: ")
root = parse_expression(expression)
result = evaluate_expression(root)
print(result)
