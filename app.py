import streamlit as st
import sympy as sp
import pandas as pd

# --- CORE ---
class HealthEngine:
    @staticmethod
    def calculate_risk(symptom, severity, duration):
        base_risk = {"göğüs ağrısı": 8, "nefes darlığı": 9, "baş ağrısı": 3, "yorgunluk": 2}
        symptom_factor = base_risk.get(symptom.lower(), 5)
        risk_score = (symptom_factor + severity) * (1 + (duration * 0.1))
        return round(risk_score, 2)

# --- INTERFACE ---
st.set_page_config(layout="wide")
st.title("🏗️ Knowledge OS: Visual Inference Core")

if "risk_history" not in st.session_state: st.session_state.risk_history = []

module = st.sidebar.selectbox("Modül:", ["Analitik Matematik", "Gök Mekaniği", "Sağlık Analitiği"])

if module == "Sağlık Analitiği":
    st.subheader("🏥 Grafiksel Risk İzleme")
    symptom = st.text_input("Belirti:")
    severity = st.slider("Şiddet (1-10):", 1, 10, 5)
    duration = st.number_input("Süre (Gün):", 0, 365, 1)
    
    if st.button("Analiz Et ve Grafiğe Ekle"):
        score = HealthEngine.calculate_risk(symptom, severity, duration)
        st.session_state.risk_history.append({"Gün": len(st.session_state.risk_history)+1, "Risk Skoru": score})
        
        st.metric("Güncel Risk Skoru", score)
        
        # Grafik Görselleştirme
        df = pd.DataFrame(st.session_state.risk_history)
        st.line_chart(df.set_index("Gün"))

# ... (Diğer modüllerin kalacak şekilde)
