import unittest
from unittest.mock import patch
from io import StringIO
from main import main

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_output(self):
        # Capture the stdout to test the print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            self.assertEqual(fake_output.getvalue().strip(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()