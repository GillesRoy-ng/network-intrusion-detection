#  Network Intrusion Detection System

## Notebook

Full analysis and training code available on Kaggle:  
[View Notebook](https://www.kaggle.com/code/gillesroy/network-intrusion-detection-system-1)

A machine learning system that detects network attacks in real-time using the CICIDS2017 dataset.

## Overview

This project builds a multiclass classifier to distinguish between benign traffic and 5 types of DoS attacks using network flow features extracted by CICFlowMeter.

## Dataset

- **Source**: CICIDS2017 (Canadian Institute for Cybersecurity)
- **File used**: Wednesday working hours (~692,000 flows)
- **Classes**: BENIGN, DoS Hulk, DoS GoldenEye, DoS Slowhttptest, DoS slowloris, Heartbleed

## Results

| Metric | Score |
|--------|-------|
| Accuracy | 100% |
| Macro F1-score | 1.00 |
| Model | Random Forest (100 trees) |

## Project Structure
├── app.py                  # Streamlit web application
├── notebook.ipynb          # Full training pipeline
└── README.md

> **Note**: The trained model files (.pkl) are not included due to file size.  
> To reproduce: run the notebook on Kaggle, download the .pkl files, and place them in the same folder as app.py.
