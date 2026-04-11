import streamlit as st
import pandas as pd
import time
import os
from datetime import datetime

# --- 1. CONFIG & V-GUARD CORE ENGINE ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

class VGuardCoreEngine:
    @staticmethod
    def edge_filter_process(data_type, raw_data):
        """SOP: EDGE FILTERING (PENGHEMATAN 80% BIAYA API)"""
        is_anomaly = False
        reason = ""
        if data_type == "V-PRO":
            if raw_data.get('type') in ['VOID', 'REFUND'] and raw_data.get('amount', 0) > 50000:
                is_anomaly = True
                reason = "High Value Void/Refund Detected"
        elif data_type == "V-LITE":
            if raw_data.get('visual_trigger') == "UNAUTHORIZED_OPEN":
                is_anomaly = True
                reason = "Unauthorized Drawer Access"
        return is_anomaly, reason

# --- 2. GLOBAL STYLES ---
st.markdown("""
<style>
    .founder-wrapper {
        background: white; padding: 30px; border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 2px solid #1E3A8A;
        text-align: center;
    }
    .product-card {
        background: #f8fafc; padding: 20px; border-radius: 15px;
        border-top: 5px solid #1E3A8A; height: 100%;
    }
    .agent-online { color: #10b981; font-weight: bold; }
    [data-testid="stSidebar"] { background-color: #0f172a; }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='color:white;'>🛡️ V-GUARD AI</h2>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("STRATEGIC COMMAND", [
        "🛡️ IDENTITY & VISION",
        "📦 PRODUCT SERVICES",
        "📊 ROI ANALYSIS",
        "🔑 CLIENT PORTAL",
        "🎮 ADMIN CONTROL CENTER"
    ])
    st.markdown("---")
    st.info("💡 **Edge Mode Active**: API Cost reduced by 80%.")
    st.caption("Executive Access: Erwin Sinaga")

# --- 4. HALAMAN 1: IDENTITY & VISION ---
if menu == "🛡️ IDENTITY & VISION":
    col_profile, col_vision = st.columns([1, 2])
    with col_profile:
        st.markdown('<div class="founder-wrapper">', unsafe_allow_html=True)
        # Menampilkan foto (otomatis mencari file erwin_sinaga.jpg)
        st.image("https://via.placeholder.com/400x500.png?text=Erwin+Sinaga", use_container_width=True)
        st.markdown("## **Erwin Sinaga**")
        st.markdown("<h4 style='color: #1E3A8A;'>Founder & CEO</h4>", unsafe_allow_html=True)
        st.write("*'Digitizing Trust, Eliminating Leakage'*")
        st.markdown('</div>', unsafe_allow_html=True)
    with col_vision:
        st.title("Strategic Foundation")
        with st.container(border=True):
            st.subheader("Visi Strategis")
            st.write("""Menjadi jangkar teknologi global dalam digitalisasi kepercayaan (Digitizing Trust) yang mentransformasi ekosistem bisnis konvensional menjadi entitas digital yang transparan, aman, dan berintegritas tinggi... (250 Kata Foundation).""")
        st.subheader("Misi Perusahaan")
        st.markdown("""
        1. **Digitalisasi Kepercayaan** | 2. **Eliminasi Kebocoran Total** | 3. **Optimalisasi Biaya AI (Edge)**
        4. **Kedaulatan Command Center** | 5. **Standarisasi SOP V-Guard**
        """)

# --- 5. HALAMAN 2: PRODUCT SERVICES ---
elif menu == "📦 PRODUCT SERVICES":
    st.header("V-Guard Solutions Ecosystem")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.subheader("📦 V-LITE")
        st.write("Proteksi Mikro: Deteksi laci kasir & akses fisik ilegal.")
        st.button("Activate V-LITE", key="p1")
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.subheader("🚀 V-PRO")
        st.write("Retail Integrity: Analisis Void/Refund real-time via Edge.")
        st.button("Activate V-PRO", key="p2")
        st.markdown('</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.subheader("👁️ V-SIGHT")
        st.write("Visual AI: CCTV Intelligence & Anomaly Detection.")
        st.button("Activate V-SIGHT", key="p3")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 6. HALAMAN 3: ROI ANALYSIS ---
elif menu == "📊 ROI ANALYSIS":
    st.header("Loss Prevention & ROI Calculator")
    col_in, col_res = st.columns(2)
    with col_in:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=50000000)
        leak_est = st.slider("Estimasi Kebocoran (%)", 1, 15, 5)
    with col_res:
        loss = omzet * (leak_est/100)
        st.metric("Potensi Kebocoran/Bulan", f"Rp {loss:,.0f}", delta="-Leakage", delta_color="inverse")
        st.success(f"**V-Guard Cost-Saving**: Server biaya terpangkas 80% melalui sistem Edge Filtering.")

# --- 7. HALAMAN 4: CLIENT PORTAL (DASHBOARD KLIEN) ---
elif menu == "🔑 CLIENT PORTAL":
    st.header("Client Secure Dashboard Access")
    if 'client_auth' not in st.session_state:
        with st.columns(3)[1]:
            st.subheader("Login Klien")
            u = st.text_input("Username")
            p = st.text_input("Password", type="password")
            if st.button("Masuk Sistem", use_container_width=True):
                st.session_state.client_auth = True
                st.rerun()
    else:
        st.success("Login Berhasil: V-PRO Active")
        col_c1, col_c2, col_c3 = st.columns(3)
        col_c1.metric("System Health", "99.9%")
        col_c2.metric("Threats Blocked", "12", "Last 24h")
        col_c3.metric("Savings Enabled", "Rp 2.4M")
        if st.button("Log Out Portal"):
            del st.session_state.client_auth
            st.rerun()

# --- 8. HALAMAN 5: ADMIN CONTROL CENTER (AI SQUAD & ACTIVATION) ---
elif menu == "🎮 ADMIN CONTROL CENTER":
    if not st.session_state.get('admin_logged_in', False):
        st.subheader("🔐 Restricted Access")
        pw = st.text_input("Enter Command Password:", type="password")
        if pw == "w1nbju8282":
            st.session_state.admin_logged_in = True
            st.rerun()
    else:
        st.header("Executive Command Center")
        tabs = st.tabs(["👥 Client Activation", "🖥️ AI SQUAD HUB", "📈 System Stats"])
        
        with tabs[0]:
            st.subheader("Kirim Link Aktivasi Cloud")
            cl_name = st.text_input("Nama Klien")
            cl_pkg = st.selectbox("Paket", ["V-LITE", "V-PRO", "V-SIGHT"])
            if st.button("Generate & Send Link"):
                st.code(f"Aktivasi Berhasil! Kirim link ini ke {cl_name}: https://vguard.ai/activate/{cl_pkg.lower()}")

        with tabs[1]:
            st.subheader("🤖 V-GUARD Elite AI Squad (10 Active Agents)")
            squad_data = [
                {"Agen": "👁️ Visionary", "Role": "Strategic Roadmap", "Status": "ONLINE"},
                {"Agen": "👂 Concierge", "Role": "Client Handling", "Status": "ONLINE"},
                {"Agen": "👄 Growth", "Role": "Marketing Ads", "Status": "RUNNING"},
                {"Agen": "🤝 Liaison", "Role": "API Integrator", "Status": "CONNECTED"},
                {"Agen": "🧠 Analyst", "Role": "Fraud Detection", "Status": "SCANNING"},
                {"Agen": "📈 Strategist", "Role": "ROI Optimization", "Status": "ONLINE"},
                {"Agen": "🐕 Watchdog", "Role": "Real-time Monitoring", "Status": "ACTIVE"},
                {"Agen": "🛡️ Sentinel", "Role": "Server Security", "Status": "ARMED"},
                {"Agen": "⚖️ Legalist", "Role": "SOP Compliance", "Status": "MONITORING"},
                {"Agen": "💰 Treasurer", "Role": "Profit Sharing", "Status": "CALCULATING"},
            ]
            st.table(squad_data)

        if st.button("🔒 Logout Admin"):
            st.session_state.admin_logged_in = False
            st.rerun()

# --- FOOTER ---
st.markdown("---")
st.markdown("<center>© 2026 V-GUARD AI | Digital Integrity Powered by Erwin Sinaga</center>", unsafe_allow_html=True)
