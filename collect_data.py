import datetime
import constants
import praw

now = datetime.datetime.now()

reddit = praw.Reddit('Bot')
redditor = praw.models.Redditor(reddit, name=constants.reddit_name)

karma_total = redditor.link_karma + redditor.comment_karma

# Add datetime to dates.txt
with open("data/dates.txt", "r") as file:
    dates = list(filter(None, file.read().split("\n")))

dates.append(str(now))

with open("data/dates.txt", "w") as file:
    for date in dates:
        file.write(date + "\n")

# Add line to karma-delta.txt
with open('data/karma-total.txt', 'r') as file:
    karma_totals = list(filter(None, file.read().split("\n")))

    try:
        karma_delta = karma_total - int(karma_totals[-1])
    except IndexError:
        karma_delta = 0

    with open('data/karma-delta.txt', 'a') as file:
        file.write(str(karma_delta) + "\n")

# Add line to karma-total.txt
with open('data/karma-total.txt', 'a') as file:
    file.write(str(karma_total) + "\n")
    karma_totals.append(str(karma_total))
