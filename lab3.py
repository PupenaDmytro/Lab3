class AVLNode:
    def __init__(self, key, height=1, left=None, right=None):
        self.key = key
        self.height = height
        self.left = left
        self.right = right

class AVLTree:
    def __init__(self):
        self.root = None

    # Функція для отримання висоти вузла
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Функція для обчислення балансу вузла
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Функція для обертання дерева вліво
    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Виконання обертання
        y.left = z
        z.right = T2

        # Оновлення висот
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Повернення нового кореня
        return y

    # Функція для обертання дерева вправо
    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Виконання обертання
        y.right = z
        z.left = T3

        # Оновлення висот
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Повернення нового кореня
        return y

    # Рекурсивна функція для вставки нового елемента
    def insert(self, node, key):
        # Крок 1: Звичайне додавання у двійкове дерево пошуку
        if not node:
            return AVLNode(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node  # Рівні ключі не дозволені

        # Крок 2: Оновлення висоти вузла
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Крок 3: Обчислення балансу вузла
        balance = self.get_balance(node)

        # Крок 4: Балансування дерева
        # Ліво-Ліво випадок
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # Право-Право випадок
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Ліво-Право випадок
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Право-Ліво випадок
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # Функція для додавання нового елемента
    def add(self, key):
        self.root = self.insert(self.root, key)

    # Функція для візуалізації дерева у вигляді тексту
    def print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            if node.left or node.right:
                self.print_tree(node.left, level + 1, "L--- ")
                self.print_tree(node.right, level + 1, "R--- ")

    # Симетричний обхід дерева (in-order traversal)
    def inorder_traversal(self, node):
        if not node:
            return []
        return self.inorder_traversal(node.left) + [node.key] + self.inorder_traversal(node.right)

    # Прямий обхід дерева (pre-order traversal)
    def preorder_traversal(self, node):
        if not node:
            return []
        return [node.key] + self.preorder_traversal(node.left) + self.preorder_traversal(node.right)

    # Зворотний обхід дерева (post-order traversal)
    def postorder_traversal(self, node):
        if not node:
            return []
        return self.postorder_traversal(node.left) + self.postorder_traversal(node.right) + [node.key]

# Приклад використання
if __name__ == "__main__":
    tree = AVLTree()
    elements = [10, 20, 30, 40, 50, 25, 65, 5, 15, 35, 45, 55, 70, 60]
    for element in elements:
        tree.add(element)

    print("AVL-дерево:")
    tree.print_tree(tree.root)

    print("\nСиметричний обхід (in-order):", tree.inorder_traversal(tree.root))
    print("Прямий обхід (pre-order):", tree.preorder_traversal(tree.root))
    print("Зворотний обхід (post-order):", tree.postorder_traversal(tree.root))
