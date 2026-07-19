import streamlit as st
import sympy as sp

# --- ARCHITECTURE CORE ---
def run_math_module():
    st.subheader("🔢 Sembolik Matematik Motoru")
    expr = st.text_input("Denklem:", "x**2 - 4")
    if st.button("Çöz"):
        try:
            x = sp.symbols('x')
            sol = sp.solve(expr, x)
            st.latex(f"S = {sp.latex(sol)}")
        except: st.error("Denklem formatını kontrol edin.")

def run_physics_module():
    st.subheader("⚛️ Fiziksel Dinamikler")
    # Sabitler modülü (Faz 1.2 için hazırlık)
    g = 9.81 
    m = st.number_input("Kütle (kg):", value=1.0)
    if st.button("Ağırlık Hesapla (G=m*g)"):
        st.write(f"### Ağırlık: ${m*g:.2f} \, \text{N}$")

# --- MAIN ENGINE (SYSTEM ARCHITECT) ---
st.set_page_config(page_title="Knowledge OS", layout="wide")
st.title("🏗️ Knowledge OS: Core Architecture")

# Sistem Mimarisi: Modül Seçici
module = st.sidebar.selectbox("Modül Seçiniz:", ["Matematik", "Fizik", "Tıp (Geliştiriliyor)"])

if module == "Matematik":
    run_math_module()
elif module == "Fizik":
    run_physics_module()
else:
    st.info("Bu modül Faz 2 kapsamında inşa ediliyor.")
