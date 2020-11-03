from bokeh.io import output_file, show
from bokeh.models.annotations import Title
from bokeh.models.ranges import FactorRange
from bokeh.plotting import figure

from bokeh.models import ColumnDataSource

output_file("bars.html")

years = ["2000", "2004", "2008", "2012", "2016"]
parties = ["Democrat", "Republican", "Other"]

data = {'years' : years,
        'Democrat': [40.29, 39.7, 55.05, 46.81, 43.07],
        'Republican': [57.73, 58.92, 43.45, 50.4, 48.57],
        "Other": [1.98, 1.38, 1.5, 2.79, 8.36]}

x = [ (year, party) for year in years for party in parties ]
years = [ year for year in years for party in parties ]
parties = [ party for year in years for party in parties ]
counts = sum(zip(data['Democrat'], data['Republican'], data['Other']), ())

color_dict = {
    "Democrat": "#718dbf",
    "Republican": "#e84d60",
    "Other": "#c9d9d3"
}

colors = [color_dict[party] for party in parties]

print(x, counts)

source = ColumnDataSource(data=dict(
    years=years,
    x=x,
    counts=counts,
    party=parties,
    colors=colors
))

TOOLTIPS = [
    ("Year", "@years"),
    ("Vote Percentage", "@counts%"),
    ("Party", "@party")
]

p = figure(x_range=FactorRange(*x), width=1600, height=900, title="Tippecanoe County presidential voting splits from 2000 to 2016",
           toolbar_location=None, tooltips=TOOLTIPS, tools="")

p.vbar(x="x", top="counts", source=source, width=0.9, color="colors")

p.xgrid.grid_line_color = None

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None
p.sizing_mode = 'scale_width'
p.yaxis[0].axis_label = 'Vote share (%)'

# p.add_layout(Title(text="Note: Voting numbers for 2020 are from early votes counted before Nov. 3.", text_font_size="0.75em", text_font_style="italic", align="left"), "below")
p.add_layout(Title(text="Source: Tippecanoe County Election Board | BY RYAN CHEN", text_font_size="0.75em", text_font_style="italic", align="left"), "below")

show(p)