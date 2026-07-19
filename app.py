import streamlit as st
import sympy as sp

# --- CORE ---
class KnowledgeOS:
    @staticmethod
    def analyze_equation(expr_str):
        x = sp.symbols('x')
        expr = sp.sympify(expr_str)
        poly = sp.Poly(expr, x)
        degree = poly.degree()
        
        context = "Doğrusal (linear)" if degree == 1 else "İkinci dereceden (parabolik)" if degree == 2 else "Yüksek dereceli"
        solutions = sp.solve(expr, x)
        return solutions, context

# --- INTERFACE ---
st.set_page_config(page_title="Knowledge OS", layout="wide")
st.title("🏗️ Knowledge OS: Memory Core")

if "history" not in st.session_state: st.session_state.history = []

expr = st.text_input("Denklem:", "x**2 - 4")
if st.button("Analiz Et"):
    solutions, context = KnowledgeOS.analyze_equation(expr)
    log_entry = f"Denklem: {expr} | Analiz: {context} | Çözüm: {solutions}"
    st.session_state.history.append(log_entry)
    
    st.success(f"Analiz: {context}")
    st.latex(f"\\text{{Çözüm: }} {sp.latex(solutions)}")

# Analiz Geçmişi (Log Defteri)
st.divider()
st.subheader("📚 Analiz Geçmişi")
for item in st.session_state.history:
    st.write(f"- {item}")
