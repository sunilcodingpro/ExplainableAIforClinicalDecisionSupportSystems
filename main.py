# main.py
from utils.data_preprocessor import preprocess_data
from models.transformer_module import ClinicalTransformer
from models.rule_engine import RuleEngine
from models.explanation_synthesizer import ExplanationSynthesizer

if __name__ == "__main__":
    # Load and preprocess data
    df = preprocess_data('data/sample_patient_data.csv')
    print('Preprocessed data:', df.head())
    # Initialize model and rule engine
    model = ClinicalTransformer(input_dim=df.shape[1], model_dim=16, num_heads=2, num_layers=2)
    rules = [
        {'condition': lambda x: x['age']>50, 'explanation': 'High risk due to age'},
        {'condition': lambda x: x['symptom_1']=='Fever', 'explanation': 'Fever detected'}
    ]
    engine = RuleEngine(rules)
    synthesizer = ExplanationSynthesizer()
    # Example patient data
    patient_data = {'age':60, 'symptom_1':'Fever'}
    rule_explanations = engine.evaluate(patient_data)
    model_output = 'Positive'  # Placeholder for model prediction
    explanation = synthesizer.synthesize(model_output, rule_explanations)
    print('Explanation:', explanation)
