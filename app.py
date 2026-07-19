import streamlit as st
import pandas as pd

# --- 1. AYARLAR VE LOG ---
st.set_page_config(layout="wide")
if "audit_log" not in st.session_state: st.session_state.audit_log = []

# --- 2. ARAYUZ ---
st.title("🌐 Universal Decision Engine")

# Basit Tab Yapısı
tab1, tab2 = st.tabs(["🔢 İşlemler", "📊 Analiz"])

with tab1:
    alan = st.selectbox("Alan Seç:", ["Matematik", "Fizik", "Tıp"])
    girdi = st.text_input("Veri girişi:")
    
    if st.button("Kaydet"):
        st.session_state.audit_log.append({"Alan": alan, "İşlem": girdi})
        st.success("Veri kaydedildi!")

with tab2:
    if st.session_state.audit_log:
        df = pd.DataFrame(st.session_state.audit_log)
        st.bar_chart(df['Alan'].value_counts())
        st.dataframe(df)
    else:
        st.write("Henüz veri yok.")
