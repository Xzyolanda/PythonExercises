from dataclasses import dataclass


@dataclass
class BinaryTree[T]:
    value: T
    left: "BinaryTree[T] | None" = None
    right: "BinaryTree[T] | None" = None
