import streamlit as st
import sympy as sp
import pandas as pd
import os

# --- CORE LOGGING ---
if not os.path.exists("logs"): 
    os.makedirs("logs")

def log_data(module, data_dict):
    df = pd.DataFrame([data_dict])
    path = f"logs/{module}_history.csv"
    df.to_csv(path, mode='a', header=not os.path.exists(path), index=False)

# --- ENGINES ---
class KnowledgeOS:
    @staticmethod
    def solve_math(expr_str):
        x = sp.symbols('x')
        expr = sp.sympify(expr_str)
        degree = sp.Poly(expr, x).degree()
        ctx = "Doğrusal" if degree == 1 else "Parabolik" if degree == 2 else "Yüksek Dereceli"
        return sp.solve(expr, x), ctx

    @staticmethod
    def calculate_kepler(a_au):
        return a_au**(3/2)

class HealthEngine:
    @staticmethod
    def calculate_risk(symptom, severity, duration):
        base_risk = {"göğüs ağrısı": 8, "nefes darlığı": 9, "baş ağrısı": 3, "yorgunluk": 2}
        score = (base_risk.get(symptom.lower(), 5) + severity) * (1 + (duration * 0.1))
        return round(score, 2)

# --- INTERFACE ---
st.set_page_config(page_title="Knowledge OS", layout="wide")
st.title("🏗️ Knowledge OS: Stabilized Core")

module = st.sidebar.selectbox("Modül Seçiniz:", ["Analitik Matematik", "Gök Mekaniği", "Sağlık Analitiği"])

if module == "Analitik Matematik":
    st.subheader("Sembolik Çözücü")
    expr = st.text_input("Denklem (örn: x**2 - 4):")
    if st.button("Analiz Et"):
        sol, ctx = KnowledgeOS.solve_math(expr)
        log_data("Math", {"Denklem": expr, "Analiz": ctx, "Çözüm": str(sol)})
        st.success(f"Analiz: {ctx}")
        st.latex(f"\\text{{Çözüm: }} {sp.latex(sol)}")

elif module == "Gök Mekaniği":
    st.subheader("🪐 Kepler Yörünge Hesaplayıcı")
    a = st.number_input("Yarı Büyük Eksen (AU):", value=1.0)
    if st.button("Periyot Hesapla"):
        t = KnowledgeOS.calculate_kepler(a)
        log_data("Astronomy", {"Eksen": a, "Periyot": t})
        st.info(f"Periyot: {t:.2f} Yıl")

elif module == "Sağlık Analitiği":
    st.subheader("🏥 Parametrik Sağlık Analizi")
    symp = st.text_input("Belirti:")
    sev = st.slider("Şiddet (1-10):", 1, 10, 5)
    dur = st.number_input("Süre (Gün):", 0, 365, 1)
    if st.button("Analiz Et"):
        score = HealthEngine.calculate_risk(symp, sev, dur)
        log_data("Health", {"Semptom": symp, "Risk": score})
        st.metric("Güncel Risk Skoru", score)
