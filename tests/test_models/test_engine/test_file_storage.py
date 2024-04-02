#!/usr/bin/python3
"""test for file storage"""
import unittest
import os
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """FileStorage test class"""

    def test_all(self):
        """Tests all"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_reload(self):
        """
        Tests reload
        """
        self.storage.save()
        root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(root, "file.json")
        with open(path, 'r') as file:
            lines = file.readlines()
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
        self.storage.save()
        with open(path, 'r') as file:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
        with open(path, "w") as file:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
