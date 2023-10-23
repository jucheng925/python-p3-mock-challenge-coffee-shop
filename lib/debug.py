#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    coffee = Coffee("Vanilla Latte")
    steve = Customer("Steve")
    dima = Customer("Dima")
    Order(steve, coffee, 2.0)
    Order(steve, coffee, 4)
    Order(dima, coffee, 5.0)
    dimaorder = Order(dima, coffee, 2.0)

    ipdb.set_trace()
