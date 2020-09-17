'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Create a new array that will hold the result. It should start out as empty.
    zeroes_list = []

    # For each number in the list...
    for num in arr:
        # Check if the number is equal to zero.
        if num == 0:
            # If it is. Add that number to zeroes_list
            zeroes_list.append(num)
            # And remove it from original array
            arr.remove(num)

    # When the above loop is over, now run through every number in the zeroes_list. This should contain only zeroes.
    for num in zeroes_list:
        # Append those zeroes to our original array.
        arr.append(num)

    # Return the modified array
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
