from priority_view import high_priority

records = [{"title": "A", "priority": "high", "completed": True}, {"title": "B", "priority": "low", "completed": False}]
assert [task["title"] for task in high_priority(records)] == ["A"]
assert high_priority([]) == []
print("Existing checks passed: selected titles and empty input")
