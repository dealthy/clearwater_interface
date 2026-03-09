import geopandas as gpd
import pandas as pd

shp_path = "cleaneddata/CWC All Props One Layer.shp"
csv_path = "HarryYu_CWC_attributes_cleaned.csv"

gdf = gpd.read_file(shp_path)
df = pd.read_csv(csv_path)

gdf = gdf.merge(df, on = "id", how = "left")

# print(len(gdf))

#gdf.insert(0, "id", range(1, len(gdf) + 1))
# print(gdf.head())

gdf.to_file(shp_path)

gdf.drop(columns="geometry").to_csv("attribute_table.csv", index=False)

