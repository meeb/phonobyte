import os
import unittest
import phonobyte


class TestEncoder(unittest.TestCase):

    def test_encode(self):
        test_input = b'test'
        expected_output = 'lab don nub lab'
        self.assertEqual(phonobyte.encode(test_input),
                         expected_output)

    def test_encode_list(self):
        test_input = b'test'
        expected_output = ['lab', 'don', 'nub', 'lab']
        self.assertEqual(phonobyte.encode(test_input, return_string=False),
                         expected_output)

    def test_decode(self):
        test_input = 'lab don nub lab'
        expected_output = b'test'
        self.assertEqual(phonobyte.decode(test_input),
                         expected_output)

    def test_decode_list(self):
        test_input = ['lab', 'don', 'nub', 'lab']
        expected_output = b'test'
        self.assertEqual(phonobyte.decode(test_input),
                         expected_output)

    def test_full_encode_decode(self):
        test_input = os.urandom(128)
        encoded_data = phonobyte.encode(test_input)
        decoded_output = phonobyte.decode(encoded_data)
        self.assertEqual(test_input,
                         decoded_output)


if __name__ == '__main__':
    unittest.main()
