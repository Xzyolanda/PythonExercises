from .core.binary_tree import BinaryTree


def search_recursive(tree: BinaryTree[int], value: int) -> BinaryTree[int] | None:
    """
    Recursively search for a value in the binary tree.

    Args:
        tree: The binary tree to search.
        value: The value to search for.

    Returns:
        The node containing the value, or None if not found.
    """
    raise NotImplementedError()


def search_iterative(tree: BinaryTree[int], value: int) -> BinaryTree[int] | None:
    """
    Iteratively search for a value in the binary tree.

    Args:
        tree: The binary tree to search.
        value: The value to search for.

    Returns:
        The node containing the value, or None if not found.
    """
    raise NotImplementedError()


def search_sorted(tree: BinaryTree[int], value: int) -> BinaryTree[int] | None:
    """
    Search for a value in a sorted binary tree.

    Args:
        tree: The binary tree to search.
        value: The value to search for.

    Returns:
        The node containing the value, or None if not found.
    """
    raise NotImplementedError()
