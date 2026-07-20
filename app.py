import streamlit as st
import sympy as sp

# --- EVRENSEL DETERMINISTIC ENGINE ---
class DeterministicEngine:
    @staticmethod
    def calculate(discipline, data):
        try:
            if discipline == "Matematik":
                return f"Sonuç: {sp.sympify(data)}"
            
            elif discipline == "Fizik (Basınç)":
                # P = F / A (Kuvvet / Alan)
                f, a = map(float, data.split(','))
                return f"Basınç: {f / a:.2f} Pascal"
            
            elif discipline == "Coğrafya (Koordinat Analizi)":
                # Basit bir koordinat mesafe/analiz öncülü
                lat, lon = map(float, data.split(','))
                return f"Konum: {lat}°N, {lon}°E bölgesindesiniz."
            
            elif discipline == "Astronomi":
                a = float(data)
                return f"Periyot: {a**1.5:.2f} Yıl (Kepler)"
                
            return "Hatalı veri girişi."
        except Exception as e:
            return f"Hata: {e} (Verileri doğru formatta girin)"

# --- ARAYÜZ ---
st.set_page_config(layout="wide")
st.title("⚖️ Universal Deterministic Engine")

discipline = st.sidebar.selectbox("Disiplin Seç:", 
    ["Matematik", "Fizik (Basınç)", "Coğrafya (Koordinat Analizi)", "Astronomi"])

# Dinamik Veri Girişi Talimatı
if discipline == "Fizik (Basınç)":
    input_text = st.text_input("Giriş (Kuvvet, Alan):", "100, 2")
elif discipline == "Coğrafya (Koordinat Analizi)":
    input_text = st.text_input("Giriş (Enlem, Boylam):", "36.88, 30.70")
else:
    input_text = st.text_input("Giriş Değeri:", "1.0")

if st.button("Analiz Et"):
    st.success(DeterministicEngine.calculate(discipline, input_text))
