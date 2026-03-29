from PIL import Image

# Di bagian Sidebar
with st.sidebar:
    # Ganti 'profil_erwin.jpg' sesuai nama file yang Anda upload
    foto_profil = Image.open('profil_erwin.jpg') 
    st.image(foto_profil, width=120)
    st.markdown("<center>Erwin Sinaga</center>", unsafe_allow_html=True)

# Di bagian Landing Page (Filosofi Kami)
c1, c2 = st.columns([1, 2])
with c1:
    st.image(foto_profil, width=300)
