import unittest

from starter import gradient_at, minimize_quadratic


class TestManualGradientDescent(unittest.TestCase):
    def test_gradient_matches_hand_computed_derivative(self):
        # dy/dx of 3x^2 - 5x + 1 is 6x - 5: exactly 13 at x=3
        self.assertAlmostEqual(gradient_at(3.0), 13.0, places=4)

    def test_gradient_at_a_second_point(self):
        # 6*(-2) - 5 = -17
        self.assertAlmostEqual(gradient_at(-2.0), -17.0, places=4)

    def test_gradient_is_a_plain_float_not_a_tensor(self):
        result = gradient_at(1.0)
        self.assertIsInstance(result, float)

    def test_descent_converges_to_the_known_minimum(self):
        final_x = minimize_quadratic(start_x=0.0, learning_rate=0.1, steps=50)
        self.assertAlmostEqual(final_x, 4.0, places=2)

    def test_descent_converges_from_the_other_side_too(self):
        final_x = minimize_quadratic(start_x=10.0, learning_rate=0.1, steps=50)
        self.assertAlmostEqual(final_x, 4.0, places=2)

    def test_descent_actually_moves_not_just_returns_start(self):
        final_x = minimize_quadratic(start_x=0.0, learning_rate=0.1, steps=3)
        self.assertNotAlmostEqual(final_x, 0.0, places=2)
        # 3 steps isn't enough to fully converge -- catching a hardcoded return 4.0
        self.assertNotAlmostEqual(final_x, 4.0, places=2)


if __name__ == "__main__":
    unittest.main()
