# p ; { * " : _ [ ) */

def selection_sort(arr : list) -> list:
    """One of the Sorting algorithm in python"""
    
    for i in range(len(arr)):
        # initializing min_index as i
        min_index = i
        
        # iterate all element in list,
        # but not the element behind i
        
        for j in range(i, len(arr)):
            # searching for element greater than current element i.e. min_index 
            # if there a number smaller than min_index, then min_index will be index of that element   
            if arr[j]<arr[min_index] : min_index = j
        
        # swapping elements at min_index and i with each other
        arr[i], arr[min_index] = arr[min_index], arr[i] 
    
    return arr
    
    
array =  [31, 32, 18, 25, 6, 3, 9, 0, 7, 28, 47, 10, 39, 34, 37, 43, 6, 35, 12, 45]
    
# sorting
sorted_array = selection_sort(array)

print("Sorted Array - ", sorted_array)  #Sorted Array -  [0, 3, 6, 6, 7, 9, 10, 12, 18, 25, 28, 31, 32, 34, 35, 37, 39, 43, 45, 47]
    
