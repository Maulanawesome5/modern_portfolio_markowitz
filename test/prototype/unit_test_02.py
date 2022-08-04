# Aplikasi ini untuk menguji penerapan mean-variance untuk
# emiten sektor properti.
# Data harga sudah diolah secara manual menggunakan microsoft excel
# karena dari kedua sumber data (investing dan yahoo)
# terdapat beberapa perbedaan.

# my keyboard broken -> g, G, h, H, '_', "_"

import numpy as np
import pandas as pd

data_path = r"D:/LATIHAN PEMROGRAMAN/modern_portfolio_markowitz/data/emiten_properti.xlsx"
data_read = pd.read_excel(data_path)

df = pd.DataFrame(data_read)
print(df)

# duplicate dataframe, include date column as index
df_copy = df.copy().set_index(keys="Date")


# Index(['Date', 'APLN', 'ASRI', 'BAPA', 'BKSL', 'BSDE', 'CTRA', 'DART', 'DMAS', 
# 'DUTI', 'GWSA', 'JRPT', 'LPKR', 'LPLI', 'PPRO', 'PWON', 'SMRA'], dtype='object')
kunci = df.keys()  # akses index
banyak_data = len(df)  # banyak data 1323, tipe data int
daftar_index = [key for key in kunci.drop(["Date"])]
banyak_index = len(daftar_index)  # jumlah list ticker saham, ada 16 ticker

# drop kolom tanggal supaya tidak di kalkulasi oleh numpy
df = df.drop(["Date"], axis=1)

# Covariance matrix
cov_matrix = df.pct_change().apply(lambda x: np.log(1 + x)).cov()
print(cov_matrix)

# Correlation matrix
corr_matrix = df.pct_change().apply(lambda x: np.log(1 + x)).corr()
print(corr_matrix)

# alokasi uang untuk investasi saham senilai Rp. 5.000.000
# 
# Ticker      Price        1 lot       total        lot_buy      total_buy       balance      allocation
# ______________________________________________________________________________________________________
# APLN        118     x     100    =   11.800    x    10    =      118.000  :   5.000.000  =  0,0236 ->  2.36 %
# BSDE       1020     x     100    =  102.000    x     5    =      510.000  :   5.000.000  =  0,102  -> 10.2  %
# DUTI       4090     x     100    =  409.000    x     4    =    1.636.000  :   5.000.000  =  0,3272 -> 32.72 %

weight_allocation = {'APLN':0.0236, 'ASRI':0.0204, 'BAPA':0.0108,
'BKSL':0.0162, 'BSDE':0.102, 'CTRA':0.104, 'DART':0.0488, 'DMAS':0.0222,
'DUTI':0.3272, 'GWSA':0.0148, 'JRPT':0.0492, 'LPKR':0.0262,
'LPLI':0.075, 'PPRO':0.052, 'PWON':0.06776, 'SMRA':0.0308}

# Portfolio variance
port_var = cov_matrix.mul(weight_allocation, axis=0).mul(weight_allocation, axis=1).sum().sum()
print(f"\nPortfolio variance = {port_var}")

# individual expected return
# individual_ExpectedReturn = df.resample('Y').last().pct_change().mean()
# print(f"\nEach shares gives a return")
# print(individual_ExpectedReturn)

print(df_copy)




