import unittest

from starter import distinct_sources, sources_in_both, sources_only_in_a


class TestSourceTracker(unittest.TestCase):
    def test_distinct_sources_deduplicates(self):
        readings = [
            {"source": "substation-12"},
            {"source": "substation-12"},
            {"source": "substation-7"},
        ]
        self.assertEqual(distinct_sources(readings), {"substation-12", "substation-7"})

    def test_distinct_sources_returns_a_set(self):
        readings = [{"source": "a"}]
        self.assertIsInstance(distinct_sources(readings), set)

    def test_sources_in_both_intersection(self):
        result = sources_in_both({"a", "b", "c"}, {"b", "c", "d"})
        self.assertEqual(result, {"b", "c"})

    def test_sources_in_both_no_overlap(self):
        self.assertEqual(sources_in_both({"a"}, {"b"}), set())

    def test_sources_only_in_a_difference(self):
        result = sources_only_in_a({"a", "b", "c"}, {"b", "c", "d"})
        self.assertEqual(result, {"a"})

    def test_sources_only_in_a_is_not_symmetric(self):
        a, b = {"x", "y"}, {"y", "z"}
        self.assertNotEqual(sources_only_in_a(a, b), sources_only_in_a(b, a))


if __name__ == "__main__":
    unittest.main()
