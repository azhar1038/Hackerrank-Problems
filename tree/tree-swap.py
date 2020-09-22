class Node:
    def __init__(self, data, depth=1):
        self.data = data
        self.left = None
        self.right = None
        self.depth = depth

    def insert(self, arr):
        leftNode = rightNode = None
        left, right = arr
        if left != -1:
            leftNode = Node(left, self.depth+1)
            self.left = leftNode
        if right != -1:
            rightNode = Node(right, self.depth+1)
            self.right = rightNode
        return (leftNode, rightNode)

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res += self.inorderTraversal(root.right)
        return res

    def swapKChildren(self, k):
        if self.depth%k==0:
            if self.left or self.right:
                leftNode = self.left
                self.left = self.right
                self.right = leftNode
        if self.left:
            self.left.swapKChildren(k)
        if self.right:
            self.right.swapKChildren(k)
        


def swapNodes(indexes, queries):
#
# Write your code here.
#
    root = Node(1)
    current=[root]
    i=0
    while i < len(indexes):
        nodes = current
        for j in range(len(nodes)):
            node = current.pop(0)
            leftNode, rightNode = node.insert(indexes[i])
            if leftNode:
                current.append(leftNode)
            if rightNode:
                current.append(rightNode)
            i += 1
    print(root.inorderTraversal(root))
    for query in queries:
        root.swapKChildren(query)
        print(root.inorderTraversal(root))


swapNodes([[2,3],[4,-1],[5, -1], [6,-1],[7,8],[-1,9],[-1,-1],[10,11],[-1,-1],[-1,-1],[-1,-1]], [2,4])

# 4 -1
# 5 -1
# 6 -1
# 7 8
# -1 9
# -1 -1
# 10 11
# -1 -1
# -1 -1
# -1 -1

