import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# --- 1. ENGINE SINIFLARI ---
class DataEngine:
    @staticmethod
    def get_weather(city): 
        # Not: API anahtarı geçici/örnek amaçlıdır, çalışmazsa kendi ücretsiz anahtarını ekleyebilirsin.
        api_key = "05391d4e078b4081c7f130421261907" 
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            res = requests.get(url).json()
            return f"{res['main']['temp']}°C, {res['weather'][0]['description']}"
        except: return "Veri alınamadı."

    @staticmethod
    def get_crypto_price(symbol): 
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}USDT"
        try:
            res = requests.get(url).json()
            return res['price']
        except: return "Fiyat alınamadı."

# --- 2. ORCHESTRATOR & LOG ---
if "audit_log" not in st.session_state: st.session_state.audit_log = []

def log(domain, op, result):
    st.session_state.audit_log.append({
        "Zaman": datetime.now().strftime("%H:%M:%S"), 
        "Alan": domain, 
        "İşlem": op, 
        "Sonuç": str(result)
    })

# --- 3. ARAYUZ ---
st.set_page_config(page_title="Universal Engine", layout="wide")
st.title("🌐 Universal Decision Engine")

tab_analiz, tab_piyasa, tab_balik = st.tabs(["🔢 Genel Analiz", "📈 Piyasa/Yazılım", "🎣 Balıkçılık (Boğaçayı)"])

with tab_piyasa:
    st.subheader("Algoritmik Takip")
    symbol = st.text_input("Sembol (örn: BTC):", value="BTC")
    if st.button("Fiyatı Getir"):
        price = DataEngine.get_crypto_price(symbol)
        st.success(f"{symbol.upper()} Fiyatı: {price} USDT")
        log("Piyasa", "Fiyat Takibi", price)

with tab_balik:
    st.subheader("Boğaçayı Analizi")
    if st.button("Hava Durumunu Kontrol Et"):
        weather = DataEngine.get_weather("Antalya")
        st.info(f"Antalya Durumu: {weather}")
        log("Balıkçılık", "Hava Kontrolü", weather)

with tab_analiz:
    st.subheader("Operasyonel Analiz Raporu")
    if st.session_state.audit_log:
        df = pd.DataFrame(st.session_state.audit_log)
        st.dataframe(df)
        st.write("İşlem Yoğunluğu:")
        st.bar_chart(df['Alan'].value_counts())
    else:
        st.info("Henüz bir işlem yapılmadı. Yukarıdaki sekmelerden veri çekebilirsin.")
