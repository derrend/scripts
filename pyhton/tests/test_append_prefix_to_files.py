import unittest
import append_prefix_to_files as f

class TestSubSeedAddressGenerator(unittest.TestCase):
    def test_vanity_address_generate(self):
        self.assertRaises(TypeError, f.append_prefix, 0, 0, 'string')
        self.assertRaises(TypeError, f.append_prefix, '/string/', 0, 0)
        self.assertRaises(TypeError, f.append_prefix, 0, 0, 0)
        self.assertRaises(TypeError, f.append_prefix, '/string/', 'string', 'string')
        self.assertRaises(ValueError, f.append_prefix, '/string/', -1, 'string')
        self.assertRaises(ValueError, f.append_prefix, '/string', 0, 'string')


if __name__ == '__main__':
    unittest.main()
