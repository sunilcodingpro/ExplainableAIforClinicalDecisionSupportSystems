# transformer_module.py
import torch
import torch.nn as nn

class ClinicalTransformer(nn.Module):
    def __init__(self, input_dim, model_dim, num_heads, num_layers):
        super(ClinicalTransformer, self).__init__()
        self.embedding = nn.Linear(input_dim, model_dim)
        encoder_layer = nn.TransformerEncoderLayer(d_model=model_dim, nhead=num_heads)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.fc = nn.Linear(model_dim, 1)
    def forward(self, x):
        x = self.embedding(x)
        x = self.transformer_encoder(x)
        x = self.fc(x.mean(dim=1))
        return torch.sigmoid(x)
