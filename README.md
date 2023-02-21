## Flask API

- Flask
- Vercel

I've deployed a Flask API to Vercel so i can send input from users to my Linear regression model.
The Flask API recieves a post request with data input from my web-application and returns a predicted
usage of kW per minute, this can be altered or used in calculating the predicted cost for a period.

There is alot that i would have changed with more time, like prediction for per hour, per day.. so on.

To use it locally just clone the repo, go into a terminal and go to root of the directory and pass:

'python api.py'

It will then run locally and you will see a adress that you can send the post request to,
most likely: http://127.0.0.1:5000

When using with cURL you can send it a request like this:

Local:
'curl -X POST -H "Content-Type: application/json" -d "{\"input\": [0.5, 0.3, 0.2, 0.4, 0.5, 0.6, 0.6]}" http://127.0.0.1:5000/predict'

Vercel:
'curl -X POST -H "Content-Type: application/json" -d "{\"input\": [0.5, 0.3, 0.2, 0.4, 0.5, 0.6, 0.6]}" https://flask-api-navy.vercel.app/predict'
