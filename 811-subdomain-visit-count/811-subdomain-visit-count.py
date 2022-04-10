# mrasimzahid.github.io

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = collections.Counter()
        for cpdomain in cpdomains:
            num, domain = cpdomain.split()
            count[domain] += int(num)
            for i in range(len(domain)):
                if domain[i] == ".":
                    count[domain[i+1:]] += int(num)
        return [f"{count[val]} {val}" for val in count]
