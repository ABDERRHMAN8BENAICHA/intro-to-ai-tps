
rules = [
    {"if": ["A", "B"], "then": "C"},
    {"if": ["P"], "then": "C"},
    {"if": ["C", "L","D"], "then": "T"},
]

facts = [
    "P",
    "L",
    "D",
]


def infer(rules, facts):
    conclusions = set()

    for rule in rules:
        if all(condition in facts for condition in rule["if"]):
            conclusions.add(rule["then"])
            facts.append(rule["then"])
    return conclusions

new_conclusions = infer(rules, facts)
print("the result is : ", new_conclusions)