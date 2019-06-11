from tkinter import *

def SOUT():
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
                    la.insert(END,(s + "\n"))
            return 1
    file = open('dictionary.txt','r')
    lines=file.readlines()
    keys=[]
    for data in lines:
        keys.append(data.strip())
    key = entry.get()
    status = ["Not found", "Found"]
    t = Trie()
    t.formTrie(keys)
    comp = t.printAutoSuggestions(key)
    if comp == -1:
       la.insert(INSERT, "No other strings found with this prefix")
    elif comp == 0:
        la.insert(INSERT, "No string found with this prefix")


window=Tk()
topframe=Frame(window)
la1=Label(topframe,text="please enter the key:")
la1.pack()
entry=Entry(topframe)
entry.pack()
button=Button(topframe,text="search",command=SOUT) 
button.pack()
topframe.pack(side = TOP)
bottomframe= Frame(window)
scroll=Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)
la=Text(bottomframe, width=100, height=20, yscrollcommand =scroll.set)
scroll.config(command=la.yview)
la.pack(side=LEFT, fill=BOTH, expand=1)
bottomframe.pack()
window.mainloop()
