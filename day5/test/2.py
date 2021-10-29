import unittest
import application

lista = [11, 22, 33]

class TestSample(unittest.TestCase):
    def test_one(self):
        self.assertEqual(application.add(lista), 66)

    def test_two(self):
        self.assertListEqual(lista, [11, 22, 44])

unittest.main()
