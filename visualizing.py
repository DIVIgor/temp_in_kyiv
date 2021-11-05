import csv

from plotly import graph_objects as go
from plotly import offline


filename = 'weather_kyiv_by_interval_2021.csv'

# getting the interval
with open(filename) as f:
    intrvl = list(csv.reader(f, delimiter=';'))[0][1:]
    interval = intrvl[0] + " - " + intrvl[-1] + " 2021"
    print(interval)

# collecting data
with open(filename) as f:
    reader = csv.reader(f, delimiter=';')
    header_row = next(reader), next(reader)

    # reading of max temperatures and dates
    min_t, max_t, dates = [], [], []
    for row in reader:
        dates.append(str(row[0]))
        min_t.append(int(row[1]))
        max_t.append(int(row[2]))

# visualizing
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=dates, y=min_t,
    mode='lines', name='Min t°C'
))
fig.add_trace(go.Scatter(
    x=dates, y=max_t,
    mode='lines', name='Max t°C'
))

fig.update_layout(
    title=f"Daily temperature graph in Kyiv, Ukraine ({interval})",
    title_x=0.5,
    xaxis_title=interval,
    xaxis_dtick=10,
    yaxis_title="Temperature, °C",
)

# fig.show()

offline.plot(fig, filename='visualizing_weather_interval.html')