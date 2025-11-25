import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

st.title("Welcome to :yellow[Movies Rating Analysis]:")
st.write("First We will work on a CSV file called Movie-Rating.csv, and it looks like this:")

# Raw Data Frame
movies = pd.read_csv(r"C:\Users\mikun\Downloads\Movie-Rating.csv")
st.dataframe(movies)

st.write("Now we clean this dataframe and it will looks like this:")

# Cleaning the dataframe
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating',
                  'BudgetMillions', 'Year']
movies.Genre = movies.Genre.astype('category')
movies.Year = movies.Year.astype('category')

# Clean DataFrame
st.dataframe(movies)
st.dataframe(movies.describe())
st.header("Analysis Between :green[CriticRating]"
             " and :green[AudienceRating]:")
st.subheader("Bivariate Analysis:", divider="gray")

col1, col2, col3, col4 = st.columns(4)

# Hex Plot
with col1:
    st.write("Hex Plot")
    j = sns.jointplot(data=movies, x="CriticRating",
                      y="AudienceRating", kind='hex')

    st.pyplot(j)

# Scatter Plot
with col2:
    st.write("Scatter Plot")
    j = sns.jointplot(data=movies, x="CriticRating",
                      y="AudienceRating", kind='scatter')

    st.pyplot(j)

# Reg-line with Scatter
with col3:
    st.write("Reg-line with scatter")
    j = sns.jointplot(data=movies, x="CriticRating",
                      y="AudienceRating", kind='reg')

    st.pyplot(j)

# KDE plot
with col4:
    st.write("KDE Plot")
    j = sns.jointplot(data=movies, x="CriticRating",
                    y="AudienceRating", kind='kde')

    st.pyplot(j)

st.html("<p style='font-size: 18px'>"
            "As you can see from all the graphs that, this is a "
                "<strong>Positive Co-relation </strong> between "
                "<strong>"
                    "<span style='color:green'>CriticRating</span>"
                "</strong> and "
                "<strong>"
                        "<span style='color:green'>Audience Rating</span>"
                "</strong>."
        "<p>")

# Univariate Analysis
st.subheader("Univariate Analysis", divider="gray")

uniCol1, uniCol2 = st.columns(2)
# AudienceRating
with uniCol1:
    st.html("<h3><strong>AudienceRating </strong></h3>")
    m1 = sns.displot(movies.AudienceRating, kde=True)
    st.pyplot(m1)

#Critic Rating
with uniCol2:
    st.html("<h3><strong>CriticRating </strong></h3>")
    m2 = sns.displot(movies.CriticRating, kde=True)
    st.pyplot(m2)

st.html("<p style='font-size: 18px'>"
            "From Univariate analysis you can see the pattern between "
            "<strong style='color: green'>AudienceRating</strong> and "
            "<strong style='color: green'>CriticRating</strong> "
            "bit different (uniform distribution and normal distribution) "
            "but in our Bivariate analysis we see they are in positive co-relation, "
            "but if you look closer the <span style='color: green'>CriticRating</span> "
            "is Slightly in normal distribution."
        "</p>")

st.header("Analysis about budget of movies", divider="gray")
budgetCol1, budgetCol2, budgetCol3 = st.columns(3)

with budgetCol1:
    st.html("<h3><strong>Overall Budget: </strong></h3>")
    fig, ax = plt.subplots()
    ax.hist(movies.BudgetMillions)
    st.pyplot(fig)

with budgetCol2:
    st.html("<p><strong>Budget According to top3:"
            "<span style='color: blue'> Action</span>, "
            "<span style='color: orange'>Thriller</span>, "
            "<span style='color: green'>Drama</span> "
            "</strong></p>")
    fig, ax = plt.subplots()
    ax.hist(movies[movies.Genre == 'Action'].BudgetMillions, bins=20)
    ax.hist(movies[movies.Genre == 'Thriller'].BudgetMillions, bins=20)
    ax.hist(movies[movies.Genre == 'Drama'].BudgetMillions, bins=20)
    ax.legend(['Action', 'Thriller', 'Drama'])
    st.pyplot(fig)

with budgetCol3:
    st.html("<p><strong>Adding the elements in on bar Analysis:</strong></p>")
    fig, ax = plt.subplots()
    ax.hist([movies[movies.Genre == 'Action'].BudgetMillions,
              movies[movies.Genre == 'Drama'].BudgetMillions,
              movies[movies.Genre == 'Thriller'].BudgetMillions,
              movies[movies.Genre == 'Comedy'].BudgetMillions],
             bins=20, stacked=True)
    plt.legend(['Action', 'Thriller', 'Drama', 'Comedy'])
    st.pyplot(fig)

st.html("<p style='font-size: 18px'>"
        "According to these 3 figure most of the"
        " movies budget are between 0 to 50 in Million."
        " And least higher budget film is in <span style='color: blue'>Action</span>"
        " and following with Thriller Genre and least lower budget file is in "
        "<span style='color: red'>comedy</span> and following with Drama Genre "
        "</p>")

# budget vs (AudienceRating and CrticRating)
st.header("Analysis between Budget vs (AudienceRating and CriticRating) with kdeplot:", divider="gray")

f, axes = plt.subplots(1, 2, figsize=(12, 6))
sns.kdeplot(data=movies, x='BudgetMillions', y='AudienceRating', cmap="Greens_r", ax=axes[0])
sns.kdeplot(data=movies, x='BudgetMillions', y='CriticRating', ax=axes[1])
st.pyplot(f)

# Analysis between Genre and crticRating
st.header("Analysis between Genre and CriticRating:", divider="gray")
colGC1, colGC2 = st.columns(2)
with colGC1:
    st.html("<h3><strong>Box Plot between: Genre and CriticRating:</strong></h3>")

    fig1, ax1 = plt.subplots()
    sns.boxplot(data=movies, x="Genre", y="CriticRating", hue='Genre', ax=ax1)
    st.pyplot(fig1)

with colGC2:
    st.html("<h3><strong>Violin plot between Genre and CriticRating:</strong></h3>")
    fig2, ax2 = plt.subplots()
    sns.violinplot(data=movies, x='Genre', y='CriticRating', hue='Genre', ax=ax2)
    st.pyplot(fig2)

st.html("<p style='font-size: 18px'>"
        "According to these 2 figure from the "
        "<span style='color: yellow'>Box Plot</span> we can see the "
        "<strong>"
            "IQR(Median, 25%, 75%), Maximum and Minimum of CriticRating in different genre. "
        "</strong>"
        "While <span style='color: pink'>violin plot</span> "
        "we use to find detailed average of CriticRating."
        "</p>")

st.sidebar.html("<h2 style='color: gray; text-align: left; font-size: 32px;'>"
                "Here we Analyze the movie rating according to different"
                  " Genre, CriticRating, AudienceRating and Budget.</h2>")
