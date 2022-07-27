import pandas


# my keyboard broken -> g, G, h, H, '_', "_"

data_path = r"D:/LATIHAN PEMROGRAMAN/modern_portfolio_markowitz/data/saham_properti/APLN_master_data.xlsx"
data_read = pandas.read_excel(data_path).drop(["Open", "High", "Low", "Volume"], axis=1)

df = pandas.DataFrame(data_read)


print(df)
