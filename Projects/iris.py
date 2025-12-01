import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title(" Here We Analys about :blue[Iris Flower]:")

iris = pd.read_csv(r"D:\Mikun\All Learnings\EDA learnings\IRIS DATASET _ ADVANCE VISUALIZATION _ EDA 2\Iris.csv")

st.dataframe(iris)

# finding rows and column of the dataset
col_row = iris.shape
st.html("<p>"
            "Here we have total of "
            f"<strong style='font-size: 18px'>{col_row[0]}</strong> rows "
            f"and <strong style='font-size: 18px'>{col_row[1]}</strong> columns."
        "</p>")

#drop the id column as data clean up
st.html("<p>"
            "Here we dropped the "
            "<strong style='color:yellow; font-size: 18px'>Id</strong> column"
            " on the dataset because we don't need it."
        "</p>")
iris.drop("Id", axis=1, inplace=True)
st.dataframe(iris)

# Missing Values Check
st.write("Checking if there are any missing values.")
st.dataframe(pd.DataFrame(iris.isna().sum()))
st.write("As we can see there are no missing values in the dataset.")

# Checking How may Species we have:
st.header("Checking how many species there are in the dataset.", divider='gray')
col1, col2 = st.columns(2)
with col1:
    st.write("Here we see there are 3 Species"
             " (Iris-setosa, Iris-versicolor, Iris-virginica).")
    st.dataframe(pd.DataFrame(iris["Species"].value_counts()))
with col2:
    st.html("<p>"
            "Here we see 3 Species in Visualization. "
            "<span style='color:blue;'>Iris-setosa</span>, "
            "<span  style='color:orange;'>Iris-versicolor</span>, "
            "<span style='color:green;'>Iris-virginica</span>."
            "</p>")
    fig, ax = plt.subplots()
    ax = sns.countplot(x=iris["Species"], hue=iris["Species"])
    st.pyplot(fig)

st.header("Relation Between Sepal Length and Sepal Width "
          "with different kind of joint plot and FacetGrid.", divider='gray')

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.write('Normal Joint Plot.')
    f = sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris)
    st.pyplot(f)

with col2:
    st.write("Regression line.")
    f = sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, kind='reg')
    st.pyplot(f)

with col3:
    st.write("Hexagonal plot")
    f = sns.jointplot(x="SepalLengthCm", y="SepalWidthCm",data=iris, kind='hex')
    st.pyplot(f)

with col4:
    st.write("FacetGrid Plot")
    f= sns.FacetGrid(iris, hue="Species", height=10)\
    .map(plt.scatter, "SepalLengthCm", "SepalWidthCm")\
    .add_legend()
    st.pyplot(f)


st.html("<p>"
            "From above data set we can see the clear relation ship between "
            "Iris-versicolor and iris-virginica but iris-setosa stays a bit different. "
        "We see that <strong>iris-Setosa's</strong> width is bigger compare to it's length and "
        "<strong>iris-Virginica and Versicolor</strong> has same sepal width and length "
        "but <strong>virginica</strong> length sometimes bigger than width."
        "</p>")


# Box Plots
st.header("Box Plot or Whisker Plot.", divider='gray')
st.write("This was  first introduced in year 1969 by Mathematician John Turkey."
         "Box plot give a statistical summary of the features being plotted.")

st.html("<style>ul, li {margin-left: 20px; padding-left: 10px;}</style>"
        "<h2>Understanding whisker Plot</h3>"
        "<ul>"
            "<li>Top line represent the max value.</li>"
            "<li>Top edge of box is third Quartile.</li>"
            "<li>Middle edge represents the Median.</li>"
            "<li>Bottom edge represents the first quartile value.</li>"
            "<li>The bottom most line represent the minimum value of the feature.</li>"
            "<li>The height of the box is called as interquartile range</li>"
            "<li>The black dots on the plot represent the outlier values in the data.</li>"
        "</ul>"
        "<hr style='border-color:gray; border-width: 2px;'></hr>")

b_col1, b_col2 = st.columns(2)
with b_col1:
    st.write("Petal Length Comparison.")
    fig, ax = plt.subplots()
    ax = sns.boxplot(x="Species", y="PetalLengthCm", data=iris,
                     order=iris["Species"].unique(),
                     linewidth=1, orient="v", dodge=False, hue="Species")
    st.pyplot(fig)

with b_col2:
    st.write("Sepal Length Comparison.")
    fig, ax = plt.subplots()
    ax = sns.boxplot(x="Species", y="SepalLengthCm", data=iris, hue="Species")
    ax = sns.stripplot(x="Species", y="SepalLengthCm", data=iris,
                       jitter=True, edgecolor="gray", hue="Species")

    st.pyplot(fig)

fig, ax = plt.subplots(figsize=(12, 6))
iris.boxplot(by="Species", ax=ax)
plt.suptitle("")
st.pyplot(fig)

st.subheader("From above Plots:")
st.html("<style>ul, li {margin-left: 20px; padding-left: 10px;}</style>"
        "<ul>"
            "<li><strong>Iris-Setosa</strong>"
                "<ul>"
                    "<li>The Petal Length of this species is lower compare to the Sepal Length.</li>"
                    "<li>The Petal Width lower compare to the Sepal Width.</li>"
                "</ul>"
            "</li>"
            "<li><strong>Iris-Versicolor:</strong>"
                "<ul>"
                    "<li>The Petal Length of this species lower compare to the Sepal Length.</li>"
                    "<li>The Petal Width lower compare to the Sepal Width.</li>"
                "</ul>"
            "</li>"
            "<li><strong>Iris-Virginica</strong>"
                "<ul>"
                    "<li>The Petal Length of this species lower compare to the Sepal Length.</li>"
                    "<li>The Petal Width lower compare to the Sepal Width.</li>"
                "</ul>"
            "</li>"
        "</ul>"
        "<p>"
        "But if you see overall from this graph you can see that size of each flower follow this pattern,"
        "<br />&nbsp;&nbsp;<strong>Iris-Setosa < Iris-Versicolor < Iris-Virginica</strong>"
        "</p>")


# Pair Plots
st.header("Pair Plot:", divider="gray")
st.write("A \"Pairs Plot\" is also known as ScatterPlot, in which one variable in the "
         "same data row is matched with another variables like this below: Pairs plots are just elaborations on"
         " this, showing all variables paired with all the other variables.")



st.pyplot(sns.pairplot(data=iris, hue="Species"))

# Haet Map:
st.header("Heat Map:", divider="gray")
st.write("<strong>Heat map</strong> is used to find out the correlation between "
         "different features in the dataset "
         "i.e between <strong>(-1 to +1)</strong>."
         
         "<ul>"
            "<li><strong>Positive correlation:</strong> if one increase other also increase.</li>"
            "<li><strong>Negative correlation:</strong> if one decrease other increase.</li>"
         "</ul>",
         unsafe_allow_html=True)

st.write("The Correlation dataset will be look like this:")
st.dataframe(data=iris.corr(numeric_only=True))

st.write("And the correlation plot looks like this:")

fig, ax = plt.subplots(figsize=(10, 7))

ax = sns.heatmap(iris.corr(numeric_only=True), annot=True,
                 cmap='cubehelix', linewidths=0.5)

ax.set_xticklabels(ax.get_xticklabels(), rotation=30)
ax.set_yticklabels(ax.get_yticklabels(), rotation=360)

plt.title("Corelation Heat Map of Iris Dataset")

st.pyplot(fig)


