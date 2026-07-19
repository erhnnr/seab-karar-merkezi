import streamlit as st

# --- 1. DISIPLIN KUTUPHANELERI ---
class PhysicsEngine:
    @staticmethod
    def calculate_force(m, a): return m * a

class ChemEngine:
    @staticmethod
    def molar_mass(mol, gram): 
        if mol <= 0 or gram <= 0: return "Lütfen geçerli değerler girin." # Sıfır kontrolü
        return gram / mol

class MedicalEngine:
    @staticmethod
    def dosage_check(w, d): return w * d

class EconEngine:
    @staticmethod
    def roi(i, r): return ((r - i) / i) * 100 if i != 0 else 0

class BioEngine:
    @staticmethod
    def population_growth(n, r): return n * (1 + r)

class AstroEngine:
    @staticmethod
    def light_year_to_km(ly): return ly * 9.461e12

class GeoEngine:
    @staticmethod
    def scale_calc(md, s): return (md * s) / 100000

class MathEngine:
    @staticmethod
    def solve(expr):
        try: return eval(expr)
        except: return "Hata"

# --- 2. ORCHESTRATOR ---
def decision_orchestrator(domain, params):
    if domain == "Matematik": return MathEngine.solve(params['expr'])
    elif domain == "Fizik": return PhysicsEngine.calculate_force(params['m'], params['a'])
    elif domain == "Kimya": return ChemEngine.molar_mass(params['mol'], params['g'])
    elif domain == "Tıp": return MedicalEngine.dosage_check(params['w'], params['d'])
    elif domain == "Ekonomi": return EconEngine.roi(params['i'], params['r'])
    elif domain == "Biyoloji": return BioEngine.population_growth(params['n'], params['r'])
    elif domain == "Astronomi": return AstroEngine.light_year_to_km(params['ly'])
    elif domain == "Coğrafya": return GeoEngine.scale_calc(params['md'], params['s'])
    return "Hata"

# --- 3. ARAYUZ ---
st.title("🌐 Universal Decision Engine")
domain = st.selectbox("Alan Seçin", ["Matematik", "Fizik", "Kimya", "Tıp", "Ekonomi", "Biyoloji", "Astronomi", "Coğrafya"])

if domain == "Matematik":
    expr = st.text_input("Denklem:")
    if st.button("Çöz"): st.info(f"Sonuç: {decision_orchestrator('Matematik', {'expr':expr})}")
elif domain == "Fizik":
    m = st.number_input("Kütle (kg):")
    a = st.number_input("İvme (m/s²):")
    if st.button("Hesapla"): st.success(f"Kuvvet: {decision_orchestrator('Fizik', {'m':m, 'a':a})} N")
elif domain == "Kimya":
    mol = st.number_input("Mol Sayısı:")
    g = st.number_input("Gram:")
    if st.button("Hesapla"): st.warning(f"Mol Kütlesi: {decision_orchestrator('Kimya', {'mol':mol, 'g':g})} g/mol")
elif domain == "Tıp":
    w = st.number_input("Hasta Ağırlığı (kg):")
    d = st.number_input("Dozaj (mg/kg):")
    if st.button("Doz Hesapla"): st.error(f"Toplam Doz: {decision_orchestrator('Tıp', {'w':w, 'd':d})} mg")
elif domain == "Ekonomi":
    i = st.number_input("Yatırım:")
    r = st.number_input("Dönüş:")
    if st.button("Hesapla"): st.success(f"ROI: %{decision_orchestrator('Ekonomi', {'i':i, 'r':r}):.2f}")
elif domain == "Biyoloji":
    n = st.number_input("Popülasyon:")
    r = st.number_input("Artış Oranı:")
    if st.button("Hesapla"): st.success(f"Yeni Popülasyon: {decision_orchestrator('Biyoloji', {'n':n, 'r':r})}")
elif domain == "Astronomi":
    ly = st.number_input("Işık Yılı:")
    if st.button("Hesapla"): st.info(f"Mesafe: {decision_orchestrator('Astronomi', {'ly':ly})} km")
elif domain == "Coğrafya":
    md = st.number_input("Harita Mesafesi (cm):")
    s = st.number_input("Ölçek Paydası:")
    if st.button("Hesapla"): st.success(f"Gerçek Mesafe: {decision_orchestrator('Coğrafya', {'md':md, 's':s})} km")
