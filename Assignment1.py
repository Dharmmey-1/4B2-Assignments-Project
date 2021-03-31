get_data = input ("Enter integers here: ")

if " " in get_data:
   
   con_list = get_data.split(" ")
  
   for  position, item in enumerate(con_list):
      con_list[position] = int(item)

   total_sum = sum(con_list) 
   no_of_items = len(con_list)
   average_value = total_sum / no_of_items

   print("the mean is {0:.2f}".format(average_value))
    
else:
       print(int(get_data))
