#this class handles one store (transaction) and all money spend/received from it)
class Transaction():
    def __init__(self, store, amount):
        self.store = store
        self.amount = float(amount)

    def get_store(self):
        return self.store

    def get_amount(self):
        return self.amount

    def add_amount(self, sum):
        self.amount += sum

class Income(Transaction):
    income_list = [] #this list includes names of income transactions
    income_object_list = [] #this list includes income transaction objects
    def __init__(self, store, amount):
        super().__init__(store, amount)
        Income.income_list.append(store)
        Income.income_object_list.append(self)

    def check_if_income_exists(name):
        for object in Income.income_object_list:
            if object.get_store() == name:
                return True
        else:
            return False

    def get_correct_income(name):
        for income_object in Income.income_object_list:
            if name == Income.get_store(income_object):
                correct_transaction_object = income_object
                return correct_transaction_object
        else:
            print("Transaction not found.")

    def get_objects():
        return Income.income_object_list


class Store(Transaction):
    store_list = [] #this list includes names of cost transactions
    store_object_list = [] #this list includes cost transaction objects
    def __init__(self, store, amount):
        super().__init__(store, amount)
        Store.store_list.append(store)
        Store.store_object_list.append(self)

    def check_if_store_exists(name):
        for object in Store.store_object_list:
            if object.get_store() == name:
                return True
        else:
            return False

    def get_correct_store(name):
        for store_object in Store.store_object_list:
            if name == Store.get_store(store_object):
                correct_transaction_object = store_object
                return correct_transaction_object
        else:
            print("Transaction not found.")

    def get_objects():
        return Store.store_object_list