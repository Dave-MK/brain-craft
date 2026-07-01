def classify_demand(reading_kw, safe_limit_kw=5000, warning_kw=4500):
    if reading_kw >= safe_limit_kw:
        return "OVERLOAD"
    elif reading_kw > warning_kw:
        return "WARNING"
    return "NORMAL"
