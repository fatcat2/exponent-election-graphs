from bokeh.io import output_file, show
from bokeh.models.annotations import Title
from bokeh.plotting import figure

from bokeh.models import ColumnDataSource

output_file("bars.html")

source = ColumnDataSource(data=dict(
    years=["1998", "2000", "2002", "2004", "2006", "2008", "2010", "2012", "2014", "2016", "2018", "2020"],
    counts=[33667, 46785, 30654, 52183, 34620, 69574, 36489, 58275, 30938, 64227, 52070, 53000]
))

TOOLTIPS = [
    ("Year", "@years"),
    ("Votes", "@counts"),
]

p = figure(x_range=["1998", "2000", "2002", "2004", "2006", "2008", "2010", "2012", "2014", "2016", "2018", "2020"],
    plot_height=250, title="Tippecanoe County voting counts from 1998 to 2020",
           toolbar_location=None, tooltips=TOOLTIPS, tools="")

p.vbar(x="years", top="counts", source=source, width=0.9, color="goldenrod")

p.xgrid.grid_line_color = None
p.y_range.start = 0
p.sizing_mode = 'scale_width'
p.add_layout(Title(text="Note: Voting numbers for 2020 are from early votes counted before Nov. 3.", text_font_size="0.75em", text_font_style="italic", align="left"), "below")
p.add_layout(Title(text="Source: Tippecanoe County Election Board | BY RYAN CHEN", text_font_size="0.75em", text_font_style="italic", align="left"), "below")

show(p)