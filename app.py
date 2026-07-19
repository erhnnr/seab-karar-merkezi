import streamlit as st
import sympy as sp
import pandas as pd

# --- CORE ---
class KnowledgeOS:
    @staticmethod
    def solve_math(expr_str):
        x = sp.symbols('x')
        expr = sp.sympify(expr_str)
        degree = sp.Poly(expr, x).degree()
        context = "Doğrusal" if degree == 1 else "Parabolik" if degree == 2 else "Yüksek Dereceli"
        return sp.solve(expr, x), context

    @staticmethod
    def calculate_kepler_period(a_au):
        return a_au**(3/2)

# --- INTERFACE ---
st.set_page_config(page_title="Knowledge OS", layout="wide")
st.title("🏗️ Knowledge OS: Celestial & Math Core")

if "history" not in st.session_state: st.session_state.history = []

module = st.sidebar.selectbox("Modül Seçin:", ["Analitik Matematik", "Gök Mekaniği"])

if module == "Analitik Matematik":
    st.subheader("Sembolik Çözücü")
    expr = st.text_input("Denklem:", "x**2 - 4")
    if st.button("Analiz Et"):
        sol, ctx = KnowledgeOS.solve_math(expr)
        st.session_state.history.append({"Denklem": expr, "Analiz": ctx, "Çözüm": str(sol)})
        st.success(f"Analiz: {ctx}")
        st.latex(f"\\text{{Çözüm: }} {sp.latex(sol)}")

elif module == "Gök Mekaniği":
    st.subheader("🪐 Kepler Yörünge Hesaplayıcı")
    a = st.number_input("Yarı Büyük Eksen (AU):", value=1.0)
    if st.button("Periyot Hesapla"):
        t = KnowledgeOS.calculate_kepler_period(a)
        st.info(f"Bu yörüngedeki cismin periyodu: {t:.2f} Dünya yılı.")
        st.latex(f"T = {a}^{{1.5}} = {t:.2f}")

# Loglar
if st.session_state.history:
    st.divider()
    st.subheader("📚 Analiz Geçmişi")
    st.dataframe(pd.DataFrame(st.session_state.history))
