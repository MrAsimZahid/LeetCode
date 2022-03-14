# mrasimzahid.github.io

# Time: O(n)

# Technique: Stack

class Solution:
    def simplifyPath(self, path: str) -> str:
        path_split = path.split("/")
        res_list = []
        for each in path_split:
            if "" == each:
                continue
            elif "." == each:
                continue
            elif ".." == each:
                if res_list:
                    res_list.pop()
            else:
                res_list.append(each)
        return "/" + "/".join(res_list)
               
