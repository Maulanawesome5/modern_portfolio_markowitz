USE saham_indonesia;
SHOW TABLES;

-- Membuat tabel notasi khusus
CREATE TABLE notasi_khusus (
    nomor_notasi INT(5) NOT NULL AUTO_INCREMENT,
    kode_notasi VARCHAR(1),
    deskripsi_notasi VARCHAR(100),
    PRIMARY KEY (nomor_notasi)
) ENGINE = InnoDB;

-- Modify struktur tabel
ALTER TABLE notasi_khusus
MODIFY deskripsi_notasi TEXT;

-- Akses data di tabel
SELECT * FROM notasi_khusus;
SHOW CREATE TABLE notasi_khusus;

-- Delete seluruh isi data di tabel
DROP TABLE notasi_khusus;  -- hapus permanen tabel
TRUNCATE notasi_khusus;  -- reset data tabel

-- Insert data ke tabel notasi khusus
INSERT INTO notasi_khusus (kode_notasi, deskripsi_notasi) VALUES
("B",   "Adanya permohonan Pernyataan Pailit"),
("M",   "Adanya permohonan Penundaan Kewajiban Pembayaran Utang (PKPU)"),
("E",   "Laporan keuangan terakhir menunjukkan ekuitas negatif"),
("A",   "Adanya Opini Tidak Wajar (Adverse) dari Akuntan Publik"),
("D",   "Adanya Opini “Tidak Menyatakan Pendapat (Disclaimer)” dari Akuntan Publik"),
("L",   "Perusahaan Tercatat belum menyampaikan laporan keuangan"),
("S",   "Laporan keuangan terakhir menunjukkan tidak ada pendapatan usaha"),
("C",   "Kejadian perkara hukum terhadap Perusahaan Tercatat, Anak Perusahaan Tercatat dan/atau anggota Direksi dan anggota Dewan Komisaris Perusahaan Tercatat yang berdampak Material"),
("Q",   "Pembatasan kegiatan usaha Perusahaan Tercatat dan/atau Anak Perusahaan Tercatat oleh regulator"),
("Y",   "Perusahaan Tercatat yang belum menyelenggarakan Rapat Umum Pemegang Saham Tahunan (RUPST) sampai dengan 6 (enam) bulan setelah tahun buku berakhir"),
("F",   "Sanksi Administratif dan/atau Perintah Tertulis dari OJK yang dikenakan terhadap Perusahaan Tercatat karena pelanggaran peraturan di bidang Pasar Modal dengan kategori Pelanggaran Ringan"),
("G",   "Sanksi Administratif dan/atau Perintah Tertulis dari OJK yang dikenakan terhadap Perusahaan Tercatat karena pelanggaran peraturan di bidang Pasar Modal dengan kategori Pelanggaran Sedang"),
("V",   "Sanksi Administratif dan/atau Perintah Tertulis dari OJK yang dikenakan terhadap Perusahaan Tercatat karena pelanggaran peraturan di bidang Pasar Modal dengan kategori Pelanggaran Berat"),
("X",   "Efek Bersifat Ekuitas Dalam Pemantauan Khusus"),
("N",   "Perusahaan Tercatat merupakan Emiten yang menerapkan Saham Dengan Hak Suara Multipel");




