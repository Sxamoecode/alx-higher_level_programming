#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        for ele in my_list:
            if idx not in range(len(my_list)):
                return None
            elif idx < 0:
                return None
            elif ele == my_list[idx]:
                return ele
