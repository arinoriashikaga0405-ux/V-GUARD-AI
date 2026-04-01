import streamlit as st
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Paket Layanan V-Guard AI", layout="wide")

# Nomor WhatsApp Bapak Erwin
WA_NUMBER = "628212190885"

# --- CSS CUSTOM UNTUK KOTAK PAKET ---
st.markdown(f"""
<style>
    .product-container {{
        display: flex;
        justify-content: space-between;
        gap: 20px;
    }}
    .product-card {{
        background-color: #f8f9fa;
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        padding: 30px 20px;
        text-align: center;
        flex: 1;
        transition: transform 0.3s, border-color 0.3s;
        min-height: 450px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}
    .product-card:hover {{
        transform: translateY(-5px);
        border-color: #1E3A8A;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }}
    .package-name {{
        font-size: 28px;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 10px;
        text-transform: uppercase;
    }}
    .price-tag {{
        font-size: 22px;
        font-weight: bold;
        color: #333;
        margin-bottom: 20px;
    }}
    .feature-list {{
        text-align: left;
        font-size: 14px;
        color: #555;
        margin-bottom: 30px;
        line-height: 1.6;
    }}
</style>
""", unsafe_allow_html=True)

st.title("Paket Layanan V-Guard AI")
st.write("---")

# --- GRID PAKET LAYANAN ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="product-card">
        <div>
            <div class="package-name">BASIC</div>
            <div class="price-tag">Rp 1.5jt/bln</div>
            <div class="feature-list">
                • Monitoring Transaksi Harian<br>
                • Log Aktivitas Standar<br>
                • Dashboard Desktop<br>
                • Support Email
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Pilih Paket", f"https://wa.me/{WA_NUMBER}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20BASIC")

with col2:
    st.markdown(f"""
    <div class="product-card">
        <div>
            <div class="package-name">SMART</div>
            <div class="price-tag">Rp 2.5jt/bln</div>
            <div class="feature-list">
                • Semua Fitur Basic<br>
                • Deteksi Fraud AI Aktif<br>
                • Notifikasi WA Real-time<br>
                • Analisis Tren Mingguan
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Pilih Paket", f"https://wa.me/{WA_NUMBER}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20SMART")

with col3:
    st.markdown(f"""
    <div class="product-card">
        <div>
            <div class="package-name">PRO</div>
            <div class="price-tag">Rp 5jt/bln</div>
            <div class="feature-list">
                • Semua Fitur Smart<br>
                • Audit Finansial Mendalam<br>
                • Laporan PDF Otomatis<br>
                • Priority Support 24/7
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Pilih Paket", f"https://wa.me/{WA_NUMBER}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20PRO")

with col4:
    st.markdown(f"""
    <div class="product-card">
        <div>
            <div class="package-name">ELITE</div>
            <div class="price-tag">Hubungi Kami</div>
            <div class="feature-list">
                • Custom AI Integration<br>
                • Pendampingan Strategis Founder<br>
                • On-site Audit Visit<br>
                • Multi-Business Control
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Hubungi Founder", f"https://wa.me/{WA_NUMBER}?text=Halo%20Pak%20Erwin,%20saya%20ingin%20konsultasi%20paket%20ELITE")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Secured by Erwin Sinaga")
