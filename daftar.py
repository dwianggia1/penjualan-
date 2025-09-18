import streamlit as st
import db

st.title("📝 Register Akun")

username = st.text_input("Username")
password = st.text_input("Password", type="password")
password2 = st.text_input("Konfirmasi Password", type="password")

if st.button("Register"):
    if password != password2:
        st.error("❌ Password tidak sama!")
    elif username == "" or password == "":
        st.warning("⚠️ Username & Password tidak boleh kosong!")
    else:
        try:
            db.add_akun(username, password)
            st.success("✅ Registrasi berhasil! Silakan login.")
        except Exception as e:
            st.error(f"❌ Gagal registrasi: {e}")
