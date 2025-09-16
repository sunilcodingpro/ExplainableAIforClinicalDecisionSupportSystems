# visualization.py
import matplotlib.pyplot as plt

def plot_patient_distribution(df):
    diagnosis_counts = df['diagnosis'].value_counts()
    diagnosis_counts.plot(kind='bar')
    plt.xlabel('Diagnosis')
    plt.ylabel('Count')
    plt.title('Patient Diagnosis Distribution')
    plt.show()