import streamlit as st
import pandas as pd
import datetime

# --- MANTIK KATMANI (Engine) ---
class DecisionEngine:
    def __init__(self):
        self.name = "Universal Core V1"

    def analyze(self, data):
        # BURASI senin algoritmalarının olacağı yer.
        # İlk prototip: Gelen veriyi basitçe analiz edip "Karar" üreten bir yapı.
        if "risk" in data.lower():
            return "Yüksek Risk: Yatırımı durdur."
        else:
            return "Kararlı: Veri normal aralıkta."

# --- ARAYÜZ KATMANI (UI) ---
engine = DecisionEngine()

st.set_page_config(page_title="Karar Motoru", layout="centered")
st.title("🧠 Universal Decision Engine")

st.sidebar.header("Motor Ayarları")
st.info(f"Sistem: {engine.name}")

user_input = st.text_input("Analiz edilecek veriyi veya durumu girin:")

if st.button("Karar Üret"):
    if user_input:
        karar = engine.analyze(user_input)
        st.subheader("Karar:")
        st.success(karar)
        
        # Loglama: Kararı hafızaya al
        st.session_state.log = {"Zaman": datetime.datetime.now(), "Girdi": user_input, "Karar": karar}
    else:
        st.warning("Lütfen bir veri girişi yapın.")
