# Klasa reprezentujaca pojedynczy wezel drzewa
# Każdy Korzeń reprezentuje drzewo 
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
            self.height = 0

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

    def MakeAvl(self, array):
        arra = array[:]
        arra.sort()
        arr = binarySplit(arra)
        for x in arr:
            self.add(x)
        return self
    
    def MakeBst(self, array):
        for x in array:
            self.add(x)
        return self
    
    def MakeDegen(self, array):
        arr = array[:]
        arr.sort()
        for x in arr:
            self.add(x)
        return self
    
    def getMin(self):
        if self.left is None:
            global minVal, minValHeight
            minVal = self.value
            minValHeight = self.height
        else:
            print(f"{self.value} - {self.height}")
            self.left.getMin()
        return f"{minVal} - {minValHeight}"
    
    def getMax(self):
        if self.right is None:
            global maxVal, maxValHeight
            maxVal = self.value
            maxValHeight = self.height
        else:
            print(f"{self.value} - {self.height}")
            self.right.getMax()
        return f"{maxVal} - {maxValHeight}"
    
    def heightElements(self):
        totalHeight = self.getHeight()
        heightElements = {}
        for i in range(totalHeight+1):
            heightElements[f"height-{i}"] = []
        return heightElements
    
    #idzie in-order przez elementy więc zapisuje jakie elementy
    #będą od lewej do prawej. Idealnie, żeby wyprincić B)
    def assignHeight(self, hDict):
        hDict[f"height-{self.height}"] += [self.value]
        if self.left:
            self.left.assignHeight(hDict)
        if self.right:
            self.right.assignHeight(hDict)
        return hDict
    
    # fills tree with 0-nodes so it can be printed prettily #
    def treeFiller(self):
        totalHeight = self.getHeight()
        if self.left is None and self.height < totalHeight:
            self.left = Node(0)
            self.left.height = self.height + 1
        elif self.height < totalHeight:
            self.left.treeFiller()
        if self.right is None and self.height < totalHeight:
            self.right = Node(0)
            self.right.height = self.height + 1
        elif self.height < totalHeight:
            self.right.treeFiller()




    # only run for AVL TREES!!!! #
    def prettyPrint(self):
        totalHeight = self.getHeight()
        for x in range(totalHeight):
            self.treeFiller()
        hDictEmpty = self.heightElements()
        hDict = self.assignHeight(hDictEmpty)
        width = 2 ** (totalHeight+2)
        level = 1
        for k, v in hDict.items():
            if sum(v) == 0:
                break
            widthT = int(width/level)
            level *= 2
            if k == f"height-{totalHeight+1}":
                return "Here's your tree!"
            else:
                print(f"{k}", end="\t")
                print("|", end="")
                for val in v:
                    print(f"{str(val):^{widthT}}", end="")
                print("|")
        return "Here's your tree!"

    #---Degenerate Tree printer---#
    def degPrint(self):
        totalHeight = self.getHeight()
        self.treeFiller()
        hDictEmpty = self.heightElements()
        hDict = self.assignHeight(hDictEmpty)
        level = 5
        for k, v in hDict.items():
            if sum(v) == 0:
                break
            level += 1
            print(f"{k}|", end="\t")
            print(f"{str(v[-1]):>{level}}")


    def preOrderList(self, elList=[]):
        if self is None:
            return "This tree doesn't exist"
        if self.value:
            elList.append(self.value)
        if self.left:
            self.left.preOrderList(elList)
        if self.right:
            self.right.preOrderList(elList)
        return elList
    
    def inOrderList(self, elList=[]):
        if self is None:
            return "This tree doesn't exist"
        if self.left:
            self.left.inOrderList(elList)
        if self.value:
            elList.append(self.value)
        if self.right:
            self.right.inOrderList(elList)
        return elList
    
    def delNode(self, val, ifRoot=1):
        if ifRoot == 1:
            global elInOrderList
            elInOrderList = self.inOrderList()
        if self.value == val:
            #---No children, because last level of tree---#
            if self.height == self.getHeight():
                self.value = 0
                return
            #---If no children---#
            elif self.left.value == 0 and self.right.value == 0 :
                self.value = 0
                return 
            #---If left Child only---#
            elif self.left.value and self.right.value == 0:
                self.value = self.left.value
                self.left.value = 0
                return
            #---If only right Child---#
            elif self.right.value and self.left.value == 0:
                self.value = self.right.value
                self.right.value = 0
                return
            #---If both Children---#
            elif self.right.value and self.left.value:
                print(elInOrderList)
                oldNodeIndex = elInOrderList.index(val)
                newNode = elInOrderList[oldNodeIndex - 1]
                print(newNode)
                self.value = newNode
                self.left.delNode(newNode)
                return
        if self.value < val:
            self.right.delNode(val, 0)
        if self.value > val:
            self.left.delNode(val, 0)
        return f"Deleted {val}"
        
    
            

                


#Makes an IN-ORDER list
def binarySplit(array, binList=[]):
    arr = array[:]
    if len(arr) < 1:
        return []
    middle_index = len(arr) // 2
    middle_element = arr.pop(middle_index)
    left_half = arr[:middle_index]
    right_half = arr[middle_index:]
    binList = [middle_element] + binarySplit(left_half, binList) + binarySplit(right_half, binList)
    return binList


# Rekurencyjne przeszukiwanie drzewa
#IN-ORDER
def search(node):
    if node.left is not None:
        search(node.left)
    print(node.value)
    if node.right is not None:
        search(node.right)



    

testList = [x for x in range(1, 41)]
testList2 = [6, 4, 3, 7, 2, 10, 5, 9, 10]
degTest = [x for x in range(1, 16)]

inTest = [6,5,4,3,2]

# --- TEST ZONE --- #

root1 = Node()
root2 = Node()
root3 = Node()
root4 = Node()

avl = root1.MakeAvl(testList)
avl2 = root3.MakeAvl(testList2)
bst = root2.MakeBst(degTest)

inAvl = root4.MakeAvl(inTest)

# print(avl)
# print(avl.getHeight())
# print(avl.getNumNodes())
# print("- "*10)
# print(bst)
# print(bst.getHeight())
# print(bst.getNumNodes())

# print(avl.getMin())
# print(minVal)
# print(bst.getMin())
# print(minVal)
# avl.add(9.5)
# print(avl.prettyPrint())
# # print(avl.inOrderList())
# avl.delNode(3)
# print(avl.prettyPrint())
# avl2.prettyPrint()
# bst.degPrint()
# bst.delNode(15)
# bst.degPrint()
# avl.prettyPrint()
# avl.delNode(4)
# avl.prettyPrint()
# avl.delNode()
# avl.prettyPrint()
# print("\n")
avl2.prettyPrint()
# print("\n")
# avl2.delNode(4)
# avl2.delNode(7)
# avl2.prettyPrint()
# bst.degPrint()

inAvl.prettyPrint()
