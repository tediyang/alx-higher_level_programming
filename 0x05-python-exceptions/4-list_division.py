#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    for i in range(list_length):
        try:
            my_list_1[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            my_list_1[i] = 0
            print("division by 0")
        except TypeError:
            my_list_1[i] = 0
            print('wrong type')
        except IndexError:
            my_list_1.append(0)
        finally:
            pass
        
    return my_list_1
