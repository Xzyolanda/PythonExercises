from exercises.trees.core.binary_tree import BinaryTree
from exercises.trees.insert import insert_sorted


def inorder_values(tree: BinaryTree[int] | None) -> list[int]:
    if tree is None:
        return []
    return inorder_values(tree.left) + [tree.value] + inorder_values(tree.right)


def assert_is_binary_search_tree(
    tree: BinaryTree[int] | None,
    lower: int | None = None,
    upper: int | None = None,
) -> None:
    if tree is None:
        return
    if lower is not None:
        assert tree.value > lower
    if upper is not None:
        assert tree.value < upper
    assert_is_binary_search_tree(tree.left, lower, tree.value)
    assert_is_binary_search_tree(tree.right, tree.value, upper)


def make_sorted_tree() -> tuple[BinaryTree[int], dict[int, BinaryTree[int]]]:
    nodes = {value: BinaryTree(value) for value in (8, 3, 10, 1, 6, 14, 4, 7, 13)}
    nodes[8].left = nodes[3]
    nodes[8].right = nodes[10]
    nodes[3].left = nodes[1]
    nodes[3].right = nodes[6]
    nodes[6].left = nodes[4]
    nodes[6].right = nodes[7]
    nodes[10].right = nodes[14]
    nodes[14].left = nodes[13]
    return nodes[8], nodes


def test_insert_sorted_adds_smaller_value_to_left_side():
    tree, nodes = make_sorted_tree()
    node = BinaryTree(2)

    insert_sorted(tree, node)

    assert nodes[1].right is node
    assert inorder_values(tree) == [1, 2, 3, 4, 6, 7, 8, 10, 13, 14]
    assert_is_binary_search_tree(tree)


def test_insert_sorted_adds_larger_value_to_right_side():
    tree, nodes = make_sorted_tree()
    node = BinaryTree(12)

    insert_sorted(tree, node)

    assert nodes[13].left is node
    assert inorder_values(tree) == [1, 3, 4, 6, 7, 8, 10, 12, 13, 14]
    assert_is_binary_search_tree(tree)


def test_insert_sorted_preserves_inserted_node_children():
    tree = BinaryTree(10)
    node = BinaryTree(5, BinaryTree(3), BinaryTree(7))

    insert_sorted(tree, node)

    assert tree.left is node
    assert inorder_values(tree) == [3, 5, 7, 10]
    assert_is_binary_search_tree(tree)
