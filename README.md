# Movie-Recommendation-System
A Content-Based Movie Recommendation System built using Python, Scikit-learn, TF-IDF Vectorization, Cosine Similarity, and Flask, providing personalized movie recommendations through an interactive web application.


# 🎬 Movie Recommendation System using Machine Learning & Flask

A complete end-to-end **Content-Based Movie Recommendation System** that recommends similar movies based on their textual features using **TF-IDF Vectorization** and **Cosine Similarity**. The project includes data preprocessing, feature engineering, similarity computation, and deployment through a responsive Flask web application.

---

## 📌 Project Overview

This project recommends movies similar to a user-selected movie by analyzing movie metadata and textual information. The recommendation engine uses Natural Language Processing (NLP) techniques to calculate similarity scores between movies and returns the most relevant recommendations.

The application is deployed using **Flask**, providing an intuitive web interface where users can search for a movie and receive personalized recommendations instantly.

---

## 🚀 Features

- Content-Based Movie Recommendation
- Data Cleaning & Preprocessing
- Feature Engineering
- TF-IDF Vectorization
- Cosine Similarity
- Real-Time Movie Recommendations
- Responsive Flask Web Application
- User-Friendly Interface
- Displays Movie Genres
- Displays Ratings
- Displays Popularity Score
- Displays Movie Overview

---

## 🛠 Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Pickle

### Machine Learning & NLP
- TF-IDF Vectorizer
- Cosine Similarity

### Web Framework
- Flask

### Frontend
- HTML5
- CSS3

### Development Tools
- Jupyter Notebook
- Visual Studio Code
- Git
- GitHub

---

## 📂 Project Structure

```
Movie-Recommendation-System
│
├── app.py
├── movie_recommendation.pkl
├── similarity.pkl
├── movies.pkl
├── requirements.txt
├── README.md
│
├── templates
│   ├── index.html
│   └── result.html
│
├── static
│   ├── style.css
│   └── background.jpg
│
├── notebook
│   └── Movies.ipynb
│
└── dataset
    └── movies.csv
```

---

## ⚙️ Machine Learning Workflow

1. Import Dataset
2. Data Cleaning
3. Handle Missing Values
4. Text Preprocessing
5. Feature Engineering
6. TF-IDF Vectorization
7. Cosine Similarity Matrix
8. Recommendation Generation
9. Save Model Using Pickle
10. Deploy Using Flask

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Movie-Recommendation-System.git
```

Navigate to the project folder

```bash
cd Movie-Recommendation-System
```

Create a virtual environment

```bash
python -m venv myvenv
```

Activate the virtual environment

Windows

```bash
myvenv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 🎥 How It Works

- Select a movie from the dropdown list.
- Click **Recommend Movies**.
- The application calculates similarity scores using TF-IDF and Cosine Similarity.
- Displays the top recommended movies with:
  - Movie Title
  - Genres
  - Rating
  - Popularity
  - Overview

---

## 📸 Application Screenshots

Include screenshots such as:

- Home Page
- Movie Selection
- Recommendation Results

---

## 📈 Future Enhancements

- Poster Display using TMDB API
- Search with Auto-Complete
- Collaborative Filtering
- Hybrid Recommendation System
- User Authentication
- Favorite Movies List
- Movie Trailer Integration
- Streamlit Deployment
- Docker Support
- REST API Development

---

## 👨‍💻 Author

**Soham Rajapurkar**

B.Tech Computer Science (Data Science)

Machine Learning | Data Science | Python | Flask | SQL | Power BI

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
