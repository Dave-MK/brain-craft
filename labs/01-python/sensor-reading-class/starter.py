"""
Lab: SensorReading Class
Lesson: python-oop-basics

Define a SensorReading class that bundles a reading's data with the
ability to classify itself.
"""


class SensorReading:
    def __init__(self, demand_kw, source, safe_limit_kw=5000, warning_kw=4500):
        # TODO: store all four parameters as attributes on self
        raise NotImplementedError("SensorReading.__init__ is not implemented yet")

    def classify(self):
        # TODO: return "OVERLOAD"/"WARNING"/"NORMAL" using self.demand_kw,
        #       self.safe_limit_kw, and self.warning_kw
        raise NotImplementedError("SensorReading.classify is not implemented yet")


if __name__ == "__main__":
    reading = SensorReading(4821, "substation-12")
    print(reading.classify())
