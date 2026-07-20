import streamlit as st
import sympy as sp
import pandas as pd

# --- CORE ENGINE ---
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
        symptom_factor = base_risk.get(symptom.lower(), 5)
        return round((symptom_factor + severity) * (1 + (duration * 0.1)), 2)

# --- INTERFACE ---
st.set_page_config(page_title="Knowledge OS", layout="wide")
st.title("🏗️ Knowledge OS: Unified Core")

if "risk_history" not in st.session_state: st.session_state.risk_history = []

module = st.sidebar.selectbox("Modül Seçin:", ["Analitik Matematik", "Gök Mekaniği", "Sağlık Analitiği"])

if module == "Analitik Matematik":
    expr = st.text_input("Denklem (örn: x**2 - 4):")
    if st.button("Analiz Et"):
        sol, ctx = KnowledgeOS.solve_math(expr)
        st.success(f"Analiz: {ctx}")
        st.latex(f"\\text{{Çözüm: }} {sp.latex(sol)}")

elif module == "Gök Mekaniği":
    a = st.number_input("Yarı Büyük Eksen (AU):", value=1.0)
    if st.button("Periyot Hesapla"):
        st.info(f"Periyot: {KnowledgeOS.calculate_kepler(a):.2f} Yıl")

elif module == "Sağlık Analitiği":
    symptom = st.text_input("Belirti:")
    severity = st.slider("Şiddet (1-10):", 1, 10, 5)
    duration = st.number_input("Süre (Gün):", 0, 365, 1)
    if st.button("Risk Analizi Yap"):
        score = HealthEngine.calculate_risk(symptom, severity, duration)
        st.session_state.risk_history.append({"Gün": len(st.session_state.risk_history)+1, "Risk Skoru": score})
        st.metric("Güncel Risk Skoru", score)
        if st.session_state.risk_history:
            st.line_chart(pd.DataFrame(st.session_state.risk_history).set_index("Gün"))
