import unittest
from unittest.mock import mock_open, patch
from main import save_todos_to_file, load_todos_from_file


class TestTodoApp(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def test_save_todos_to_file(self, mock_file):
        todos = ["Buy groceries", "write tests", "Call friend"]
        file_path = "todos.txt"

        # Call the function
        save_todos_to_file(file_path, todos)

        # Ensure the file was opened in write mode
        mock_file.assert_called_once_with(file_path, "w")
        # Check that the correct data was written to the file
        mock_file().writelines.assert_called_once_with(todo + "\n" for todo in todos)

    @patch("builtins.open", mock_open(read_data="Buy groceries\nwrite tests\nCall friend\n"))
    def test_load_todos_from_file(self):
        file_path = "todos.txt"

        # Call the function
        result = load_todos_from_file(file_path)

        # Check that the returned list matches the file content
        self.assertEqual(result, ["Buy groceries", "write tests", "Call friend"])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_todos_from_file_file_not_found(self, mock_file):
        file_path = "todos.txt"

        # Call the function
        result = load_todos_from_file(file_path)

        # Ensure an empty list is returned when the file doesn't exist
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
