import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

file_path = 'inform_data.csv'
top_n = 20
weight_natural = 1.0
weight_human = 1.0
weight_lack_of_coping = 1.0
weight_corruption = 1.0

data = pd.read_csv(file_path)

def calculate_harmonized_score(df, weight_natural, weight_human, weight_lack_of_coping, weight_corruption):
    df['Harmonized Score'] = (
        df['Natural'] * weight_natural +
        df['Human'] * weight_human +
        df['Lack of Coping Capacity'] * weight_lack_of_coping +
        df['Corruption'] * weight_corruption
    )
    return df

def get_top_countries(df, top_n, weight_natural, weight_human, weight_lack_of_coping, weight_corruption):
    df = calculate_harmonized_score(df, weight_natural, weight_human, weight_lack_of_coping, weight_corruption)
    top_countries = df[['Country', 'ISO3', 'Harmonized Score']].sort_values(by='Harmonized Score', ascending=False).head(top_n)
    return top_countries

top_countries = get_top_countries(data, top_n, weight_natural, weight_human, weight_lack_of_coping, weight_corruption)

print(top_countries)

world = gpd.read_file('ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')

# remove antarctica
world = world[world['CONTINENT'] != 'Antarctica']

world = world.merge(top_countries, how='left', left_on='ADM0_A3', right_on='ISO3')

fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.boundary.plot(ax=ax, linewidth=0.2, edgecolor='white')  
world.plot(column='Harmonized Score', ax=ax, legend=True, 
           legend_kwds={'label': f"Harmonized Score Range of Result Set", 'orientation': "horizontal"}, cmap='OrRd',
           missing_kwds={'color': 'lightgrey'}, linewidth=0.2, edgecolor='white') 
plt.title(f'Top {top_n} Countries by Harmonized Score')
plt.show()