# 20:30
import sys
n = int(sys.stdin.readline())
dict = {}

class node():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right



for _ in range(n):
    value, left, right = sys.stdin.readline().split()

    nod = node(value,left,right)
    dict[value] = nod


def preorder(parent, left, right):
    if parent.value ==  '.':
        return 
    print(parent.value, end = '')

    if left !=  '.':
        preorder(dict[left], dict[left].left, dict[left].right)
    if right !=  '.':
        preorder(dict[right], dict[right].left, dict[right].right)

def inorder(parent, left, right):
    if parent.value ==  '.':
        return 

    if left !=  '.':
        inorder(dict[left], dict[left].left, dict[left].right)
    print(parent.value, end = '')
    if right !=  '.':
        inorder(dict[right], dict[right].left, dict[right].right)

def postorder(parent, left, right):
    if parent.value ==  '.':
        return 
    
    if left !=  '.':
        postorder(dict[left], dict[left].left, dict[left].right)
    if right !=  '.':
        postorder(dict[right], dict[right].left, dict[right].right)
    print(parent.value, end = '')

preorder(dict['A'],dict['A'].left,dict['A'].right)
print()
inorder(dict['A'],dict['A'].left,dict['A'].right)
print()
postorder(dict['A'],dict['A'].left,dict['A'].right)
print()