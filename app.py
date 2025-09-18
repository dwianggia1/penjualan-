import streamlit as st
import db
import pandas as pd
# Authentication Check
if not st.session_state.get("login", False):
    st.error("Please login")
    st.switch_page("login.py")

st.title ("Welcome " + st.session_state.get("username", ""))
# Logout Button
if st.button("Logout"):
    st.session_state["login"] = False
    st.switch_page("login.py")

st.title("CRUD Mahasiswa")
menu = st.sidebar.selectbox("Menu", ["Tambah", "Lihat", "Ubah", "Hapus"])

#Tambah Data
if menu == "Tambah":
    st.subheader("Tambah Data Mahasiswa")
    nim = st.text_input("NIM")   
    name = st.text_input("Nama")
    angkatan = st.number_input("Angkatan", min_value=2020, max_value=2030, step=1) 
    email = st.text_input("Email")
    if st.button("Simpan"):
        if nim and name and angkatan and email:
            db.add_students(nim, name, angkatan, email)
            st.success("Data berhasil ditambahkan")
        else:
            st.error("Mohon isi semua field")

#Lihat Data
elif menu == "Lihat":
    st.subheader("Daftar Mahasiswa")
    data = db.get_students()
    st.dataframe(pd.DataFrame(data))

#Ubah Data
elif menu == "Ubah":
    st.subheader("Ubah Data Mahasiswa")
    data = db.get_students()
    df = pd.DataFrame(data)
    if not df.empty:
        selected_id = st.selectbox("Pilih ID Mahasiswa", df["id"])
        selected_row = df[df["id"] == selected_id].iloc[0]
        new_name = st.text_input("Nama", value=selected_row["name"])
        if st.button("Update"):
            db.update_students(selected_id, new_name)
            st.success("Data berhasil diubah")
    else:
        st.info("Tidak ada data untuk diubah")

#Hapus Data
elif menu == "Hapus":
    st.subheader("Hapus Data Mahasiswa")
    data = db.get_students()
    df = pd.DataFrame(data)
    if not df.empty:
        selected_id = st.selectbox("Pilih ID Mahasiswa", df["id"])
        if st.button("Hapus"):
            db.delete_students(selected_id)
            st.success("Data berhasil dihapus")
    else:
        st.info("Tidak ada data untuk dihapus")