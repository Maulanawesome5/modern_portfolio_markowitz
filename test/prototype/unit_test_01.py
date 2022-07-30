import pandas as pd


# my keyboard broken -> g, G, h, H, '_', "_"

# akses data
data_path_01 = r"D:/LATIHAN PEMROGRAMAN/modern_portfolio_markowitz/data/saham_properti/APLN_master_data.xlsx"
data_path_02 = r"D:/LATIHAN PEMROGRAMAN/modern_portfolio_markowitz/data/saham_properti/CTRA_master_data.xlsx"

data_read_01 = pd.read_excel(data_path_01).drop(["Open", "High", "Low", "Volume"], axis=1)
data_read_02 = pd.read_excel(data_path_02).drop(["Open", "High", "Low", "Volume"], axis=1)


# Menambahkan prefix supaya bisa di join
data_read_01 = data_read_01.add_prefix("APLN_")
data_read_02 = data_read_02.add_prefix("CTRA_")


# Membuat dataframe
df = pd.DataFrame(data_read_01).join(data_read_02.drop(["CTRA_Date"], axis=1))
print(df)
