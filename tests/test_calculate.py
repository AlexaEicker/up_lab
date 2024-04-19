import unittest
from unittest.mock import patch
import numpy as np
from up_lab.calculate.basic_calc import type_change, statistical_analysis

class TestTypeChangeFunction(unittest.TestCase):
    
    def test_numpy_to_list(self):
        values = np.array([1, 2, 3])
        result = type_change(values, list)
        self.assertEqual(result, [1, 2, 3])
    
    def test_list_to_numpy(self):
        values = [1, 2, 3]
        result = type_change(values, np.array)
        np.testing.assert_array_equal(result, np.array([1, 2, 3]))
    
    def test_dict_to_numpy(self):
        values = {'a': [1, 2, 3]}
        result = type_change(values, np.array)
        np.testing.assert_array_equal(result, np.array([1, 2, 3]))
    
    def test_invalid_to_type(self):
        values = np.array([1, 2, 3])
        with self.assertRaises(ValueError):
            type_change(values, int)
    
    def test_unexpected_type(self):
        values = 123  
        with self.assertRaises(TypeError):
            type_change(values, np.array)

    @patch('builtins.input', side_effect=['a'])  # Mocking input to return 'a'
    def test_dict_to_numpy_with_input(self, mock_input):
        values = {'a': [1, 2, 3]}
        result = type_change(values, np.array)
        np.testing.assert_array_equal(result, np.array([1, 2, 3]))
    
    @patch('builtins.input', side_effect=['nonexistent_key', 'a'])  # Mocking input for a nonexistent key and then 'a'
    def test_dict_to_numpy_with_invalid_input(self, mock_input):
        values = {'b': [1, 2, 3]}
        with self.assertRaises(ValueError):
            type_change(values, np.array)


class TestStatisticalAnalysisFunction(unittest.TestCase):
    
    def test_dict_output(self):
        data = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7]
        result = statistical_analysis(data)
        expected_result = {'Mean': 4.4, 'Median': 5.0, 'Mode': 5, 'Standard deviation': 1.4966629547095764, 'Variance': 2.24, 'Range': 6}
        self.assertEqual(result, expected_result)
    
    def test_separate_values_output(self):
        data = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7]
        result = statistical_analysis(data, dict_out=False)
        expected_result = (4.4, 5.0, 5, 1.4966629547095764, 2.24, 6)
        self.assertEqual(result, expected_result)
    
    def test_empty_data(self):
        data = []
        with self.assertRaises(ValueError):
            statistical_analysis(data)
    
    def test_invalid_output_format(self):
        data = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7]
        with self.assertRaises(TypeError):
            statistical_analysis(data, dict_out="invalid_format")

if __name__ == '__main__':
    unittest.main()
