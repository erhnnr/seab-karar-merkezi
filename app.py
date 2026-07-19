import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. DISIPLIN KUTUPHANELERI VE VALIDATOR'LAR ---
class Validator:
    @staticmethod
    def check(domain, value):
        # Örnek Limitler: Burayı istediğin gibi özelleştirebilirsin
        limits = {
            "Tıp": {"min": 0.1, "max": 500}, 
            "Ekonomi": {"min": 0, "max": 1000000},
            "Fizik": {"max": 10000} # Kuvvet limiti
        }
        if domain in limits:
            if value < limits[domain]["min"] or value > limits[domain]["max"]:
                return "BLOCK (Limit Aşıldı!)"
        return "PASS (Güvenli)"

class PhysicsEngine:
    @staticmethod
    def calculate_force(m, a): return m * a

class ChemEngine:
    @staticmethod
    def molar_mass(mol, gram): return gram / mol if mol != 0 else 0

class MedicalEngine:
    @staticmethod
    def dosage_check(w, d): return w * d

class EconEngine:
    @staticmethod
    def roi(i, r): return ((r - i) / i) * 100 if i != 0 else 0

# (Diğer sınıflar aynı kalıyor...)

# --- 2. ORCHESTRATOR & KARAR MOTORU ---
def log_and_solve(domain, operation_name, params, result_func, *args):
    result = result_func(*args)
    
    # Karar Motoru Kontrolü
    if isinstance(result, (int, float)):
        karar = Validator.check(domain, result)
    else:
        karar = "N/A"
    
    log_entry = {
        "Zaman": datetime.now().strftime("%H:%M:%S"),
        "Disiplin": domain,
        "İşlem": operation_name,
        "Karar": karar,
        "Sonuç": str(result)
    }
    st.session_state.audit_log.append(log_entry)
    return result, karar

# --- 3. ARAYUZ ---
st.set_page_config(page_title="Universal Decision Engine", layout="wide")
st.title("🌐 Universal Decision Engine - Karar Destekli")

if "audit_log" not in st.session_state: st.session_state.audit_log = []

domain = st.selectbox("Alan Seçin", ["Fizik", "Tıp", "Ekonomi"])

# Örnek Kullanım:
if domain == "Tıp":
    w = st.number_input("Ağırlık (kg):")
    d = st.number_input("Doz (mg/kg):")
    if st.button("Hesapla"):
        res, karar = log_and_solve("Tıp", "Dozaj", f"w:{w}, d:{d}", MedicalEngine.dosage_check, w, d)
        if "BLOCK" in karar: st.error(f"DURUM: {karar} | Sonuç: {res}")
        else: st.success(f"DURUM: {karar} | Sonuç: {res}")

# ... (Diğer disiplinler de aynı mantıkla eklenecek) ...

with st.expander("📜 Denetim Kayıtları"):
    if st.session_state.audit_log:
        st.dataframe(pd.DataFrame(st.session_state.audit_log))
