import time
import re
def quickSort(unsorted_list):
    support_quickSort(unsorted_list, 0, len(unsorted_list)-1)
    return unsorted_list
 
def support_quickSort(unsorted_list, gauche, droite):
    temp_stack = []
    temp_stack.append((gauche, droite))
    
    while temp_stack:      
        pos = temp_stack.pop()
        droite, gauche = pos[1], pos[0]
        pivot = partition(unsorted_list, gauche, droite)
        
      
        if (pivot - 1) > gauche:
            temp_stack.append((gauche, pivot - 1))
            
       
        if (pivot + 1) < droite:
            temp_stack.append((pivot + 1, droite))            
       

def partition(unsorted_list, premier, dernier):
    pivot = unsorted_list[premier]

    gauche = premier + 1
    droite = dernier
    
    est_complet = False
    while not est_complet:

        while gauche <= droite and unsorted_list[gauche] <= pivot:
            gauche = gauche + 1
     
        while unsorted_list[droite] >= pivot and droite >= gauche:
            droite = droite -1
     
        if droite < gauche:
            est_complet = True
        else:
            # Swap 
            unsorted_list[gauche], unsorted_list[droite] = unsorted_list[droite], unsorted_list[gauche]
    
    # Swap 
    unsorted_list[premier], unsorted_list[droite] = unsorted_list[droite], unsorted_list[premier]
    
    return droite
   
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
    sorted_list = quickSort(unsorted_list)
    end_time = time.time()
    #^If you are opening as a stand-alone file and want to see the sorted list, please add the code: print(sorted_list)
    str= "Quick Sort with %s elements Time:"% len(sorted_list), (end_time-start_time)
    x=(end_time-start_time)
    return str,x

