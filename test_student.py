import unittest
from typing import *
from proj2 import *

class TestParseRow(unittest.TestCase):

    def test_parse_row_missing_data(self):
    # An example of what the CSV reader gives us
        fake_csv_line = ["Aruba", "1990", "0.5", "", "1.2", "4.5", "", ""]

        expected_row= Row(country='Aruba', 
                        year=1990,
                        electricity_and_heat_co2_emissions=0.5,
                        electricity_and_heat_co2_emissions_per_capita=None,
                        energy_co2_emissions=1.2,
                        energy_co2_emissions_per_capita=4.5,
                        total_co2_emissions_excluding_lucf=None,
                        total_co2_emissions_excluding_lucf_per_capita=None
                        )
    
        self.assertEqual(parse_row(fake_csv_line), expected_row)

class TestLinkedListFunctions(unittest.TestCase):

    def test_listlen(self):
        # 1. Load the fake data from your tiny CSV
        my_list = read_csv_lines("sample.csv")
        
        self.assertEqual(listlen(my_list), 4)

    def test_filter_rows(self):
        # 1. Load the data
        my_list = read_csv_lines("sample.csv")
        
        filtered_list = filter_rows(my_list, "year", "equal", 2007)

        self.assertEqual(listlen(filtered_list), 1)
        pass
    
if __name__ == "__main__":
    unittest.main()