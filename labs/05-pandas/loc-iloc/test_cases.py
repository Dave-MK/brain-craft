import unittest

from starter import build_dataframe, select_by_label, select_by_position, set_timestamp_index

RECORDS = [
    {"timestamp": "2026-07-01T09:00", "demand_kw": 4821, "source": "substation-12"},
    {"timestamp": "2026-07-01T10:00", "demand_kw": 4790, "source": "substation-12"},
    {"timestamp": "2026-07-01T11:00", "demand_kw": 5100, "source": "substation-7"},
]


class TestLocIloc(unittest.TestCase):
    def test_build_dataframe_has_correct_shape(self):
        df = build_dataframe(RECORDS)
        self.assertEqual(len(df), 3)
        self.assertEqual(set(df.columns), {"timestamp", "demand_kw", "source"})

    def test_set_timestamp_index_removes_timestamp_as_a_column(self):
        df = set_timestamp_index(build_dataframe(RECORDS))
        self.assertNotIn("timestamp", df.columns)
        self.assertIn("2026-07-01T09:00", df.index)

    def test_select_by_label_uses_the_real_index_label(self):
        df = set_timestamp_index(build_dataframe(RECORDS))
        self.assertEqual(select_by_label(df, "2026-07-01T10:00", "demand_kw"), 4790)

    def test_select_by_position_uses_integer_position_not_label(self):
        df = set_timestamp_index(build_dataframe(RECORDS))
        # after set_index, column 0 is demand_kw, column 1 is source
        self.assertEqual(select_by_position(df, 0, 0), 4821)
        self.assertEqual(select_by_position(df, 2, 1), "substation-7")

    def test_loc_and_iloc_agree_on_the_same_cell(self):
        df = set_timestamp_index(build_dataframe(RECORDS))
        self.assertEqual(
            select_by_label(df, "2026-07-01T11:00", "demand_kw"),
            select_by_position(df, 2, 0),
        )


if __name__ == "__main__":
    unittest.main()
