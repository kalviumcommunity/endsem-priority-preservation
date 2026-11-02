from copy import deepcopy
from sample_data import TASKS
from priority_view import high_priority


def check(label, actual, expected):
    assert actual == expected, f"{label}: actual={actual!r}, expected={expected!r}"
    print(f"PASS {label}: {actual!r}")


def run_checks():
    records = deepcopy(TASKS)
    before = None  # COMPLETE independent snapshot of records, not an alias
    selected = high_priority(records)
    check("mixed input preserved", records, before)
    check("mixed selected values and order", selected, [TASKS[0], TASKS[2]])
    check("completed high included", selected[1]["completed"], True)
    check("new mixed result list", selected is not records, True)
    cases = [
        ("no match", [{"title": "Low", "priority": "low", "completed": False}], []),
        ("all match", [TASKS[2], TASKS[0]], [TASKS[2], TASKS[0]]),
        ("empty", [], []),
    ]
    for label, data, expected in cases:
        snapshot = deepcopy(data)
        result = high_priority(data)
        check(label + " selection", result, expected)
        check(label + " records preserved", data, snapshot)
        check(label + " new result list", result is not data, True)
    print("Complete regression passed")


if __name__ == "__main__":
    run_checks()
