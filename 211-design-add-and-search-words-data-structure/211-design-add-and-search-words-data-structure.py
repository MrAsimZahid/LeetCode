# mrasimzahid.github.io

class WordDictionary:

    def __init__(self):
        # self.index = []
        self.content = collections.defaultdict(list)

    def addWord(self, word: str) -> None:
        if word:
            self.content[len(word)].append(word)
        
        # len_word = len(word)
        # if self.content.get(len_word):
        #     list_data = self.contetnt[len(word)]
        # else: 
        #     list_data = []
        # self.content[len_word] = list_data.append(word)


    def search(self, word: str) -> bool:
        len_word = len(word)
        if not word:
            return False
        if "." not in word:
            return word in self.content[len_word]
        for each in self.content[len_word]:
            flag = True
            for index, char in enumerate(word):
                if char != each[index] and char != ".":
                    flag = False
                    break
            if flag:
                return True
        return False
        
        # index = []
        # for i in range(len_data):
        #     if word[i] is ".":
        #         index.append(i)
        # word = word.replace(".", "")
        # for each in self.content.get(len_data):
        #     for i in reverse(index):
        #         each.pop(i)
        #     if each is word:
        #         return True
        # return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)