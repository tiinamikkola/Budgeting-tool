#this class reads a csv-file, extracts needed data and returns it as a list

class ReadFile:
    def __init__(self, file):
        self.input = file

    def openfile(self):
        self.input = open(self.input, "r")
        return self.input

    def readlines(self):
        transaction_list = []
        header = self.readline()
        lines = self.readlines()
        if len(lines) == 0:
            raise Exception("File has no lines to read.")
        for line in lines:
            line_osat = line.split(";")
            if len(line_osat) < 5:
                print("Faulty line skipped: " + line )
            else:
                amount = line_osat[2].replace('"','')
                amount = amount.replace(',', '.')
                store = line_osat[5].replace('"', '')
                transaction_data = store + ";" + amount
                transaction_list.append(transaction_data)
            if len(transaction_list) == 0:
                raise Exception("File has no lines to read.")
        return transaction_list #returns a list with items of type store;amount






