import unittest

from prob4_localization_program import localize, show, sense, move


class LocalizeTest(unittest.TestCase):
    def test_sense_one_R(self):
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

    def test_sense_two_R(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        measurement = 'R'
        sensor_right = 1.0
        correct_answer = (
            [[0.0, 0.0, 0.0],
             [0.0, 0.5, 0.5],
             [0.0, 0.0, 0.0]])
        self.assertEqual(sense(colors, measurement, sensor_right), correct_answer)

    def test_sense_two_R_with_error(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        measurement = 'R'
        sensor_right = 0.8
        correct_answer = (
            [[0.06666666666, 0.06666666666, 0.06666666666],
             [0.06666666666, 0.26666666666, 0.26666666666],
             [0.06666666666, 0.06666666666, 0.06666666666]])
        answer = sense(colors, measurement, sensor_right)
        for row_index in range(len(answer)):
            for tile_index in range(len(answer[row_index])):
                difference = answer[row_index][tile_index] - correct_answer[row_index][tile_index]
                # make sure that the difference between the elements is negligible
                self.assertLess(difference, abs(.000000001))

    def test_move_single_row(self):
        pmap = [[0,1,0,0,0]]
        motion = [0,1]
        p_move = 1.0
        answer = move(pmap, motion, p_move)

        correct_answer = [[0,0,1,0,0]]
        self.assertEqual(answer, correct_answer)

    def test_move_single_row_negative(self):
        pmap = [[0,1,0,0,0]]
        motion = [0,-1]
        p_move = 1.0
        answer = move(pmap, motion, p_move)

        correct_answer = [[1,0,0,0,0]]
        self.assertEqual(answer, correct_answer)

    def test_move_single_row_with_move_error(self):
        pmap = [[0,1,0,0,0]]
        motion = [0,1]
        p_move = 0.8
        answer = move(pmap, motion, p_move)

        correct_answer = [[0,0.2,0.8,0,0]]
        for row_index in range(len(answer)):
            for tile_index in range(len(answer[row_index])):
                difference = answer[row_index][tile_index] - correct_answer[row_index][tile_index]
                # make sure that the difference between the elements is negligible
                self.assertLess(difference, abs(.000000001))

    def test_move_single_row_two_moves(self):
        pmap = [[0,1,0,0,0]]
        motion = [0,2]
        p_move = 1.0
        answer = move(pmap, motion, p_move)

        correct_answer = [[0,0,0,1,0]]
        self.assertEqual(answer, correct_answer)

    def test_move_column(self):
        pmap = [[0, 0], [1, 0], [0, 0], [0, 0], [0, 0]]
        motion = [1,0]
        p_move = 1.0
        answer = move(pmap, motion, p_move)

        correct_answer = [[0, 0], [0, 0], [1, 0], [0, 0], [0, 0]]
        self.assertEqual(answer, correct_answer)

    def test_localize(self):
        pass
    def test_show(self):
        pass