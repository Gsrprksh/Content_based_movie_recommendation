from turtle import pd
from flask import Flask, render_template, url_for, send_file,Response, request, jsonify, redirect
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = Flask(__name__)

df = pd.read_csv('recommondation1.csv')

cv = CountVectorizer(max_features = 5000, stop_words='english')
scores = cv.fit_transform(df['tags']).toarray()

similarity = cosine_similarity(scores)


@app.route('/',methods = ['POST','GET'])
def home():
    return render_template('index.html')

@app.route('/recommond', methods = ['POST','GET'])
def recommond():
    x = request.form['Enter_Movie_Name Here']
    ind = df[df['title'] == x].index[0]
    distance = similarity[ind]
    reco = sorted(list(enumerate(distance)),reverse = True, key = lambda x:x[1])[1:5]
    li =[]
    for i in reco:
        x = df.iloc[i[0]].title
        li.append(x)
    return render_template('index.html',result = li)




if __name__ == "__main__":
    app.run(debug = True)