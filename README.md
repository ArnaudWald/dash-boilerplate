# dash-boilerplate
Generic code used for my Dash apps.

This is the code I used regularly to deploy my [Dash](https://dash.plotly.com) apps with Docker. Clone and modify as needed.


## Run locally

```bash
# Just the main page
python index.py

# Start each job individually
python job1.py
python job2.py

# Start app with job scheduler
python flask_scheduler.py
```


## Build

Because I keep forgetting :

```bash
docker build -t my-dash-app -f Dockerfile .

docker run --name some-dash-app -p 8050:8050 -d my-dash-app

docker logs -f some-dash-app

docker rm -f some-dash-app
```
