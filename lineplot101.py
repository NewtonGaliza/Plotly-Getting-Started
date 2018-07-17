import plotly
import plotly.graph_objs as go

plotly.offline.init_notebook_mode(connected=True)

axisX = []
axisY = []

for i in range(10):
    x = i
    y = i + 1
    axisX.append(x)
    axisY.append(y)

plotly.offline.iplot({
   "data": [go.Scatter(x = axisX, y = axisY)],
    "layout": go.Layout(title="XY")    
})
