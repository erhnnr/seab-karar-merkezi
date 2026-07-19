import streamlit as st
import pandas as pd
import requests # Yeni ekledik
from datetime import datetime

# --- 1. DISIPLIN KUTUPHANELERI (API Destekli) ---
class EconEngine:
    @staticmethod
    def get_live_rate(base, target):
        # Ücretsiz bir API (Örnek: Exchangerate-api)
        url = f"https://api.exchangerate-api.com/v4/latest/{base}"
        try:
            response = requests.get(url).json()
            return response['rates'].get(target, 0)
        except:
            return 0

    @staticmethod
    def roi(i, r): 
        return ((r - i) / i) * 100 if i != 0 else 0

# (Diğer sınıflar burada kalmaya devam edecek...)

# --- 2. ORCHESTRATOR ---
# Buraya EconEngine içindeki yeni metodu çağıracak bir yapı ekliyoruz.

# --- 3. ARAYUZ ---
elif domain == "Ekonomi":
    st.subheader("Canlı Kur Analizi")
    base = st.text_input("Baz Birim (örn: USD):", value="USD")
    target = st.text_input("Hedef Birim (örn: TRY):", value="TRY")
    
    if st.button("Canlı Kuru Getir"):
        rate = EconEngine.get_live_rate(base.upper(), target.upper())
        st.info(f"Anlık Kur: {rate}")
        
    i = st.number_input("Yatırım Miktarı:")
    r = st.number_input("Dönüş Miktarı:")
    if st.button("ROI Hesapla"): 
        res = EconEngine.roi(i, r)
        st.success(f"ROI: %{res:.2f}")
