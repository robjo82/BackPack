"""
The BackPack problem can be compared to this new problem :
We have a backpack with a capacity of 20 kg. We have a list of items with their weight and value.
We want to put the items in the backpack so that the total weight is less than or equal to the capacity and the total value is maximum.
"""
from random import gammavariate


gave_list = [[18,14], [37,2], [1,4], [25,3], [4,50], [12,7], [9,10], [16,9], [7,24], [5,21]] # list of items, weight and value
max_weight = int(input("Enter the max weight of the backpack : "))

def greedy_methode(gave_list) :
    used_list = gave_list

    for item in used_list :
        item.append(used_list.index(item))
        item.append(item[1]/item[0])
        
    print(used_list)
    used_list.sort(key=lambda x: x[3], reverse=True) # sort by ratio
    print(used_list)

    while weight_sum(used_list) > max_weight :
        used_list.pop()
        print(used_list)
    return used_list

def weight_sum(gave_list) :
    sum = 0
    for item in gave_list :
        sum += item[0]
    return sum

def display_backpack(gave_list) :
    print("\nThe items in the backpack are : ")
    for item in gave_list :
        print("Number {}, wich weighs {} and has a value of {}, so a ratio of {}".format(item[2], item[0], item[1], item[3]))
    print("The total weight of the backpack is : {}".format(weight_sum(gave_list)))

display_backpack(greedy_methode(gave_list))