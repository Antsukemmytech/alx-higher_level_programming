#!/usr/bin/python3
def no_c(sting):
    my_string = " "
    for char in string:
        if char != "c" and char != "C":
            my_string += char
    return my_string