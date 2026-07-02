import unittest

from starter import render_dashboard_summary, summarize_top_trade_off

EXPLANATION = {
    "recommendation": "discharge",
    "supporting_quantities": {"cost": -1.5, "emissions": 0.2, "safety_margin": 0.35, "loss_percent": 2.1},
    "alternatives_considered": ["charge", "hold"],
    "confidence_statement": "validated on 3 periods",
}


class TestSummarizeTopTradeOff(unittest.TestCase):
    def test_keeps_the_two_largest_by_absolute_value(self):
        result = summarize_top_trade_off(EXPLANATION["supporting_quantities"])
        self.assertEqual(set(result.keys()), {"loss_percent", "cost"})
        self.assertEqual(result["cost"], -1.5)

    def test_absolute_value_not_raw_value_decides(self):
        # -10 beats +5 on magnitude even though it's "smaller"
        result = summarize_top_trade_off({"a": -10, "b": 5, "c": 1})
        self.assertEqual(set(result.keys()), {"a", "b"})

    def test_exactly_two_entries_come_back(self):
        result = summarize_top_trade_off(EXPLANATION["supporting_quantities"])
        self.assertEqual(len(result), 2)


class TestRenderDashboardSummary(unittest.TestCase):
    def test_unsafe_status_raises_the_banner(self):
        summary = render_dashboard_summary(EXPLANATION, {"is_safe": False})
        self.assertEqual(summary["alert_banner"], "UNSAFE")

    def test_safe_status_shows_no_banner(self):
        summary = render_dashboard_summary(EXPLANATION, {"is_safe": True})
        self.assertIsNone(summary["alert_banner"])

    def test_recommendation_is_top_level(self):
        summary = render_dashboard_summary(EXPLANATION, {"is_safe": True})
        self.assertEqual(summary["primary_recommendation"], "discharge")

    def test_detail_stays_nested_not_flattened_to_top_level(self):
        # THE planted bug: flattening every field to the top level gives
        # the safety banner the same visual weight as routine detail.
        summary = render_dashboard_summary(EXPLANATION, {"is_safe": True})
        self.assertNotIn("alternatives_considered", summary, "routine detail leaked to the top level -- it belongs inside details_expandable")
        self.assertNotIn("confidence_statement", summary)
        self.assertEqual(summary["details_expandable"], EXPLANATION)

    def test_top_level_has_exactly_the_four_summary_keys(self):
        summary = render_dashboard_summary(EXPLANATION, {"is_safe": False})
        self.assertEqual(
            set(summary.keys()),
            {"alert_banner", "primary_recommendation", "key_trade_off", "details_expandable"},
        )


if __name__ == "__main__":
    unittest.main()
