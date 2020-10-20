import unittest
import unittest.mock as mock

class testBoiler(unittest.TestCase):

    def test_1(self):
       self.assertEqual(True, True)

    @mock.patch("module.class.method")
    def test_mock(self, mock):
        mock.side_effect = ['return1', 'return2']

