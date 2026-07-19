import streamlit as st

# --- 1. DISIPLIN KUTUPHANELERI ---
class PhysicsEngine:
    @staticmethod
    def calculate_force(m, a): return m * a
    @staticmethod
    def calculate_velocity(d, t): return d / t if t != 0 else "Hata: Zaman 0 olamaz"

class ChemEngine:
    @staticmethod
    def molar_mass(mol, gram): return gram / mol if mol != 0 else "Hata: Mol 0 olamaz"

class MathEngine:
    @staticmethod
    def solve(expr):
        try: return eval(expr)
        except: return "Hata: Geçersiz ifade"

# --- 2. ORCHESTRATOR ---
def decision_orchestrator(domain, params):
    if domain == "Fizik":
        if params['type'] == 'Kuvvet': return PhysicsEngine.calculate_force(params['m'], params['a'])
        return PhysicsEngine.calculate_velocity(params['d'], params['t'])
    elif domain == "Kimya":
        return ChemEngine.molar_mass(params['mol'], params['g'])
    elif domain == "Matematik":
        return MathEngine.solve(params['expr'])
    return "Bilinmeyen Disiplin"

# --- 3. ARAYUZ ---
st.title("🌐 Universal Decision Engine")
domain = st.selectbox("Alan Seçin", ["Matematik", "Fizik", "Kimya"])

if domain == "Matematik":
    expr = st.text_input("İfade:")
    if st.button("Çöz"): st.info(f"Sonuç: {decision_orchestrator('Matematik', {'expr':expr})}")

elif domain == "Fizik":
    sub = st.radio("İşlem:", ["Kuvvet", "Hız"])
    if sub == "Kuvvet":
        m = st.number_input("Kütle:")
        a = st.number_input("İvme:")
        if st.button("Hesapla"): st.success(f"Kuvvet: {decision_orchestrator('Fizik', {'type':'Kuvvet', 'm':m, 'a':a})}")
    else:
        d = st.number_input("Mesafe:")
        t = st.number_input("Zaman:")
        if st.button("Hesapla"): st.success(f"Hız: {decision_orchestrator('Fizik', {'type':'Hız', 'd':d, 't':t})}")

elif domain == "Kimya":
    mol = st.number_input("Mol Sayısı:")
    g = st.number_input("Gram:")
    if st.button("Hesapla"): st.warning(f"Moleküler Ağırlık: {decision_orchestrator('Kimya', {'mol':mol, 'g':g})} g/mol")
