# import dataset
import pandas as pd

df = pd.read_csv(
    r"C:/Users/LENOVO/OneDrive/Desktop/Binar Academy-Data Science Bootcamp/data/covid-time-series-indonesia.csv"
)

# seperate dataset into two (for provinces only and for whole Indonesia)
df_indonesia = df[df["Location"] == "Indonesia"].reset_index(drop=True).copy()
df_indonesia = df_indonesia.drop(
    ["City or Regency", "Province", "Island", "Time Zone", "Special Status"], axis=1
)
df_indonesia = df_indonesia.fillna(0.0)

df_provinces = df[df["Location"] != "Indonesia"].reset_index(drop=True).copy()
df_provinces = df_provinces.drop(
    [
        "City or Regency",
        "Special Status",
        "Growth Factor of New Cases",
        "Growth Factor of New Deaths",
    ],
    axis=1,
)
df_provinces = df_provinces.fillna(0.0)

# convert df to csv
df_indonesia.to_csv(
    r"C:/Users/LENOVO/OneDrive/Desktop/Binar Academy-Data Science Bootcamp/data/Data Covid Indonesia.csv",
    encoding="utf-8-sig",
    index=False,
)
df_provinces.to_csv(
    r"C:/Users/LENOVO/OneDrive/Desktop/Binar Academy-Data Science Bootcamp/data/Data Covid Provinsi.csv",
    encoding="utf-8-sig",
    index=False,
)
