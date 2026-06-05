from .core.binary_tree import BinaryTree


def delete_node(tree: BinaryTree[int], node: BinaryTree[int]) -> BinaryTree[int] | None:
    """
    Delete a node from the binary tree.

    Args:
        tree: The binary tree to delete from.
        node: The node to delete.

    Returns:
        The updated binary tree after deletion, or None if the tree is empty.
    """
    raise NotImplementedError()


def delete_node_by_value(tree: BinaryTree[int], value: int) -> BinaryTree[int] | None:
    """
    Delete a node from the binary tree by its value.

    Args:
        tree: The binary tree to delete from.
        value: The value of the node to delete.

    Returns:
        The updated binary tree after deletion, or None if the tree is empty.
    """


def delete_node_by_sorted_value(
    tree: BinaryTree[int], value: int
) -> BinaryTree[int] | None:
    """
    Delete a node from the binary tree by its sorted value.

    Args:
        tree: The binary tree to delete from.
        value: The sorted value of the node to delete.

    Returns:
        The updated binary tree after deletion, or None if the tree is empty.
    """
    raise NotImplementedError()
