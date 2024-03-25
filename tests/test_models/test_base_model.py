#!/usr/bin/python3
"""BaseModel unit test"""

import unittest
import models
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """BaseModel class test"""

    def test_docstring(self):
        """Test if funcions, methods, classes
        and modules have docstring"""
        message = "Module does not has docstring"
        self.assertIsNotNone(models.base_model.__doc__, message)
        message = "Class does not has docstring"
        self.assertIsNotNone(BaseModel.__doc__, message)

    def test_executable_file(self):
        """Test if file has permissions u+x to execute"""

        readAccess = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(readAccess)

        writeAccess = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(writeAccess)

        execAccess = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(execAccess)

    def test_init_BaseModel(self):
        """Test if an object is of type BaseModel"""
        my_object = BaseModel()
        self.assertIsInstance(my_object, BaseModel)

    def testId(self):
        """Test that id is unique"""
        firstBaseModelId = BaseModel()
        secondBaseModelId = BaseModel()
        self.assertNotEqual(firstBaseModelId.id, secondBaseModelId.id)

    def testStr(self):
        """Check if the output of str is in the specified format"""
        myStringifyBaseModel = BaseModel()
        __dict = myStringifyBaseModel.__dict__
        string1 = "[BaseModel] ({}) {}".format(myStringifyBaseModel.id, __dict)
        string2 = str(myStringifyBaseModel)
        self.assertEqual(string1, string2)

    def testSave(self):
        """Check if date update when save"""
        myBaseModel = BaseModel()
        firstUpdate = myBaseModel.updated_at
        myBaseModel.save()
        secondUpdate = myBaseModel.updated_at
        self.assertNotEqual(firstUpdate, secondUpdate)

    def test_to_dict(self):
        """Check if to_dict returns a dictionary, if add a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format."""
        myBaseModel = BaseModel()
        myBaseModelDict = myBaseModel.to_dict()
        self.assertIsInstance(myBaseModelDict, dict)
        for key, value in myBaseModelDict.items():
            flag = 0
            if myBaseModelDict['__class__'] == 'BaseModel':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in myBaseModelDict.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
