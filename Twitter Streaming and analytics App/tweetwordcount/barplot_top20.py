import sys
import matplotlib.pyplot as plt
import numpy as np
import psycopg2


# Use psycopg to connect to Postgres
# Database name: Tcount;  Fields :  word and count 
# Table name: tweetwordcount 
conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")


# Create a cursor 
cur = conn.cursor()   

# Pull out seleced data from Tweetwordcount   
cur.execute("SELECT word, count FROM tweetwordcount ORDER by COUNT DESC LIMIT 20;") 
words = []
word_count = []

records = cur.fetchall()

words = [x[0] for x in records]
word_count= [x[1] for x in records]
n=len(records)

# Creating the plot 'Top 20 Words'

plt.ylim([-1, n])
plt.yticks(np.arange(n), words)
plt.ylabel('Most popular words')
plt.xlabel('Word count')
plt.title('Top 20 Words')
plt.barh(np.arange(n), cnt, align = 'center')

# Saving the plot in a png file

plt.savefig("Top20_words.png")

#Closing cursor and connection
cur.close()
conn.close()
