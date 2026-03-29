import streamlit as st

# 1. Judul di Tab Browser
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️")

# 2. Branding Utama di Halaman Depan
st.title("🛡️ VGUARD AI Systems")
st.markdown("### *Intelligence for Your Business Security*")

# 3. Deskripsi Singkat di Menu "Tentang Kami"
st.info("""
**VGUARD AI Systems** adalah platform audit digital dan keamanan operasional 
berbasis Kecerdasan Buatan (AI). Kami membantu pengusaha di Indonesia 
mengamankan aset dan mencegah kerugian secara sistemik.
""")

# 4. Update Nama di Daftar Produk
with st.container():
    st.write("---")
    st.write("#### Katalog Layanan VGUARD AI Systems")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("**V-START**")
        st.caption("Entry Level Security")
    with col2:
        st.warning("**V-GROW**")
        st.caption("Operational Control")
    with col3:
        st.error("**V-PRIME**")
        st.caption("Strategic Audit")
