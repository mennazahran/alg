#!/usr/bin/env python
# coding: utf-8

# In[28]:


# Insertion Sort


def insertionSort(arr):

  
   for i in range(1, len(arr)):

       
       key = arr[i]
       
   
       j = i-1
      
       while j >=0 and key < arr[j] :
               arr[j+1] = arr[j]
               j -= 1
       arr[j+1] = key



arr = [10, 11, 15, 6, 4]
insertionSort(arr)
print(arr)


# In[27]:


# merge sort

def mergeSort(myList): # Insertion Sort


def insertionSort(arr):

   
    for i in range(1, len(arr)):

        
        key = arr[i]
        
    
        j = i-1
       
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key



arr = [10, 11, 15, 6, 4]
insertionSort(arr)
print(arr)


    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

       
        mergeSort(left)
        mergeSort(right)

        
        i = 0
        j = 0
        
       
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              
              myList[k] = left[i]
             
              i += 1
            else:
                myList[k] = right[j]
                j += 1
           
            k += 1

        
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [54,30,93,20,77,60,44,15,40]
mergeSort(myList)
print(myList)


# In[29]:


# kruskal


class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []
 
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
 
 
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
 
    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
  
    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("Edge:",u, v,end =" ")
            print("-",weight)
 
 
g = Graph(5)
g.add_edge(0, 1, 8)
g.add_edge(0, 2, 5)
g.add_edge(1, 2, 9)
g.add_edge(1, 3, 11)
g.add_edge(2, 3, 15)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 7)
g.kruskal()


# In[ ]:




