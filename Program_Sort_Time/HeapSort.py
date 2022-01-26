import time
import re
def HeapSort(unsorted_list):
    taille = len( unsorted_list ) - 1
    petit_parent = taille // 2
   
    for i in range (petit_parent, -1, -1 ):
        suport_HeapSort(unsorted_list, i, taille)
 
    for i in range(taille, 0, -1):
        if unsorted_list[0] > unsorted_list[i]:
            # Swap 
            unsorted_list[0], unsorted_list[i] = unsorted_list[i], unsorted_list[0]
            suport_HeapSort(unsorted_list, 0, i-1)
    
    return unsorted_list
 
def suport_HeapSort(unsorted_list, premier, dernier):
    plus_grand = 2 * premier + 1
    while plus_grand <= dernier:
        if (plus_grand < dernier) and (unsorted_list[plus_grand] < unsorted_list[plus_grand + 1]):
            plus_grand += 1
 
        if unsorted_list[plus_grand] > unsorted_list[premier]:
            # Swap 
            unsorted_list[plus_grand],unsorted_list[premier] = unsorted_list[premier],unsorted_list[plus_grand]
            
            premier = plus_grand;
            plus_grand = 2 * premier + 1
        else:
            return 
        
def ListMaker(raw_values):
    unsorted_list = re.findall(r"[\w']+", raw_values)
    #^Removes characters in between elements
    unsorted_list = [int(x) for x in unsorted_list]
    #^Converts the list type into Integer
    return unsorted_list

def main(raw_values):
   
    unsorted_list = ListMaker(raw_values)
    start_time = time.time()
    sorted_list = HeapSort(unsorted_list)
    end_time = time.time()
    str= "Heap Sort with %s elements Time:"% len(sorted_list), (end_time-start_time)
    x=(end_time-start_time)
    return str,x


