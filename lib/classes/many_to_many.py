class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not hasattr(self,"_name"):
            if isinstance(name, str) and len(name) >= 3:
                self._name = name
            else:
                raise Exception("Coffee name needs to be a string with more than three letters")
        else:
            raise Exception("Can not change the coffee name.")
        
    def orders(self):
        return [order for order in Order.all if order.coffee is self]
    
    def customers(self):
        all_order = set([order.customer for order in self.orders()])
        return list(all_order)
    
    def num_orders(self):
        return len(self.orders()) 
    
    def average_price(self):
        return sum([order.price for order in self.orders()])/self.num_orders() if self.num_orders() > 0 else 0


class Customer:
    all =[]
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(1,15):
            self._name = name
        else:
            raise Exception("Customer name needs to be a string with a length btw 1 to 15 chars")

    def orders(self):
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        all_coffees = set([order.coffee for order in self.orders()])
        return list(all_coffees)
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    def amount_spent(self, coffee):
        return sum([order.price for order in Order.all if order.coffee is coffee and order.customer is self])
    
    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.customers():
            return None
        else:
            coffee_dict = {customer: customer.amount_spent(coffee) for customer in cls.all}
            # coffee_max = max(coffee_dict, key=lambda x:coffee_dict[x]) --another way to write it
            coffee_max = max(coffee_dict, key = coffee_dict.get)
            return coffee_max
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if not hasattr(self, "_price"):
            if isinstance(price, (int, float)) and (1.0 <= price <= 10.0):
                self._price = price
            else:
                raise Exception("Price needs to be a float btw 1.0 and 10.0")
        else:
            raise Exception("Can not change the price.")

    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("customer need to be an instance of Customer")
    
    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception("coffee needs to be an instance of Coffee.")