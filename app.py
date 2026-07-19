import streamlit as st
import sympy as sp
import pandas as pd

# --- CORE ---
class KnowledgeOS:
    @staticmethod
    def analyze_health(symptom, duration):
        # Basit bir mantıksal çıkarım motoru
        risk_map = {
            "göğüs ağrısı": "ACİL (Kardiyoloji)",
            "nefes darlığı": "ACİL (Göğüs Hastalıkları)",
            "baş ağrısı": "Düşük/Orta (Nöroloji)",
            "yorgunluk": "Düşük (Dahiliye)"
        }
        
        discipline = risk_map.get(symptom.lower(), "Genel Tıp")
        
        # Aciliyet çıkarımı
        if "ACİL" in discipline or duration > 3:
            urgency = "⚠️ YÜKSEK ACİLİYET - En yakın sağlık kuruluşuna başvurun."
        else:
            urgency = "ℹ️ Rutin Kontrol - Bir uzmanla görüşmeniz önerilir."
            
        return discipline, urgency

# --- INTERFACE ---
st.set_page_config(layout="wide")
st.title("🏗️ Knowledge OS: Clinical Inference Engine")

module = st.sidebar.selectbox("Modül:", ["Analitik Matematik", "Gök Mekaniği", "Sağlık Analitiği"])

if module == "Sağlık Analitiği":
    st.subheader("🏥 Akıllı Belirti Analizcisi")
    symptom = st.text_input("Belirti (örn: göğüs ağrısı):")
    duration = st.number_input("Süre (Gün):", min_value=0, value=1)
    
    if st.button("Analiz Et"):
        disc, urg = KnowledgeOS.analyze_health(symptom, duration)
        st.success(f"Disiplin: {disc}")
        st.markdown(f"### {urg}")
        st.caption("Not: Bu analiz akademik çıkarım motoru ile yapılmıştır, teşhis değildir.")

# ... (Diğer modüllerin kalacak şekilde)
