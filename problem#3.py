###############################
#  This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.

####################################


# Define node used in the tree.
class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

#### we rely on the fact that for each node (root_index = 0)
#### left_child = 2* parent_index + 1,
#### right_child = 2* parent_index + 2.
def add_new_node_to_tree(arr, index):
     ### base case that the index is always in the array bounds
    if (index < len(arr)):
        temp = Node(arr[index])
        root =temp

        root.left = add_new_node_to_tree(arr, 2 * index + 1)
        root.right = add_new_node_to_tree(arr, 2 * index + 2)
        return root

#create the tree from the array starting from index 0 which is the root.
def create_tree_from_array(arr):
    return add_new_node_to_tree(arr, 0)


### we populate the value of the array_index.
def add_node_to_array(root, index, array):
    ### base case that the root is not null
    if root:
        array[index] = root.data
        add_node_to_array(root.left, 2 * index + 1, array)
        add_node_to_array(root.right, 2 * index + 2,array)

#create the array that is going to be populated depending on each node mapped index.
def create_array_from_tree(root, n):
    array = [0] * n
    add_node_to_array(root, 0, array)
    return array


def calculate_tree_nodes_number(root):
    if not root:
        return 0
    if root:
        return 1 + calculate_tree_nodes_number(root.left) + calculate_tree_nodes_number(root.right)

def convert_list_to_string(list):

    # Converting integer list to string list
    s = [str(i) for i in list]

    # Join list items using join()
    res = (',').join(s)

    return(res)

def convert_string_to_list(string):
    string_array = string.split(",")
    integer_array = [int(i) for i in string_array ]
    return integer_array

def serialize(root):
    # calculate the number of nodes in the tree
    tree_nodes = calculate_tree_nodes_number(root)
    #create the array of values indicating the tree nodes.
    array_generated = create_array_from_tree(root, tree_nodes)
    #serialize the list to a string
    serialized_array = convert_list_to_string(array_generated)
    return serialized_array

def deserialize(string):
    tree_list_representation = convert_string_to_list(string)
    root = create_tree_from_array(tree_list_representation)
    return root


##### try the code.
array = [1,2,3,4,5,6,7,8]

##Assume this is the input, a pointer to the head node.
root = create_tree_from_array(array)

serialized_tree = serialize(root)
## this is the tree as a list in a string format.
print(serialized_tree)

deserialized_tree = deserialize(serialized_tree)
## this is the root node.
print(deserialized_tree)

