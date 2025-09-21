class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        path_set = set(folder)
        ans = []
        for path in folder:
            for i, char in enumerate(path):
                if char == "/" and path[:i] in path_set:
                    break
            else:
                ans.append(path)
        return ans
































s = Solution()
print(s.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(s.removeSubfolders(["/a","/a/b/c","/a/b/d"]))
print(s.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))


