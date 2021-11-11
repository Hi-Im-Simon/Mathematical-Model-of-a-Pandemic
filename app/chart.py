from bokeh.plotting import figure
from bokeh.embed import components

#from app.maths import out
from app.models import Database


def generate_chart():
    par1 = Database.query[-1].mask_rate
    par2 = Database.query[-1].mask_fall_rate

    plot = figure()
    x = [i for i in range(100)]
    y = [i * i * par1 - par2 * 10000 for i in x]
        
    plot.circle(x=x, y=y)
    
    plot.toolbar.logo = None
    plot.toolbar_location = None

    script, div = components(plot)

    file = open('app/templates/chart.html', 'w+')
    file.write(script)
    file.write(div)
    file.close()

