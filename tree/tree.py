class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, arr=[]):
        self.arr = arr
        self.root = self.generate_tree()

    def __repr__(self):
        return "Tree's root = {}".format(self.root.val)

    def pprint(self):
        stack = [(0, self.root)]
        while stack:
            level, node = stack.pop(-1)
            if node.right:
                stack.append((level + 1, node.right))
            if node.left:
                stack.append((level + 1, node.left))
            print("{}TreeNode(val={})".format('\t' * level, node.val))

    def generate_tree(self):
        try:
            root = TreeNode(int(self.arr[0]))
        except ValueError:
            return TreeNode(val=None)
        
        current_level, child_level = [root], []
        i = 1
        while True:
            if i >= len(self.arr):
                break
            shift = 0
            while i + shift < len(self.arr) and shift < 2 * len(current_level):
                child_level.append(self.arr[i+shift])
                shift += 1
            i += shift
            for _ in range(len(current_level)):
                current_node = current_level.pop(0)
                try:    # Left child
                    value = int(child_level[0])
                    node = TreeNode(value)
                    current_node.left = node
                    current_level.append(node)
                except:
                    pass
                    
                if not child_level:
                    break

                child_level.pop(0)
                try:    # Right child
                    value = int(child_level[0])
                    node = TreeNode(value)
                    current_node.right = node
                    current_level.append(node)
                except:
                    pass
                if child_level:
                    child_level.pop(0)
        return root


if __name__ == '__main__':
    import sys
    input_arr_string = sys.argv[1]
    input_arr = input_arr_string.split(',')
    t = Tree(input_arr)
    t.pprint()
