from __future__ import annotations
from typing import Dict


# Trie를 구성할 node
class Node:
    def __init__(self):
        self.children: Dict[str, Node] = {}
        # 한 단어의 끝 노드임을 나타내기 위한 변수
        self.word = False


class Trie:
    def __init__(self):
        # root node는 아무런 char도 값으로 갖지 않는다.
        self.root = Node()

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True

    def find(self, word: str):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return node.word

    def insert(self, word: str):
        node = self.root
        # 단어를 char 단위로 끊어서 반복을 돌면서
        for char in word:
            # 현재 노드의 자식 중에 char를 값으로 가지는 node가 있는지 확인
            if char not in node.children:
                # 없으면 새로운 노드를 만든다.
                node.children[char] = Node()
            # 현재 노드를 자식 노드로 옮겨준다.
            node = node.children[char]

        # 한 단어의 끝 노드라는 표식을 남긴다.
        node.word = True

    def delete(self, word: str):
        node = self.root

        def _delete(node: Node, d=0):
            if d == len(word):
                # 단어의 끝이라는 표시를 없애준다.
                node.word = False
            else:
                char = word[d]
                if char in node.children and _delete(node.children[char], d + 1):
                    del node.children[char]

            # node가 단어의 마지막 노드가 아니면서 자식 노드가 없으면 True를 반환한다.
            # 이 재귀 함수에서 유일하게 True가 반환되는 경우다.
            return not node.word and len(node.children) == 0

        _delete(node)
