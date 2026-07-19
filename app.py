import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# --- 1. MODÜLER ENGINELER ---
class DataEngine:
    @staticmethod
    def get_weather(city): # Balıkçılık için
        api_key = "05391d4e078b4081c7f130421261907" # Örnek ücretsiz API
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            res = requests.get(url).json()
            return f"Sıcaklık: {res['main']['temp']}°C, Durum: {res['weather'][0]['description']}"
        except: return "Hava verisi alınamadı."

    @staticmethod
    def get_crypto_price(symbol): # Algoritmik takip için
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
        try:
            res = requests.get(url).json()
            return res['price']
        except: return "Fiyat alınamadı."

# --- 2. ORCHESTRATOR & ANALIZ ---
if "audit_log" not in st.session_state: st.session_state.audit_log = []

def log(domain, op, result):
    st.session_state.audit_log.append({"Zaman": datetime.now().strftime("%H:%M:%S"), "Alan": domain, "İşlem": op, "Sonuç": str(result)})

# --- 3. GÜNCEL ARAYÜZ ---
st.title("🌐 Universal Decision Engine")
tab_analiz, tab_piyasa, tab_balik = st.tabs(["🔢 Genel Analiz", "📈 Algoritmik/Piyasa", "🎣 Balıkçılık (Boğaçayı)"])

with tab_piyasa:
    symbol = st.text_input("Kripto Sembolü (örn: BTC):", value="BTC")
    if st.button("Anlık Fiyat"):
        price = DataEngine.get_crypto_price(symbol.upper())
        st.success(f"{symbol} Fiyatı: {price} USDT")
        log("Piyasa", "Fiyat Takibi", price)

with tab_balik:
    if st.button("Boğaçayı Hava Durumu"):
        weather = DataEngine.get_weather("Antalya")
        st.info(f"Boğaçayı Analizi: {weather}")
        log("Balıkçılık", "Hava Kontrolü", weather)

with tab_analiz:
    st.subheader("İşlem Geçmişi")
    if st.session_state.audit_log:
        df = pd.DataFrame(st.session_state.audit_log)
        st.dataframe(df)
        st.bar_chart(df['Alan'].value_counts())
