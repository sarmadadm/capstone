def my_median(my_list):
    try:
        if type(my_list) is list:
            list_len = len(my_list)
            if list_len % 2 == 0:
                list_len = list_len / 2    
                even_median = (my_list[list_len + 1] + my_list[list_len - 1]) /2
                return even_median
                
            else:
                list_len = int(list_len/2)
                return  list_len
    except:
       return  print("Arguement is not a list")
        
my_median('sss')