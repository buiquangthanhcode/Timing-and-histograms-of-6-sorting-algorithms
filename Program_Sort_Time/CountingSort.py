import time
import re
def CountingSort(unsorted_list):
  
    lst_compte = [0 for i in range(len(unsorted_list) + 1)]
    for i in range(len(unsorted_list)-1):
        lst_compte[i] += 1
    pos_in_lst = 0;
    j = 0
    while j < (len(unsorted_list) + 1):
       
        while 0 < lst_compte[j]:
            unsorted_list[pos_in_lst] = j
            pos_in_lst += 1
            lst_compte[j] -= 1
        j += 1
    return unsorted_list

def ListMaker(raw_values):
    unsorted_list = re.findall(r"[\w']+", raw_values)
    #^Removes characters in between elements
    unsorted_list = [int(x) for x in unsorted_list]
    #^Converts the list type into Integer
    return unsorted_list

def main(raw_values):
   
    unsorted_list = ListMaker(raw_values)
    start_time = time.time()
    sorted_list = CountingSort(unsorted_list)
    end_time = time.time()
    str="Counting Sort with %s elements Time: "% len(sorted_list), (end_time-start_time) 
    x=(end_time-start_time)
    return str,x

