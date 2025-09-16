# ExplainableClinicalAI

**Explainable AI for Clinical Decision Support Systems: A Hybrid Transformer-Rule-Based Approach in Healthcare Diagnostics**

## Features

- Clinical BERT transformer model (can be swapped for MedBERT, etc.)
- Attention-guided, statistically validated, ontology-linked rule mining
- Visual explanations (attention heatmaps, feature importance)
- EHR connector for simulated patient data
- Clinician feedback interface (API)
- REST API (Flask) for inference, feedback, and EHR fetch

## Getting Started

1. Install Python 3.8+ and pip, plus [PyTorch](https://pytorch.org/get-started/locally/).
2. `pip install -r requirements.txt`
3. `python src/main.py`
4. Test with `python tests/test_api.py`

## API Usage

- `POST /predict` - inference with EHR data/clinical notes
- `GET /attention_heatmap` - fetch attention heatmap PNG
- `GET /fetch_ehr/<patient_id>` - simulated EHR data
- `POST /feedback` - add clinician feedback to rules

## Customization

- Add/replace transformer model (Bio_ClinicalBERT, MedBERT, etc.)
- Extend ontology mapping for clinical features
- Integrate real EHR connectors
- Add multimodal support for images (imaging analysis)

## License

Patent-pending. Academic/non-commercial use only.
