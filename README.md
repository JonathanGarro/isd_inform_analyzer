# Country Risk Assessment Visualization

## Overview

This tool helps calculate and visualize the harmonized risk scores of countries based on various risk factors. The harmonized score combines natural, human, coping capacity, and corruption risk factors to provide a comprehensive risk assessment. The top `n` countries with the highest harmonized scores are highlighted on a world map using `matplotlib`.

## Files

- `inform_data.csv`: Contains the risk data for the elements listed above. This is a simplified version of `inform_data.xlsx` which is also available in the repo, in case you want to adapt this using other INFORM categories.
- `ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp`: This is the shapefile used for the world map visualization.
- `Transparency International Corruption Index`: This isn't directly referenced by the script, but has been checked into the repo as this data has been imported into `inform_data.csv` since the requestor of this tool wanted that dimension added to the calculation, but isn't available in INFORM. Some manipulation of this data was necessary, including normalizing the values to match the 0-10 scale of INFORM.

## Dependencies

- `pandas`
- `geopandas`
- `matplotlib`

## Installation

To install the required libraries, you can create a virtual environment with `python3 -m venv venv`, activate it with `source venv/bin/activate`, then use pip:

```bash
pip install pandas geopandas matplotlib
```

## Usage

Assuming you're happy with the variables that have been pre-selected, all you have to do is configure the variables at the top of the script, including the number of countries you want to return, and weightings of each category. Then just run the file with `python3 inform_analyzer.py`