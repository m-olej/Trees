import sys


class Node:
    def __init__(self, value):
        # Wartosc przechowywana w wezle
        self.value = value
        # Lewy syn
        self.left = None
        # Prawy syn
        self.right = None
        self.height = 0

class Tree:

# Tree types
    def Avlmaker(self, root, elements, p, q):
        if p > q:
            return root
        else:
            mid = (p + q) // 2
            el = elements[mid]
            root = Node(el)
            root.left = self.Avlmaker(root.left, elements, p, mid - 1)
            root.right = self.Avlmaker(root.right, elements, mid + 1, q)
        # Get high returns -1 so it works
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        return root

    def Degeneratmaker(self, root, elements, cur, depth):
        root = Node(elements[cur])
        if depth>0:
            root.right = self.Degeneratmaker(root.right, elements, cur+1, depth-1)
        if root.right is None:
            root.height = 0
        else:
            root.height = root.right.height + 1
        return root

# Nie wime czy to jest potrzebne xd
    def add(self, root, value):
        if root is None:
            return Node(value)
        else:
            if root.value == value:
                return root
            elif root.value < value:
                root.height +=1
                # Rekurencyjnie będziesz szło wzdłuż gałęzi, aż nie znajdzie pusej przestrznie gdzie może wsadzić elemnt, i wtedy zwróci elemnt

                root.right = self.add(root.right, value)
            else:
                root.height += 1
                root.left = self.add(root.left, value)
        return root

#---Rotations----
    def rotate_left(self, to_rotate):
        l =  to_rotate.left
        l_r = l.right
        l.right = to_rotate
        to_rotate.left = l_r
        return l

    def rotate_right(self, to_rotate):
        r = to_rotate.right
        r_l = r.left
        r.left = to_rotate
        to_rotate.right = r_l
        return r
#---Searches-----
    def post_order_search(self, root):
        if root is not None:
            self.post_order_search(root.left)
            self.post_order_search(root.right)
            if root.value is not None:
                sys.stdout.write(str(root.value))
                sys.stdout.write(' ')
                print(root.value)

    def in_order_search(self, root):
        if root.left is not None:
            self.in_order_search(root.left)
        sys.stdout.write(str(root.value))
        sys.stdout.write(' ')
        if root.right is not None:
            self.in_order_search(root.right)

    def pre_order_search(self, root):
        if root is not None:
            sys.stdout.write(str(root.value))
            sys.stdout.write(' ')
            self.pre_order_search(root.left)
            self.pre_order_search(root.right)
# Finding Values
    def max_height(self, root):
        if root.left is not None and root.right is not None:
            left = self.max_height(root.left)
            right = self.max_height(root.right)
        elif root.left is not None:
            left = self.max_height(root.left)
            right = -1
        elif root.right is not None:
            right = self.max_height(root.right)
            left = -1
        else:
            return 0
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        return root.height

    def get_height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def min_value(self, root):
        if root is None:
            return root
        if root.left is None:
            sys.stdout.write(str(root.value))
            return root.value
        sys.stdout.write(str(root.value))
        sys.stdout.write('--->')
        return self.min_value(root.left)

    def max_value(self, root):
        if root is None or root.right is None:
            sys.stdout.write(str(root.value))
            return root.value
        sys.stdout.write(str(root.value))
        sys.stdout.write('--->')
        return self.max_value(root.right)


# Balance the tree DWS
    def degenerate(self, root):
        if root.left is not None:
            root = self.rotate_left(root)
            root = self.degenerate(root)
        elif root.right is not None:
            root.right = self.degenerate(root.right)
        return root
    def rotator(self, root, steps):
        # print(steps)
        if steps > 0:
            root.right.right = self.rotator(root.right.right, steps - 1)
            root = self.rotate_right(root)

        return root

    def log2(self, x):
        y = 1
        while x > 1:
            x >>= 1
            y <<= 1
        return y

    def balance(self, root):
        x = self.max_height(root)
        z = self.log2(x + 1)
        steps = x + 1 - z
        root = self.rotator(root, steps)
        x = x - steps
        x = x >> 1
        while x>=1:
            root = self.rotator(root, x)
            x = x >> 1

        return root
# Delete an element
    def delete(self, root, value):
        if root is None:
            return root
        if root.value < value:
            root.right = self.delete(root.right, value)
        elif root.value > value:
            root.left = self.delete(root.left, value)
        else:
            if root.left is None:
                new_root = root.right
                root = None
                return new_root
            elif root.right is None:
                new_root = root.left
                root = None
                return new_root
            new_value = self.min_value(root.right)
            root.value = new_value
            root.right = self.delete(root.right, new_value)
        return root

# Delete whole tree
    def delete_all(self, root):
        if root is None:
            return root
        if root is not None:
            root.left = self.delete_all(root.left)
            root.right = self.delete_all(root.right)
        return None


#Print the tree
    def printer(self, cur, indent, last):
        if cur is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R---")
                indent+="   "
            else:
                sys.stdout.write("L---")
                indent += "|   "
            print(cur.value)
            self.printer(cur.left, indent, False)
            self.printer(cur.right,indent, True)






