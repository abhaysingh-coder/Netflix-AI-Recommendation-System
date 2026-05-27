# Netflix AI Recommendation System

## Overview
Netflix AI Recommendation System is a Machine Learning based web application built using Django, Python, Bootstrap, and Netflix Dataset Analysis.  
The system recommends similar movies and TV shows using a similarity matrix algorithm and provides a modern Netflix-style user interface.

---

# Features

- AI Based Movie Recommendation
- Similarity Matrix Recommendation Engine
- Netflix Dataset Analysis
- Search Movie Recommendations
- Recommendation History Tracking
- Modern Netflix Inspired UI
- Responsive Design
- Animated Carousel Homepage
- Recommendation Statistics
- Error Handling Page
- Dynamic Rating Cards
- Search History Dropdown System

---

# Technologies Used

## Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Font Awesome

## Backend
- Python
- Django

## Machine Learning
- Pandas
- NumPy
- Scikit-learn
- Cosine Similarity

---

# Project Structure

```bash
Netflix-AI-Recommendation-System/
│
├── mainapp/
│   ├── static/
│   │   ├── CSS/
│   │   ├── JS/
│   │   └── Image/
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── recommendation.html
│   │   ├── history.html
│   │   ├── about.html
│   │   └── error.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── Netflix/
│
├── Data.csv
├── similarity_matrix.pkl
├── manage.py
└── README.md
```

---

# How Recommendation Works

1. User enters a movie name.
2. System searches the movie in dataset.
3. Similarity matrix calculates similarity score.
4. Top similar movies are selected.
5. Recommended movies are displayed.
6. Search history is stored in database.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/Netflix-AI-Recommendation-System.git
```

## Move Into Project Folder

```bash
cd Netflix-AI-Recommendation-System
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Start Server

```bash
python manage.py runserver
```

---

# Developer

## Abhay Singh

- Email: me.abhaysingh13@gmail.com
- Location: Lucknow, Uttar Pradesh, India

---

# License

This project is created for educational and learning purposes.
"# Netflix-AI-Recommendation-System" 
"# Netflix-AI-Recommendation-System" 
