import avl_example as avl_tree


if __name__ == "__main__":
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    print("Заповнюємо AVL дерево")
    for key in keys:
        root = avl_tree.insert(root, key)

    print("AVL-Дерево:")
    print(root)

    print("Максимальне значення:")
    print(avl_tree.max_value_node(root))

    print("Мінімальне значення:")
    print(avl_tree.min_value_node(root))

    print("Сума всих значень:")
    print(avl_tree.get_sum(root))