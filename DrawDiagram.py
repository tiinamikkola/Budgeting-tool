from Transactions import Income, Store
from Group import Income_group, Store_group

class Diagrams():
    def income_data():
        sum = 0
        transactions = []
        object_list = Income.get_objects()
        for object in object_list:
            sum += object.get_amount()
        for object in object_list:
            share = (object.get_amount() / sum) * 100
            name = object.get_store()
            amount = object.get_amount()
            transaction_data = str(name) + ";" + str(amount) + ";" + str(share)
            transactions.append(transaction_data)
        return transactions # list with items of type income;amount;share

    def store_data():
        sum = 0
        transactions = []
        object_list = Store.get_objects()
        for object in object_list:
            sum += -(object.get_amount())
        for object in object_list:
            share = ((-object.get_amount()) / sum) * 100
            transaction_data = str(object.get_store()) + ";" + str((-object.get_amount())) + ";" + str(share)
            transactions.append(transaction_data)
        return transactions # list with items of type store;amount;share

    def income_group_data():
        sum = 0
        group_list = []
        object_list = Income.get_objects()
        for object in object_list:
            sum += object.get_amount() #sum is total spending
        groups = Income_group.get_groups()
        for group in groups:
            group_name = group.get_group_object_name()
            group_amount = 0
            incomes_in_group = group.get_group_object_list()
            for incomes in incomes_in_group:
                group_amount += incomes.get_amount()
            share = (group_amount/sum) * 100
            group_data = group_name + ";" + str(group_amount) + ";" + str(share)
            group_list.append(group_data)
        return group_list # list with items of type income_group;amount;share

    def store_group_data():
        sum = 0
        group_list = []
        object_list = Store.get_objects()
        for object in object_list:
            sum += (-object.get_amount())
        groups = Store_group.get_groups()
        for group in groups:
            group_name = group.get_group_object_name()
            group_amount = 0
            stores_in_group = group.get_group_object_list()
            for stores in stores_in_group:
                group_amount += (-stores.get_amount())
            share = (group_amount / sum) * 100
            group_data = group_name + ";" + str(group_amount) + ";" + str(share)
            group_list.append(group_data)
        return group_list  # list with items of type store_group;amount;share


