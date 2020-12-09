import argparse
import cProfile
import logging

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

def minTreeTier(tree):
    tier = 1
    nodes = [tree]
    while len(nodes) > 0:
        for i in range(0, len(nodes)):
            node = nodes.pop(0)
            if node.left is None and node.right is None:
                return tier
            nodes.append(node.left)
            nodes.append(node.right)
        tier += 1

def getTree(treeArray):
    nodesToPopulateLeaf = []
    nodeValue = treeArray.pop(0)
    rootNode = Node(nodeValue)
    nodesToPopulateLeaf.append(rootNode) # add the root
    
    while len(treeArray) > 0:
        for i in range(0, len(nodesToPopulateLeaf)):
            node = nodesToPopulateLeaf.pop(0) # remove the one already has leaf populated
            if len(treeArray) > 0: 
                left = treeArray.pop(0)
                if left.lower() != 'null'.lower():
                    node.left = Node(left)
                    nodesToPopulateLeaf.append(node.left)
            if len(treeArray) > 0:
                right = treeArray.pop(0)
                if right.lower() != 'null'.lower():    
                    node.right = Node(right)
                    nodesToPopulateLeaf.append(node.right)

    return rootNode    

class Node: 
    def __init__(self, value, left=None, right=None): 
        self._value = value
        self._left = left
        self._right = right
    
    @property
    def left(self):
        return self._left
    
    @left.setter 
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self): # this mehtod is like toString in java class
        return "value {}, left {}, right {}".format(self.value, self.left.value, self.right.value)
    
    def __repr__(self): # this method is to print object in array prettily
        return str(self)    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # arguments ref: https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    parser.add_argument("--tree", help="provide numbers like 1,2,3,4,5", nargs='?', type=str, default="3,9,20,null,null,15,7")
    args = parser.parse_args()
    tree = getTree(args.tree.split(','))
    print(tree)

    minTier = minTreeTier(tree)
    logging.info("minTier of %s is %s", tree, minTier)
  