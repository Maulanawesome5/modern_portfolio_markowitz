import pandas


# my keyboard broken -> g, G, h, H, '_', "_"

data_path = r"D:/LATIHAN PEMROGRAMAN/modern_portfolio_markowitz/data/emiten_properti.xlsx"
data_read = pandas.read_excel(data_path)

df = pandas.DataFrame(data_read)


print(df)
