import streamlit as st
import sympy as sp
import numpy as np

# --- 1. CORE ENGINE (Sistem Çekirdeği) ---
class KnowledgeOS:
    @staticmethod
    def solve_symbolic(expression):
        x = sp.symbols('x')
        return sp.solve(expression, x)

    @staticmethod
    def calculate_force(m, a):
        return m * a

# --- 2. MODÜLER YÖNETİCİ ---
def render_sidebar():
    st.sidebar.title("🏗️ Knowledge OS")
    return st.sidebar.selectbox("Modül Seçin:", ["Analitik Matematik", "Klasik Mekanik", "Tıp (Tasarım Aşamasında)"])

# --- 3. ARAYÜZ (INTERFACE) ---
def main():
    st.set_page_config(page_title="Knowledge OS", layout="wide")
    module = render_sidebar()

    if module == "Analitik Matematik":
        st.header("🔢 Sembolik Matematik Motoru")
        expr = st.text_input("Denklem girin (örn: x**2 - 9):")
        if st.button("Çözümle"):
            result = KnowledgeOS.solve_symbolic(expr)
            st.latex(f"\\text{{Çözüm kümesi: }} {sp.latex(result)}")

    elif module == "Klasik Mekanik":
        st.header("⚛️ Fiziksel Dinamikler")
        col1, col2 = st.columns(2)
        m = col1.number_input("Kütle (kg):", value=1.0)
        a = col2.number_input("İvme (m/s²):", value=9.81)
        if st.button("Kuvvet Hesapla"):
            f = KnowledgeOS.calculate_force(m, a)
            st.metric("Hesaplanan Kuvvet", f"{f} N")

if __name__ == "__main__":
    main()
