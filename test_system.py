# test_system.py
import unittest
from models.transformer_module import ClinicalTransformer
from models.rule_engine import RuleEngine
from models.explanation_synthesizer import ExplanationSynthesizer
class TestSystem(unittest.TestCase):
    def test_transformer(self):
        model = ClinicalTransformer(input_dim=10, model_dim=16, num_heads=2, num_layers=2)
        self.assertTrue(hasattr(model, 'forward'))
    def test_rule_engine(self):
        rules = [{'condition': lambda x: x['age']>50, 'explanation': 'Age above 50'}]
        engine = RuleEngine(rules)
        result = engine.evaluate({'age':60})
        self.assertIn('Age above 50', result)
    def test_explanation_synthesizer(self):
        synthesizer = ExplanationSynthesizer()
        explanation = synthesizer.synthesize('Positive', ['Rule1'])
        self.assertIn('Model predicts: Positive', explanation)
if __name__ == "__main__":
    unittest.main()