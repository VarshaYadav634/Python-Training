def rev_arr(array):
    left = 0
    right = len(array)-1
    while left<right:
        array[left], array[right] = array[right], array[left]
        left+=1
        right-=1
    print(array)
rev_arr([1, 5, 7, 16, 30])