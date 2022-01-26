import time
import re
import math 
def RadixSort(unsorted_list, max_len = 10):
    
    NB_BUCKETS = 10 
    for x in range(max_len):
       
        buckets = [[] for i in range(NB_BUCKETS)]
        
    
        for y in unsorted_list:
            buckets[math.floor( (y / 10 ** x) % NB_BUCKETS)].append(y)
        unsorted_list = []
        for section in buckets:
            unsorted_list.extend(section)
            
    return unsorted_list

def ListMaker(raw_values):
    unsorted_list = re.findall(r"[\w']+", raw_values)
    #^Removes characters in between elements
    unsorted_list = [int(x) for x in unsorted_list]
    #^Converts the list type into Integer
    return unsorted_list

def main(raw_values):
    #^If you are opening as a stand-alone file, please replace "main(raw_values)" with "main(raw_values = input('Please enter values:')"
    unsorted_list = ListMaker(raw_values)
    start_time = time.time()
    sorted_list = RadixSort(unsorted_list,10)
    end_time = time.time()
    #^If you are opening as a stand-alone file and want to see the sorted list, please add the code: print(sorted_list)
    str= "Radix Sort with %s elements Time: "% len(sorted_list), (end_time-start_time);
    x=(end_time-start_time)
    return str,x    


