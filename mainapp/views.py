from django.shortcuts import render
import joblib
import numpy as np
import pandas as pd
from .models import *

# Create Functions
def load_model():
    try:
        similarity_matrix = joblib.load('similarity_matrix.pkl')
        data = pd.read_csv('Data.csv')
        return similarity_matrix, data
    except Exception as E:
        return render('error.html', {'error' : E })
similarity_matrix, data = load_model()

def recommend(matches):
    movie_index = matches.index[0]
    similarity_scores = list(enumerate(similarity_matrix[movie_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    top_movies = similarity_scores[1:11]
    movie_indices = [i[0] for i in top_movies]
    available_columns = []
    for col in ["title", "director", "cast", "listed_in", "rating", "description"]:
        if col in data.columns:
            available_columns.append(col)
    return data.iloc[movie_indices][available_columns]


# Create your views here.
def index(request):
    try:
        history = RecommendationHistory.objects.all()
        rating = list(history.values_list('rating', flat=True).distinct())[0:4]
        context = {
            'tab' : 'Index',
            'rating' : rating
            }
        return render(request, 'index.html', context)
    except Exception as e:
        return render(request, 'error.html', {'error': e})

def error(request):
    return render(request, 'error.html')

def recommendation(request):
    try:
        message =''
        movies = None
        if request.method == 'POST':
            movie_name = request.POST.get('movie_name')
            movie_name = movie_name.lower()
            matches = data[data["title"].str.lower().str.contains(movie_name, na=False)]
            if matches.empty:
                message = "Movie not found in dataset."
            else :
                movies = recommend(matches).to_dict('records')
                list_title =[]
                for movie in movies:
                    list_title.append(movie['title'])
                RecommendationHistory.objects.create(requested = movie_name, rating = movie['rating'] ,rec_1 = list_title[0], rec_2 = list_title[1], rec_3 = list_title[2], rec_4 = list_title[3], rec_5 = list_title[4], rec_6 = list_title[5], rec_7 = list_title[6], rec_8 = list_title[7], rec_9 = list_title[8], rec_10 = list_title[9])
        context = {
            'tab' : 'Recommendation',
            'message' : message,
            'movies' : movies
            }
        return render(request, 'recommendation.html', context)
    except Exception as e:
        return render(request, 'error.html', {'error': e})

def about(request):
    try:
        context = {
            'tab' : 'About',
        }
        return render(request, 'about.html', context)
    except Exception as e:
        return render(request, 'error.html', {'error': e})

def history(request):
    try:
        history = RecommendationHistory.objects.all()
        context = {
            'tab' : 'History',
            'history' : history,
            'count' : history.count()
        }
        return render(request, 'history.html', context)
    except Exception as e:
        return render(request, 'error.html', {'error': e})


