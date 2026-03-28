# --- DESIGN WEBSITE V-GUARD MOBILE RESPONSIVE ---
st.markdown("""
<style>
    /* Mengatur latar belakang agar bersih */
    .main {
        background-color: #f0f2f6;
    }
    
    /* Membuat tampilan kartu data lebih modern di HP */
    [data-testid="stMetric"] {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #e1e4e8;
        margin-bottom: 10px;
    }

    /* Memperbesar tombol agar mudah ditekan jari (Touch Friendly) */
    div.stButton > button {
        background-color: #004a99;
        color: white;
        border-radius: 10px;
        height: 3.5em;
        width: 100%;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Menghilangkan padding berlebih di HP agar layar lebih luas */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    /* Tulisan Header yang lebih elegan */
    h1 {
        font-size: 1.8rem !important;
        color: #1e3a8a;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)
