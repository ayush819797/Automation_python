def merge(arr):

    if len(arr)<=1:
        return arr

    mid = (len(arr))//2
    left = arr[:mid]
    right = arr[mid:]

    left_arr = merge(left)
    right_arr = merge(right)

    return mer(left_arr, right_arr)

def mer(arr1, arr2):

    i = j = 0
    temp = []

    while (i<len(arr1) and j<len(arr2)):

        if arr1[i]<arr2[j]:
            temp.append(arr1[i])
            i = i + 1
        else:
            temp.append(arr2[j])
            j = j + 1


    while(i<len(arr1)):
        temp.append(arr1[i])
        i = i+1

    while(j<len(arr2)):
        temp.append((arr2[j]))
        j = j+1

    return temp


arr = [2, 34,55,1,0, -1]

p = merge(arr)
print(p)

