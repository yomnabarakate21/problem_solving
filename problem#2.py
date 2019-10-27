####################################
### This problem was asked by Uber.

# Given an array of integers,
# return a new array such that each element at index i of the new array
#  is the product of all the numbers
#  in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24].
#  If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?
##############################################

##case1: Allowing division
def list_product(array):
    product = 1
    for element in array:
        product *= element
    return product

def get_product(index, product, arr):
    return (product / arr[index])

array = [1, 2, 3, 4, 5]
solution = [0]* len(array)
product = list_product(array)
for i, value in enumerate(array):
    solution[i] = int(get_product(i, product,array))

print (solution)

###################################################################################

##case2: No division allowed

def populate_left_products(arr):
    left_product_array = [1] * len(arr)
    for i, value in enumerate(arr):
        if i ==0:
            left_product_array[i] = value
        else:
            left_product_array[i] = left_product_array[i-1] * value
    return left_product_array

def populate_right_products(arr):
    right_product_array =[1] *len(arr)
    for i, value in reversed(list(enumerate(arr))):
        if i == len(arr)-1:
            right_product_array[i] = value
        else:
            right_product_array[i]= right_product_array[i+1] *value
    return right_product_array


### for each index, we calcuate the product of subarray on it's left and the subrray on it's right.
left_product_array = populate_left_products(array)
right_product_array = populate_right_products(array)
result = []
for i, value in enumerate(array):
    #handle left corner case
    if i == 0:
        result.append(right_product_array[i+1])
    #handle right corner case
    elif i == len(array)-1:
        result.append(left_product_array[i-1])

    else:
        result.append(left_product_array[i-1] * right_product_array[i+1])

print(result)
