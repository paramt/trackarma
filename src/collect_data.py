import os
import datetime
import praw
import src.constants as constants


def main(usePreset: bool, reddit_name=constants.reddit_name):
    if(usePreset):
        reddit = praw.Reddit('Bot')
    else:
        reddit = praw.Reddit(client_id=os.environ['CLIENT_ID'],
                             client_secret=os.environ['CLIENT_SECRET'],
                             user_agent=os.environ['USER_AGENT'])

    redditor = praw.models.Redditor(reddit, name=reddit_name)
    now = datetime.datetime.now()
    karma_total = redditor.link_karma + redditor.comment_karma

    # Add datetime to dates.txt
    with open("data/dates.txt", "r") as file:
        dates = file.read().splitlines()

    dates.append(str(now))

    with open("data/dates.txt", "w") as file:
        for date in dates:
            file.write(date + "\n")

    # Add line to karma-delta.txt
    with open('data/karma-total.txt', 'r') as file:
        karma_totals = file.read().splitlines()

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

if __name__ == "__main__":
    main(True)
