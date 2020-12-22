keys = ["le","lee","leet","code"]

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = {}
        self.isEnd = False
        
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tempNode = self
        for i in word:
            if i not in tempNode.node: 
                newNode = Trie()
                tempNode.node[i] = newNode
                tempNode = newNode
            else:
                tempNode = tempNode.node[i]
                
        tempNode.isEnd = True
            
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tempNode = self        
        for i in word:
            if i not in tempNode.node:
                return False
            else:
                tempNode = tempNode.node[i]
        if tempNode.isEnd == True:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tempNode = self        
        for i in prefix:
            if i not in tempNode.node:
                return False
            else:
                tempNode = tempNode.node[i]
        return True
        

root = Trie()
for i in keys:
    root.insert(i)

#for i in keys:
#    print(root.search(i))
    
print(root.search("co"),"cdddddddd")    
print(root.startsWith("co"),"************")
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)