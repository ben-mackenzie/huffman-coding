"""
File: node.py
Author: Ken Lambert
"""

class Node(object):
    """Represents a node."""

    def __init__(self, freq = 0, char = None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        self.path = ''
