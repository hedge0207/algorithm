from typing import Dict


class Node:
    def __init__(self):
        self.children: Dict[str, Node] = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True

    def search(self, word: str):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return node.word

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.word = True