from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress

# Folder of this project: the CSV is read from it and the chart is saved
# in it, no matter which folder the script is run from.
BASE_DIR = Path(__file__).resolve().parent

# Read data from file
df = pd.read_csv(BASE_DIR / 'epa-sea-level.csv')


def draw_plot():
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=15, label='Data')

    # Create first line of best fit using all data, extended to the year 2050
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = pd.Series(range(int(df['Year'].min()), 2051))
    ax.plot(
        years,
        result.intercept + result.slope * years,
        color='red',
        label='Best fit: 1880-2013',
    )

    # Create second line of best fit using data from year 2000 onward
    df_2000 = df[df['Year'] >= 2000]
    result_2000 = linregress(
        df_2000['Year'],
        df_2000['CSIRO Adjusted Sea Level'],
    )
    years_2000 = pd.Series(range(2000, 2051))
    ax.plot(
        years_2000,
        result_2000.intercept + result_2000.slope * years_2000,
        color='green',
        label='Best fit: 2000-2013',
    )

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save the chart in the project folder and return the axes (used by tests)
    fig.savefig(BASE_DIR / 'sea_level_plot.png')
    return ax
draw_plot()