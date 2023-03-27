from binarytree import build


# Klasa reprezentujaca pojedynczy wezel drzewa
class Node:
    def __init__(self, value=None):
        # Wartosc przechowywana w wezle
        self.value = value
        # Lewy syn
        self.left = None
        # Prawy syn
        self.right = None
        # Wysokość na jakiej znajduje się wartość
        self.height = 0
    
    def __str__(self) -> str:
        return f"Wartość: [{self.value}] - {self.height}, Dzieci: Lewe: \n {self.left} \t Prawe: {self.right} \n " 
    
    # --- Dodaje i ustala na jakiej wysokości jest każdy element --- #
    def add(self, value, height=0):
        if self.value:
            height += 1
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                    self.left.height = height
                else:
                    self.left.add(value, height)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)    
                    self.right.height = height
                else:
                    self.right.add(value, height)
        else:
            self.value = value

    def getHeight(self, heightList = []):
        if self.left is None and self.right is None:
            heightList.append(self.height)
        if self.left:
            self.left.getHeight(heightList)
        if self.right:
            self.right.getHeight(heightList)
        return max(heightList)
    
    # --- oblicza ilość elementów w drzewie --- #
    def getNumNodes(self):
        total = 0
        if self.left:
            total += self.left.getNumNodes()
        if self.right:
            total += self.right.getNumNodes()
        return total + 1


# Rekurencyjne przeszukiwanie drzewa
#IN-ORDER
def search(node):
    if node.left is not None:
        search(node.left)
    print(node.value)
    if node.right is not None:
        search(node.right)


test = [1,2,3,4,5,6,7,8,9,10,11,12]

#Makes an IN-ORDER list
def binarySplit(arr):
    if len(arr) < 1:
        return []
    middle_index = len(arr) // 2
    middle_element = arr.pop(middle_index)
    left_half = arr[:middle_index]
    right_half = arr[middle_index:]
    return binarySplit(right_half) + binarySplit(left_half) + [middle_element]

def CreateAVLTree(arr):
    arr.sort()
    binList = binarySplit(arr)
    binList.reverse()
    root = Node()
    for n in binList:
        root.add(n)
    return root

def CreateTree(arr):
    root = Node()
    for n in arr:
        root.add(n)
    return root
    
def printTree(root):
    

testList = [1,2,3,4,5,6,7,8,9,10,11,12]
testList2 = [x for x in range(40)]

avl = CreateAVLTree(testList)










# # Korzen drzewa
# root = Node(7)
# # Dodajemy dzieci "recznie"
# root.left = Node(4)
# root.right = Node(9)
# root.left.right = Node(5)

# # Przeszukujemy drzewo w kolejnosci in-order
# search(root)

