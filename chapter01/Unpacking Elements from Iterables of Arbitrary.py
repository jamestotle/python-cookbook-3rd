#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-25 11:28:59
# @Author  : River Jiang (jamestotle@gmail.com)
# @Link    : http://nobody.com
# @Version : $Id$

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
print (name)
print (email)
print (phone_numbers)

def avg_qtr(sales_record):
    *trailing_qtrs, current_qtr = sales_record
    trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
    return avg_comparison(trailing_avg, current_qtr)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print (trailing)
print (current)


#
records = [
('foo', 1, 2),
('bar', 'hello'),
('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

name, *_, (*_, year) = user_record
print (name)
print (year)

items = [1, 10, 7, 4, 5, 9]
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print (sum(items))
