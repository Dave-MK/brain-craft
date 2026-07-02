import unittest

from starter import loss_percent, transmission_loss_kw


class TestTransmissionLoss(unittest.TestCase):
    def test_hand_computed_loss_at_distribution_voltage(self):
        # I = 5,000,000 W / 11,000 V = 454.545... A
        # loss = I^2 * 0.5 = 103,305.79 W = 103.3 kW
        loss = transmission_loss_kw(5000, 11, 0.5)
        self.assertAlmostEqual(loss, 103.3058, places=2)

    def test_hand_computed_loss_at_transmission_voltage(self):
        # I = 5,000,000 / 400,000 = 12.5 A; loss = 156.25 * 0.5 = 78.125 W = 0.078 kW
        loss = transmission_loss_kw(5000, 400, 0.5)
        self.assertAlmostEqual(loss, 0.078125, places=5)

    def test_doubling_voltage_quarters_the_loss(self):
        # THE defining relationship of the lesson: loss scales with I^2,
        # and I halves when V doubles at fixed power.
        low = transmission_loss_kw(5000, 100, 0.5)
        high = transmission_loss_kw(5000, 200, 0.5)
        self.assertAlmostEqual(low / high, 4.0, places=6)

    def test_doubling_power_quadruples_the_loss(self):
        # loss depends on the square of current, hence of power at fixed V
        # -- exactly why a flat "loss percent per edge" was unrealistic.
        base = transmission_loss_kw(2500, 100, 0.5)
        double = transmission_loss_kw(5000, 100, 0.5)
        self.assertAlmostEqual(double / base, 4.0, places=6)

    def test_loss_percent_hand_computed(self):
        # 103.3058 kW of 5000 kW is ~2.066%
        self.assertAlmostEqual(loss_percent(5000, 11, 0.5), 2.0661, places=3)

    def test_loss_percent_is_not_constant_across_power_levels(self):
        # The Mission 5 flat-percentage assumption fails here: at fixed
        # voltage, the loss PERCENT itself grows with power flow.
        self.assertGreater(loss_percent(5000, 100, 0.5), loss_percent(2500, 100, 0.5))


if __name__ == "__main__":
    unittest.main()
