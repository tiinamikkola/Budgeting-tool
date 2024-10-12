#this class includes and handles groups (example: "Groceries"), where transactions can be organized into
class Groups():
    def __init__(self, group_name):
        self.name = group_name
        self.transactions = [] #this includes transaction-objects that belong to Group-object

    def get_group_object_name(self):
        return self.name

    def get_group_object_list(self):
        return self.transactions

    def remove_transaction_from_group(self, transaction):
        self.transactions.remove(transaction)

    def add_transaction_to_group(self, transaction):
        if transaction in self.transactions:
            print("Transaction is already in this group!")
        elif transaction not in self.transactions:
            self.transactions.append(transaction)
            print("Transaction added to group.")


class Income_group(Groups):
    income_group_list = [] #this includes names of income groups
    income_group_object_list = [] #this includes all income group-objects
    def __init__(self, group_name):
        super().__init__(group_name)
        Income_group.income_group_list.append(group_name)
        Income_group.income_group_object_list.append(self)

    def delete_income_group(self, group):
        self.income_group_list.remove(self.name)
        self.income_group_object_list.remove(self)
        del self
        print("Income group " + group + " removed.")

    def check_if_income_group_exists(name):
        for object in Income_group.income_group_object_list:
            if object.get_group_object_name() == name:
                return True
        else:
            return False

    def get_correct_group(group):
        for income_group_object in Income_group.income_group_object_list:
            if group == Income_group.get_group_object_name(income_group_object):
                correct_group_object = income_group_object
                return correct_group_object
        else:
            print("Group not found.")

    def get_groups():
        return Income_group.income_group_object_list


class Store_group(Groups):
    store_group_list = [] #this includes names of cost group-objects
    store_group_object_list = [] #this includes all cost group-objects
    def __init__(self, group_name):
        super().__init__(group_name)
        Store_group.store_group_list.append(group_name)
        Store_group.store_group_object_list.append(self)

    def delete_store_group(self, group):
        self.store_group_list.remove(self.name)
        self.store_group_object_list.remove(self)
        del self
        print("Store group " + group + " removed.")

    def check_if_store_group_exists(name):
        for object in Store_group.store_group_object_list:
            if object.get_group_object_name() == name:
                return True
        else:
            return False

    def get_correct_group(group):
        for store_group_object in Store_group.store_group_object_list:
            if group == Store_group.get_group_object_name(store_group_object):
                correct_group_object = store_group_object
                return correct_group_object
        else:
            print("Group not found.")

    def get_groups():
        return Store_group.store_group_object_list
