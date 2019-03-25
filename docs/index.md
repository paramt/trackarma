The script logs karma daily and dynamically generates a chart 
with the data it's collected. Here's an example of my account &ndash; 
[/u/hypnotic-hippo](https://www.reddit.com/user/hypnotic-hippo). 

![Image](http://206.167.183.187/chart.png)

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
```
[Bot]
client_id=[YOUR APP'S ID]
client_secret=[YOUR APP'S SECRET]
username=[YOUR REDDIT USERNAME]
password=[YOUR REDDIT PASSWORD]
user_agent=Karma Tracker Bot 1.0
```

#### 4. Configure this script
- Open `constants.py`
- Change the value of `reddit_name` to the username you wish to track


#### 5. Set up a scheduled task
Run `sudo python app.py` daily using [Crontab](https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/) on Linux or  [Task Scheduler](http://theautomatic.net/2017/10/03/running-python-task-scheduler/) on Windows

I would suggest running this script once per day, but you may choose to run it at any interval. 
If you run the script at any interval other than once per day, 
remember to change the value of `frequency` in `constants.py`. This is just to 
makes sure that the chart's x-axis will be accurate.

## Output
The script will output everything in `data/`

- `chart.png` &ndash; a line graph displaying the Redditor's karma over time
- `karma-total.txt` &ndash; a record of the Redditor's karma over time, separated with newlines
- `karma-delta.txt` &ndash; a record of the Redditor's karma gain over time, separated with newlines
