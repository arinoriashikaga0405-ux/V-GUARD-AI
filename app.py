import streamlit as st
import os

# 1. KONFIGURASI & VARIABEL UTAMA (Didefinisikan di awal agar tidak error)
wa_num = "6282122190885" 

# 2. MENU PROFIL (Halaman 4)
st.header("Strategic Leadership")
col_p1, col_p2 = st.columns([1, 2])

with col_p1:
    # Menggunakan file lokal erwin.jpg sesuai foto Bapak
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Erwin Sinaga, Founder V-Guard AI", use_container_width=True)
    else:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)

with col_p2:
    st.markdown("### Erwin Sinaga")
    st.markdown("#### *Founder & Chief Executive Officer*")
    
    # Deskripsi 100+ Kata (Tetap Sesuai Permintaan Bapak)
    st.markdown("""
Bapak Erwin Sinaga adalah seorang *Senior Business Leader* visioner dengan rekam jejak impresif selama lebih dari 10 tahun di posisi krusial sebagai CEO dan CSO dalam industri perbankan serta manajemen aset. Pengalaman mendalam beliau dalam mengelola risiko operasional, memimpin transformasi digital, dan menjaga integritas aset bernilai tinggi menjadi pondasi kuat di balik berdirinya **V-Guard AI Systems**.

Dengan latar belakang keahlian strategis yang komprehensif, Pak Erwin berdedikasi penuh untuk mendemokratisasi akses terhadap teknologi keamanan finansial kelas dunia. Beliau melihat celah krusial antara prototipe teknologi dengan solusi *production-grade* yang benar-benar siap menjawab tantangan pasar di tahun 2026. Komitmen utama beliau adalah membangun solusi 'End-to-End Intermediary' yang cerdas, adaptif, dan memiliki daya jual tinggi (*high conversion*), yang tidak hanya melindungi UMKM lokal dari kehancuran finansial akibat *fraud*, tetapi juga memberikan kepastian keamanan di tingkat Korporat global.
""")

    # Menggunakan tombol resmi Streamlit (Lebih aman dari NameError & TypeError)
    wa_direct = f"https://wa.me/{wa_num}?text=Halo%20Pak%20Erwin%2C%20saya%20ingin%20konsultasi%20strategis"
    st.link_button("📲 Hubungi Pak Erwin via WhatsApp", wa_direct, use_container_width=True, type="primary")
