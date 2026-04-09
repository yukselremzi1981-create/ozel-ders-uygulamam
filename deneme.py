import streamlit as st
import datetime
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# 1. Giriş Kontrolü
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login():
    st.subheader("Öğrenci Giriş Ekranı")
    username = st.text_input("Kullanıcı Adı")
    password = st.text_input("Şifre", type="password")
    if st.button("Giriş Yap"):
        # Buraya istediğiniz kadar öğrenci ekleyebilirsiniz
        kullanicilar = {"ogrenci1": "1234", "ali": "4321"}
        if username in kullanicilar and kullanicilar[username] == password:
            st.session_state.authenticated = True
            st.session_state.user = username
            st.rerun()
        else:
            st.error("Kullanıcı adı veya şifre hatalı!")

if not st.session_state.authenticated:
    login()
else:
    st.title(f"Hoş geldin, {st.session_state.user}")
    
    # 2. Soru Alanı
    st.subheader("Fizik Sorusu: Atış Hareketleri")
    h = st.slider("Yükseklik (metre)", 0, 100, 20)
    answer = st.radio("Cismin yere düşme süresi nedir?", [1, 2, 4, 5])
    
    if st.button("Cevabı Gönder"):
        try:
            # Google Sheets Bağlantısı
            conn = st.connection("gsheets", type=GSheetsConnection)
            
            # Kendi tablo linkinizi buraya yapıştırın:
            url = "https://docs.google.com/spreadsheets/d/1NFi3sVnKedDwrtg6bCXKmIhmbROJ9nGbt3eEMJsxHbk/edit?gid=0#gid=0"
            
            # Mevcut veriyi oku
            df = conn.read(spreadsheet=url)
            
            # Yeni satır oluştur
            yeni_veri = pd.DataFrame([{
                "zaman": str(datetime.datetime.now()),
                "ogrenci": st.session_state.user,
                "cevap": answer
            }])
            
            # Eski veriyle yeni veriyi birleştir
            guncel_df = pd.concat([df, yeni_veri], ignore_index=True)
            
            # Tabloyu güncelle
            conn.update(spreadsheet=url, data=guncel_df)
            
            st.success("Cevabın başarıyla kaydedildi!")
        except Exception as e:
            st.error(f"Veri kaydedilirken bir hata oluştu: {e}")