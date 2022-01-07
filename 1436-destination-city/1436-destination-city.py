# mrasimzahid.github.io


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        key, val = zip(*paths)
        return list(set(val) - set(key))[0]