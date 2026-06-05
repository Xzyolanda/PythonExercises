from exercises.trees.balance import balance_sorted_tree
from exercises.trees.core.binary_tree import BinaryTree


def inorder_values(tree: BinaryTree[int] | None) -> list[int]:
    if tree is None:
        return []
    return inorder_values(tree.left) + [tree.value] + inorder_values(tree.right)


def height(tree: BinaryTree[int] | None) -> int:
    if tree is None:
        return 0
    return 1 + max(height(tree.left), height(tree.right))


def assert_balanced(tree: BinaryTree[int] | None) -> None:
    if tree is None:
        return
    assert abs(height(tree.left) - height(tree.right)) <= 1
    assert_balanced(tree.left)
    assert_balanced(tree.right)


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


def make_right_skewed_sorted_tree(values: list[int]) -> BinaryTree[int]:
    root = BinaryTree(values[0])
    current = root
    for value in values[1:]:
        current.right = BinaryTree(value)
        current = current.right
    return root


def test_balance_sorted_tree_preserves_values_and_binary_search_tree_order():
    tree = make_right_skewed_sorted_tree([1, 2, 3, 4, 5, 6, 7])

    balanced = balance_sorted_tree(tree)

    assert inorder_values(balanced) == [1, 2, 3, 4, 5, 6, 7]
    assert_is_binary_search_tree(balanced)


def test_balance_sorted_tree_returns_height_balanced_tree():
    tree = make_right_skewed_sorted_tree([1, 2, 3, 4, 5, 6, 7])

    balanced = balance_sorted_tree(tree)

    assert_balanced(balanced)
    assert height(balanced) == 3


def test_balance_sorted_tree_handles_already_balanced_tree():
    tree = BinaryTree(
        4,
        left=BinaryTree(2, BinaryTree(1), BinaryTree(3)),
        right=BinaryTree(6, BinaryTree(5), BinaryTree(7)),
    )

    balanced = balance_sorted_tree(tree)

    assert inorder_values(balanced) == [1, 2, 3, 4, 5, 6, 7]
    assert_balanced(balanced)
    assert_is_binary_search_tree(balanced)
