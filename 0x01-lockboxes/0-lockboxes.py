#!/usr/bin/python3
"""
    Lockboxex
"""


def canUnlockAll(boxes):
    """
       Returns true if all boxes can be opened
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    while keys:
        current = keys.pop()
        for key in boxes[current]:
            if not opened[key]:
                opened[key] = True
                keys.append(key)
    return all(opened)
