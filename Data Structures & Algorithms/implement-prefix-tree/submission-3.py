class TrieNode:
    def __init__(self):
        self.children = {}  # Store child nodes for each character
        self.endofword = False  # Track whether a complete word ends here


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()  # Create the root of our Trie

    def insert(self, word: str) -> None:
        cur = self.root  # Start from the root

        for c in word:  # Process each character
            if c not in cur.children:  # Check whether the character exists
                cur.children[c] = TrieNode()  # Create a node if missing

            cur = cur.children[c]  # Move to the next node

        cur.endofword = True  # Mark the end of the inserted word

    def search(self, word: str) -> bool:
        cur = self.root  # Start from the root

        for c in word:  # Check each character
            if c not in cur.children:  # Missing character means word doesn't exist
                return False

            cur = cur.children[c]  # Move to the next node

        return cur.endofword  # True only if a complete word ends here

    def startsWith(self, prefix: str) -> bool:
        cur = self.root  # Start from the root

        for c in prefix:  # Check every prefix character
            if c not in cur.children:  # Prefix doesn't exist
                return False

            cur = cur.children[c]  # Move to the next node

        return True  # Every character of the prefix exists