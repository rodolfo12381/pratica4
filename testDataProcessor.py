import os
import unittest
from dataProcessor import read_json_file
from dataProcessor import avgAgeCountry, transform_age

class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
       
        self.assertEqual(len(data), 1000)  # Ajustar o número esperado de registros
        self.assertEqual(data[0]['name'], 'Alfred Clark')
        self.assertEqual(data[1]['age'], 18)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")

    def test_avgAgeCountry_empty_json(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
        result = avgAgeCountry(data)
        self.assertEqual(result, {})

    def test_avgAgeCountry_missing_age_values(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
        result = avgAgeCountry(data)
        self.assertEqual(result, {"USA": None, "Canada": None})

    def test_avgAgeCountry_missing_country_values(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
        result = avgAgeCountry(data)
        self.assertEqual(result, {"Unknown": 27.5})

    def test_avgAgeCountry_with_age_transformation(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
        result = avgAgeCountry(data, transform_age)
        self.assertEqual(result, {"USA": 300, "Canada": 360})


if __name__ == '__main__':
    unittest.main()