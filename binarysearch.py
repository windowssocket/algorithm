def bsearch(sorted_array, ele, start, end):
    mid = len(sorted_array) / 2
    if start <= end and start >= 0 and len(sorted_array)>0:
        if sorted_array[mid] > ele:
            end = end - mid
            bsearch(sorted_array[:mid], ele, start, end)
        elif sorted_array[mid] < ele:
            start = start + mid + 1
            bsearch(sorted_array[mid + 1:], ele, start, end)
        elif sorted_array[mid] == ele:
            print start
            print end
            print start+mid
    else:
        print ("not found")


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start = 0
end = len(a) - 1
element = 9
bsearch(a, element, start, end)
