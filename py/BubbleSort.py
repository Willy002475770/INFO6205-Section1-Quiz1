def bubble_sort(arr):
    """
    Bubble sort implementation to sort a list in ascending order.

    Args:
        arr (list): The list of integers to sort.

    Returns:
        list: The sorted list.
    """
    
    def swap(i, j):
        """
        Swap two elements in the list at indices i and j.

        Args:
            i (int): Index of the first element.
            j (int): Index of the second element.
        """
                    
        arr[i], arr[j] = arr[j], arr[i]
    
    boundary = -1  
    while True:
        swapped = False
        i = 0
            
        while i < len(arr) - 1 and i+1 != boundary:
            if arr[i] > arr[i+1]:
                swap(i, i+1)
                swapped = True
            i += 1
                
        if not swapped:
            break
        boundary = i

    return arr

