import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from PIL import Image
pd.set_option('display.max_colwidth', None)


st.title('Cryptocurrency Predictor')
st.write("""
Based on twitter sentiments,
google trends and volume of Bitcoins traded and closing prices
we tried to forecast its price using both statistical inference methods
and recurrent neural networks.

Period of study: 21/02/2021 - 20/03/2021
""")

## Paths
btc_path = 'data/crypto/BTCUSDT_1h_data.csv'
tweets_path = 'data/twitter/tweets.csv'
scores_path = 'data/twitter/scores_sample.csv'
google_path = 'data/google_trends/bitcoin_trends.csv'
var_pred_path = 'data/forecasts/var.csv'
lstm_pred_path = 'data/forecasts/lstm.csv'
gru_pred_path = 'data/forecasts/gru.csv'

## Getting dfs ready
# Bitcoin
df_btc = pd.read_csv(btc_path, parse_dates=True, index_col='timestamp')
df_btc = df_btc[(df_btc.index >= '2021-02-21 00:00:00') & (df_btc.index <= '2021-03-20 23:50:31')]
# Tweets
df_tweets = pd.read_csv(tweets_path, parse_dates=['created_at'])
df_tweets['weekday'] = df_tweets['created_at'].dt.weekday
day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df_tweets['weekday'] = df_tweets['weekday'].apply(lambda x: day_name[x])
# Scores
df_scores = pd.read_csv(scores_path)
# Google trends
df_google = pd.read_csv(google_path, parse_dates=True)
# VAR forecasts
var_forecast = pd.read_csv(var_pred_path, index_col='date', parse_dates=True)
# LSTM forecasts
lstm_forecast = pd.read_csv(lstm_pred_path, index_col='dates', parse_dates=True)
# GRU forecasts
gru_forecast = pd.read_csv(gru_pred_path, index_col='dates', parse_dates=True)

## Image as intro

## Select option from the side bar
option = st.sidebar.selectbox('Choose an option', ('Features', 'EDA', 'Predictions'))


## Features
if option == 'Features':
    st.write("""
    Four variables were used to carry out the project.
    1. *Bitcoin prices themselves* past information was used to make predictions.
    2. *Twitter sentiments*
    3. *Google trends*
    4. *Volume of Bitcoins traded*
    """)
    ## Bitcoin prices plot
    st.subheader('Bitcoin closing prices overview')
    fig = px.line(x=df_btc.index, y=df_btc['close'], labels={'x': 'date', 'y': '$'})
    st.plotly_chart(fig, use_container_width=True)

    ## Twitter
    st.subheader('Tweets extraction')
    st.write('Over 1,500,000 tweets were collected during 4 consecutive weeks (28 days).')
    # plotly fig
    fig = px.histogram(df_tweets, x='weekday',
                       template='seaborn',
                       title='Tweets distribution over time')
    # plot it!
    st.plotly_chart(fig, use_container_width=True)
    # tweet scores
    st.write('**A sentiment score was calculated for each tweet**')
    st.dataframe(df_scores.sample(3))

    ## Google Trends
    st.subheader('Google Trends')
    st.write('How popular is Bitcoin according to google searches?')
    fig = px.line(x=df_google['date'], y=df_google['bitcoin'], labels={'x': 'date', 'y': 'searches'})
    st.plotly_chart(fig, use_container_width=True)

    ## Volume of Bitcoin Traded
    st.subheader('Volume of Bitcoins traded')
    st.write('How many purchases of Bitcoin were there?')
    fig = px.line(x=df_btc.index, y=df_btc['volume'], labels={'x': 'date', 'y': 'bitcoins'})
    st.plotly_chart(fig, use_container_width=True)

## EDA
elif option == 'EDA':
    st.subheader('Insights of Twitter sentiments')
    st.write('Since each tweet has a polarity score we classified them as positive or negative.')
    for wc, emotion in zip(['images/wc_pos.jpg', 'images/wc_neg.jpg'], ['positive', 'negative']):
        st.write(f'**Top words for {emotion} Bitcoin tweets**')
        with Image.open(wc) as img:
            st.image(img)

else:
    model = st.sidebar.selectbox('Select a forecast method', ('VAR', 'LSTM', 'GRU'))
    if model == 'VAR':
        st.subheader('Vector Autoregressive Model')
        st.write('Explanation')
        # plotly figure
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=var_forecast.index, y=var_forecast['actual'],
                                 mode='lines',
                                 name='actual'))
        fig.add_trace(go.Scatter(x=var_forecast.index, y=var_forecast['forecast'],
                                 mode='lines',
                                 name='forecast'))
        # plot it
        st.plotly_chart(fig, use_container_width=True)
    elif model == 'LSTM':
        st.subheader('Long Short-Term Memory (LSTM)')
        st.write('It is a type of recurrent neural network...')
        # plotly figure
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=lstm_forecast.index, y=lstm_forecast['actual'],
                                 mode='lines',
                                 name='actual'))
        fig.add_trace(go.Scatter(x=lstm_forecast.index, y=lstm_forecast['forecast'],
                                 mode='lines',
                                 name='forecast'))
        # plot it
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.subheader('Gated Recurrent Units (GRU)')
        st.write('It is a type of recurrent neural network...')
        # plotly figure
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=gru_forecast.index, y=gru_forecast['actual'],
                                 mode='lines',
                                 name='actual'))
        fig.add_trace(go.Scatter(x=gru_forecast.index, y=gru_forecast['forecast'],
                                 mode='lines',
                                 name='forecast'))
        # plot it
        st.plotly_chart(fig, use_container_width=True)