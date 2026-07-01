import unittest

import pandas as pd

from starter import filter_overload, filter_overload_from_source, summarize_by_source

DF = pd.DataFrame({
    "source": ["substation-12", "substation-12", "substation-12", "substation-7", "substation-7"],
    "demand_kw": [4821, 5100, 5300, 4600, 3800],
})


class TestMaskGroupby(unittest.TestCase):
    def test_filter_overload_default_threshold(self):
        result = filter_overload(DF)
        self.assertEqual(sorted(result["demand_kw"].tolist()), [5100, 5300])

    def test_filter_overload_custom_threshold(self):
        result = filter_overload(DF, threshold=4700)
        self.assertEqual(sorted(result["demand_kw"].tolist()), [4821, 5100, 5300])

    def test_filter_overload_from_source_combines_both_conditions(self):
        result = filter_overload_from_source(DF, threshold=5000, source="substation-12")
        self.assertEqual(sorted(result["demand_kw"].tolist()), [5100, 5300])

    def test_filter_overload_from_source_excludes_other_sources_even_if_over_threshold(self):
        # threshold=3000 is low enough that both substation-7 readings pass it,
        # AND low enough that substation-12's (higher) readings would also
        # pass on demand_kw alone -- this only works if the source filter is
        # genuinely being applied, not just the threshold.
        result = filter_overload_from_source(DF, threshold=3000, source="substation-7")
        self.assertEqual(sorted(result["demand_kw"].tolist()), [3800, 4600])
        self.assertTrue((result["source"] == "substation-7").all())

    def test_summarize_by_source_mean_and_max(self):
        summary = summarize_by_source(DF)
        self.assertAlmostEqual(summary.loc["substation-12", "mean"], (4821 + 5100 + 5300) / 3)
        self.assertEqual(summary.loc["substation-12", "max"], 5300)
        self.assertEqual(summary.loc["substation-7", "max"], 4600)


if __name__ == "__main__":
    unittest.main()
