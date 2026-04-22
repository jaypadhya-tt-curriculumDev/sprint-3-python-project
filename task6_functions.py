# Task 6 — Functions

def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def summarize(scores):
    return {
        "avg": average(scores),
        "max": max(scores),
        "min": min(scores),
    }

print(summarize([88, 92, 75, 61, 99]))
