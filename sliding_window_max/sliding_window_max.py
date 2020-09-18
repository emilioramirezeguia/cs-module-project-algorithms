'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # keep track of the size of the window
    window_size = k
    # list that will contain values inside the window
    window = []
    # list where we'll add the maximum value for each position of the window
    final_result = []

    # iterator that allows us to loop through the entire list starting at index 0 and ending
    # at the end of the array minus the window size plus 1
    for index1 in range(len(nums) - window_size + 1):
        # max_number starts as first number in the window
        # which is where our second loop starts
        max_number = nums[index1]

        # dynamic iterator that allows us to loop through values inside the window size
        # and slide one place to the right after an entire pass
        for index2 in range(index1, window_size + index1):
            # current number we're checking
            current_num = nums[index2]
            # for reference: the values that compose the window
            window = nums[index1: window_size + index1]
            # check whether the current value is greater than our max_number
            if current_num > max_number:
                # if it is, assign max_number to be that number
                max_number = current_num

        # before shifting the window again, add the max_number found to final_result
        final_result.append(max_number)

    # after you're done shifting the window, return the final array
    return final_result


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
