import numpy as np
import matplotlib.pyplot as plt


# data for 2-dim kd-tree
array_data = np.array( [
    [3,    12],
    [4,    25],
    [5,    25],
   [18,    22],
    [1,     5],
   [10,    20],
    [4,    16],
   [20,    30],
   [15,    20],
   [11,    25],
   [10,    14],
    [2,    13],
   [14,    25],
    [1,     3],
    [2,     4],
    [6,    11]
    ] )
isovalue = 10.5


def partition(index_input, array_input, criterion):

    if criterion == "max":
        m = np.argsort(array_data[index_input,1])
    else :  
        m = np.argsort(array_data[index_input,0])
        
    return index_input[m]
    
#build kd-tree

def build(index_input, array_input, criterion):
    
    s = len(index_input)
    new_index = partition(index_input, array_input,criterion)
    
    if criterion == "min":
        criterion = "max"
    else:
        criterion = "min"
    
    if(s == 0):
        return None 
    
    if(s == 1):
        return [index_input[0], [None,None]]
    

    if s%2 == 0:
        newsize = int(s/2)
        left_child = build(new_index[:newsize],array_input,criterion)
        right_child = build(new_index[newsize+1:], array_input,criterion)
        
    else:
        newsize = int((s-1)/2)
        left_child = build(new_index[:newsize],array_input,criterion)
        right_child = build(new_index[newsize+1:], array_input,criterion)

    listIndex = [new_index[newsize]] #parent
    listIndex.append(left_child) #add left_child
    listIndex.append(right_child) #add right_child
    
    return listIndex
    
    
def build_kd_tree(array_input):

    return build(np.arange(len(array_input[:,0])),array_input, "min")

kd = build_kd_tree(array_data)


# display kd- tree
def getDataLevels(arr,criterion,array_input): 
    if criterion=="max":
        criterion = "min"
    else:
        criterion = "max"
    if arr is None:
        return []
 
    if (len(arr) == 2):
        if(arr[1] == [None,None]):
            print(array_input[arr[0]].tolist(), ": ", [], " ", [])
            return [arr[0]]
       
    if (len(arr) == 3):
        if (arr[1] is None) and (arr[2] is None):
            return [arr[0]]
    
    parent = [arr[0]]
    leftChild = getDataLevels(arr[1],criterion,array_input)
    rightChild = getDataLevels(arr[2],criterion,array_input)
    left = []
    right = []
    
    for i in leftChild:
        left.append(array_input[i].tolist())
        
    for i in rightChild:
        right.append(array_input[i].tolist())
        
    if criterion == "max":
        
        print(array_input[arr[0]].tolist(), ": ", left, " ", right)
    else:
        print(array_input[arr[0]].tolist(), ": ", right, " ", left)
        
    return parent + leftChild + rightChild

def display_kd_tree(index_array, array_input):
    getDataLevels(index_array,"min", array_input) 

display_kd_tree(kd, array_data)

'''
Output dislplays left and right points of the parent points. [parent-coordinate] : [left-point coordinates] [right-point coordinates]

[1, 3] :  []   []
[1, 5] :  []   [[1, 3]]
[3, 12] :  []   []
[2, 4] :  [[1, 5], [1, 3]]   [[3, 12]]
[4, 16] :  []   []
[5, 25] :  []   []
[4, 25] :  [[4, 16]]   [[5, 25]]
[2, 13] :  [[4, 25], [4, 16], [5, 25]]   [[2, 4], [1, 5], [1, 3], [3, 12]]
[10, 14] :  []   []
[15, 20] :  []   []
[10, 20] :  [[10, 14]]   [[15, 20]]
[11, 25] :  []   []
[20, 30] :  []   []
[14, 25] :  [[11, 25]]   [[20, 30]]
[18, 22] :  [[14, 25], [11, 25], [20, 30]]   [[10, 20], [10, 14], [15, 20]]
[6, 11] :  [[2, 13], [2, 4], [1, 5], [1, 3], [3, 12], [4, 25], [4, 16], [5, 25]]   [[18, 22], [10, 20], [10, 14], [15, 20], [14, 25], [11, 25], [20, 30]]
'''


