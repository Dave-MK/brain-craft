import unittest

from starter import build_status_report


class TestSensorIntake(unittest.TestCase):
    def test_returns_all_expected_fields(self):
        report = build_status_report(demand_kw=4821, temperature_c=18.5, solar_output_kw=1200)
        for key in ("demand_kw", "demand_mw", "temperature_c", "solar_output_kw"):
            self.assertIn(key, report)

    def test_computes_demand_mw_correctly(self):
        report = build_status_report(demand_kw=4821, temperature_c=18.5, solar_output_kw=1200)
        self.assertAlmostEqual(report["demand_mw"], 4.821)

    def test_preserves_raw_readings_unchanged(self):
        report = build_status_report(demand_kw=5000, temperature_c=-3.2, solar_output_kw=0)
        self.assertEqual(report["demand_kw"], 5000)
        self.assertEqual(report["temperature_c"], -3.2)
        self.assertEqual(report["solar_output_kw"], 0)

    def test_handles_zero_demand(self):
        report = build_status_report(demand_kw=0, temperature_c=10.0, solar_output_kw=500)
        self.assertEqual(report["demand_mw"], 0)


if __name__ == "__main__":
    unittest.main()
