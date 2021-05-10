import unittest
import coder

class EncodeTestCases(unittest.TestCase):

    def test_encode_programozok(self):
        self.assertEqual(coder.string_encoding("Programozok"), [80, 34, -3, -8, 11, -17, 12, 2, 11, -11, -4])

    def test_encode_barack(self):
        self.assertEqual(coder.string_encoding("Barack"), [66, 31, 17, -17, 2, 8])

    def test_encode_2es(self):
        self.assertEqual(coder.string_encoding("2es"), [50, 51, 14])


class DecodeTestCases(unittest.TestCase):

    def test_decode_programozok(self):
        self.assertEqual(coder.string_decoding([80, 34, -3, -8, 11, -17, 12, 2, 11, -11, -4]), "Programozok")

    def test_decode_barack(self):
        self.assertEqual(coder.string_decoding([66, 31, 17, -17, 2, 8]), "Barack")

    def test_decode_2es(self):
        self.assertEqual(coder.string_decoding([50, 51, 14]), "2es")

if __name__ == "__main__":
    unittest.main()