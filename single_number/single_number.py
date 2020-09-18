'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # list of non repeated numbers
    non_repeated_numbers = []

    # loop through every number in the list
    for num in arr:
        # check whether num is inside non_repeated_numbers list, they won't first time arround
        if num in non_repeated_numbers:
            # if number is there, that means it's repeated, so remove it from the list
            non_repeated_numbers.remove(num)
        else:
            # if number is not there, make sure to add it
            non_repeated_numbers.append(num)

    # grab the only value that's left from non_repeated_numbers
    result = non_repeated_numbers[0]

    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
