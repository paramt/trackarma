import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mpd
import constants


def main():
    plt.switch_backend('Agg')
    plt.rcParams["figure.figsize"] = (10, 6)

    # Open dates.txt
    with open("data/dates.txt", "r") as file:
        dates = list(filter(None, file.read().split("\n")))

    # Open karma-total.txt
    with open('data/karma-total.txt', 'r') as file:
        karma_totals = list(filter(None, file.read().split("\n")))

    # Format everything
    formatted_dates = []

    for date in dates:
        date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        mpl_dates = mpd.date2num(date)
        formatted_dates.append(mpl_dates)

    karma_totals = [int(x) for x in karma_totals]

    ylabel = ""

    try:
        if max(karma_totals) > 1000000:
            karma_totals = [int(x) / 1000000 for x in karma_totals]
            ylabel = "(millions)"
        elif max(karma_totals) > 1000:
            karma_totals = [int(x) / 1000 for x in karma_totals]
            ylabel = "(thousands)"
    except (IndexError, ValueError):
        pass

    # Create chart
    fig, ax = plt.subplots()
    plt.title(constants.chart_title)
    plt.xlabel("Time (UTC)")
    plt.ylabel('Karma' + ylabel)
    fig.autofmt_xdate()

    # Plot data
    plt.plot_date(formatted_dates, karma_totals,
                  marker="", linestyle="-",
                  lw=constants.width, color=constants.color)

    # Configure settings
    ax.grid(constants.show_grid)
    plt.xticks()
    locator = mpd.AutoDateLocator(interval_multiples=False)
    ax.xaxis.set_major_locator(locator)

    plt.savefig('data/chart.png')

if __name__ == "__main__":
    main()
