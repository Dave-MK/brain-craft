import unittest

from starter import SensorReading


class TestSensorReadingClass(unittest.TestCase):
    def test_stores_attributes(self):
        r = SensorReading(4821, "substation-12")
        self.assertEqual(r.demand_kw, 4821)
        self.assertEqual(r.source, "substation-12")

    def test_classify_overload_boundary(self):
        r = SensorReading(5000, "substation-12")
        self.assertEqual(r.classify(), "OVERLOAD")

    def test_classify_warning(self):
        r = SensorReading(4600, "substation-12")
        self.assertEqual(r.classify(), "WARNING")

    def test_classify_normal(self):
        r = SensorReading(1000, "substation-12")
        self.assertEqual(r.classify(), "NORMAL")

    def test_custom_thresholds_per_instance(self):
        r1 = SensorReading(900, "a", safe_limit_kw=1000, warning_kw=800)
        r2 = SensorReading(900, "b", safe_limit_kw=2000, warning_kw=1800)
        self.assertEqual(r1.classify(), "WARNING")
        self.assertEqual(r2.classify(), "NORMAL")

    def test_instances_do_not_share_state(self):
        r1 = SensorReading(5000, "a")
        r2 = SensorReading(100, "b")
        self.assertEqual(r1.classify(), "OVERLOAD")
        self.assertEqual(r2.classify(), "NORMAL")
        self.assertEqual(r1.demand_kw, 5000)
        self.assertEqual(r2.demand_kw, 100)


if __name__ == "__main__":
    unittest.main()
