drop table if exists gajian;
create table gajian (
	id serial,
	nama_karyawan text,
	id_karyawan text,
	jenis_kelamin text,
	divisi text,
	jabatan text,
	gaji text,
	uang_lembur text,
	waktu_transfer time,
	tanggal_transfer date
);

insert into gajian (nama_karyawan, id_karyawan, jenis_kelamin, divisi, jabatan, gaji, uang_lembur, waktu_transfer, tanggal_transfer) 
values
	('Sigit', 22004,'Pria','Personalia', 'Karyawan Tetap', 4000000, 150000, '08:00', '2023-10-01'),
	('Rara',19005, 'Wanita', 'Pemasaran','Kepala Divisi',10000000,500000, '09:00', '2022-10-02')
	;