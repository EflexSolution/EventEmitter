# test_eventemitter.py
"""
Tests for EventEmitter module.
"""

import unittest
from eventemitter import EventEmitter

class TestEventEmitter(unittest.TestCase):
    """Test cases for EventEmitter class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EventEmitter()
        self.assertIsInstance(instance, EventEmitter)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EventEmitter()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
