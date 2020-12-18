def merge_sort(merge):
    if len(merge) <= 1:
        return merge
    left = []
    right = []
    for i in range (0, len(merge)):
        if i < (len(merge)/2):
            left.append(merge[i])
        else:
            right.append(merge[i])
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right) 
    
def merge(left, right):
    result = []
    i = 0
    j = 0
    while len(left) != i and len(right) != j:
        if left[i] <= right[j]:
            result.append(left[i])
            i = i+1
        else:
            result.append(right[j])
            j = j+1
    while left != i:
        result.append(left[i])
        i = i+1
    while right != j:
        result.append(right[j])
        j = j+1
    print(result)
merge = ([1, 3, 5], [2, 7, 8])
merge_sort= []
