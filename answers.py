#creating an empty list called my_list
my_list = []

#appending the following items to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting the value 15 at the secon position of the list
my_list.insert(1, 15)

#extending my list with another list (list1)
list1 = [50, 60, 70]
my_list.extend(list1)

#removing the last element from my list
del my_list[-1]

#sorting my list in ascending order
my_list.sort()

#finding and printing the index of 30 in my_list
print('The index of 30 in my_list is: ', my_list.index(30))

#printing my overall list
print('Sorted list(my_list): ', my_list)