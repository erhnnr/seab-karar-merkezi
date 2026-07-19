import streamlit as st

# --- 1. DISIPLIN KUTUPHANELERI ---
class PhysicsEngine:
    @staticmethod
    def calculate_force(m, a): return m * a

class ChemEngine:
    @staticmethod
    def molar_mass(mol, gram): return gram / mol if mol != 0 else "Hata: Mol 0 olamaz"

class MedicalEngine:
    @staticmethod
    def dosage_check(weight, dosage_per_kg): return weight * dosage_per_kg

class EconEngine:
    @staticmethod
    def roi(investment, return_val): return ((return_val - investment) / investment) * 100

class MathEngine:
    @staticmethod
    def solve(expr):
        try: return eval(expr)
        except: return "Hata: Geçersiz ifade"

# --- 2. ORCHESTRATOR ---
def decision_orchestrator(domain, params):
    if domain == "Fizik": return PhysicsEngine.calculate_force(params['m'], params['a'])
    elif domain == "Kimya": return ChemEngine.molar_mass(params['mol'], params['g'])
    elif domain == "Tıp": return MedicalEngine.dosage_check(params['w'], params['d'])
    elif domain == "Ekonomi": return EconEngine.roi(params['i'], params['r'])
    elif domain == "Matematik": return MathEngine.solve(params['expr'])
    return "Bilinmeyen Disiplin"

# --- 3. ARAYUZ ---
st.title("🌐 Universal Decision Engine")
domain = st.selectbox("Alan Seçin", ["Matematik", "Fizik", "Kimya", "Tıp", "Ekonomi"])

if domain == "Matematik":
    expr = st.text_input("Denklem:")
    if st.button("Çöz"): st.info(f"Sonuç: {decision_orchestrator('Matematik', {'expr':expr})}")

elif domain == "Fizik":
    m = st.number_input("Kütle (kg):")
    a = st.number_input("İvme (m/s²):")
    if st.button("Hesapla"): st.success(f"Kuvvet: {decision_orchestrator('Fizik', {'m':m, 'a':a})} Newton")

elif domain == "Kimya":
    mol = st.number_input("Mol Sayısı:")
    g = st.number_input("Gram:")
    if st.button("Hesapla"): st.warning(f"Moleküler Ağırlık: {decision_orchestrator('Kimya', {'mol':mol, 'g':g})} g/mol")

elif domain == "Tıp":
    w = st.number_input("Hasta Ağırlığı (kg):")
    d = st.number_input("Dozaj (mg/kg):")
    if st.button("Doz Hesapla"): st.error(f"Toplam Doz: {decision_orchestrator('Tıp', {'w':w, 'd':d})} mg")

elif domain == "Ekonomi":
    i = st.number_input("Yatırım Miktarı:")
    r = st.number_input("Dönüş Miktarı:")
    if st.button("ROI Hesapla"): st.success(f"ROI (Getiri Oranı): %{decision_orchestrator('Ekonomi', {'i':i, 'r':r}):.2f}")
