import streamlit as st
import sympy as sp
import pandas as pd

# --- CORE ---
class HealthEngine:
    @staticmethod
    def calculate_risk(symptom, severity, duration):
        # Parametrik risk hesaplama
        base_risk = {"göğüs ağrısı": 8, "nefes darlığı": 9, "baş ağrısı": 3, "yorgunluk": 2}
        
        symptom_factor = base_risk.get(symptom.lower(), 5)
        # Risk Skoru Formülü: RS = (Semptom Ağırlığı + Şiddet) * Süre Çarpanı
        risk_score = (symptom_factor + severity) * (1 + (duration * 0.1))
        
        if risk_score > 15:
            verdict = "🔴 YÜKSEK RİSK: Uzman Müdahalesi Gerekli."
        elif risk_score > 8:
            verdict = "🟡 ORTA RİSK: Tetkik Edilmesi Önerilir."
        else:
            verdict = "🟢 DÜŞÜK RİSK: İzlemeye Alınabilir."
            
        return round(risk_score, 2), verdict

# --- INTERFACE ---
st.set_page_config(layout="wide")
st.title("🏗️ Knowledge OS: Advanced Inference Engine")

module = st.sidebar.selectbox("Modül:", ["Analitik Matematik", "Gök Mekaniği", "Sağlık Analitiği"])

if module == "Sağlık Analitiği":
    st.subheader("🏥 Parametrik Sağlık Analizi")
    symptom = st.text_input("Belirti:")
    severity = st.slider("Şiddet (1-10):", 1, 10, 5)
    duration = st.number_input("Süre (Gün):", 0, 365, 1)
    
    if st.button("Risk Analizi Yap"):
        score, verdict = HealthEngine.calculate_risk(symptom, severity, duration)
        st.metric("Hesaplanan Risk Skoru", score)
        st.subheader(verdict)
        st.caption("Not: Bu bir akademik modeldir, teşhis değildir.")
