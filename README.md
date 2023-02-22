## Flask API

- Flask
- Vercel
- Jupyter notebook

I've deployed a Flask API to Vercel so i can send input from users to my Linear regression model.
The Flask API recieves a post request with data input from my web-application and returns a predicted
usage of kW per minute, this can be altered or used in calculating the predicted cost for a period.

Notebook for the model is "kWperMinPred.ipynb" and the saved model is model.joblib in the directory.

The dataset i used was found at: https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption

To use it locally just clone the repo, go into a terminal and go to root of the directory and pass:

1. 'pip install -r requirements.txt' to get the packags you need.
2. 'python api.py'

It will then run locally and you will see a adress that you can send the post request to,
most likely: http://127.0.0.1:5000

When using with cURL you can send it a request like this:

Local:
'curl -X POST -H "Content-Type: application/json" -d "{\"input\": [0.5, 0.3, 0.2, 0.4, 0.5, 0.6, 0.6]}" http://127.0.0.1:5000/predict'

Vercel:
'curl -X POST -H "Content-Type: application/json" -d "{\"input\": [0.5, 0.3, 0.2, 0.4, 0.5, 0.6, 0.6]}" https://flask-api-navy.vercel.app/predict'

Credit:
This project uses data from the UCI Machine Learning Repository (Dua, D. and Graff, C., 2019), which is available at [http://archive.ics.uci.edu/ml]. The UCI Machine Learning Repository is maintained by the University of California, School of Information and Computer Science in Irvine, CA.
