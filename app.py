import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# --- 1. DISIPLIN KUTUPHANELERI ---
class EconEngine:
    @staticmethod
    def get_live_rate(base, target):
        url = f"https://api.exchangerate-api.com/v4/latest/{base}"
        try:
            response = requests.get(url).json()
            return response['rates'].get(target.upper(), 0)
        except: return 0

    @staticmethod
    def roi(i, r): return ((r - i) / i) * 100 if i != 0 else 0

class PhysicsEngine:
    @staticmethod
    def calculate_force(m, a): return m * a

# --- 2. ORCHESTRATOR & LOG ---
if "audit_log" not in st.session_state: st.session_state.audit_log = []

def log_and_solve(domain, op, params, func, *args):
    result = func(*args)
    log_entry = {"Zaman": datetime.now().strftime("%H:%M:%S"), "Disiplin": domain, "İşlem": op, "Sonuç": str(result)}
    st.session_state.audit_log.append(log_entry)
    return result

# --- 3. ARAYUZ ---
st.title("🌐 Universal Decision Engine")
domain = st.selectbox("Alan Seçin", ["Fizik", "Ekonomi"])

# FIZIK BOLUMU
if domain == "Fizik":
    m = st.number_input("Kütle:")
    a = st.number_input("İvme:")
    if st.button("Hesapla"):
        res = log_and_solve("Fizik", "Kuvvet", f"m:{m},a:{a}", PhysicsEngine.calculate_force, m, a)
        st.success(f"Kuvvet: {res}")

# EKONOMI BOLUMU
elif domain == "Ekonomi":
    st.subheader("Canlı Kur")
    base = st.text_input("Baz Birim (örn: USD):", value="USD")
    target = st.text_input("Hedef Birim (örn: TRY):", value="TRY")
    if st.button("Kuru Getir"):
        rate = EconEngine.get_live_rate(base, target)
        st.info(f"Anlık Kur: {rate}")
    
    i = st.number_input("Yatırım:")
    r = st.number_input("Dönüş:")
    if st.button("ROI Hesapla"):
        res = log_and_solve("Ekonomi", "ROI", f"i:{i},r:{r}", EconEngine.roi, i, r)
        st.success(f"ROI: %{res:.2f}")

# LOG GORUNTULEME
with st.expander("📜 Denetim Kayıtları"):
    st.dataframe(pd.DataFrame(st.session_state.audit_log))
