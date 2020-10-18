import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """test city_functions.py"""
    def test_city_country(self):
        """能否正确输出如Tokyo, Japan这样的结果"""
        result_city = city_country('tokyo','japan')
        self.assertEqual(result_city,'Tokyo, Japan')
    
    def test_city_country_population(self):
        """test when population entered"""
        result_city = city_country('tokyo','japan','30000000')
        self.assertEqual(result_city,'Tokyo, Japan - Population 30000000')

if __name__ == "__main__":
    unittest.main()