# --- 1. ENGINE SINIFLARI (GÜNCEL MANTIK) ---
class Engines:
    @staticmethod
    def solve(domain, params):
        if domain == "Matematik":
            try: return eval(params)
            except: return "Matematiksel hata."
        
        elif domain == "Fizik":
            # Örnek: F = m * a hesaplaması (m,a formatında girilirse)
            try:
                m, a = map(float, params.split(','))
                return f"Kuvvet: {m * a} N"
            except: return "Girdi formatı 'kütle,ivme' olmalı."

        elif domain == "Tıp":
            # Tıbbi notlara göre basit kategorizasyon
            if "ağrı" in params.lower(): return "Not: Ağrı kaydı oluşturuldu, takip edilecek."
            return f"Tıbbi not kayıt altına alındı."

        elif domain == "Kimya":
            return f"Kimyasal analiz: {params} verisi işleniyor..."
            
        elif domain == "Ekonomi":
            # Döviz hesaplaması örneği
            try: return f"Tahmini TRY karşılığı: {float(params) * 33.0} TL" # Basit kur simülasyonu
            except: return "Sayısal değer girin."

        return f"{domain} işlemi tamamlandı."
