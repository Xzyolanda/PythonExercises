from collections import Counter

from exercises.trees.core.binary_tree import BinaryTree
from exercises.trees.delete import (
    delete_node,
    delete_node_by_sorted_value,
    delete_node_by_value,
)


def values_preorder(tree: BinaryTree[int] | None) -> list[int]:
    if tree is None:
        return []
    return [tree.value] + values_preorder(tree.left) + values_preorder(tree.right)


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


def make_binary_tree() -> tuple[BinaryTree[int], dict[str, BinaryTree[int]]]:
    nodes = {
        "root": BinaryTree(1),
        "left": BinaryTree(2),
        "right": BinaryTree(3),
        "left_left": BinaryTree(4),
        "left_right": BinaryTree(5),
        "right_left": BinaryTree(6),
    }
    nodes["root"].left = nodes["left"]
    nodes["root"].right = nodes["right"]
    nodes["left"].left = nodes["left_left"]
    nodes["left"].right = nodes["left_right"]
    nodes["right"].left = nodes["right_left"]
    return nodes["root"], nodes


def make_sorted_tree() -> BinaryTree[int]:
    root = BinaryTree(8)
    root.left = BinaryTree(
        3, BinaryTree(1), BinaryTree(6, BinaryTree(4), BinaryTree(7))
    )
    root.right = BinaryTree(10, None, BinaryTree(14, BinaryTree(13), None))
    return root


def assert_deleted_one_value(
    before: list[int],
    after_tree: BinaryTree[int] | None,
    deleted_value: int,
) -> None:
    expected = Counter(before)
    expected[deleted_value] -= 1
    if expected[deleted_value] == 0:
        del expected[deleted_value]
    assert Counter(values_preorder(after_tree)) == expected


def test_delete_node_removes_the_given_leaf_node_from_binary_tree():
    tree, nodes = make_binary_tree()
    before = values_preorder(tree)

    updated = delete_node(tree, nodes["left_right"])

    assert_deleted_one_value(before, updated, 5)


def test_delete_node_returns_none_when_deleting_the_only_node():
    tree = BinaryTree(1)

    assert delete_node(tree, tree) is None


def test_delete_node_by_value_removes_matching_leaf_from_binary_tree():
    tree, _ = make_binary_tree()
    before = values_preorder(tree)

    updated = delete_node_by_value(tree, 6)

    assert_deleted_one_value(before, updated, 6)


def test_delete_node_by_value_leaves_tree_values_unchanged_when_value_is_absent():
    tree, _ = make_binary_tree()
    before = values_preorder(tree)

    updated = delete_node_by_value(tree, 999)

    assert Counter(values_preorder(updated)) == Counter(before)


def test_delete_node_by_sorted_value_removes_leaf_from_binary_search_tree():
    tree = make_sorted_tree()

    updated = delete_node_by_sorted_value(tree, 13)

    assert inorder_values(updated) == [1, 3, 4, 6, 7, 8, 10, 14]
    assert_is_binary_search_tree(updated)


def test_delete_node_by_sorted_value_removes_node_with_two_children():
    tree = make_sorted_tree()

    updated = delete_node_by_sorted_value(tree, 3)

    assert inorder_values(updated) == [1, 4, 6, 7, 8, 10, 13, 14]
    assert_is_binary_search_tree(updated)


def test_delete_node_by_sorted_value_returns_none_when_deleting_the_only_node():
    tree = BinaryTree(1)

    assert delete_node_by_sorted_value(tree, 1) is None


def test_delete_node_by_sorted_value_leaves_tree_unchanged_when_value_is_absent():
    tree = make_sorted_tree()

    updated = delete_node_by_sorted_value(tree, 999)

    assert inorder_values(updated) == [1, 3, 4, 6, 7, 8, 10, 13, 14]
    assert_is_binary_search_tree(updated)
