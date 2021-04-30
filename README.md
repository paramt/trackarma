# Trackarma <img align="left" width=42 src="https://www.param.me/trackarma/favicon.png">

[![Build](https://img.shields.io/travis/paramt/trackarma/master.svg?style=for-the-badge)](https://travis-ci.org/paramt/trackarma)
[![CodeFactor](https://www.codefactor.io/repository/github/paramt/trackarma/badge/?style=for-the-badge)](https://www.codefactor.io/repository/github/paramt/trackarma)

A simple python script that uses [PRAW](https://praw.readthedocs.io/en/latest/)
to track Reddit karma. The script logs an account's total karma and dynamically
generates a chart with the data it's collected. Below is an example using data
collected from [/u/GallowBoob](https://www.reddit.com/user/GallowBoob) &ndash;
a Redditor who's infamous for his high karma count. The chart is showing data that
was collected every minute for over 3 months.

![Image](http://api.param.me/trackarma/charts/transparent/nogrid.png)

## Setup

#### 1. Clone the repo
`git clone https://github.com/paramt/trackarma.git`

#### 2. Install dependencies
- `pip install praw`
- `pip install matplotlib`

#### 3. Configure PRAW
- Create a new app on Reddit
    * [Follow this link](https://www.reddit.com/prefs/apps/)
    * Click `create new app`
    * Choose `personal use script`
    * Add a name and description
    * Click `create app` and copy the ID and secret
- Create a file named `praw.ini` inside the repo
- Make a new configuration that looks like this
```ini
[Bot]
client_id=[YOUR APP ID]
client_secret=[YOUR APP SECRET]
user_agent=Karma Tracker Bot 1.0
```

#### 4. Configure Trackarma
- Open `constants.py`
- Change the value of `reddit_name` to the username you're tracking
- Optionally, you can change other constants there (like the chart's title)

#### 5. Set up a scheduled task
Run `sudo python -m src.collect_data` at a constant interval using [Crontab](https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/) on Linux or  [Task Scheduler](http://theautomatic.net/2017/10/03/running-python-task-scheduler/) on Windows.
To generate the chart, run `sudo python -m src.generate_chart`. The live example is running both commands every minute, but you may choose to run them at any interval

#### Output
The script will output everything in `data/`

- `chart.png` &ndash; a line graph displaying the Redditor's karma over time
- `dates.txt`&ndash; the datetime entries of each time `collect_data.py` ran 
- `karma-total.txt` &ndash; a record of the Redditor's karma over time
- `karma-delta.txt` &ndash; a record of the Redditor's karma gain over time

## License
This project is licensed under the [MIT license](LICENSE). You are free to use, modify, and distribute the source code as long as you include the original license file.
