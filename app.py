import streamlit as st
import pandas as pd
import plotly.express as px

# 1. OPTIMASI PERFORMA (Caching Data Statis)
@st.cache_data
def get_static_data():
    return {
        "Mikro": {"S": "2.5jt", "B": "750rb", "F": ["Monitoring Real-time", "Limit 1rb Tx"]},
        "Menengah": {"S": "7.5jt", "B": "2.5jt", "F": ["WA Alert", "Advanced AI", "Limit 5rb Tx"]},
        "Enterprise": {"S": "50jt", "B": "8.5jt", "F": ["ERP Integration", "AI CCTV Basic"]},
        "Corporate": {"S": "85jt", "B": "15jt", "F": ["AI CCTV Face Recog", "CSO Advisory"]}
    }

# 2. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI | Secure Dashboard", page_icon="🛡️", layout="wide")

# 3. SESSION STATE & LOGIN
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI SECURE GATE")
    pwd = st.text_input("Admin Access Code:", type="password")
    if st.button("Authorize Access"):
        if pwd == st.secrets.get("ADMIN_PASSWORD", "admin123"): # Fallback jika secrets belum set
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Access Denied.")
    st.stop()

# 4. SIDEBAR NAVIGATION
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
page = st.sidebar.selectbox("Main Menu", ["🏠 Overview", "📊 Live Monitoring", "💎 Investment Plans", "👤 Corporate Profile"])

# --- HALAMAN 1: OVERVIEW (Engagement) ---
if page == "🏠 Overview":
    st.title("Welcome, Pak Erwin Sinaga")
    st.markdown("### *Empowering Businesses Through Intelligent Protection*")
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Our Vision 2026")
        st.info("Menjadi standar keamanan finansial global berbasis AI yang adaptif dan proaktif.")
    with col2:
        st.subheader("Digital Trust")
        st.success("Sistem V-Guard telah memproteksi aset senilai Rp 500M+ di wilayah Tangerang & Jakarta.")

# --- HALAMAN 2: MONITORING (Interactive UI) ---
elif page == "📊 Live Monitoring":
    st.header("📊 Intelligence Ops Center")
    tab1, tab2 = st.tabs(["Risk Analysis", "Transaction Flow"])
    
    with tab1:
        df = pd.DataFrame({'Status': ['Safe', 'Flagged'], 'Count': [94, 6]})
        fig = px.pie(df, values='Count', names='Status', hole=0.5, color_discrete_sequence=['#2ecc71', '#e74c3c'])
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        st.info("Fitur Grafik Aliran Transaksi sedang dioptimalkan untuk integrasi API.")

# --- HALAMAN 3: PLANS (Dynamic & Persuasive) ---
elif page == "💎 Investment Plans":
    st.header("💎 Choose Your Shield")
    data = get_static_data()
    wa_num = "6282122190885"
    
    # Pricing Comparison Table (Dinamis)
    st.subheader("Comparison Matrix")
    compare_df = pd.DataFrame([
        {"Package": "Mikro", "Setup": "2.5jt", "Monthly": "750rb", "AI Level": "Basic"},
        {"Package": "Menengah", "Setup": "7.5jt", "Monthly": "2.5jt", "AI Level": "Intermediate"},
        {"Package": "Enterprise", "Setup": "50jt", "Monthly": "8.5jt", "AI Level": "Advanced"},
        {"Package": "Corporate", "Setup": "85jt", "Monthly": "15jt", "AI Level": "Expert (Custom)"}
    ])
    st.table(compare_df)

    cols = st.columns(4)
    for i, (name, detail) in enumerate(data.items()):
        with cols[i]:
            st.markdown(f"### {name}")
            st.metric("Monthly", detail['B'])
            st.write(f"**Setup: {detail['S']}**")
            for f in detail['F']:
                st.markdown(f"- {f}")
            
            msg = f"Halo Pak Erwin, saya tertarik paket {name}. Bisa diskusi?"
            url = f"https://wa.me/{wa_num}?text={msg.replace(' ', '%20')}"
            st.link_button(f"Pesan {name}", url, use_container_width=True, type="primary")

# --- HALAMAN 4: CORPORATE PROFILE ---
elif page == "👤 Corporate Profile":
    st.header("Strategic Leadership")
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", caption="Erwin Sinaga, CEO")
    with c2:
        st.markdown("#### Erwin Sinaga")
        st.markdown("*Senior Business Leader with 10+ years in Banking & Asset Management.*")
        st.write("Berdomisili di Tangerang, mengarahkan V-Guard AI untuk menjadi solusi 'End-to-End Intermediary' bagi dunia B2B.")

st.write("---")
st.caption("V-Guard AI Systems © 2026 | Secure Transactional Environment")
