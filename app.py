import streamlit as st
import sympy as sp
import pandas as pd

# --- CORE ---
class KnowledgeOS:
    @staticmethod
    def analyze_equation(expr_str):
        x = sp.symbols('x')
        expr = sp.sympify(expr_str)
        degree = sp.Poly(expr, x).degree()
        context = "Doğrusal" if degree == 1 else "Parabolik" if degree == 2 else "Yüksek Dereceli"
        return sp.solve(expr, x), context

# --- INTERFACE ---
st.set_page_config(layout="wide")
st.title("🏗️ Knowledge OS: Data Core")

if "history" not in st.session_state: st.session_state.history = []

expr = st.text_input("Denklem:", "x**2 - 4")
if st.button("Analiz Et"):
    sol, ctx = KnowledgeOS.analyze_equation(expr)
    st.session_state.history.append({"Denklem": expr, "Analiz": ctx, "Çözüm": str(sol)})
    
    st.success(f"Analiz: {ctx}")
    st.latex(f"\\text{{Çözüm: }} {sp.latex(sol)}")

# Tablolu Raporlama
if st.session_state.history:
    st.divider()
    st.subheader("📊 Akademik Rapor Tablosu")
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df, use_container_width=True)
    
    # CSV Olarak İndirme
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Raporu CSV Olarak İndir", csv, "analiz_raporu.csv", "text/csv")
