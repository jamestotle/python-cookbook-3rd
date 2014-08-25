#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-25 11:15:33
# @Author  : River Jiang (jamestotle@gmail.com)
# @Link    : http://nobody.com
# @Version : $Id$

p = (4, 5)
x, y = p
print (x,y)

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print (name)
print (shares)
print (date)

name, shares, price, (year, mon, day) = data
print (name, shares, price, year, mon, day)

s = 'hello'
a, b, c, d, e = s
print (a, b, c, d, e)

_, shares, price, _ = data
print (shares, price)