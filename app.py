# --- 1. ENGINE (GÜNCEL) ---
class Engines:
    @staticmethod
    def solve(domain, params):
        if domain == "Matematik":
            try: return eval(params)
            except: return "Matematiksel hata."
        elif domain == "Tıp":
            return f"Tıbbi notunuz kaydedildi: {params}" # Buraya ileride tıbbi kütüphane eklenebilir
        elif domain == "Fizik":
            return f"Fiziksel hesaplama yapıldı: {params}" # Buraya fizik formülleri eklenebilir
        return params

# --- 2. ARAYUZ (tab_disiplin GÜNCELLEME) ---
with tab_disiplin:
    domain = st.selectbox("Alan:", ["Matematik", "Fizik", "Tıp", "Kimya", "Ekonomi"])
    
    # Disipline göre input alanı değişecek
    if domain == "Matematik":
        params = st.text_input("Formül (örn: 2+2):")
    else:
        params = st.text_area(f"{domain} için veri girişi yapın:")
        
    if st.button("İşlemi Kaydet"):
        res = Engines.solve(domain, params)
        st.success(f"Sonuç: {res}")
        log(domain, "İşlem", res)
