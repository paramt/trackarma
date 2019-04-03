import constants
import datetime
import matplotlib.pyplot as plt, matplotlib.dates as mpd

plt.switch_backend('Agg')
plt.rcParams["figure.figsize"] = (10, 6)

# Open dates.txt
with open("data/dates.txt", "r") as file:
    dates = list(filter(None, file.read().split("\n")))

# Open karma-total.txt
with open('data/karma-total.txt', 'r') as file:
    karma_totals = list(filter(None, file.read().split("\n")))

# Format everything
formatted_dates = [mpd.date2num(datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')) for date in dates]
karma_totals = [int(x) for x in karma_totals]

ylabel = ""

if max(karma_totals) > 1000000:
    karma_totals = [x/1000000 for x in karma_totals]
    ylabel = "(millions)"
elif max(karma_totals) > 1000:
    karma_totals = [x/1000 for x in karma_totals]
    ylabel = "(thousands)"

# Create chart
fig, ax = plt.subplots()
plt.title(constants.chart_title)
plt.xlabel("Time (UTC)")
plt.ylabel('Karma ' + ylabel)
fig.autofmt_xdate()
plt.plot_date(formatted_dates, karma_totals, marker="", linestyle="-", lw=constants.width, color=constants.color)
ax.grid(constants.show_grid)
plt.savefig('data/chart.png')
