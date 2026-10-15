def bubble_sort(arr): # [50, 20, 40, 10, 30]
    print(f"length = {len(arr)}")
    for i in range(len(arr)): # 0 ->50
        for j in range(len(arr) - i - 1):   #  4 - 0 - 1 = 3
            print(f"{i} = {arr[i]}, {j} = {arr[j]}")
            if arr[j] > arr[j + 1]: # 50 > 20
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # [20, 50, 40, 10, 30]
            print(f"{arr}")
    return arr


def selection_sort(arr): # [50, 20, 40, 10, 30]
    for i in range(len(arr)): # 0 - 4 
        min_index = i # 0

        for j in range(i + 1, len(arr)): # 1 - 4
            if arr[j] < arr[min_index]: # j:1:20 < min_index:0:50
                min_index = j # 1
        print(f"Before i {arr[i]}, min index {arr[min_index]} = min index {arr[min_index]}, i {arr[i]}")
        arr[i], arr[min_index] = arr[min_index], arr[i]        
        print(f" After i {arr[i]}, min index {arr[min_index]} = min index {arr[min_index]}, i {arr[i]}")

    return arr


def insertion_sort(arr): # [50, 20, 40, 10, 30]
    for i in range(1, len(arr)): # 1 - 4
        key = arr[i] # 1->20
        j = i - 1 # 1 - 1 = 0

        while j >= 0 and arr[j] > key: # 0 >= 0 and 50 > 20         
            arr[j + 1] = arr[j] # 0 = 1 = 1, 20 -> 50
            j -= 1 # -1

        arr[j + 1] = key
        print(f"{arr}")

    return arr


def merge_sort(arr): # [50, 20, 40, 10, 30]
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 # 2
    print(f"mid: {mid}")

    left = merge_sort(arr[:mid]) # 0 - 2
    right = merge_sort(arr[mid:]) # 2 - end
    print(f"left {left}")
    print(f"right {right}")

    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    print(f"result {result}")
    return result + left + right


def quick_sort(arr): 
    # [50, 20, 40, 10, 30]
    # [20, 40, 10, 30]
    # [40, 30]
    if len(arr) <= 1:
        return arr

    pivot = arr[0] 
    # 50
    # 20
    # 40

    left = [x for x in arr[1:] if x <= pivot] 
    # [20, 40, 10, 30]
    # [10]
    # [30]
    right = [x for x in arr[1:] if x > pivot] 
    # 
    # [40, 30]
    #
    
    temp = quick_sort(left) + [pivot] + quick_sort(right)
    # [10, 20, 30, 40, 50]
    # [10, 20, 30, 40]
    # [30, 40]
    print(f"{temp}")
    return temp # quick_sort(left) + [pivot] + quick_sort(right)


def heap_sort(arr): # [50, 20, 40, 10, 30]
    import heapq

    heapq.heapify(arr)

    result = []

    while arr:
        result.append(heapq.heappop(arr))
        print(f"Heapify: {arr}")
        print(f"Result:{result}")

    return result


def main():
    numbers = [50, 20, 40, 10, 30]

    print("Original :", numbers)
    # print("Bubble   :", bubble_sort(numbers.copy()))
    # print("Selection:", selection_sort(numbers.copy()))
    # print("Insertion:", insertion_sort(numbers.copy()))
    # print("Merge    :", merge_sort(numbers.copy()))
    # print("Quick    :", quick_sort(numbers.copy()))
    print("Heap     :", heap_sort(numbers.copy()))


if __name__ == "__main__":
    main()