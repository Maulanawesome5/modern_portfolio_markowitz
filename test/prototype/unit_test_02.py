import numpy
import pandas


# my keyboard broken -> g, G, h, H, '_', "_"

data_path = r"D:/LATIHAN PEMROGRAMAN/modern_portfolio_markowitz/data/emiten_properti.xlsx"
data_read = pandas.read_excel(data_path)

df = pandas.DataFrame(data_read)


print(df)

# Index(['Date', 'APLN', 'ASRI', 'BAPA', 'BKSL', 'BSDE', 'CTRA', 'DART', 'DMAS', 
# 'DUTI', 'GWSA', 'JRPT', 'LPKR', 'LPLI', 'PPRO', 'PWON', 'SMRA'], dtype='object')
kunci = df.keys()  # akses index
banyak_data = len(df)  # banyak data 1323, tipe data int
daftar_index = [key for key in kunci.drop(["Date"])]
banyak_index = len(daftar_index)  # jumlah list ticker saham, ada 16 ticker

