# Bitcoin Predictor

## Requirements

To create an environment, run the following command
```conda
$ conda create --name <env> --file requirements.txt
```


To activate it, run the following command
```conda
$ conda activate <env>
```


In order to run the notebooks you will need to download the data used for the study [here](https://drive.google.com/drive/folders/1m_9TyEM0wyw5RhoAT2oQ0sGVswz0m18r?usp=sharing) and save it locally to the repo directory.


Applying for API keys:
- Twitter --> [apply](https://developer.twitter.com/en/apply-for-access)
- Binance --> [apply](https://www.binance.com/en/support/faq/360002502072)



## Introduction

Since 2009, there has been a radical new way of making payments. The creation of the first decentralized peer-to-peer payment system, Bitcoin, has led to the creation of a novel and booming set of payment services, known collectively as cryptocurrencies. These virtual currencies are not created or backed by any government, nor does anyone user have complete control over them.

Bitcoin is the largest cryptocurrency out there in market capitalization and its price has been rapidly increasing since it was created in 2009 by Satoshi Nakamoto, reaching over $ 60,000 per coin on April 2021.

In the recent years, cryptocurrencies have been widely used for trading and speculation, and many investors are seeking their chance to make a fortune out of them, as the crypto market is, indeed, extremely volatile.

Accurate stock market predictions are of great interest to these investors; however, crypto markets are influenced by volatile factors such as any kind of news that make it hard to predict based on merely historical data.

Nowadays, social media contains both, financial news and personal opinions of leading figures that can change investors’ behavior.

In this project we present a method for predicting Bitcoin closing prices utilizing Twitter sentiments and Google Trends as well as the volume of Bitcoins traded and past Bitcoin closing prices. 



## Data

Data has been collected from several sources.

Refer to the [1 Data Extraction](notebooks/1_data_extraction.ipynb) notebook.

### Twitter

The [Twitter API](https://developer.twitter.com/en/docs/twitter-api) was used to retrieve real time English tweets that contain Bitcoin in them. It is limited up to 450 requests every 15 minutes. Each request can get a maximum of 100 tweets.

In order to make requests to this API, `tweepy` library came pretty handy. Tweepy is a Python library for accessing the Twitter API. It is great for simple automation and it has a nice [documentation](https://docs.tweepy.org/en/latest/).

A script was made in order to be collecting tweets for 4 consecutive weeks (28 days). We end up with over 1,500,000 tweets that contain Bitcoin. We extract the follwing features for each tweet:

- Tweet ID
- Text
- Username
- Number of followers
- Retweet count
- Favorite count
- Date of post
- Source

API credentials will be necessary.

### Google Trends

Google Trends is a website supported by Google that analyzes the popularity of a specific keyword search queries in Google Search.

Thanks to `pytrends`, python unofficial Google Trends library we were able to extract Bitcoin searches in Google hourly.

### Crypto

The [Binance API](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md#general-api-information) was utilized to retrieve Bitcoin closing prices and volume of Bitcoins traded minutely and hourly. `binance` python library was used to make requests.

Binance has quickly grown to become one of the largest cryptocurrency exchanges offering trading in more than 500 coins and tokens.

`binance` library was installed by running `conda install -c royalnorton binance` *compatible with python 3.6*

API credentials will be necessary.



## Repo Structure

1. **frontend:** Code to execute from the terminal. Made with `streamlit`
  - [Bitcoin predictions](frontend/bitcoin_predictor.py)

2. **images:** Two wordclouds for streamlit purposes

3. **notebooks:** Jupyter notebooks with explanations
  - [1 Data Extraction](notebooks/1_data_extraction.ipynb): Scripts were built to retrive data from the Twitter API, Bitcoin data, from Binance API and Bitcoin Google searches from `pytrends`.
  - [2 EDA](notebooks/2_EDA.ipynb): We aim to get some meaningful information from Bitcoin tweets and apply a sentiment analyser to get a polarity score for each one of the tweets. Then we calculate a main score for each tweet by taking into account the users' number of followers.
  - [3 Crypto Analysis](notebooks/3_crypto_analysis.ipynb): We aim to study the correlations between Bitcoin closing prices and the input features: Twitter sentiment scores, Google Trends and volume of Bitcoins traded.
  - [4 Time Series](notebooks/4_time_series.ipynb): Multivariate time series forecasting with Vector Autorregressive Model.
  - [5 Recurrent Neural Networks](notebooks/5_RNN.ipynb): Bitcoin closing prices predictions with LSTM and GRU

4. [requirements](requirements.txt)

