
# Project Title
Content-based-movie-recommendation-engine



## Data Collection

The data have been collected from the Kaggle.
## Pre processing steps

### Creating dataframes
There were two csv files named creits.csv and movied.csv. both files do have a title feature in common.

### 1st step
the files has been merged on the basis of title column.

### 2nd step
there are many un necessary columns which may not be useful in building the recommendation engine.
only 7 columns were considered out of 23 columns.

those columns as follows below

1. title,
2. id
3. overview
4. genres
5. cast
6. crew
7. keywords

### Null value operation

there were only three null values out of whole dataframe. those rows were dropped as the percentage of null rows were too less.

### Processing the data

the columns 'overview','genres','cast','crew','keywords' do have some validation errors that need to be fixed.

1. the column 'overview' has the values in string format. they need to be converted into lists.
2. the columns 'keywords','genres','cast','crew' do have the values in the dictionary format. and they also need to be converted into list format.
3. out of those columns, the 'cast' and 'crew' columns do have many key and value pairs with in the each dictionary. for that i have extracted only first three key,value pairs out of the cast column.
4. and only director value has been extracted from the 'crew' column.
5. Now the those five columns need to be merged in order to ceate a 'bag of model' or 'TFIDF' model.


### NLP pre processing steps.

before getting the 'bag of model' or 'TFIDF' model there should be some pre processing steps need to be performed.

1. lowering the data
2. removing the unnecessary words using stopwords.
3. stemming or lemmatizing the data





## model building

For this particular problem the 'Bag Of Model' model was used to convert the desired column to vector format.
the 'Bag Of Model' can be imported from the sklearn.feature_extraction.text.CountVectorizer.
the number of features parameter was given with 5000.
that means 5000 columns can be generated and each word of each sentence has a particular number. remaining all do have value '0'.

## cosine similarity

'cosine similaity' can be used in finding distance between the two vectors.
the 'cosine similaity' can be imported from the sklearn.metrics.pairwise.cosine similarity.

here, we are creating a square matrix having a shape equal to the no.of rows in the preprocessed dataframe.

# recommonding the movies.

here a function has been defined with the operatins of finding the index of the input movie in the original data frame 
and finding same index value column in our cosine similarity matrix.

along with the above operations the function will get the top coorelated values according to the descending order and will be displayed the recommonded movies.





## flask application

I have used flask framework to build the api and web application. 


## deployment

Deployement was performed in the Heroku architecture. which is a platform as a service, where we can have runtime and server for ready to use.

