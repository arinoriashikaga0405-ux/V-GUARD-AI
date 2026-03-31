import streamlit as st
import os
from datetime import datetime
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# 2. CSS CUSTOM PREMIUM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; margin-top: 5px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; font-size: 16px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 8px rgba(0,0,0,0.02); }
    .vision-box { background: #fdfdfd; padding: 25px; border-left: 5px solid #007bff; border-radius: 10px; margin-bottom: 25px; }
    .security-info { color: #666; font-size: 12px; font-weight: bold; margin-top: 10px; text-align: center; border: 1px dashed #ccc; padding: 8px; border-radius: 8px; background: #fafafa; }
    .invoice-output { background: #f8f9fa; padding: 20px; border-left: 8px solid #007bff; border-radius: 5px; font-family: monospace; white-space: pre-wrap; font-size: 14px; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● Intelligence Active</p>', unsafe_allow_html=True)
    
    # Navigasi yang telah disederhanakan
    menu = st.radio("Navigasi:", ["1. 👤 Profil Founder", "2. 🎯 Visi & ROI", "3. 📝 Registrasi & Penawaran"])
    st.write("---")
    
    st.markdown("### Support Center")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")
    st.markdown('<div class="security-info">🔐 End-to-End Encrypted System</div>', unsafe_allow_html=True)

# --- FOLDER 1: PROFIL FOUNDER (MINIMAL 100 KATA) ---
if menu == "1. 👤 Profil Founder":
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.markdown("""<div class="profile-box">
        <b>Bapak Erwin Sinaga</b> merupakan seorang Pemimpin Bisnis Senior (Senior Business Leader) yang telah mengukir rekam jejak profesional impresif selama lebih dari sepuluh tahun di industri perbankan dan manajemen aset nasional. Sepanjang perjalanan kariernya, beliau telah dipercaya memegang berbagai tanggung jawab strategis, termasuk peran krusial sebagai Chief Executive Officer (CEO) dan Chief Sales Officer (CSO). Dalam kapasitas tersebut, beliau bertanggung jawab penuh atas mitigasi risiko operasional, kepatuhan sistem, serta perlindungan aset korporasi dalam skala besar. Pengalaman mendalam di sektor finansial ini memberikan beliau perspektif unik dan tajam dalam mengidentifikasi titik-titik lemah sistem manajemen konvensional yang sering kali menjadi celah terjadinya inefisiensi finansial. <br><br>
        V-Guard AI didirikan berdasarkan dedikasi beliau untuk menghadirkan teknologi pengawasan berbasis Artificial Intelligence yang mampu bekerja secara otonom dan presisi selama 24 jam penuh. Beliau sangat meyakini bahwa integritas dan transparansi data adalah fondasi utama bagi pertumbuhan bisnis yang berkelanjutan. Oleh karena itu, melalui kepemimpinan beliau, V-Guard AI berkomitmen untuk mendemokratisasi standar keamanan tingkat tinggi agar dapat diakses oleh pemilik bisnis UMKM hingga perusahaan menengah di Indonesia. Dengan visi untuk membangun benteng pertahanan digital yang tangguh, Bapak Erwin Sinaga terus memastikan bahwa setiap inovasi yang dihadirkan mampu memberikan nilai ekonomi nyata serta ketenangan pikiran (peace of mind) bagi para pengusaha dalam mengelola aset berharga mereka secara profesional.
        </div>""", unsafe_allow_html=True)

# --- FOLDER 2: VISI & ROI ---
elif menu == "2. 🎯 Visi & ROI":
    st.header("🎯 Analisis Strategis & ROI")
    st.markdown("""<div class="vision-box">
        <h3>Visi Perusahaan</h3>
        <p>Menjadi mitra pertahanan digital terdepan di Indonesia yang menjamin transparansi operasional total melalui inovasi kecerdasan buatan.</p>
        <h3>Misi Perusahaan</h3>
        <ul>
            <li>Mengeliminasi potensi kebocoran aset bisnis secara sistemik.</li>
            <li>Menyediakan laporan audit otomatis yang akurat dan transparan.</li>
            <li>Memberikan rasa aman bagi pemilik bisnis melalui deteksi anomali real-time.</li>
        </ul>
    </div>""", unsafe_allow_html=True)
    st.write("---")
    st.subheader("📊 Simulasi Penyelamatan Aset")
    omzet = st.number_input("Input Omzet Bulanan Bisnis (Rp):", value=500000000, step=10000000)
    st.success(f"🛡️ Estimasi Kebocoran yang Dicegah: **Rp {omzet * 0.045:,.0f}** / bulan.")

# --- FOLDER 3: REGISTRASI & PENAWARAN ---
elif menu == "3. 📝 Registrasi & Penawaran":
    st.header("📝 Registrasi Layanan & Penawaran")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama Pelanggan (PIC):")
        n_bis = c1.text_input("Nama Bisnis/Perusahaan:")
        h_pen = c2.number_input("Nilai Investasi (Rp):", value=2500000)
        wa_no = c2.text_input("No. WhatsApp Klien (Contoh: 62812...):")
        
        btn_reg = st.form_submit_button("Simpan & Buat Penawaran WA")
        
        if btn_reg and n_pel:
            st.success("✅ Data Berhasil Disimpan!")
            
            # Isi Pesan WA Otomatis dengan Rekening BCA Bapak
            inv_msg = f"""*PENAWARAN V-GUARD AI SYSTEMS*
            
Yth. {n_pel} ({n_bis}),

Berikut rincian biaya aktivasi sistem V-Guard AI:
- Nilai Investasi: Rp {h_pen:,.0f}

*INSTRUKSI PEMBAYARAN:*
Transfer ke Rekening Resmi Founder:
🏦 *Bank:* BCA
💳 *No. Rekening:* 3450074658
👤 *Atas Nama:* ERWIN SINAGA

Mohon konfirmasi bukti transfer untuk proses aktivasi sistem. 
Salam, Erwin Sinaga (Founder)."""
            
            st.markdown(f'<div class="invoice-output">{inv_msg}</div>', unsafe_allow_html=True)
            
            # Tombol Kirim WA
            wa_encoded = urllib.parse.quote(inv_msg)
            st.link_button("🚀 KIRIM PENAWARAN KE WHATSAPP", f"https://wa.me/{wa_no}?text={wa_encoded}")

# 4. FOOTER
st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Intelligence by Erwin Sinaga</div>', unsafe_allow_html=True)
