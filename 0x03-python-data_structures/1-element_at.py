#!/usr/bin/python3
def element_at(my_list, idx):
    """for i in my_list:"""    
    """idx = my_list.index(i)"""
    element = my_list[idx]
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return element