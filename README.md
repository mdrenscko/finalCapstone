
# Project Title

Natural Language Processing Application

A Python program performs sentiment analysis on a dataset of product reviews from Amazon.

The sentiment analysis model is implemented using spaCy: the
en_core_web_sm spaCy model enables natural language processing
tasks. This model will help you analyse and classify the sentiment of the product reviews.
## Table of Contents


1. Download a dataset of product reviews: Consumer Reviews of Amazon Products (https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products) You can save it as a CSV file, naming it:amazon_product_reviews.csv.
2. Locate the Python script, named: sentiment_analysis.py for sentiment analysis. Within the script, you will perform the following tasks using the spaCy library:
3. Implement a sentiment analysis model using spaCy: Load the
en_core_web_md spaCy model to enable natural language processing
tasks. This model will help you analyse and classify the sentiment of the product reviews.
4. Preprocess the text data: Remove stopwords, and perform any
necessary text cleaning to prepare the reviews for analysis (this is included in the script).
5. Create a function for sentiment analysis. Define a function that takes a product review as input and predicts its sentiment. First the polarity of each review is analyzed using a function called analyze_polarity(data) that returns polarity. Then, according to the polarity, a sentiment is assigned to each review.
6. Test your model on sample product reviews: Test the sentiment
analysis function on a few sample product reviews to verify its accuracy in predicting sentiment.
7. Write a brief report or summary in a PDF file:
sentiment_analysis_report.pdf that must include:
7.1. A description of the dataset used.
7.2. Details of the preprocessing steps.
7.3. Evaluation of results.
7.4. Insights into the model's strengths and limitations.

## Installation

Install my-project 

Prerequisites

npm
npm install npm@latest -g

1. Get a free API Key at https://example.com

2. Clone the repo 
git clone https://github.com/mdrenscko/finalCapstone.git

3. Install NPM packages 
npm install

4. Enter your API in config.js
const API_KEY = 'ENTER YOUR API';
    
## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Run Locally

Clone the project

```bash
  git clone https://github.com/mdrenscko/finalCapstone.git
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


## Usage/Examples

The function that was created for sentiment analysis takes a product review as input and predicts its sentiment based on a polarity score:

for item in data:
    polarity_score = analyze_polarity(item) 

    if polarity_score > 0:
        sentiment = 'positive'
    elif polarity_score < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'



#The model can be tested on sample product reviews. Test the sentiment analysis function on a few sample product reviews to verify its accuracy in predicting sentiment.

#The code retrieves a review from the 'review.text' column at index 0. You can select two reviews of your choice using indexing. However, please be cautious not to use an index that is out of bounds, meaning it exceeds the number of data points or rows in the dataset.

#For example:


test1 = data[2]
print(test1)
print(analyze_polarity(data[2]))
print(f"The sentiment prediction is: {sentiment}")



test2 = data[10]
print(test2)
print(analyze_polarity(data[10]))
print(f"The sentiment prediction is: {sentiment}")


## Authors

- [Mihaela Drenscko](https://www.github.com/mdrenscko)


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
 - [Academic Tutorial - Facilitator-guided attempts of tasks](https://skills-sessions.cogrammar.com/)


## Summary

1. A description of the dataset used.
This is a list of over 34,000 consumer reviews for Amazon products like the Kindle, Fire TV Stick, and more provided by Datafiniti's Product Database.
There are 24 features/variables in the data set, with 28,332 observations for each feature, except for the columns with missing values. There are 7 numerical variables : 'dateAdded', 'dateUpdated', 'manufacturerNumber', 'reviews.date', 'reviews.dateSeen', 'reviews.numHelpful', 'reviews.rating' and 14 categorical variables are: 'id', 'name', 'asins', 'brand', 'categories', 'primaryCategories', 'imageURLs', 'keys', 'manufacturer', 'reviews.didPurchase', 'reviews.doRecommend', 'reviews.id', 'reviews.numHelpful', 'reviews.sourceURLs', 'reviews.text', 'reviews.title', 'reviews.username', 'sourceURLs'.
Following is a short description of each feature:
• 'id' (identity of the review).
• 'dateAdded' (the date when the review was first added, for example, 2015-10-30).
• 'dateUpdated' (date of the updated review, for example, 2019-04-25 – approximately four years after the review was first posted).
• 'name' (name of the product that was reviewed by a customer, for example: AmazonBasics AAA Performance Alkaline Batteries, Fire Kids Edition Tablet, Fire HD 8 Tablet with Alexa, All-New Fire HD 8 Tablet with Alexa, etc).
• 'asins' (Amazon Standard Identification Number. It’s a unique identifier of 10 letters and/or numbers for a product that’s assigned by Amazon.com. It’s primarily used for product-identification within their product catalog of billions of items. For books, the ASIN is the same as the ISBN number. For all other products, a new ASIN is created when an item is uploaded to Amazon’s catalog. ASINs are only guaranteed to be unique within a marketplace. That means different national Amazon sites may use different ASINs for the same product.)
• 'brand' (for example, Amazon and Amazon Basics (often stylized as AmazonBasics) is Amazon's original private label brand that was launched in 2009. The brand offers many products, including home goods, electronics, travel, office supplies, and much more.)
• 'categories' (for example AA, AAA, Health, Electronics, Health & Household, etc.)
• 'primaryCategories' (for example, Electronics, Toys & Games, Health & Beauty).
• 'imageURLs' (shows the URL of the product’s image).
• 'keys' (provides delivery of packages and groceries into your garage, behind your gate and inside multi-unit buildings – discontinued).
• 'manufacturer' (for example Amazon and AmazonBasics).
• 'manufacturerNumber' (unique identifier to find specific products).
• 'reviews.date' (for example, 2016-12-21).
• 'reviews.dateSeen' (when the review was seen by the designated person, for example 2017-09-09).
• 'reviews.didPurchase' (NaN).
• 'reviews.doRecommend' (NaN, True).
• 'reviews.id' (NaN).
• 'reviews.numHelpful' (NaN, 0).
• 'reviews.rating' (for example: 2, 4, 5, where 1 is the lowest mark and 5 is the highest mark).
• 'reviews.sourceURLs'
• 'reviews.text' (the text of the product review, as entered by the consumer, for example: “Works as expected. Good value just as good as duracell”; “Good tablet. A lot of tablet for the money.”)
• 'reviews.title' (for example, Best Kindle Ever, Love My Echo, Cool little gadget, Seems like good budget batteries, Happy kids, Great small tablet, Great fun for the family).
• 'reviews.username' (for example, ByNannymac47, ByForced48, brettdavis4, ByIrish, Mynameisluist, KCRoyas).
• 'sourceURLs'

2. Details of the preprocessing steps.
• Made use of the lower() to convert upper case letters to lower cases.
• Made use of strip() to eliminate leading and trailing whitespaces.
• Lemmatization was done to reduce a word to its root form using lemma.
• Removed all missing values from the column.
• Removed stopwords, by utilizing the .is_stop attribute in spaCy.
• Removed punctuation, by utilizing .is_punct attribute in spaCy.

3. Evaluation of results.
Here are the results of the sentiment analysis for the Amazon products purchased or viewed by consumers:
Positive percentage: 82.98%
Negative percentage: 7.26%
Neutral percentage: 9.76%
It can be concluded that generally, consumers have a good feeling about Amazon products: 82.98% of sentiments are positive, 9.76 are neutral, and only 7.26% are negative.
Testing the model prediction for two values gives the following analysis of sentiment for two data points:
data[2] = well duracell price happy
polarity = 0.8, therefore the sentiment predicted is negative
data[10] = find amazon basics batteries equal superior name brand ones cant believe didnt start buying sooner packages large price great
polarity = 0.43, therefore the sentiment is negative.

4. Insights into the model's strengths and limitations.
The model gives a numerical measurement of the polarity and sentiments related to the consumers who posted reviews for the products they bought or viewed on Amazon. It is a good calculator of the polarity of the sentences in product reviews and in calculating consumer sentiment based on positive and negative values of polarity scores, where a polarity greater than 0 shows a positive sentiment, less than 0 – a negative sentiment and a polarity score neither greater than 0 nor less than 0 shows a neutral sentiment.
From the testing of the model, it can be deduced that the sentiment analysis is not quite accurate. A reading of data[1] shows positive–like words, such as “well” and “happy”, yet the model gave it 0.8 negative qualificatives. A reading of data[10] reveals that the consumer regrets not having bought the product sooner because Amazon batteries are equal to those of a superior brand name. So, the model is not infallible, it has its limitations and cannot predict with high precision the consumer sentiment inferred from product review.