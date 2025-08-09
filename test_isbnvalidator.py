# test_isbnvalidator.py
"""
Tests for IsbnValidator module.
"""

import unittest
from isbnvalidator import IsbnValidator

class TestIsbnValidator(unittest.TestCase):
    """Test cases for IsbnValidator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = IsbnValidator()
        self.assertIsInstance(instance, IsbnValidator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IsbnValidator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
