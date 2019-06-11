class TrieNode():
    def __init__(self):
        self.children ={}
        self.last = False
class Trie():
    def __init__(self):
        self.root = TrieNode()
        self.word_list = []

    def formTrie(self, keys):
        for key in keys:
            self.insert(key)  
    def insert(self, key):
        node = self.root
        for a in list(key):
            if not node.children.get(a):
                node.children[a] = TrieNode()
            node = node.children[a]
        node.last = True
    def search(self, key):
        node = self.root
        found = True
        for a in list(key):
            if not node.children.get(a):
                found = False
                break
            node = node.children[a]
        return node and node.last and found
    def suggestionsRec(self, node, word):
        if node.last:
            self.word_list.append(word)
        for a,n in node.children.items():
            self.suggestionsRec(n, word + a)
    def printAutoSuggestions(self, key):
        node = self.root
        not_found = False
        temp_word = ''
        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break
            temp_word += a
            node = node.children[a]
        if not_found:
            return 0
        elif node.last and not node.children:
            return -1
        self.suggestionsRec(node, temp_word)
        for s in self.word_list:
            print(s)
        return 1
keys = ["hello i am mihir","DSU sagar university","good morning qoutes", "it's going to rain now", "i am an intern", "ek tha tiger [2011] HD",
        "go goa gone[2012]HD ","avengers endgame <3", "helps", "helping","Avnegers endgame <3","arpit nariya life biography"]
key = input("hello there \nwhat do you want to search for :\n")
status = ["Not found", "Found"]
t = Trie()
t.formTrie(keys)
comp = t.printAutoSuggestions(key)
if comp == -1:
    print("No other strings found with this prefix\n")
elif comp == 0:
    print("No string found with this prefix\n")
