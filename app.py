import streamlit as st
import pandas as pd
import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI | Interactive Dashboard", page_icon="🛡️", layout="wide")

# --- 2. CSS UNTUK UI RESPONSIVE & TOOLTIP ---
st.markdown("""
<style>
    /* Tooltip Custom */
    .tooltip {
        position: relative; display: inline-block; border-bottom: 1px dotted #0D47A1; color: #0D47A1; cursor: help;
    }
    /* Mobile Optimization: Sidebar Width */
    [data-testid="stSidebar"] { min-width: 250px; max-width: 300px; }
    /* Dashboard Cards */
    .card {
        background: #F8FAFC; padding: 20px; border-radius: 10px; border-left: 5px solid #00BCD4;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. SECURITY: ROLE-BASED ACCESS GUARD ---
if 'user_role' not in st.session_state:
    st.session_state.user_role = "Viewer" # Default role aman

def check_admin_access():
    """Guard untuk mencegah unauthorized edit."""
    if st.session_state.user_role != "Admin":
        st.error("🚫 Akses Ditolak: Anda memerlukan peran 'Admin' untuk mengubah konfigurasi ini.")
        return False
    return True

# --- 4. SIDEBAR NAVIGASI FLEKSIBEL ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1004/1004666.png", width=50)
    st.title("V-Guard AI")
    st.markdown("---")
    
    # Switcher Role untuk keperluan Demo/Testing Bapak
    st.session_state.user_role = st.selectbox("Current Role (Demo Mode):", ["Admin", "Viewer"])
    
    menu = st.radio("Navigasi:", ["🏠 Dashboard", "👥 Manajemen User", "⚙️ Pengaturan AI"])
    st.markdown("---")
    st.caption(f"Logged in as: **Erwin Sinaga** ({st.session_state.user_role})")

# --- 5. AREA KONTEN UTAMA ---
if menu == "🏠 Dashboard":
    st.header("📊 Dashboard Overview")
    
    # Row 1: Widget Ringkasan dengan Tooltip
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="card"><b>Total Saldo Dipantau</b> <span class="tooltip" title="Total dana dari seluruh rekening terhubung">ℹ️</span><h3>Rp 1.42 M</h3></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><b>Potensi Fraud</b> <span class="tooltip" title="Transaksi yang ditandai AI sebagai anomali">ℹ️</span><h3>2 Alert</h3></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="card"><b>Cash Flow Health</b> <span class="tooltip" title="Stabilitas arus kas berdasarkan prediksi AI">ℹ️</span><h3>Optimal</h3></div>', unsafe_allow_html=True)

    st.markdown("---")
    
    # Row 2: Charts Interaktif (Simulasi Plotly/Native Streamlit)
    st.subheader("📈 Proyeksi Arus Kas (Interaktif)")
    df = pd.DataFrame({
        'Bulan': ['Jan', 'Feb', 'Mar', 'Apr'],
        'Cash Flow': [100, 125, 110, 150]
    }).set_index('Bulan')
    
    # Menggunakan Native Chart yang responsif (Otomatis menyesuaikan container width)
    st.area_chart(df, color="#0D47A1", use_container_width=True)
    st.info("💡 Tip: Hover pada grafik untuk melihat detail nilai per bulan.")

elif menu == "⚙️ Pengaturan AI":
    st.subheader("⚙️ Konfigurasi Mesin Deteksi AI")
    
    # Require-role guard
    if check_admin_access():
        sensitivity = st.slider("Sensitivitas AI (Threshold):", 0.0, 1.0, 0.85)
        st.write(f"Sensitivitas saat ini diatur pada: **{sensitivity}**")
        if st.button("Simpan Perubahan"):
            st.success("Konfigurasi berhasil diperbarui oleh Admin.")

# --- 6. FOOTER ---
st.write("---")
st.caption("© 2026 V-Guard AI
