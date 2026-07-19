import streamlit as st

# --- 1. DISIPLIN KUTUPHANELERI ---
class BioEngine:
    @staticmethod
    def population_growth(n, r): return n * (1 + r) # Basit popülasyon artışı

class AstroEngine:
    @staticmethod
    def light_year_to_km(ly): return ly * 9.461e12 # Işık yılı -> km

class GeoEngine:
    @staticmethod
    def scale_calc(map_dist, scale): return map_dist * scale # Harita mesafesi hesaplama

# ... (Daha önce eklediğimiz Physics, Chem, Medical, Econ, Math Engine sınıfları burada kalmaya devam edecek) ...

# --- 2. ORCHESTRATOR (Guncellenmis) ---
def decision_orchestrator(domain, params):
    # Yeni eklenenler
    if domain == "Biyoloji": return BioEngine.population_growth(params['n'], params['r'])
    elif domain == "Astronomi": return AstroEngine.light_year_to_km(params['ly'])
    elif domain == "Coğrafya": return GeoEngine.scale_calc(params['md'], params['s'])
    # Mevcutlar
    elif domain == "Fizik": return PhysicsEngine.calculate_force(params['m'], params['a'])
    elif domain == "Kimya": return ChemEngine.molar_mass(params['mol'], params['g'])
    elif domain == "Tıp": return MedicalEngine.dosage_check(params['w'], params['d'])
    elif domain == "Ekonomi": return EconEngine.roi(params['i'], params['r'])
    elif domain == "Matematik": return MathEngine.solve(params['expr'])
    return "Bilinmeyen Disiplin"

# --- 3. ARAYUZ ---
st.title("🌐 Universal Decision Engine")
domain = st.selectbox("Alan Seçin", ["Matematik", "Fizik", "Kimya", "Tıp", "Ekonomi", "Biyoloji", "Astronomi", "Coğrafya"])

# ... (Her alan için ilgili inputlar eklenir) ...

elif domain == "Biyoloji":
    n = st.number_input("Başlangıç Popülasyonu:")
    r = st.number_input("Artış Oranı (örn: 0.1):")
    if st.button("Hesapla"): st.success(f"Yeni Popülasyon: {decision_orchestrator('Biyoloji', {'n':n, 'r':r})}")

elif domain == "Astronomi":
    ly = st.number_input("Işık Yılı:")
    if st.button("Hesapla"): st.info(f"Mesafe (km): {decision_orchestrator('Astronomi', {'ly':ly})}")

elif domain == "Coğrafya":
    md = st.number_input("Harita Mesafesi (cm):")
    s = st.number_input("Ölçek Paydası (örn: 100000):")
    if st.button("Hesapla"): st.success(f"Gerçek Mesafe (km): {decision_orchestrator('Coğrafya', {'md':md, 's':s})/100000}")
