import pytest

from exercises.trees.core.binary_tree import BinaryTree
from exercises.trees.search import search_iterative, search_recursive, search_sorted


def make_unsorted_tree() -> tuple[BinaryTree[int], dict[str, BinaryTree[int]]]:
    nodes = {
        "root": BinaryTree(10),
        "left": BinaryTree(4),
        "right": BinaryTree(12),
        "left_left": BinaryTree(18),
        "left_right": BinaryTree(7),
        "right_left": BinaryTree(3),
    }
    nodes["root"].left = nodes["left"]
    nodes["root"].right = nodes["right"]
    nodes["left"].left = nodes["left_left"]
    nodes["left"].right = nodes["left_right"]
    nodes["right"].left = nodes["right_left"]
    return nodes["root"], nodes


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


@pytest.mark.parametrize("search", [search_recursive, search_iterative])
def test_binary_tree_search_finds_values_anywhere_in_unsorted_tree(search):
    tree, nodes = make_unsorted_tree()

    assert search(tree, 10) is nodes["root"]
    assert search(tree, 18) is nodes["left_left"]
    assert search(tree, 3) is nodes["right_left"]


@pytest.mark.parametrize("search", [search_recursive, search_iterative])
def test_binary_tree_search_returns_none_when_value_is_absent(search):
    tree, _ = make_unsorted_tree()

    assert search(tree, 999) is None


def test_search_sorted_finds_existing_nodes_in_binary_search_tree():
    tree, nodes = make_sorted_tree()

    assert search_sorted(tree, 8) is nodes[8]
    assert search_sorted(tree, 1) is nodes[1]
    assert search_sorted(tree, 13) is nodes[13]


def test_search_sorted_returns_none_when_value_is_absent():
    tree, _ = make_sorted_tree()

    assert search_sorted(tree, 5) is None
