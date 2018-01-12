import unittest

from prob4_localization_program import localize, show, sense

class LocalizeTest(unittest.TestCase):
    def test_sense(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'G'],
                  ['G', 'G', 'G']]
        measurement = 'R'
        sensor_right = 1.0
        correct_answer = (
            [[0.0, 0.0, 0.0],
             [0.0, 1.0, 0.0],
             [0.0, 0.0, 0.0]])
        self.assertEqual(sense(colors, measurement, sensor_right), correct_answer)

    def test_localize(self):
        pass
    def test_show(self):
        pass