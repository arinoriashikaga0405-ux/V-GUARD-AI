# Potongan kode untuk bagian Profil Kepemimpinan
if nav == "Profil Kepemimpinan & ROI":
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga — Founder")
    with col2:
        with st.container(border=True):
            st.write("""
            Bapak **Erwin Sinaga** adalah sosok **Founder** di balik **V-Guard AI Intelligence**, 
            sebuah platform inovatif yang lahir dari dedikasi mendalam terhadap keamanan 
            aset dan transparansi bisnis. Beliau memiliki rekam jejak profesional yang 
            prestisius selama lebih dari satu dekade, menempati berbagai posisi strategis 
            dan manajerial senior di industri perbankan serta manajemen aset nasional. 
            Pengalaman panjang tersebut telah membentuk ketajaman analitis beliau dalam 
            mengidentifikasi berbagai pola risiko finansial dan celah operasional yang 
            sering kali luput dari sistem pengawasan konvensional.

            Di bawah visi kepemimpinannya, V-Guard AI dikembangkan bukan sekadar sebagai 
            alat audit, melainkan sebagai benteng pertahanan digital bagi para pengusaha. 
            Beliau sangat memahami bahwa integritas data dan perlindungan modal adalah 
            fondasi utama bagi keberlanjutan bisnis di era digital yang penuh tantangan. 
            Berdomisili di Tangerang, beliau aktif menjembatani kebutuhan dunia usaha 
            dengan solusi teknologi kecerdasan buatan yang aplikatif dan efisien. Fokus 
            utama beliau adalah memberikan ketenangan pikiran bagi pemilik usaha melalui 
            sistem audit real-time yang mampu meminimalisir potensi kerugian secara 
            signifikan. Bapak Erwin dikenal sebagai pemimpin yang visioner, disiplin, 
            dan memiliki komitmen tanpa kompromi dalam membantu bisnis mencapai standar 
            tata kelola yang bersih, aman, dan berkelanjutan.
            """)
