class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key, level):
    print(f"Root: {root.key if root else None}, Key: {key}, Level: {level}")
    if root is None:
        return Node(key)

    level += 1
    if key < root.key:
        root.left = insert(root.left, key, level)
    else:
        root.right = insert(root.right, key, level)

    return root


def search(root, key, level):
    print(f"Root: {root.key if root else None}, Key: {key}, Level: {level}")
    if root is None or root.key == key:
        return root

    level += 1
    if key < root.key:
        return search(root.left, key, level)
    
    return search(root.right, key, level)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def main():
    root = None

    # Create BST
    for value in [50, 30, 70, 20, 40, 60, 80]:
        root = insert(root, value, 0)

#         50
#        /  \
#      30    70
#     / \    / \
#    20 40  60 80

    print("Inorder traversal:")
    inorder(root)

    # Search
    key = 30
    result = search(root, key, 0)

    if result:
        print(f"\n{key} found in BST")
    else:
        print(f"\n{key} not found in BST")


if __name__ == "__main__":
    main()