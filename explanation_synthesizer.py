# explanation_synthesizer.py
class ExplanationSynthesizer:
    def __init__(self):
        pass
    def synthesize(self, model_output, rule_explanations):
        explanation = f"Model predicts: {model_output}. Rules suggest: {', '.join(rule_explanations)}"
        return explanation
