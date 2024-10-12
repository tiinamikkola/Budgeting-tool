from Group import Income_group, Store_group
from readfiles import ReadFile
import Transactions
from Transactions import Income, Store
from DrawDiagram import Diagrams

def get_best_match(word, list): #suggest a best match for user input. If no matches found, returns the input itself. Best match = largest number of same letters in same position of string.
    max_match = 0
    match = ""
    search_list = []

    # split word into possible substrings
    for a in range(len(word)):
        for b in range(a + 1, len(word) + 1):
            substring = word[a:b].lower()
            search_list.append(substring)

    #split option list items into all possible substrings, and find longest common substring
    for option in list:
        option_list = []
        for a in range(len(option)):
            for b in range(a + 1, len(option) + 1):
                substring = option[a:b].lower()
                option_list.append(substring)
        for string in search_list:
            for search_string in option_list:
                if search_string == string:
                    if len(string) > max_match:
                        max_match = len(string)
                        match = option

    if max_match <= 2: #if longest common substring is one or two letters, do not suggest it as mach
        return word
    ask = input("Did you mean '" + match + "'? (yes/no) ")
    ask = ask.lower()
    ask = ask.strip()
    while ask != "yes" and ask != "no":
        ask = input("Did you mean '" + match + "'? (yes/no) ")
        ask = ask.lower()
        ask = ask.strip()
    if ask == "yes":
        return match
    elif ask == "no":
        return word

def make_transaction_objects(transaction_list):
    for transactions in transaction_list:
        transaction = transactions.split(";")
        store = transaction[0]
        amount = float(transaction[1])
        if amount > 0:
            if Income.check_if_income_exists(store):
                Income.add_amount(transaction_object, amount)
            elif not Income.check_if_income_exists(store):
                transaction_object = Transactions.Income(store, amount)
        elif amount <= 0:
            if Store.check_if_store_exists(store):
                Store.add_amount(transaction_object, amount)
            elif not Store.check_if_store_exists(store):
                transaction_object = Store(store, amount)

def make_groups():
    group_type = input("Do you want to add a group for incomes or costs? (income/cost): ")
    group_type = group_type.lower()
    group_type = group_type.rstrip()
    while group_type != "income" and group_type != "cost":
        group_type = input("Please select 'cost' or 'income'.")
        group_type = group_type.lower()
        group_type = group_type.rstrip()
    group_name = input("Please enter name of new group: ")
    if group_type == "cost":
        if Store_group.check_if_store_group_exists(group_name):
            print("Cost group " + group_name + " already exists.")
        elif not Store_group.check_if_store_group_exists(group_name):
            group_object = Store_group(group_name)
            print("Cost group " + group_name + " added.")
    elif group_type == "income":
        if Income_group.check_if_income_group_exists(group_name):
            print("Income group " + group_name + " already exists.")
        elif not Income_group.check_if_income_group_exists(group_name):
            group_object = Income_group(group_name)
            print("Income group " + group_name + " added.")

def add_transactions_to_groups():
    # asks for group type
    group_type = input("Do you want to add transactions to income or cost groups? (income/cost): ")
    group_type = group_type.lower()
    group_type = group_type.rstrip()
    while group_type != "income" and group_type != "cost":
        group_type = input("Please select 'cost' or 'income'.")
        group_type = group_type.lower()
        group_type = group_type.rstrip()

    #asks for income group and transaction
    if group_type == "income":
        if len(Income_group.income_group_list) == 0:
            print("You have no income groups!")
            return None
        print("Current income groups: " + str(Income_group.income_group_list))

        group = input("Choose a group in which you want to add transactions: ")
        while not Income_group.check_if_income_group_exists(group):
            group = get_best_match(group, Income_group.income_group_list)
            if not Income_group.check_if_income_group_exists(group):
                group = input("Income group " + group + " does not exist. Choose another group: ")


        print("Current income transactions: " + str(Income.income_list))
        transaction = input("Which income transaction do you want to add to group " + group + "?: ")
        while not Income.check_if_income_exists(transaction):
            transaction = get_best_match(transaction, Income.income_list)
            if not Income.check_if_income_exists(transaction):
                transaction = str(input("Transaction " + transaction + " does not exist. Choose another transaction: "))

        # adds income transaction to group
        correct_transaction_object = Income.get_correct_income(transaction)
        correct_group_object = Income_group.get_correct_group(group)
        correct_group_object.add_transaction_to_group(correct_transaction_object)

     #asks for cost group and transaction
    elif group_type == "cost":
        if len(Store_group.store_group_list) == 0:
            print("You have no cost groups!")
            return None
        print("Current cost groups:" + str(Store_group.store_group_list))
        group = input("Choose a group in which you want to add transactions: ")
        while not Store_group.check_if_store_group_exists(group):
            group = get_best_match(group, Store_group.store_group_list)
            if not Store_group.check_if_store_group_exists(group):
                group = input("Cost group " + group + " does not exist. Choose another group: ")
        print("Current cost transactions: " + str(Store.store_list))
        transaction = input("Which cost transaction do you want to add to group " + group + "?: ")
        while not Store.check_if_store_exists(transaction):
            transaction = get_best_match(transaction, Store.store_list)
            if not Store.check_if_store_exists(transaction):
                transaction = input("Transaction does not exist. Choose transaction from list above. ")

        # add cost transaction to group
        correct_transaction_object = Store.get_correct_store(transaction)
        correct_group_object = Store_group.get_correct_group(group)
        correct_group_object.add_transaction_to_group(correct_transaction_object)

def remove_transaction_from_group():
    #asks for group
    type = input("Do you want to remove transaction from cost or income group? (cost/income) ")
    while type != "income" and type != "cost":
        type = input("Please select either 'cost' or 'income'. ")
    if type == "cost":
        if len(Store_group.store_group_list) == 0:
            print("You have no cost groups!")
            return None
        print("Current cost groups are " + str(Store_group.store_group_list))
    elif type == "income":
        if len(Income_group.income_group_list) == 0:
            print("You have no income groups!")
            return None
        print("Current income groups are " + str(Income_group.income_group_list))
    group = input("Which group do you want to remove transactions from? ")
    if type == "cost":
        while not Store_group.check_if_store_group_exists(group):
            group = get_best_match(group, Store_group.store_group_list)
            if not Store_group.check_if_store_group_exists(group):
                group = input("Cost group " + group + " does not exists. Choose another group: ")
        correct_group_object = Store_group.get_correct_group(group)
    elif type == "income":
        while not Income_group.check_if_income_group_exists(group):
            group = get_best_match(group, Income_group.income_group_list)
            if not Income_group.check_if_income_group_exists(group):
                group = input("Income group " + group + " does not exists. Choose another group: ")
        correct_group_object = Income_group.get_correct_group(group)

    #asks for transaction, then removes it from group
    i = 0
    cost_list = correct_group_object.get_group_object_list()
    if len(cost_list) == 0:
        print("This group is already empty!")
    else:
        print("Current transactions in this group are:")
        for costs in cost_list:
            print(costs.get_store())
        transaction = input("Choose a transaction which you want to remove from group. ")
        for costs in cost_list:
            if transaction == costs.get_store():
                i += 1
                correct_transaction_object = costs
                correct_group_object.remove_transaction_from_group(correct_transaction_object)
                print("Transaction removed from group.")
        #if no exact match found, tries to find a close match
        if i == 0:
            transaction = get_best_match(transaction, cost_list)
            for costs in cost_list:
                if transaction == costs.get_store():
                    i += 1
                    correct_transaction_object = costs
                    correct_group_object.remove_transaction_from_group(correct_transaction_object)
                    print("Transaction removed from group.")
        #if no close match found either, quits trying
        if i == 0:
            print("Transaction is not in this group.")


def remove_group():
    check = True
    type = input("Do you want to remove cost or income group? (cost/income) ")
    while type != "income" and type != "cost":
        type = input("Please select either 'cost' or 'income'. ")
    if type == "cost":
        if len(Store_group.store_group_list) == 0:
            print("You have no cost groups!")
            check = False
        else:
            print("Current cost groups are " + str(Store_group.store_group_list))
    elif type == "income":
        if len(Income_group.income_group_list) == 0:
            print("You have no income groups!")
            check = False
        else:
            print("Current income groups are " + str(Income_group.income_group_list))
    if check:
        group = input("Which group do you want to remove? ")
        if type == "cost":
            while not Store_group.check_if_store_group_exists(group):
                group = get_best_match(group, Store_group.store_group_list)
                if not Store_group.check_if_store_group_exists(group):
                    group = input("Cost group " + group + " does not exists. Choose another group: ")
            correct_group_object = Store_group.get_correct_group(group)
            correct_group_object.delete_store_group(group)
        elif type == "income":
            while not Income_group.check_if_income_group_exists(group):
                group = get_best_match(group, Income_group.income_group_list)
                if not Income_group.check_if_income_group_exists(group):
                    group = input("Income group " + group + " does not exists. Choose another group: ")
            correct_group_object = Income_group.get_correct_group(group)
            correct_group_object.delete_income_group(group)


def print_stats():
    data = int(input("What data do you want to print? (1 = incomes individually, 2 = costs individually, 3 = income groups, 4 = cost groups) "))
    while data != 1 and data != 2 and data != 3 and data != 4:
        data = int(input("Choose a number between 1 and 4 (1 = incomes individually, 2 = costs individually, 3 = income groups, 4 = cost groups). "))
    if data == 1:
        list = Diagrams.income_data()
        name = "Transaction"
        sum = "sum"
        share = "% of total income"
    if data == 2:
        list = Diagrams.store_data()
        name = "Transaction"
        sum = "sum"
        share = "% of total spending"
    if data == 3:
        list = Diagrams.income_group_data()
        name = "Group"
        sum = "sum"
        share = "% of total income"
    if data == 4:
        list = Diagrams.store_group_data()
        name = "Group"
        sum = "sum"
        share = "% of total spending"
    print("****************************************************************")
    print("{:35s}{:10s}{:10s}".format(name, sum, share))
    print("----------------------------------------------------------------")
    for x in list:
        data = x.split(";")
        print("{:30s}{:10.2f}{:10.2f}".format(data[0], float(data[1]), float(data[2])))
    print("****************************************************************")


def main():
     try:
         #opens and reads a file, returns list of all transactions
         file = input("Please enter the name of file: ")
         file_object = ReadFile(file)
         file_opened = ReadFile.openfile(file_object)
         transaction_list = ReadFile.readlines(file_opened)

         #makes store/income objects
         make_transaction_objects(transaction_list)

         #asks what user wants to do
         print("File read. Now you can organize transactions into groups (example: Groceries).")
         do = int(input("What would you like to do? (1 = add new groups, 2 = add transactions to existing groups, 3 = remove transactions from groups 4 = delete groups, 5 = print statistics, 6 = exit): "))
         while do != 6:
            while do != 1 and do != 2 and do != 3 and do != 4 and do != 5:
                do = int(input("Please select number between 1 and 6 (1 = add new groups, 2 = add transactions to existing groups, 3 = remove transactions from groups 4 = delete groups, 5 = print statistics, 6 = exit): "))
            if do == 1: #make groups
                make_groups()
            if do == 2: #add transactions to groups
                add_transactions_to_groups()
            if do == 3: #remove transactions from groups
                remove_transaction_from_group()
            if do == 4: #remove groups
                remove_group()
            if do == 5: #print results
                print_stats()
            do = int(input("What would you like to do next? (1 = add new groups, 2 = add transactions to existing groups, 3 = remove transactions from groups, 4 = delete groups, 5 = print statistics 6 = exit): "))
         if do == 6:
            exit
     except OSError:
        print("File incorrect.")
main()
