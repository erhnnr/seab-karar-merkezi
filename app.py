import streamlit as st
import pandas as pd
from datetime import datetime

# --- MOTOR MANTIĞI ---
def analyze_medical(drugs):
    drug_list = [d.strip().lower() for d in drugs.split(",")]
    if "warfarin" in drug_list and "aspirin" in drug_list:
        return "BLOCK", "HIGH_RISK_BLEEDING: Majör kanama riski."
    return "PASS", "Güvenli"

# --- DASHBOARD ARAYÜZÜ ---
st.set_page_config(page_title="SEAB Karar Merkezi", layout="wide")
st.title("🛡️ SEAB: Operasyonel Kontrol Odası")

if 'history' not in st.session_state:
    st.session_state.history = []

tab1, tab2 = st.tabs(["Analiz Terminali", "Denetim Kayıtları (Audit Log)"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Tıbbi Analiz")
        drugs = st.text_input("İlaçlar (Virgülle ayırın):")
        if st.button("Tıbbi Analizi Çalıştır"):
            status, msg = analyze_medical(drugs)
            st.session_state.history.append({"Tarih": datetime.now().strftime("%H:%M:%S"), "Plugin": "Tıbbi", "Karar": status, "Detay": msg})
            if status == "BLOCK": st.error(msg)
            else: st.success("İşlem Onaylandı: " + msg)

    with col2:
        st.subheader("Finansal Analiz")
        lev = st.number_input("Kaldıraç:", min_value=1)
        if st.button("Finansal Analizi Çalıştır"):
            status = "BLOCK" if lev > 5 else "PASS"
            msg = "Kaldıraç limiti (5x) aşıldı" if status == "BLOCK" else "İşlem Güvenli"
            st.session_state.history.append({"Tarih": datetime.now().strftime("%H:%M:%S"), "Plugin": "Finans", "Karar": status, "Detay": msg})
            if status == "BLOCK": st.error(msg)
            else: st.info(msg)

with tab2:
    st.subheader("Sistem İşlem Geçmişi")
    st.table(pd.DataFrame(st.session_state.history))
