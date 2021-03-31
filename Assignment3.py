# creating empty list
get_list = []

# asking for the number of elements that will be in the list
num_list = int(input("Enter number of elements in list: "))

# iterating till num_list to append elements in list
for i in range(1, num_list + 1):
	new_list = int(input("Enter one element: "))
	get_list.append(new_list)

# print second maximum element using sorted() method
print("Second largest element is:", sorted(get_list)[-2])

