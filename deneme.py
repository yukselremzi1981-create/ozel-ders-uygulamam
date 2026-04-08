import streamlit as st

# 1. Giriş Kontrolü (Basit Mantık)
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login():
    username = st.text_input("Kullanıcı Adı")
    password = st.text_input("Şifre", type="password")
    if st.button("Giriş Yap"):
        if username == "ogrenci1" and password == "1234":
            st.session_state.authenticated = True
            st.session_state.user = username
            st.rerun()

if not st.session_state.authenticated:
    login()
else:
    st.title(f"Hoş geldin, {st.session_state.user}")
    
    # 2. Soru Alanı
    st.subheader("Fizik Sorusu: Atış Hareketleri")
    h = st.slider("Yükseklik (metre)", 0, 100, 20)
    v0 = st.number_input("İlk Hız (m/s)", value=0)
    
    answer = st.radio("Cismin yere düşme süresi nedir?", [1, 2, 4, 5])
    
    if st.button("Cevabı Gönder"):
        # Burada veritabanına (Sheets veya SQL) kayıt gönderilecek
        # save_to_db(st.session_state.user, answer)
        st.success("Cevabın kaydedildi, hocamıza iletildi!")