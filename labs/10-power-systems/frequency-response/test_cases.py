import unittest

from starter import frequency_deviation_hz, recovery_timeline


class TestFrequencyDeviation(unittest.TestCase):
    def test_shortfall_gives_negative_deviation(self):
        # (4950 - 5000) / (5 * 1000) = -0.01 Hz
        self.assertAlmostEqual(frequency_deviation_hz(4950, 5000), -0.01)

    def test_surplus_gives_positive_deviation(self):
        self.assertAlmostEqual(frequency_deviation_hz(5100, 5000), 0.02)

    def test_balance_gives_zero_deviation(self):
        self.assertAlmostEqual(frequency_deviation_hz(5000, 5000), 0.0)


class TestRecoveryTimeline(unittest.TestCase):
    def test_fast_response_recovers_in_hand_computed_steps(self):
        # 200 kW spike, ramping 50/step: outputs 50,100,150,200 ->
        # remaining 150,100,50,0 -- four steps
        timeline = recovery_timeline(200, response_capacity_kw=500, ramp_rate_kw_per_step=50)
        self.assertEqual(timeline, [150, 100, 50, 0])

    def test_slower_ramp_takes_more_steps_than_faster_ramp(self):
        # The lesson's core point: response SPEED, not just capacity,
        # determines how long the imbalance persists.
        slow = recovery_timeline(200, response_capacity_kw=500, ramp_rate_kw_per_step=25)
        fast = recovery_timeline(200, response_capacity_kw=500, ramp_rate_kw_per_step=100)
        self.assertGreater(len(slow), len(fast))

    def test_ramp_never_exceeds_capacity(self):
        # 300 kW spike but only 100 kW of response capacity: the
        # imbalance plateaus at 200 -- an instant-correction bug would
        # show 0 here.
        timeline = recovery_timeline(300, response_capacity_kw=100, ramp_rate_kw_per_step=50)
        self.assertEqual(timeline[-1], 200)
        self.assertNotIn(0, timeline)

    def test_single_step_recovery_when_ramp_covers_everything(self):
        timeline = recovery_timeline(50, response_capacity_kw=500, ramp_rate_kw_per_step=100)
        self.assertEqual(timeline, [0])


if __name__ == "__main__":
    unittest.main()
