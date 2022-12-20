def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
            new.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            if len(new) < list_length:
                new.append(0)
            print("division by 0")
        except TypeError:
            if len(new) < list_length:
                new.append(0)
            print('wrong type')
        except IndexError:
            if len(new) < list_length:
                new.append(0)
            print("out of range")
        finally:
            pass

    return new
