# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root

        if not prefix:
            current_node = -1

        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return -1

        return current_node


# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def suffixes(self):
        # Recursive function that collects the suffix for
        # all complete words below this point
        suffix_list = []

        for child in self.children:
            suffix_list.extend(self.children[child].suffix_recur(child))

        return suffix_list

    def suffix_recur(self, suffix):
        suffix_list = []

        if self.is_word:
            suffix_list.append(suffix)

        for child in self.children:
            suffix_list.extend(self.children[child].suffix_recur(suffix+child))

        return suffix_list


# Tests
# Add words
valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their', 'byee', 'byebyebye']
word_trie = Trie()
for valid_word in valid_words:
    word_trie.insert(valid_word)

print('[Edge Case]')
print(word_trie.find('zzz'))
print()
# -1

print('[Edge Case]')
print(word_trie.find(''))
print()
# -1

prefix = word_trie.find('bye')
for element in prefix.suffixes():
    print(element)
print()
# 'e', 'byebye'

print(word_trie.find('any'))
print()
# <__main__.TrieNode object>

valid_words = ['and', 'aardvark', 'ardor', 'abreast', 'about', 'abdominal', 'anchor']
word_trie2 = Trie()
for valid_word in valid_words:
    word_trie2.insert(valid_word)

prefix = word_trie2.find('a')
for element in prefix.suffixes():
    print(element)
print()
# 'e', 'byebye'
