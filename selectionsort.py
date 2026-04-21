def selectionSort(arr):

    n = len(arr)

    for i in range(n):

        min_idx = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap smallest with current position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Main Program
arr = list(map(int, input("Enter elements separated by space: ").split()))

print("Original array:", arr)

sorted_arr = selectionSort(arr)

print("Sorted array:", sorted_arr)