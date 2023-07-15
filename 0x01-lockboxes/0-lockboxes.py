#!/usr/bin/python3
"""A method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """this method creates a system that can keep track of the
     boxes open and groups them into a stack which is later
     popped till empty"""
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)