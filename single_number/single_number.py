'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Thoughts
    # The array is never empty
    # Every element is repeated, except for one

    # How I understand the problem
    # I need some way to inspect every element in the array
    # Since I know the array will never be empty, I don't need to confirm that before inspecting the elements
    # Every time I run through the numbers, I need a way to keep track of the current value I'm checking against
    # I also need some way to confirm if the current value was found again or not
    # Finally, I need to return the only value that I didn't confirm as repeated

    # test_list = [4, 1, 2, 1, 2]
    # if arr in test_list:
    #     print(True)
    # else:
    #     print(False)
    # for index, num in arr:
    #     repeated = []
    #     if

    # for num1 in range(len(arr)-1):
    #     for num2 in range(num1 + 1, len(arr)):
    #         found = 0
    #         if arr[num1] == arr[num2]:
    #             found += 1
    #             print(found)

    # if __name__ == '__main__':
    #     # Use the main function to test your implementation
    #     arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    #     print(f"The odd-number-out is {single_number(arr)}")

    # single_number([4, 1, 2, 1, 2])
single_number(10)
