def high_priority(tasks):
    tasks[:] = [task for task in tasks if task["priority"] == "high"]
    return list(tasks)
