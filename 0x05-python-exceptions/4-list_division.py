#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    
    try:
        for i in range(list_length):
            try:
                dividend = my_list_1[i]
                divisor = my_list_2[i]
                division_result = dividend / divisor
            except ZeroDivisionError:
                print("division by 0")
                division_result = 0
            except (TypeError, ValueError):
                print("wrong type")
                division_result = 0
            except IndexError:
                print("out of range")
                division_result = 0
            finally:
                result_list.append(division_result)
    except:
        pass
    finally:
        return result_list
