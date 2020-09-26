import math


class BTree:

    class _Node:
        """
        Nested Class that implements Exercise1 Node
        """
        __slots__ = '_elements', '_children', '_last', '_parent'

        def __init__(self, last=True, parent = None):
            self._elements = []  # Contains tuples (key, value)
            self._children = []  # Contains Node's children
            self._parent = parent  # Node Parent
            self._last = last  # Parameter that shows if the Node is in the last raw of the Tree

        def _is_last(self):
            return self._last

    __slots__ = '_d', '_root'

    def __init__(self, d):
        self._d = d   # d of the Exercise1, from which derive both a and B
        self._root = None  # root of the Tree

    def insert(self, key, value):
        if self._root is None:  # If there is not a root
            self._root = self._Node()  # Creates a root as a new Node
            self._root._elements.append((key, value))  # Then a tuple (key, value) is inserted inside Node's elements
        else:
            self._insert_element(self._root, key, value)  # If there's a root yet, a support function is called

    def _insert_element(self, node, key, value):
        """
        Support function, that implements the insertion af a tuple (key, value)
        :param node:
        :param key:
        :param value:
        :return:
        """
        if node._is_last():  # if the node is in the last row
            position, check = self._binary_search_check(key, node._elements, 0, len(node._elements))  # find the right position in which tuple has to be stored
            node._elements.insert(position, (key, value))  # insert he tuple
            if len(node._elements) == self._d and node._parent is None:   # if the maximum number of keys is reached and the node is the root (it has no parent)
                new_root = self._Node(False)  # create a ew root
                old_root = self._root  # make a copy of the old root
                self._root = new_root  # assign the new root to the tree
                old_root._parent = self._root  # assign the new root as parent of the old one
                new_root._children.insert(0, old_root)  # insert the old root between new one's children
                self._split(self._root._children[0])  # call the support function, that performs, split
        else:
            # find the child in which I have to insert the tuple
            i = len(node._elements) - 1
            while i >= 0 and key < node._elements[i][0]:
                i -= 1
            i += 1

            # make the insertion and verify if the maximum number of keys is reached; then this is made also for the root, craeting a new root if needed
            self._insert_element(node._children[i], key, value)
            if len(node._children[i]._elements) == self._d:
                self._split(node._children[i])
            if len(self._root._elements) == self._d:
                new_root = self._Node(False)
                old_root = self._root
                self._root = new_root
                old_root._parent = self._root
                old_root._last = False
                new_root._children.insert(0, old_root)
                self._split(self._root._children[0])


    def _split(self, node):
        """
        Support function that implements split on a node that has reached the maximum number of keys
        :param node: node to be splitted
        :return:
        """
        a = math.ceil(self._d / 2)  # minimum number of child in a Exercise1
        node2 = self._Node(node._is_last(), node._parent)  # create a new node, in which I will store elements, after splitting
        node2._elements = node._elements[a: (self._d)]  # insert elements in node2
        index = node._parent._children.index(node) + 1
        node._parent._children.insert(index, node2)  # update children inside node's parent, adding node2
        position, check = self._binary_search_check(node._elements[a-1][0], node._parent._elements, 0, len(node._parent._elements))
        node._parent._elements.insert(position, node._elements[a-1])  # update keys inside node's parent, after finding the right position
        node._elements = node._elements[0: (a - 1)]  # update node's elements, deleting the one stored in node2
        if not node._is_last():  # if node is not in the last row
            node2._children = node._children[a: 2*a]  # update node2 children
            for n in node2._children:  # update node2 children's parent
                n._parent = node2
            node._children = node._children[0:a]  # update node children

    def search(self, key):
        """
        Function that returns the value associated to the key, if it is inside the Exercise1, else None
        :param key: Key to search
        :return: The value associated to the key, if the it is inside the Exercise1, and the node in which the key is located
        """
        if self._root is None:  # if the Exercise1 is empty, return None
            return None, None
        else:  # search if the key is inside the root
            pos, check = self._binary_search_check(key, self._root._elements, 0, len(self._root._elements) - 1)
            if check:  # if the binary search has found the key in the root
                print(self._root._elements[pos - 1][1])
                return self._root, pos
            elif not self._root._is_last(): # if the root has some children
                return self._search_children(self._root, key)
            else: # the root has no children, so the key is not inside the Exercise1
                print("Element not found")
                return None, None


    def _search_children(self,node, key):
        """
        Support function to find a key inside the children of node
        :param node:
        :param key:
        :return: the value associated to the key, if the it is inside the Exercise1, and the node in which the key is located
        """
        if key < node._elements[0][0]:  # if the key is less than the minimum key between the keys of the children
            find_node, pos, check = self._search_element(node._children[0], key)  # search the element in the first child
            if check:   # if the key is found
                print(find_node._elements[pos][1])
                return find_node, pos
            elif not find_node._is_last(): # if the key is not found, but node's child has some children, i search recursively on them
                return self._search_children(find_node, key)
            else:  # the key is not inside the Btree
                print("Element not found")
                return None, None
        elif key > node._elements[- 1][0]: # if the key is greater than the maximum key between the keys of the children
            find_node, pos, check = self._search_element(node._children[len(node._elements)], key)  # search the element in the last child
            if check:   # if the key is found
                print(find_node._elements[pos][1])
                return find_node, pos
            elif not find_node._is_last():  # if the key is not found, but node's child has some children, i search recursively on them
                return self._search_children(find_node, key)
            else:  # the key is not inside the Btree
                print("Element not found")
                return None, None
        else:  # search the key in the middle children
            i = 1
            while i < len(node._elements) - 1 and key < node._elements[i][0]:  # search the position in which the key can be
                i += 1
            find_node, pos, check = self._search_element(node._children[i], key)  # call the search on the i-th child
            if check:  # if the key is found
                print(find_node._elements[pos][1])
                return find_node, pos
            elif not find_node._is_last():  # if the key is not found, but node's child has some children, i search recursively on them
                return self._search_children(find_node, key)
            else:  # the key is not inside the Btree
                print("Element not found")
                return None, None

    def _search_element(self, node, key):
        """
        Support function that performs a binary search on the elements of a node
        :param node:
        :param key:
        :return: The key in which the node has to be, the position and a boolean that indicates if the key is found
        """
        pos, check = self._binary_search_check(key, node._elements, 0, len(node._elements) - 1)
        return node, pos, check

    def _binary_search_check(self, key, sequence, left, right):
        """
        Support function that implements Binary search
        :param key:
        :param sequence:
        :param left:
        :param right:
        :return:
        """
        if left == right:
            if len(sequence) > right:
                if sequence[right][0] == key:
                    return right, True
                else:
                    return right, False
            else:
                return right, False
        else:
            pivot = math.floor((left + right) / 2)
            if key == sequence[pivot][0]:
                return pivot, True
            elif key > sequence[pivot][0]:
                return self._binary_search_check(key, sequence, left=pivot + 1, right=right)
            else:
                return self._binary_search_check(key, sequence, left, right=pivot)

    def before(self, key):
        """
        Support function that returns the predecessor af an element for the Remove function
        :param key:
        :return: The node in which the predecessor is stored and the predecessor
        """
        if self._root is None:  # If the Exercise1 is empty, return None
            print("No element found")
            return None, None

        find, pos = self.search(key)  # Verify if the key is inside the tree

        if find is None:  # if the key is not inside the Exercise1, return None
            print("No element found")
            return None, None
        else:
            if find._is_last(): # NON ANCORA IMPLEMENTATO, DATO CHE NON SERVE PER LA REMOVE
                return None, None
            else:
                new = find._children[pos]
                while not new._is_last():
                    new = new._children[- 1]
                return new, new._elements[- 1]

    def remove(self, key, node=None, pos=None):
        """
        Function that performs the deletion of key if it is inside the Exercise1

        :param key:
        :param node:
        :param pos:
        :return:
        """
        node_discovered, pos_discovered = self.search(key)  # search for the key inside the Exercise1
        if node_discovered is not None:  # if node_discovered is None, but the key is inside the tree, it has been swapped with his predecessor, so node, pos are passed to the function by a recursive call
            node, pos = node_discovered, pos_discovered
        a = math.ceil((self._d) / 2)
        if node is None: # if node is None after all, the key is not inside the tree
            print("The key is not inside the Tree")
        elif node._is_last():  # if the key is in the last row
            if len(node._elements) > a - 1:  # if the node has a number of keys grater than a, i can simply delete the element
                node._elements.pop(pos)
            else:
                index = node._parent._children.index(node)
                if index > 0:
                    sibling = node._parent._children[index - 1]
                else:
                    sibling = node._parent._children[index + 1]
                if len(sibling._elements) < self._d - 1:  # if the sibling has a number of children lower than d-1, I can use fusion on it
                    node._elements.pop(pos)  # so the element is removed
                    self._fusion(node, sibling, index, a)  # and the fusion is called
                else: # perform a transfer
                    node._elements.pop(pos)
                    self._transfer(node, sibling, index)
        else:  # if the key is not in the last row, i have to swap it with his predecessor
            node_before, element = self.before(key)  # search the predecessor of the node
            to_remove = node._elements.pop(pos)  # remove the element from from the node
            new_index = node_before._elements.index(element)  # take the index of the predecessor inside his node
            node_before._elements.pop(new_index)  # remove the predecessor
            node_before._elements.insert(new_index, to_remove) # and put it in the node of the element that has to be deleted
            node._elements.insert(pos, element)  # insert the predecessor inside his new node
            return self.remove(key, node_before, new_index)  # call the remove recursively on the node in which I store the key that has to be deleted.
            # the function takes also the index of the key inside the new node


    def _fusion(self, node, sibling, index, a):
        """
        Support function that implements fusion operation in case of underflow after a deletion
        :param node: node with underflow
        :param sibling: Left sibling of the node, if it exists, first right one otherwise
        :param index: Index of the node between his parent's children
        :param a: Minimum number of elements for a node
        """
        node._parent._children.pop(index)  # the node is deleted from his parent child
        if index > 0: # if the node is not the first child of his parent
            element = node._parent._elements.pop(index - 1)  # the key associated to the child
            sibling._elements.append(element)  # insert the key inside the sibling
            i = 0
            while i < len(node._children):  # insert the elements and children of the node inside his sibling
                sibling._children.append(node._children[i])
                if len(node._elements) != 0:
                    to_merge = node._elements.pop(0)
                    sibling._elements.append(to_merge)
                i += 1
        else:  # if the node is the first child
            element = node._parent._elements.pop(index)  # take the fist key from the parent'ones
            sibling._elements.insert(index, element)  # insert the key inside the sibling of the node
            i = 0
            while i < len(node._children):  # insert the elements and children of the node inside his sibling
                sibling._children.insert(i, node._children[i])
                if len(node._elements) != 0:
                    to_merge = node._elements.pop(0)
                    sibling._elements.insert(i, to_merge)
                i += 1

        new_node = sibling._parent  # consider the parent of the two nodes
        if new_node._parent is not None:  # if the parent of the new node is not None
            if len(new_node._elements) < a:  # if the new node has a number of children lower than a, I have to call fusion recursively
                new_index = new_node._parent._children.index(new_node)
                if new_index > 0:
                    new_sibling = new_node._parent._children[new_index - 1]
                else:
                    new_sibling = new_node._parent._children[new_index + 1]
                return self._fusion(new_node, new_sibling, new_index, a)
        else:  # if the parent hasn't elements, we need a need root
            if len(new_node._elements) < 1:
                sibling._parent = None
                self._root = sibling  # the new root is the sibling of the node on which the fusion is performed

    def _transfer(self, node, sibling, index):
        """
        Support function that performs Transfer operation in case of underflow
        :param node: Node with underflow
        :param sibling: Left sibling of the node, if it exists, first right one otherwise
        :param index: Index of the node between his parent's children
        """
        if index > 0:
            element = node._parent._elements.pop(index - 1)
            element_to_transfer = sibling._elements.pop()
            node._elements.append(element)
            node._parent._elements.insert(index - 1, element_to_transfer)
        else:
            element = node._parent._elements.pop(index)
            element_to_transfer = sibling._elements.pop(index)
            node._elements.append(element)
            node._parent._elements.insert(index, element_to_transfer)
