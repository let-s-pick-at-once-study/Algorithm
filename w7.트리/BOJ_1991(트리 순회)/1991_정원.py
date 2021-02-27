
from sys import stdin

class Node:
    def __init__(self, val, left, right):
        self.value = val # 루트 노드
        self.left = left # 왼쪽 자식노드
        self.right = right # 오른쪽 자식노드

def preorder(node): # 전위순회
    print(node.value, end = "")
    if node.left != ".": preorder(tree[node.left])
    if node.right != ".": preorder(tree[node.right])

def inorder(node): # 중위순회
    if node.left != ".": inorder(tree[node.left])
    print(node.value, end = "")
    if node.right != ".": inorder(tree[node.right])

def postorder(node): # 후위순회
    if node.left != ".": postorder(tree[node.left])
    if node.right != ".": postorder(tree[node.right])
    print(node.value, end = "")

n = int(stdin.readline())
tree = {} # 딕셔너리형식으로 구성
for _ in range(n):
    data = stdin.readline().rstrip().split()
		tree[data[0]] = Node(val=data[0], left=data[1], right=data[2])

# 항상 A가 루트 노드
preorder(tree["A"])
print() # 이 부분이 없으면 (end = "") 옵션 때문에 위의 결과에 그대로 이어져서 출력됨 
inorder(tree["A"])
print()
postorder(tree["A"])
