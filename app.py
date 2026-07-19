
import streamlit as st

# --- 1. DISIPLIN KUTUPHANELERI ---
class PhysicsEngine:
    @staticmethod
    def calculate_force(mass, acceleration):
        return mass * acceleration  # F = m*a

class MathEngine:
    @staticmethod
    def solve_complex(expression):
        return eval(expression)

# --- 2. ORCHESTRATOR (Yönetici) ---
def decision_orchestrator(domain, action, params):
    if domain == "Fizik":
        return PhysicsEngine.calculate_force(params['m'], params['a'])
    elif domain == "Matematik":
        return MathEngine.solve_complex(params['expr'])
    return "Bilinmeyen Disiplin"

# --- 3. ARAYUZ ---
st.title("🌐 Universal Decision Engine")
domain = st.selectbox("Alan Seçin", ["Fizik", "Matematik"])

if domain == "Fizik":
    m = st.number_input("Kütle (kg):")
    a = st.number_input("İvme (m/s²):")
    if st.button("Analiz Et"):
        st.write(f"Sonuç (Kuvvet): {decision_orchestrator('Fizik', None, {'m':m, 'a':a})} Newton")

elif domain == "Matematik":
    expr = st.text_input("Denklem:")
    if st.button("Çöz"):
        st.write(f"Sonuç: {decision_orchestrator('Matematik', None, {'expr':expr})}")
