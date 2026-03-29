# --- TAMBAHKAN LIBRARY INI DI BAGIAN ATAS KODE ---
import os
from PIL import Image

# ... [Pertahankan kode CSS dan konfigurasi AI Bapak] ...

# --- KODE BARU UNTUK SIDEBAR (Ganti baris 30-43) ---
with st.sidebar:
    # Menggunakan columns di dalam sidebar untuk mensejajarkan foto dan teks
    # Col_pic untuk foto, col_text untuk nama dan jabatan
    col_pic, col_text = st.columns([1, 2])
    
    with col_pic:
        try:
            # Pastikan nama file fotonya benar: 'bapak.png'
            image = Image.open('bapak.png')
            st.image(image, use_column_width=True)
        except FileNotFoundError:
            # Jika foto tidak ditemukan, pakai ikon default
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", use_column_width=True)
            st.error("Gagal memuat foto 'bapak.png'. Cek nama file di GitHub.")

    with col_text:
        st.markdown(
            """
            <div style="display: flex; flex-direction: column; justify-content: center; height: 100%;">
                <p style="font-weight: bold; font-size: 16px; margin-bottom: 0px; color: white;">Erwin Sinaga</p>
                <p style="font-size: 14px; margin-top: 0px; color: white; opacity: 0.8;">Founder V-GUARD</p>
            </div>
            """, 
            unsafe_allow_html=True
        )

    st.divider()
    halaman = st.radio("Pilih Halaman:", ["🌐 Promosi & Umum", "👥 Area Layanan Klien", "🔐 Panel Admin"])
    st.divider()
    st.write("📍 Tangerang, Banten, Indonesia")
