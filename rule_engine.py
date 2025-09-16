# rule_engine.py
class RuleEngine:
    def __init__(self, rules):
        self.rules = rules
    def evaluate(self, patient_data):
        explanations = []
        for rule in self.rules:
            if rule['condition'](patient_data):
                explanations.append(rule['explanation'])
        return explanations
