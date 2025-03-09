from collections import defaultdict


class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        tree = defaultdict(list)
        for edge in edges:
            source, target = edge
            tree[source].append(target)
            tree[target].append(source)

        bob_path = [0] * len(amount)
        bob_path[bob] = 1
        cnt = 1
        def dfs_bob(par_node, cur_node):
            nonlocal cnt
            if cur_node == 0:
                return True

            for next_node in tree.get(cur_node):
                if next_node == par_node:
                    continue

                if dfs_bob(cur_node, next_node):
                    bob_path[next_node] = 1
                    cnt += 1
                    return True

        dfs_bob(None, bob)

        result = float("-inf")
        def dfs(parent, cur_node, score, d):
            nonlocal result

            is_leaf = True

            for next_node in tree[cur_node]:
                if parent == next_node:
                    continue
                cost = amount[next_node]
                if bob_path[next_node]:
                    if cnt//2 <= d:
                        if cnt/2 % d == 0.5:
                            print("!")
                            cost //= 2
                        else:
                            cost = 0

                is_leaf = False

                dfs(cur_node, next_node, score + cost, d + 1)

            if is_leaf:
                result = max(result, score)

        amount[bob] = 0
        dfs(None, 0, amount[0], 1)

        return result
