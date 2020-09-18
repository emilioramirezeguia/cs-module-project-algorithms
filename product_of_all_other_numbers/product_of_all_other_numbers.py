'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Create an iterator equal to the length of the array...
    # This will be used to replace the value at a specific position
    # Create a second iterator equal to the length of the array...
    # It equals the same length since we want to check from the beginning of the loop again
    # Check if the number at the first index is equal to the number at the second index
    # If it is, skip that value
    # Multiply the rest and save the result to a variable

    result = []
    product_of_numbers = 1
    
    for index1 in range(len(arr)):
        for index2 in range(len(arr)):
            if index1 == index2:
                continue
            product_of_numbers *= arr[index2]

        result.append(product_of_numbers)
        product_of_numbers = 1

    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
    #        9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
