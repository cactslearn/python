def bubble_sort(arr):
    for i in range(len(arr)):        
        for j in range(len(arr) - i - 1):            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:            
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    return result + left + right


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    

    return quick_sort(left) + [pivot] + quick_sort(right)


def heap_sort(arr):
    import heapq

    heapq.heapify(arr)

    result = []

    while arr:
        result.append(heapq.heappop(arr))
        print(f"Reuslt:{result}")

    return result


def main():
    numbers = [50, 20, 40, 10, 30]

    print("Original :", numbers)
    print("Bubble   :", bubble_sort(numbers.copy()))
    print("Selection:", selection_sort(numbers.copy()))
    print("Insertion:", insertion_sort(numbers.copy()))
    print("Merge    :", merge_sort(numbers.copy()))
    print("Quick    :", quick_sort(numbers.copy()))
    print("Heap     :", heap_sort(numbers.copy()))


if __name__ == "__main__":
    main()