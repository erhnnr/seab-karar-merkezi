import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# --- 1. ENGINE SINIFLARI ---
class Engines:
    @staticmethod
    def solve(domain, params):
        if domain == "Matematik":
            try: return eval(params)
            except: return "Matematiksel hata."
        return f"{domain} için veriniz alındı: {params}"

    @staticmethod
    def get_weather(city):
        api_key = "05391d4e078b4081c7f130421261907"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            res = requests.get(url).json()
            return f"{res['main']['temp']}°C, {res['weather'][0]['description']}"
        except: return "Veri yok"

# --- 2. ORCHESTRATOR & LOG ---
if "audit_log" not in st.session_state: st.session_state.audit_log = []

def log(domain, op, result):
    st.session_state.audit_log.append({"Zaman": datetime.now().strftime("%H:%M:%S"), "Alan": domain, "İşlem": op, "Sonuç": str(result)})

# --- 3. ARAYUZ ---
st.set_page_config(page_title="Universal Engine", layout="wide")
st.title("🌐 Universal Decision Engine")

# Öneri Motoru
if len(st.session_state.audit_log) > 2:
    df = pd.DataFrame(st.session_state.audit_log)
    favori = df['Alan'].mode()[0]
    st.sidebar.info(f"💡 AI Tahmini: Genelde {favori} ile ilgileniyorsun.")

# Sekmeleri tanımla
tab1, tab2, tab3, tab4 = st.tabs(["🔢 Disiplinler", "📈 Piyasa", "🎣 Balıkçılık", "📊 Analiz"])

with tab1:
    domain = st.selectbox("Alan:", ["Matematik", "Fizik", "Tıp", "Kimya", "Ekonomi"])
    if domain == "Matematik":
        params = st.text_input("Formül:")
    else:
        params = st.text_area("Veri girişi:")
    if st.button("İşlemi Kaydet"):
        res = Engines.solve(domain, params)
        st.success(f"Sonuç: {res}")
        log(domain, "İşlem", res)

with tab2:
    symbol = st.text_input("Sembol:", value="BTC")
    if st.button("Fiyat Getir"):
        try:
            res = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}USDT").json()
            st.success(f"Fiyat: {res['price']}")
            log("Piyasa", "Fiyat", res['price'])
        except: st.error("Hata")

with tab3:
    if st.button("Boğaçayı Kontrol"):
        w = Engines.get_weather("Antalya")
        st.info(f"Hava: {w}")
        log("Balıkçılık", "Hava", w)

with tab4:
    if st.session_state.audit_log:
        df = pd.DataFrame(st.session_state.audit_log)
        st.bar_chart(df['Alan'].value_counts())
        st.dataframe(df)
