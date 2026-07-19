import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# --- 1. ENGINE SINIFLARI ---
class Engines:
    @staticmethod
    def calculate(domain, params):
        # Matematik/Fizik/Tıp vs için temel hesaplayıcı
        try:
            return eval(params) # Çok basit ve hızlı hesaplama için
        except: return "Hata"

    @staticmethod
    def get_weather(city):
        api_key = "05391d4e078b4081c7f130421261907"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            res = requests.get(url).json()
            return f"{res['main']['temp']}°C, {res['weather'][0]['description']}"
        except: return "Veri alınamadı."

# --- 2. ORCHESTRATOR & LOG ---
if "audit_log" not in st.session_state: st.session_state.audit_log = []

def log(domain, op, result):
    st.session_state.audit_log.append({"Zaman": datetime.now().strftime("%H:%M:%S"), "Alan": domain, "İşlem": op, "Sonuç": str(result)})

# --- 3. ARAYUZ ---
st.set_page_config(page_title="Universal Engine", layout="wide")
st.title("🌐 Universal Decision Engine")

tab_disiplin, tab_piyasa, tab_balik, tab_analiz = st.tabs(["🔢 Disiplinler", "📈 Piyasa", "🎣 Balıkçılık", "📊 Analiz"])

with tab_disiplin:
    domain = st.selectbox("Alan Seçin", ["Matematik", "Fizik", "Tıp", "Kimya", "Ekonomi"])
    params = st.text_input("İşlem/Parametre gir (örn: 2*2 veya 0.05*0.04):")
    if st.button("Hesapla"):
        res = Engines.calculate(domain, params)
        st.success(f"Sonuç: {res}")
        log(domain, "Hesaplama", res)

with tab_piyasa:
    symbol = st.text_input("Sembol (örn: BTC):", value="BTC")
    if st.button("Fiyat Getir"):
        res = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}USDT").json()
        price = res.get('price', 'Hata')
        st.success(f"Fiyat: {price}")
        log("Piyasa", "Fiyat", price)

with tab_balik:
    if st.button("Boğaçayı Kontrol"):
        weather = Engines.get_weather("Antalya")
        st.info(f"Hava: {weather}")
        log("Balıkçılık", "Hava", weather)

with tab_analiz:
    if st.session_state.audit_log:
        df = pd.DataFrame(st.session_state.audit_log)
        st.bar_chart(df['Alan'].value_counts())
        st.dataframe(df)
