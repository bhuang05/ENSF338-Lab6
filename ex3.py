import sys

class TreeNode:
    def __init__(self, val='', left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#Below functions made with help from ChatGPT
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    postfix = []
    operator_stack = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            postfix.append(expression[i:j])
            i = j
        elif expression[i] in precedence:
            while operator_stack and operator_stack[-1] != '(' and precedence[operator_stack[-1]] >= precedence[expression[i]]:
                postfix.append(operator_stack.pop())
            operator_stack.append(expression[i])
            i += 1
        elif expression[i] == '(':
            operator_stack.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operator_stack and operator_stack[-1] != '(':
                postfix.append(operator_stack.pop())
            operator_stack.pop()
            i += 1
        else:
            i += 1
    while operator_stack:
        postfix.append(operator_stack.pop())
    return postfix

def build_tree(expression):
    postfix = infix_to_postfix(expression)
    stack = []
    for char in postfix:
        if char.isdigit():
            node = TreeNode(char)
            stack.append(node)
        else:
            right = stack.pop()
            left = stack.pop()
            node = TreeNode(char, left, right)
            stack.append(node)
    return stack.pop()

def evaluate_expression(root: TreeNode) -> int:
    if root:
        left_val = evaluate_expression(root.left)
        right_val = evaluate_expression(root.right)

        if root.val.isdigit():
            return int(root.val)
        else:
            if root.val == '+':
                return left_val + right_val
            elif root.val == '-':
                return left_val - right_val
            elif root.val == '*':
                return left_val * right_val
            elif root.val == '/':
                return left_val // right_val  

    return 0  


arguments = sys.argv[1:]
expression = ' '.join(arguments)
tree = build_tree(expression)
print(evaluate_expression(tree))

