import streamlit as st
from sqlalchemy import text

list_jenis_kelamin = ['', 'Pria', 'Wanita']
list_divisi = ['', 'Personalia', 'Keuangan', 'Pemasaran', 'Produksi']
list_jabatan =['', 'Kepala Divisi', 'Karyawan Tetap','Karyawan Magang']
conn = st.connection("postgresql", type="sql", 
                     url="postgresql://nurhaliza0601:lhiIofE8Y2we@ep-raspy-salad-19174195.ap-southeast-1.aws.neon.tech/fpmbd")#diganti akun masing2

st.header('DATABASE PEMBAYARAN GAJI BULANAN KARYAWAN')#ganti judul
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM gajian ORDER By id;', ttl="0").set_index('id') #ganti nama tabel
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO gajian (nama_karyawan, id_karyawan, jenis_kelamin, divisi, jabatan, gaji, uang_lembur, waktu_transfer,tanggal_transfer) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'', '5':'', '6':'', '7':'', '8':None, '9':None})#ganti isi tabel dan tipe nya
            session.commit()

    data = conn.query('SELECT * FROM gajian ORDER By id;', ttl="0")
    for _, result in data.iterrows():        #ganti seluruh variabel, biarkan id tetap ada
        id = result['id']
        nama_karyawan_lama = result["nama_karyawan"]
        id_karyawan_lama = result["id_karyawan"]
        jenis_kelamin_lama = result["jenis_kelamin"]
        divisi_lama = result["divisi"]
        jabatan_lama = result["jabatan"]
        gaji_lama = result["gaji"]
        uang_lembur_lama = result["uang_lembur"]
        waktu_transfer_lama = result["waktu_transfer"]
        tanggal_transfer_lama = result["tanggal_transfer"]

        with st.expander(f'a.n. {nama_karyawan_lama}'):
            with st.form(f'data-{id}'):
                nama_karyawan_baru =  st.text_input("nama_karyawan", nama_karyawan_lama)
                id_karyawan_baru = st.text_input("id_karyawan", id_karyawan_lama)
                jenis_kelamin_baru = st.selectbox("jenis_kelamin", list_jenis_kelamin, list_jenis_kelamin.index(jenis_kelamin_lama))
                divisi_baru = st.selectbox("divisi", list_divisi, list_divisi.index(divisi_lama))
                jabatan_baru = st.selectbox("jabatan", list_jabatan, list_jabatan.index(jabatan_lama))
                gaji_baru = st.text_input("gaji", gaji_lama)
                uang_lembur_baru = st.text_input("uang_lembur", uang_lembur_lama)
                waktu_transfer_baru = st.time_input("waktu_transfer", waktu_transfer_lama)
                tanggal_transfer_baru = st.date_input("tanggal_transfer", tanggal_transfer_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE schedule \
                                          SET nama_karyawan=:1, id_karyawan=:2, jenis_kelamin=:3, divisi=:4, \
                                          jabatan=:5, gaji=:6, uang_lembur=:7, waktu_transfer=:8, tanggal_transfer=:9 \
                                          WHERE id=:10;')
                            session.execute(query, {'1':nama_karyawan_baru, '2':id_karyawan_baru, '3':jenis_kelamin_baru, '4':divisi_baru, 
                                                    '5':jabatan_baru, '6':gaji_baru, '7':uang_lembur_baru, '8':waktu_transfer_baru, '9':tanggal_transfer_baru, '10':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM gajian WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()