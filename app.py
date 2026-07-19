import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
if "audit_log" not in st.session_state: st.session_state.audit_log = []

st.title("🌐 Universal Decision Engine")

tab1, tab2 = st.tabs(["🔢 İşlemler", "📊 Analiz"])

with tab1:
    alan = st.selectbox("Alan Seç:", ["Matematik", "Fizik", "Tıp"])
    
    # Her disiplin için özel girdi mantığı
    if alan == "Matematik":
        girdi = st.text_input("Formül (örn: 2*5):")
        if st.button("Hesapla"):
            try:
                sonuc = eval(girdi)
                st.session_state.audit_log.append({"Alan": alan, "İşlem": girdi, "Sonuç": sonuc})
                st.success(f"Sonuç: {sonuc}")
            except: st.error("Hatalı formül.")
            
    elif alan == "Fizik":
        girdi = st.text_input("Kütle ve İvme gir (örn: 10,2):")
        if st.button("Kuvvet Hesapla"):
            try:
                m, a = map(float, girdi.split(','))
                sonuc = m * a
                st.session_state.audit_log.append({"Alan": alan, "İşlem": f"{m}kg * {a}m/s2", "Sonuç": f"{sonuc} N"})
                st.success(f"Kuvvet: {sonuc} Newton")
            except: st.error("Format: 10,2 şeklinde giriniz.")
            
    elif alan == "Tıp":
        girdi = st.text_area("Tıbbi notunuz:")
        if st.button("Notu Kaydet"):
            st.session_state.audit_log.append({"Alan": alan, "İşlem": "Not", "Sonuç": girdi})
            st.info("Not sisteme eklendi.")

with tab2:
    if st.session_state.audit_log:
        df = pd.DataFrame(st.session_state.audit_log)
        st.bar_chart(df['Alan'].value_counts())
        st.dataframe(df)
    else:
        st.write("Henüz veri yok.")
