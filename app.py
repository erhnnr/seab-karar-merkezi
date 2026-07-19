import streamlit as st
import sympy as sp

# --- ARCHITECTURE CORE ---
class KnowledgeOS:
    @staticmethod
    def analyze_equation(expr_str):
        x = sp.symbols('x')
        expr = sp.sympify(expr_str)
        
        # Matematiksel Analiz
        poly = sp.Poly(expr, x)
        degree = poly.degree()
        
        # Yorumlama Motoru (Meta-Cognition)
        if degree == 1:
            context = "Bu bir doğrusal (linear) denklemdir. Sabit bir değişim hızını temsil eder."
        elif degree == 2:
            context = "Bu bir ikinci dereceden (parabolik) denklemdir. Bir ivme veya kavisli hareketi ifade eder."
        else:
            context = "Bu yüksek dereceli bir denklemdir. Karmaşık sistem davranışlarını modellemek için kullanılır."
            
        solutions = sp.solve(expr, x)
        return solutions, context

# --- INTERFACE ---
st.set_page_config(page_title="Knowledge OS", layout="wide")
st.title("🏗️ Knowledge OS: Meta-Cognitive Core")

module = st.sidebar.selectbox("Modül Seçin:", ["Analitik Matematik"])

if module == "Analitik Matematik":
    st.subheader("Akademik Yorumlayıcı")
    expr = st.text_input("Denklem girin:", "x**2 - 4")
    if st.button("Analiz Et ve Yorumla"):
        try:
            solutions, context = KnowledgeOS.analyze_equation(expr)
            st.success(f"Analiz: {context}")
            st.latex(f"\\text{{Çözüm: }} {sp.latex(solutions)}")
        except Exception as e:
            st.error("Lütfen geçerli bir denklem girin.")
