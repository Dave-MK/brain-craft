"""
Lab: Sensor Intake
Lesson: python-variables

You've received three raw sensor readings: demand (kW), temperature (C),
and solar output (kW). Build a status report that holds all three
readings under clearly named keys, plus one derived value: demand
converted from kW to MW.

Implement build_status_report() below.
"""


def build_status_report(demand_kw, temperature_c, solar_output_kw):
    """Return a dict with demand_kw, demand_mw, temperature_c, solar_output_kw."""
    # TODO: compute demand_mw from demand_kw (divide by 1000)
    # TODO: return a dict containing all four values under those exact keys
    raise NotImplementedError("build_status_report is not implemented yet")


if __name__ == "__main__":
    report = build_status_report(demand_kw=4821, temperature_c=18.5, solar_output_kw=1200)
    print(report)
