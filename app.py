import streamlit as st
import sympy as sp
import pandas as pd
from astropy.coordinates import EarthLocation, AltAz, SkyCoord
import astropy.units as u

# --- CORE ---
class KnowledgeOS:
    @staticmethod
    def calculate_kepler_period(a_au):
        """ Kepler'in 3. yasası: T^2 = a^3 (Güneş sistemi için) """
        return a_au**(3/2)

# --- INTERFACE ---
st.set_page_config(layout="wide")
st.title("🏗️ Knowledge OS: Celestial Core")

module = st.sidebar.selectbox("Modül Seçin:", ["Analitik Matematik", "Gök Mekaniği"])

if module == "Gök Mekaniği":
    st.subheader("🪐 Kepler Yörünge Hesaplayıcı")
    a = st.number_input("Yarı Büyük Eksen (AU - Astronomik Birim):", value=1.0)
    if st.button("Periyot Hesapla"):
        t = KnowledgeOS.calculate_kepler_period(a)
        st.info(f"Bu yörüngedeki bir cismin periyodu: {t:.2f} Dünya yılıdır.")
        st.latex(f"T^2 = a^3 \implies T = {a}^{{1.5}} = {t:.2f}")

elif module == "Analitik Matematik":
    # ... (Matematik modülü önceki gibi kalacak)
