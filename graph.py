class Graph:
    class Node: 
        def __init__(self, string):
            self.string = string
            self.neighbors = []
        def add_neighbor(self,node):
            if node not in self.neighbors:
                self.neighbors.append(node)
        
    def __init__(self, words):
        self.nodes = []
        for word in words:
            node = self.Node(word)
            self.nodes.append(node)
    
    def check_edge(self,word1, word2):
        temp_word = word2
        last_four = word1[1:]
        for char in last_four:
            if char not in temp_word:
                return False
            temp_word = temp_word.replace(char,'', 1)
        return True
    
    def find_edges(self):
        for node1 in self.nodes:
            for node2 in self.nodes:
                if node1 != node2:
                    if self.check_edge(node1.string, node2.string):
                        node1.add_neighbor(node2)
                        
    def shortest_path(self, word1, word2):
        for node in self.nodes:
            if node.string == word1:
                return self.bfs(node, word2)
                
    def bfs(self, start, final_string):
        if start.string == final_string:
            return "0"
        
        q = [start]
        visited = {node: False for node in self.nodes}
        pred = {node: None for node in self.nodes}

        while q:
            v = q.pop(0)
            for w in v.neighbors:
                if not visited[w]:
                    visited[w] = True
                    q.append(w)
                    pred[w] = v
                if w.string == final_string:
                   return self.count_path(pred, w, start)
                    
        return "Impossible"
    
    def count_path(self, pred, w, start):
        count = 0
        current = w
        while current != start:
            count += 1
            current = pred[current]
        return count
                    
                
            
            
        
        
        
                
        
                    
                
                    
                
                
    
                    
                        
    

        

    
    
            
