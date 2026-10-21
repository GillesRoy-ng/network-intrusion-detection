import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model, scaler, label encoder
rf = joblib.load('random_forest_nids.pkl')
scaler = joblib.load('scaler.pkl')
le = joblib.load('label_encoder.pkl')

feature_names = ['Destination Port', 'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets', 'Total Length of Fwd Packets', 'Total Length of Bwd Packets', 'Fwd Packet Length Max', 'Fwd Packet Length Min', 'Fwd Packet Length Mean', 'Fwd Packet Length Std', 'Bwd Packet Length Max', 'Bwd Packet Length Min', 'Bwd Packet Length Mean', 'Bwd Packet Length Std', 'Flow Bytes/s', 'Flow Packets/s', 'Flow IAT Mean', 'Flow IAT Std', 'Flow IAT Max', 'Flow IAT Min', 'Fwd IAT Total', 'Fwd IAT Mean', 'Fwd IAT Std', 'Fwd IAT Max', 'Fwd IAT Min', 'Bwd IAT Total', 'Bwd IAT Mean', 'Bwd IAT Std', 'Bwd IAT Max', 'Bwd IAT Min', 'Fwd PSH Flags', 'Fwd Header Length', 'Bwd Header Length', 'Fwd Packets/s', 'Bwd Packets/s', 'Min Packet Length', 'Max Packet Length', 'Packet Length Mean', 'Packet Length Std', 'Packet Length Variance', 'FIN Flag Count', 'SYN Flag Count', 'RST Flag Count', 'PSH Flag Count', 'ACK Flag Count', 'URG Flag Count', 'ECE Flag Count', 'Down/Up Ratio', 'Average Packet Size', 'Avg Fwd Segment Size', 'Avg Bwd Segment Size', 'Fwd Header Length.1', 'Subflow Fwd Packets', 'Subflow Fwd Bytes', 'Subflow Bwd Packets', 'Subflow Bwd Bytes', 'Init_Win_bytes_forward', 'Init_Win_bytes_backward', 'act_data_pkt_fwd', 'min_seg_size_forward', 'Active Mean', 'Active Std', 'Active Max', 'Active Min', 'Idle Mean', 'Idle Std', 'Idle Max', 'Idle Min']

st.title('🔒 Network Intrusion Detection System')
st.write('Upload a CSV file of network flows to detect attacks.')

uploaded_file = st.file_uploader('Upload CSV', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()

    st.subheader('Raw Data Preview')
    st.dataframe(df.head())

    try:
        X = df[feature_names]
        X_scaled = scaler.transform(X)
        predictions = rf.predict(X_scaled)
        labels = le.inverse_transform(predictions)

        df['Prediction'] = labels

        st.subheader('Predictions')
        st.dataframe(df[['Prediction']].join(df.drop(columns='Prediction')).head(50))

        st.subheader('Summary')
        st.bar_chart(df['Prediction'].value_counts())

    except Exception as e:
        st.error(f'Error: {e}')