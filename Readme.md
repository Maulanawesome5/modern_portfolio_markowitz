# PENGANTAR

---
**NOTE** :
Repository ini merupakan remake dari repo sebelumnya. Karena alasan manajemen program yang tidak teratur, dan mata kuliah untuk project ini sudah berakhir, maka saya putuskan untuk melakukan remake dengan tujuan untuk di pakai skripsi.

---

Repository ini dibuat sebagai program *machine learning* dalam bidang financial market, yaitu teori portofolio modern (*modern portfolio theory*) model markowitz. Teori ini pertama kali diperkenalkan oleh seorang ilmuwan bernama Harry Markowitz pada tahun 1952 melalui suatu makalah berjudul *Portfolio Selection* yang diterbitkan pada Journal of Finance.

MPT bekerja dengan asumsi bahwa investor enggan mengambil resiko, investor lebih memilih portofolio dengan resiko lebih rendah untuk tingkat pengembalian tertentu. Berdasarkan asumsi ini, investor hanya akan melakukan investasi beresiko tinggi jika mereka dapat mengharapkan return yang lebih besar.

## DATA SOURCE

Data financial market berupa file csv dan excel yang ada di dalam repository ini saya peroleh melalui laman <https://www.investing.com> (untuk WTI, XBR, XAU, XAG) sedangkan untuk data harga saham saya peroleh melalui <https://finance.yahoo.com> karena kedua laman ini lah yang menyediakan data yang bisa diakses secara gratis.

## DATA SOURCE DISCLAIMER

Disclaimer: Fusion Media would like to remind you that the data contained in this website is not necessarily real-time nor accurate. All derived (stocks, indexes, futures), cryptocurrencies, and Forex prices are not provided by exchanges but rather by market makers, and so prices may not be accurate and may differ from the actual market price, meaning prices are indicative and not appropriate for trading purposes. Therefore Fusion Media doesn't bear any responsibility for any trading losses you might incur as a result of using this data.
Fusion Media or anyone involved with Fusion Media will not accept any liability for loss or damage as a result of reliance on the information including data, quotes, charts and buy/sell signals contained within this website. Please be fully informed regarding the risks and costs associated with trading the financial markets, it is one of the riskiest investment forms possible.

## REFERENSI DAN TUTORIAL

1. Web
    * <https://faq.bibit.id/id/article/apa-itu-modern-portfolio-theory-ge80pt/>
    * <https://belajarpython.com/tutorial/akses-database-python#>
    * <https://www.idxchannel.com/economics/teori-portofolio-markowitz-risiko-dianggap-masalah-oleh-investor>
    * <https://ajaib.co.id/apa-itu-standar-deviasi-dan-hubungannya-dengan-investasi/>
    * <https://yefadvisor.com/cara-menghitung-expected-return-portofolio/>
    * <http://www.bigbrothersinvestment.com/detailpost/teori-portofolio-investasi-modern-markowitz>
    * <https://pluang.com/id/blog/resource/teknik-diversifikasi-investasi-markowitz>

2. Youtube (coming soon)
3. Jurnal (coming soon)
4. Buku (coming soon)

## PYTHON MODULE AND PACKAGE

Program ini saya tulis menggunakan bahasa pemrograman Python, karena memang Python cukup mudah dipelajari serta didukung oleh banyak modul yang berguna untuk machine learning, data science, dan khususnya financial market sebagai topik utama yang saya buat. Dibawah ini adalah modul dan package yang mungkin harus diinstal pada PC/laptop sebelum bisa mengeksekusi semua program pada repository ini.

1. pymysql
    > PyMySQL adalah sebuah antarmuka untuk menghubungkan ke server database MySQL dari Python. Ini mengimplementasikan API Database Python v2.0 dan berisi perpustakaan klien MySQL murni-Python. Tujuan PyMySQL adalah penggantian drop-in untuk MySQLdb.

2. pandas-datareader
    > Pandas Datareader is a Python package that allows us to create a pandas DataFrame object by using various data sources from the internet. It is popularly used for working with realtime stock price datasets.

3. matplotlib
    > Matplotlib adalah pustaka plot untuk bahasa pemrograman Python dan ekstensi matematika numeriknya NumPy. Ini menyediakan API berorientasi objek untuk menyematkan plot ke dalam aplikasi menggunakan toolkit GUI tujuan umum seperti Tkinter, wxPython, Qt, atau GTK.

4. pandas
    > Pandas adalah perpustakaan perangkat lunak yang ditulis untuk bahasa pemrograman Python untuk manipulasi dan analisis data. Secara khusus, ia menawarkan struktur data dan operasi untuk memanipulasi tabel numerik dan deret waktu. Ini adalah perangkat lunak gratis yang dirilis di bawah lisensi BSD tiga klausa.

5. numpy
    > NumPy adalah sebuah pustaka untuk bahasa pemrograman Python, NumPy memberikan dukungan untuk himpunan dan matriks multidimensi yang besar, dan dilengkapi koleksi sejumlah besar fungsi matematika tingkat tinggi untuk beroperasi pada himpunan ini.

## "Next line"
