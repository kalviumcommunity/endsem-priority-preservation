from copy import deepcopy
from sample_data import TASKS
from priority_view import high_priority

records = deepcopy(TASKS)
print("Before:", records)
print("Selected:", high_priority(records))
print("After:", records)
