#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cmpt = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
            cmpt += 1
        except Exception as error:
            break
    print('')
    return cmpt
