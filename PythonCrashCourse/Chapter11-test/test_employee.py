import unittest
from employee import Employee

class RaiseTestCase(unittest.TestCase):
    def setUp(self):
        '''default and non-default test cases'''
        first_name = 'Tom'
        last_name = 'Willson'
        year_income = 10000
        self.my_employee = Employee(first_name,last_name,year_income)
        self.raise_num = [None,2500]
    
    def test_default_raise(self):
        '''test for default raise'''
        self.my_employee.give_raise()
        self.assertEqual(15000,self.my_employee.year_income)
    
    def test_non_default_raise(self):
        '''test for non default raise'''
        self.my_employee.give_raise(self.raise_num[1])
        self.assertEqual(self.raise_num[1]+10000,self.my_employee.year_income)

if __name__ == "__main__":
    unittest.main()