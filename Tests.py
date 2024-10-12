import unittest
from readfiles import ReadFile
from Group import Store_group
from Transactions import Store

#checks that readlines-function from ReadFile class extracts correct data
class TestReadLines(unittest.TestCase):
    def test_readinglines(self):
        file = open("testfile", "r")
        test_object = ReadFile.readlines(file)
        test_list = ["KELA/FPA;268.23"]
        self.assertEqual(test_object, test_list)
        file.close()

#checks that cost transaction is not deleted when group which it belongs to is deleted
class TestGroupRemoving(unittest.TestCase):
    def test_delete_group(self):
        test_store = Store("Testtransaction", 10.0)
        test_group = Store_group("Testgroup")
        test_group.add_transaction_to_group(test_store)
        test_group.delete_store_group("Testgroup")
        check = Store.check_if_store_exists("Testtransaction")
        self.assertTrue(check, "Test failed: transaction deleted.")



