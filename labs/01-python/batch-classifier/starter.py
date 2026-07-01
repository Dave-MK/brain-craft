"""
Lab: Batch Classifier
Lesson: python-loops

Classify a whole list of demand readings at once, reusing the same
threshold logic from the Control Flow lesson.
"""


def classify_batch(readings, safe_limit_kw=5000, warning_threshold_kw=4500):
    """Return a list of "OVERLOAD"/"WARNING"/"NORMAL" strings, one per reading."""
    # TODO: loop over readings and classify each one using the same rules as
    #       the threshold-classifier lab (>= safe_limit_kw is OVERLOAD,
    #       > warning_threshold_kw is WARNING, otherwise NORMAL)
    # TODO: return the list of classifications, same length and order as readings
    raise NotImplementedError("classify_batch is not implemented yet")


if __name__ == "__main__":
    print(classify_batch([4821, 4790, 5100, 4650]))
