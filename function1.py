#!/usr/bin/env python
#-*- coding = utf-8 -*-
def fact(n):
    s=1
    for i in range(n):
        s *= n
    return s
a= fact(4)
print(a)