#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    arr = []
    for i in range(list_length):
        try:
            aux = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            aux = 0
        except (ValueError, TypeError):
            print("wrong type")
            aux = 0
        except IndexError:
            print("out of range")
            aux = 0
        finally:
            arr.append(aux)
    return arr
