######################################################
# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2.
# The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

######################################################

# this method rearranges the input array such that all positive numbers are on the right
# and all negative numbers are on the left
def rearrange_array(arr):
    left = 0
    right = len(arr)-1
    while(left < right):
        if arr[left] <= 0 and arr[right] > 0:
            temp = arr[right]
            arr[right] = arr[left]
            arr[left] = temp
        elif arr[left] > 0:
            left +=1
        elif arr[right] <=0:
            right -=1
    return arr

## this method shall now
def get_positive_bound(arr):
    for i, element in enumerate(arr):
        if element <= 0:
            return i


## perform hashing in the array, such that every positve element will be marked as seen by
## changing it's arr[element -1 ] to -arr[element-1]
## this way if any positive element is found in the array, it's index would be negative.
## we accordingly look for positive values only.
def get_smallest_positive_missing_number(arr):
    arr = rearrange_array(arr)

    #indicates the index where positive numbers end and negative number starts.
    positive_bound_index = get_positive_bound(arr)

    ## handle the case if all numbers are negative or zero.
    if(positive_bound_index == 0):
        return 1

    for i in range(0, positive_bound_index):
        number = abs(arr[i])
        if (number - 1) < positive_bound_index and arr[number - 1] > 0:
            arr[number-1] = -arr[number-1]

    #traverse the modified array to get the missing number,
    # note that it's arr[index] will be a positive one.
    for i in range(0, positive_bound_index):
        if arr[i] > 0:
            return i + 1

    return i + 2





result = get_smallest_positive_missing_number([1, 2, 0])
print(result)