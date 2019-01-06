# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:29:39 2019

@author: Murilo S. Spina
"""

from textblob import TextBlob as tb #modulo para tokenizar palavras
import tweepy #API do twitter
import numpy as np


#regstro dos tokens para login na API(twitter)
consumer_key = 'pGmGmb7zsXRJvi6P5Qcr7i0fm'
consumer_secret = '4XPDR8ztLURs1BDgCRb3GVMIWFfrRfrUhQKt2q6AYXdoSw7t6R'

access_token = '66722263-fdBbcy0COuLWF7hFnrj9fzip1b8THeV3uMNFGXuwg'
access_token_secret = 'jJTnXQbCEbppmNHJcuAIFXikf5VnF2RQ18azREyDsNdye'

#Acessao à API(twitter)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#chamando API
api = tweepy.API(auth)

#procura por tweets
public_tweets = api.search('NFL')

#registrando a variável com "none" para usar posteriormente
analysis = None 

#Loop para cada tweet e sentimento identificado
tweets = []
for tweet in public_tweets:
    print(tweet.text) #imprime o texto dos tweets
    analysis = tb(tweet.text)#analisa o sentimento do tweet
    print(analysis.sentiment)#imprime o sentimento identificado e o subject(o quanto de opinião existe no tweet)
    polarity = analysis.sentiment.polarity
    tweets.append(polarity)#acumula a polaridade(sentimentos) dos tweets
       
#Imprime a média de sentimento dos tweets analisados
print('SENTIMENT AVERAGE: ' + str(np.mean(tweets)))
