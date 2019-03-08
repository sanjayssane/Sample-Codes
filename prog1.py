import pandas as pd

df = pd.read_csv("G:/Statistics (Python)/Datasets/RidingMowers.csv")

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

# Create the figure: p
p = figure(x_axis_label='Income', y_axis_label='Area Owned')

# Add a circle glyph to the figure p
p.circle(df['Income'], df['Lot_Size'])

# Call the output_file() function and specify the name of the file
output_file('G:/Statistics (Python)/ridingMowers.html')

# Display the plot
show(p)
