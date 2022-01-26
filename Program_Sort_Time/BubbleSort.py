import re
import time

def BubbleSort(unsorted_list):
    while True:
        streak = 0
        for i in range(len(unsorted_list)-1):
            if unsorted_list[i] > unsorted_list[i+1]:
                temp = unsorted_list[i]
              
                unsorted_list[i] = unsorted_list[i+1]
                unsorted_list[i+1] = temp
                streak = 0
            else:
                streak = streak + 1
               
        if (streak >= len(unsorted_list) - 1):
            return unsorted_list

def ListMaker(raw_values):
    unsorted_list = re.findall(r"[\w']+", raw_values)
    unsorted_list = [int(x) for x in unsorted_list]
    return unsorted_list

def main(raw_values):
   
    unsorted_list = ListMaker(raw_values)
    start_time = time.time()
    sorted_list = BubbleSort(unsorted_list)
    end_time = time.time()
    str= "Bubble Sort with %s elements Time: "% len(sorted_list), (end_time-start_time)
    x=(end_time-start_time)
    return str,x

