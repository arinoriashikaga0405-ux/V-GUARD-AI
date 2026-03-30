import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- 1. PERFORMANCE OPTIMIZATION (CACHING) ---
st.set_page_config(page_title="V-Guard AI | Fast Insights", page_icon="🛡️", layout="wide")

@st.cache_data(ttl=3600)  # Cache data selama 1 jam untuk load <1 detik
def get_optimized_data():
    """Simulasi load data besar yang sudah di-cache."""
    return pd.DataFrame({
        'Tanggal': pd.date_range(start='2026-03-01', periods=10),
        'Cash_Flow': [100, 120, 115, 140, 130, 160, 155, 180, 175, 200],
        'Risiko_Skor': [0.1, 0.2, 0.15, 0.6, 0.2, 0.1, 0.8, 0.2, 0.1, 0.15]
    })

# --- 2. UI/UX: CUSTOM STYLING & MOBILE OPTIMIZATION ---
st.markdown("""
<style>
    /* Desain Centered on Decisions */
    .stApp { background-color: #FFFFFF; }
    [data-testid="stSidebar"] { background-color: #0D47A1; }
    .decision-card {
        background: #F0F7FF; padding: 20px; border-radius: 12px;
        border-left: 5px solid #0D47A1; margin-bottom: 20px;
    }
    /* Mobile optimization: Perkecil padding di layar kecil */
    @media (max-width: 600px) { .main .block-container { padding: 10px; } }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGASI & DARK MODE SIMULATION ---
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    st.write(f"Eksekutif: **Erwin Sinaga**")
    st.markdown("---")
    page = st.radio("Menu Center:", ["📊 Dashboard", "⚙️ Pengaturan AI", "📜 Audit Log"])
    dark_mode = st.toggle("🌙 Dark Mode (Beta)")
    st.markdown("---")
    st.caption("v2.6.0 - Production Ready")

# --- 4. DASHBOARD UTAMA (INTERAKTIF & FAST) ---
if page == "📊 Dashboard":
    st.header("Decision Support System")
    
    # Decision Card (Focus on Action)
    st.markdown("""
    <div class="decision-card">
        <h4 style="margin:0; color:#0D47A1;">⚠️ Rekomendasi Tindakan</h4>
        <p style="margin:0;">Ditemukan 1 anomali transaksi (TX-99). Segera verifikasi vendor "Unknown Corp" untuk mencegah loss.</p>
    </div>
    """, unsafe_allow_html=True)

    # Load Data dengan Spinner
    with st.spinner("Memuat data cepat..."):
        df = get_optimized_data()

    # Plotly Interaktif (Zoom/Hover)
    fig = px.area(df, x='Tanggal', y='Cash_Flow', title="Tren Arus Kas (Interaktif)",
                  color_discrete_sequence=['#0D47A1'])
    fig.update_layout(hovermode="x unified", margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig, use_container_width=True)

    # Filter Dinamis & Drill-down
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Filter Risiko")
        min_risk = st.slider("Ambang Batas Skor Risiko", 0.0, 1.0, 0.5)
        filtered_df = df[df['Risiko_Skor'] >= min_risk]
        st.write(f"Menampilkan {len(filtered_df)} transaksi di atas ambang batas.")

    with col2:
        st.subheader("Detail Transaksi")
        st.dataframe(filtered_df, use_container_width=True)

# --- 5. FOOTER ---
st.write("---")
st.caption(f"© 2026 V-Guard AI | Optimasi Performa & UX untuk UMKM Indonesia")
