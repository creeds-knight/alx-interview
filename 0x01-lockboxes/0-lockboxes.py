#!/usr/bin/python3
"""
    Lockboxex
"""


def canUnlockAll(boxes):
    """
       Returns true if all boxes can be opened
    """
    if not boxes:
        return False

    opened = set()

    n = len(boxes)
    keys = [0]

    while keys:
        current = keys.pop()
        if current not in opened:
            opened.add(current)
            for key in boxes[current]:
                if key < n:
                    keys.append(key)
    return (len(opened) == n)
