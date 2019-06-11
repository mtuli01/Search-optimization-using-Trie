# Search-optimization-using-Trie

Introduction:-
The current level of development in search optimization is fairly complicated, yet interesting as well. In this project, we were supposed to develop a search optimization technique. An autocomplete system is a perfect use case. Many of the websites use this feature to help there users with suggestions & autocomplete. Also, in this post we will define a Trie interface and then work through this 


As we know from the previous text that a Trie is a tree like data structure which stores words such that the search for a word is proportional to the length of the word. Imagine a situation where a user is typing a word and he is mid way through. If you want to display all possible suggestions which he could have meant, then you need to find all the  words which starts with that prefix. This is one class of problems which Trie is meant to solve. When the user starts typing, we initialize a character buffer which serves as a prefix. And every time there is a new character we append it to the prefix and search our Trie for the prefix. If the prefix exists, we return all the words followed by that.


Trie is an efficient information retrieval data structure. Using Trie, search complexities can be brought to optimal limit (key length). If we store keys in binary search tree, a well balanced BST will need time proportional to M * log N, where M is maximum string length and N is number of keys in tree. Using Trie, we can search the key in O(M) time. However the penalty is on Trie storage requirements 
Every node of Trie consists of multiple branches. Each branch represents a possible character of keys. We need to mark the last node of every key as end of word node. A Trie node field is end of word is used to distinguish the node as end of word node.


Without the use of a proper search optimization technique a user is unable to find the specific topic he/she is looking for in certain search.Earlier without a auto complete search feature a search can not be completey conducted without knowing complete keyword of the search.

Disadvantage of Trie:-
The main disadvantage of tries is that they need lot of memory for storing the strings. For each node we have too many node pointers(equal to number of characters of the alphabet), If space is concern, then Ternary Search Tree can be preferred for dictionary implementations. In Ternary Search Tree, time complexity of search operation is O(h) where h is height of the tree. Ternary Search Trees also supports other operations supported by Trie like prefix search, alphabetical order printing and nearest neighbor search.

Now with every input given by the user is given some choices which can help reducing the time and give user what he is looking for.
With Trie, we can insert and find strings in O(L) time where L represent the length of a single word. This is obviously faster that BST. This is also faster than Hashing because of the ways it is implemented. We do not need to compute any hash function. No collision handling is required (like we do in open addressing and separate chaining).

Another advantage of Trie is, we can easily print all words in alphabetical order which is not easily possible with hashing.

We can efficiently do prefix search (or auto-complete) with Trie


The program is implemented entirely in Python. User experience (UX) has become a large industry and many companies are now looking specifically for UX engineers. Autocomplete has been one piece of UX that seems to be everywhere now; from our phones to the web browser. It doesn’t seem like a technology that is necessarily difficult or complex to implement. From many aspects I think that is true, however, if you’re trying to optimize performance or do fuzzy matching then it can become very slow very quickly. Let’s say for example we’re building a feature that is similar to the Google search bar. As you type words, it gives you suggestions based on what you’ve typed so far.
 
you’re not shown just any random words. Google has a way of weighting each suggestion as a next word. In practice, there would likely be some dynamic weighting based on sentence structure, but let’s assume for the purpose of this post that each word has a simple weighting based on how common it is.

When thinking about ways to solve this problem, you may think of a couple things. We could sort the list of words, and then iterate through all the words starting with the first character. Of course, that would be very slow, O(n) if n is the number of words in our dictionary. We can do better than that! What about a database? Could we store each word in a database and do a query like so?

We could do that, however, then we’ll need to properly index the database and maintain it. What if I told you we can do this in less than 100 lines of Python? And what if I told you we can store every word in with less than 500MB of memory? I’m here to tell you, it’s possible! Let’s go back to our original example of sorting our list of words and iterating through all the words starting with the first character of our word. How would we know where to start? Well, if we used a dictionary we could store the first letter of each word (26 lowercase characters, excluding punctuation) as the key and then each word as a list under it. That’s a good start! We can still do better though! What if we then used a similar structure for each character in each of those words? We’d get a structure similar to this:

 
What is trie ?
This data structure is called a “Trie”. It’s very similar to a tree where each node stores a single character. At most, each node will store 26 children keys. Seems straightforward enough right? Let’s first look at how we can add words to our Trie data structure then look into how to query it.
Python 3 introduced the __slots__ class level attribute which does not use an internal __dict__ for storing attributes. This reduces the memory needed for each class as well as makes attribute lookups much faster. When writing this article the memory used without __slots__ was almost 900MB. After using __slots__ it decreased to just over 500MB. Our TrieNode class will just have a value, end_of_word, children, and weight attributes. To add a new word, we’ll look at the word character by character. For the word “foo”, we could think of our path as root -> “f” -> “o” -> “o”. Where each “->” denotes a child access. As we recurse through each character node, we take off one character after each level. Finally, when we are at the last character, we mark it as the end of the word.
How do we actually query our Trie? This is the most complicated part in my opinion. We need to keep two lists; one that is of the characters we haven’t seen yet and the characters we have seen so far.



 
