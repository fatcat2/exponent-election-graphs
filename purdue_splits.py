from bokeh.io import output_file, show
from bokeh.models.annotations import Title
from bokeh.models.ranges import FactorRange
from bokeh.plotting import figure

from bokeh.models import ColumnDataSource

output_file("bars.html")

years_og = ["2012", "2016"]
parties = ["Democrat", "Republican", "Other"]

data = {'years' : years_og,
        'Democrat': [6447,5692],
        'Republican': [8008, 9331],
        "Other": [457, 1549]}

percentages = {'years' : years_og,
        'Democrat': [53.70,34.34],
        'Republican': [43.23, 56.31],
        "Other": [3.07, 9.35]}

x = [ (year, party) for year in years_og for party in parties ]
years = [ year for year in years_og for party in parties ]
parties = [ party for year in years_og for party in parties ]
counts = sum(zip(percentages['Democrat'], percentages['Republican'], percentages['Other']), ())

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

p = figure(x_range=FactorRange(*x), width=1600, height=900, title="Purdue area presidential voting splits from 2012 and 2016",
           toolbar_location=None, tooltips=TOOLTIPS, tools="")

p.vbar(x="x", top="counts", source=source, width=0.9, color="colors")

p.xgrid.grid_line_color = None

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None
p.sizing_mode = 'scale_width'
p.yaxis[0].axis_label = 'Vote share (%)'

p.add_layout(Title(text="Note: Data was chosen from precincts Wabash-2 to Wabash-30, which were defined in 2011.", text_font_size="0.75em", text_font_style="italic", align="left"), "below")
p.add_layout(Title(text="Source: Tippecanoe County Election Board | BY RYAN CHEN", text_font_size="0.75em", text_font_style="italic", align="left"), "below")

show(p)