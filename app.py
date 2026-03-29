import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM (ALAT KERJA VISUAL) ---
st.markdown("""
    <style>
    .main { background-color: #f1f5f9; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; white-space: pre-wrap; background-color: #f8fafc;
        border-radius: 10px 10px 0 0; gap: 0; padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] { background-color: #1e3a8a !important; color: white !important; }
    .work-card {
        background-color: white; padding: 20px; border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); border-left: 5px solid #1e3a8a;
        margin-bottom: 15px;
    }
    .status-urgent { color: #ef4444; font-weight: bold; background: #fee2e2; padding: 2px 8px; border-radius: 4px; }
    .status-safe { color: #10b981; font-weight: bold; background: #dcfce7; padding: 2px 8px; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    try: st.image("erwin.jpg", width=100)
    except: st.info("👤 CEO: ERWIN")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI")
    if st.button("🏠 Beranda Utama"):
        st.session_state.page = "Home"
        st.rerun()

# --- 4. LOGIKA NAVIGASI ---
if st.session_state.page == "Admin":
    st.title("💻 Command Center - Alat Kerja Audit")
    
    # ALAT KERJA 1: TABS OPERASIONAL
    tab1, tab2, tab3 = st.tabs(["🔥 Fraud Detection", "💰 Monitoring Piutang (AR)", "📈 Laporan Eksekutif"])
    
    with tab1:
        st.subheader("🛡️ Alat Deteksi Fraud")
        st.error("🚨 [ALARM] Terdeteksi 1 Transaksi Mencurigakan: Store 01 - Void Tidak Wajar")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔍 Investigasi Detail"):
                st.info("Membuka rekaman CCTV & Log Kasir...")
        with col2:
            if st.button("🔔 Kirim Fire Alarm ke WhatsApp"):
                st.success("Notifikasi dikirim ke Owner!")

    with tab2:
        st.subheader("💸 Alat Kontrol Piutang (AR)")
        st.write("Daftar Piutang Jatuh Tempo Mendatang:")
        
        # ALAT KERJA NYATA: DATAFLOW PIUTANG
        ar_list = [
            {"klien": "PT. Niaga Sakti", "nilai": "Rp 75.000.000", "tempo": "Besok", "status": "Urgent"},
            {"klien": "Toko Berkah", "nilai": "Rp 12.000.000", "tempo": "3 Hari lagi", "status": "Safe"},
            {"klien": "CV. Media Tech", "nilai": "Rp 34.500.000", "tempo": "Hari Ini", "status": "Urgent"}
        ]
        
        for item in ar_list:
            status_class = "status-urgent" if item["status"] == "Urgent" else "status-safe"
            st.markdown(f"""
                <div class="work-card">
                    <div style="display:flex; justify-content:space-between;">
                        <b>{item['klien']}</b>
                        <span class="{status_class}">{item['status']}</span>
                    </div>
                    <div style="font-size: 1.2rem; margin: 10px 0;">{item['nilai']}</div>
                    <div style="font-size: 0.8rem; color: #64748b;">Jatuh Tempo: {item['tempo']}</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"📲 Kirim Tagihan ke {item['klien']}", key=item['klien']):
                st.success(f"Reminder Tagihan untuk {item['klien']} Terkirim!")

    with tab3:
        st.subheader("📊 Summary Profit")
        st.bar_chart({"Jan": 100, "Feb": 120, "Mar": 150})

else:
    # --- HALAMAN DEPAN ---
    st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>🛡️ VGUARD AI SYSTEMS</h1>", unsafe_allow_html=True)
    st.info("Saya **Erwin**, membawa **10 tahun pengalaman perbankan** untuk memastikan integritas aset Anda.")
    
    if st.button("🚀 MASUK KE ALAT KERJA ADMIN"):
        st.session_state.page = "Admin"
        st.rerun()

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin")
