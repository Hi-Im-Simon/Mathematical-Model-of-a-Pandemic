from bokeh.models.tools import SaveTool
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import Range1d



def generate_chart(data):
    plot = figure(
        width=800,
        height=400, 
        active_scroll='wheel_zoom', 
        x_range=Range1d(0, len(data[0])), 
        y_range=Range1d(0, max([item for sublist in data for item in sublist])),
        
    )
    colors = ['red', 'blue', 'green', 'yellow', 'brown', 'black', 'pink', 'orange', 'grey', 'magenta', 'silver']
    
    for i, d in enumerate(data):
        x = [i for i in range(len(d))]
        y = d
        plot.line(x=x, y=y, color=colors[i])
        plot.circle(x=x, y=y, color=colors[i])
    
    plot.toolbar.logo = None

    script, div = components(plot)

    file = open('app/templates/chart.html', 'w+')
    file.write(script)
    file.write(div)
    file.close()

