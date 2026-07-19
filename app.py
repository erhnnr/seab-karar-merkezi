import streamlit as st
import sympy as sp

# --- ARCHITECTURE CORE ---
class KnowledgeOS:
    @staticmethod
    def solve_math(expr):
        x = sp.symbols('x')
        solution = sp.solve(expr, x)
        # Farkındalık: Denklem tipini analiz et (Basit bir örnek)
        context = "Polinom denklemi" if "x" in str(expr) else "Cebirsel ifade"
        return solution, context

# --- INTERFACE ---
st.set_page_config(page_title="Knowledge OS", layout="wide")
st.title("🏗️ Knowledge OS: Intelligent Core")

module = st.sidebar.selectbox("Modül:", ["Analitik Matematik", "Dinamik Fizik"])

if module == "Analitik Matematik":
    st.subheader("Sembolik Çözücü")
    expr = st.text_input("Denklem:", "x**2 - 4")
    if st.button("Analiz Et"):
        sol, context = KnowledgeOS.solve_math(expr)
        st.info(f"Sistem Farkındalığı: Bu bir {context}.")
        st.latex(f"\\text{{Çözüm: }} {sp.latex(sol)}")
