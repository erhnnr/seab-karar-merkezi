import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. DISIPLIN KUTUPHANELERI (Geliştirilmiş Kontrollerle) ---
class PhysicsEngine:
    @staticmethod
    def calculate_force(m, a): return m * a

class ChemEngine:
    @staticmethod
    def molar_mass(mol, gram): 
        if mol <= 0 or gram <= 0: return "Hata: Değerler 0'dan büyük olmalı."
        return gram / mol

class MedicalEngine:
    @staticmethod
    def dosage_check(w, d): 
        if w <= 0 or d <= 0: return "Hata: Değerler 0'dan büyük olmalı."
        return w * d

class EconEngine:
    @staticmethod
    def roi(i, r): 
        if i <= 0: return "Hata: Yatırım 0 veya daha az olamaz."
        return ((r - i) / i) * 100

class BioEngine:
    @staticmethod
    def population_growth(n, r): 
        if n < 0: return "Hata: Başlangıç popülasyonu negatif olamaz."
        return n * (1 + r)

class AstroEngine:
    @staticmethod
    def light_year_to_km(ly): 
        if ly < 0: return "Hata: Mesafe negatif olamaz."
        return ly * 9.461e12

class GeoEngine:
    @staticmethod
    def scale_calc(md, s): 
        if md <= 0 or s <= 0: return "Hata: Değerler 0'dan büyük olmalı."
        return (md * s) / 100000

class MathEngine:
    @staticmethod
    def solve(expr):
        try: 
            if not expr: return "Lütfen bir denklem girin."
            return eval(expr)
        except ZeroDivisionError: return "Hata: Sıfıra bölme hatası."
        except: return "Hata: Geçersiz ifade."

# --- 2. HAFIZA BAŞLATMA ---
if "audit_log" not in st.session_state:
    st.session_state.audit_log = []

# --- 3. ORCHESTRATOR & LOG KAYITÇI ---
def log_and_solve(domain, operation_name, params, result_func, *args):
    result = result_func(*args)
    
    # Hata kontrolü ve loglama
    status = "BLOCK/HATA" if str(result).startswith("Hata") else "PASS/BAŞARILI"
    
    log_entry = {
        "Zaman": datetime.now().strftime("%H:%M:%S"),
        "Disiplin": domain,
        "İşlem/Parametreler": f"{operation_name} -> {params}",
        "Durum": status,
        "Sonuç": str(result)
    }
    st.session_state.audit_log.append(log_entry)
    return result

# --- 4. ARAYÜZ (Geliştirilmiş Yan Panel Tasarımı) ---
st.set_page_config(page_title="Universal Decision Engine", layout="wide")
st.title("🌐 Universal Decision Engine")

# Sekmeli Yapı
tab_analiz, tab_log = st.tabs(["🔬 Disiplinlerarası Analiz", "📜 Denetim Kayıtları (Audit Log)"])

with tab_analiz:
    domain = st.selectbox("Alan Seçin", ["Matematik", "Fizik", "Kimya", "Tıp", "Ekonomi", "Biyoloji", "Astronomi", "Coğrafya"])
    st.write("---")

    if domain == "Matematik":
        expr = st.text_input("Denklem (örn: 25 * 4 / 2):")
        if st.button("Çöz"): 
            res = log_and_solve("Matematik", "Denklem Çözümü", f"İfade: {expr}", MathEngine.solve, expr)
            st.info(f"Sonuç: {res}")

    elif domain == "Fizik":
        m = st.number_input("Kütle (kg):", value=0.0)
        a = st.number_input("İvme (m/s²):", value=0.0)
        if st.button("Hesapla"): 
            res = log_and_solve("Fizik", "Kuvvet Hesabı", f"m:{m}, a:{a}", PhysicsEngine.calculate_force, m, a)
            st.success(f"Kuvvet: {res} N")

    elif domain == "Kimya":
        mol = st.number_input("Mol Sayısı:", value=0.0)
        g = st.number_input("Gram:", value=0.0)
        if st.button("Hesapla"): 
            res = log_and_solve("Kimya", "Mol Kütlesi Hesabı", f"mol:{mol}, g:{g}", ChemEngine.molar_mass, mol, g)
            st.warning(f"Sonuç: {res} {'' if str(res).startswith('Hata') else 'g/mol'}")

    elif domain == "Tıp":
        w = st.number_input("Hasta Ağırlığı (kg):", value=0.0)
        d = st.number_input("Dozaj (mg/kg):", value=0.0)
        if st.button("Doz Hesapla"): 
            res = log_and_solve("Tıp", "Toplam Doz Hesabı", f"w:{w}, d:{d}", MedicalEngine.dosage_check, w, d)
            st.error(f"Sonuç: {res} {'' if str(res).startswith('Hata') else 'mg'}")

    elif domain == "Ekonomi":
        i = st.number_input("Yatırım Miktarı:", value=0.0)
        r = st.number_input("Dönüş Miktarı:", value=0.0)
        if st.button("Hesapla"): 
            res = log_and_solve("Ekonomi", "ROI Analizi", f"i:{i}, r:{r}", EconEngine.roi, i, r)
            st.success(f"Sonuç: {'' if str(res).startswith('Hata') else '%'}{res}")

    elif domain == "Biyoloji":
        n = st.number_input("Mevcut Popülasyon:", value=0.0)
        r = st.number_input("Artış Oranı (örn: 0.05):", value=0.0)
        if st.button("Hesapla"): 
            res = log_and_solve("Biyoloji", "Popülasyon Artışı", f"n:{n}, r:{r}", BioEngine.population_growth, n, r)
            st.success(f"Yeni Popülasyon: {res}")

    elif domain == "Astronomi":
        ly = st.number_input("Işık Yılı:", value=0.0)
        if st.button("Hesapla"): 
            res = log_and_solve("Astronomi", "Işık Yılı -> Km", f"ly:{ly}", AstroEngine.light_year_to_km, ly)
            st.info(f"Mesafe: {res} km")

    elif domain == "Coğrafya":
        md = st.number_input("Harita Mesafesi (cm):", value=0.0)
        s = st.number_input("Ölçek Paydası (örn: 100000):", value=0.0)
        if st.button("Hesapla"): 
            res = log_and_solve("Coğrafya", "Gerçek Mesafe Haritalama", f"md:{md}, s:{s}", GeoEngine.scale_calc, md, s)
            st.success(f"Gerçek Mesafe: {res} km")

with tab_log:
    st.subheader("Sistem İşlem Geçmişi")
    if st.session_state.audit_log:
        df = pd.DataFrame(st.session_state.audit_log)
        st.dataframe(df, use_container_width=True)
        
        # CSV İndirme Butonu
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📊 Raporu CSV Olarak İndir",
            data=csv,
            file_name=f"universal_engine_log_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
        )
    else:
        st.info("Henüz bir işlem yapılmadı. Yapılan hesaplamalar burada listelenecektir.")
