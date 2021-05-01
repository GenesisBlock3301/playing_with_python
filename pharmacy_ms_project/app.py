class Base:
    def __init__(self, id, name, address, phone_number):
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address


class Employee(Base):
    def __init__(self, id, name, address, phone_number, salary, payment):
        super().__init__(id, name, address, phone_number)
        self.salary = salary
        self.payment = payment

    def __str__(self):
        return self.name

    def salary_due(self):
        if self.salary > self.payment:
            return abs(self.salary - self.payment)


class Customer(Base):
    def __init__(self, id, name, address, phone_number, medicine_price, payment):
        super().__init__(id, name, address, phone_number)
        self.medicine_price = medicine_price
        self.payment = payment

    def __str__(self):
        return self.name

    def customer_due(self):
        if self.medicine_price > self.payment:
            return self.medicine_price - self.payment


class SalesManagement:
    def __init__(self, medicine_name, location, number_of_medicine, original_price, selling_price,
                 sold_number_of_medicine, sold_at_a_time):
        self.medicine_name = medicine_name
        self.location = location
        self.number_of_medicine = number_of_medicine
        self.original_price = original_price
        self.selling_price = selling_price
        self.sold_number_of_medicine = sold_number_of_medicine
        self.sold_at_a_time = sold_at_a_time

    def __str__(self):
        return self.medicine_name

    def sold_medicine_value(self):
        return self.sold_number_of_medicine * self.selling_price

    def expense(self):
        return self.original_price * self.number_of_medicine

    def profit(self):
        if self.sold_medicine_value() > self.expense():
            return self.sold_medicine_value() - self.expense()

    def loss(self):
        if self.sold_medicine_value() < self.expense():
            return self.expense() - self.sold_medicine_value()

    def medicine_quantity(self, *args, **kwargs):
        if self.sold_at_a_time <= self.number_of_medicine:
            self.number_of_medicine -= self.sold_at_a_time
            self.sold_number_of_medicine += self.sold_at_a_time
            self.sold_at_a_time = 0
            return self.number_of_medicine, self.sold_number_of_medicine
