import streamlit as st

# --- 1. DISIPLIN KUTUPHANELERI ---
class PhysicsEngine:
    @staticmethod
    def calculate_force(mass, acceleration):
        return mass * acceleration

class MathEngine:
    @staticmethod
    def solve_complex(expression):
        try:
            # Girdiyi temizle
            if not expression: return "Lütfen bir denklem girin."
            # Sadece güvenli karakterlere izin ver
            allowed_chars = "0123456789+-*/(). "
            if any(char not in allowed_chars for char in expression):
                return "Hata: Sadece matematiksel karakterler kullanın."
            return eval(expression)
        except ZeroDivisionError:
            return "Hata: Sıfıra bölme yapılamaz."
        except:
            return "Hata: Geçersiz ifade."

# --- 2. ORCHESTRATOR ---
def decision_orchestrator(domain, params):
    if domain == "Fizik":
        return PhysicsEngine.calculate_force(params['m'], params['a'])
    elif domain == "Matematik":
        return MathEngine.solve_complex(params['expr'])
    return "Bilinmeyen Disiplin"

# --- 3. ARAYUZ ---
st.set_page_config(page_title="Universal Engine", layout="wide")
st.title("🌐 Universal Decision Engine")

domain = st.selectbox("Analiz Yapılacak Alanı Seçin", ["Fizik", "Matematik"])

if domain == "Fizik":
    col1, col2 = st.columns(2)
    with col1: m = st.number_input("Kütle (kg):", value=1.0)
    with col2: a = st.number_input("İvme (m/s²):", value=9.8)
    if st.button("Analiz Et"):
        st.success(f"Sonuç (Kuvvet): {decision_orchestrator('Fizik', {'m':m, 'a':a})} Newton")

elif domain == "Matematik":
    expr = st.text_input("Denklem Girin (örn: 25 * 4 / 2):")
    if st.button("Çöz"):
        sonuc = decision_orchestrator('Matematik', {'expr':expr})
        st.info(f"Sonuç: {sonuc}")
