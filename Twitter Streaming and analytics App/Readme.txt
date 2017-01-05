
*** Prepare the Environment needed for running the application ***

1. Install psycopg

pip install psycopg2

2. Install tweepy

pip install tweepy

3. Create postgreSQL database TCount  

Log into postgres as postgres user :

psql -U postgres;

Run following command to create database Tcount 

create database Tcount;

Connect to the TCount database 

\c Tcount;

4. Create a table ‘tweetwordcount’ as per following instruction to store the words and counts  from the tweets of the streaming application


CREATE TABLE tweetwordcount
       (word TEXT PRIMARY KEY NOT NULL,
       count INT NOT NULL);


*** Run the Application ***

5. Navigate to tweetwordcount folder.

Run sparse and stop after desired number of seconds.
type the command, "sparse run", to start the storm application for the tweetwordcount project. 

sparse run -t 120

Above command will run for 120 seconds. The duration of the application run can be adjusted as desired. If it is run without any parameter, then the streaming run will continue indefinitely until terminated by Ctl+C.

The emitted words and word counts will be saved into the table “tweetwordcount" under the Database "Tcount”.


*** Perform Exploratory Data Analysis ***

6. Exploratory Data Analysis can be done from the data saved in tweetwordcount table as follows:

i. Run following command with a word as an argument to return the Total No. of word occurrences from the stream run stored in the table.

Running the command without any argument will return all the words in the table and their total count
of occurrences.

python finalresults.py

ii. Run following command with 2 integers as arguments to return all the words from the table whose total number of occurrences in the table is between those two integers

python histogram.py 10 100

The above command will show all the words with counts between 10 and 100 , both inclusive.

iii. Run the following command to create a horizontal bar plot of top 20 words and their number of occurrences as captured in the tweetwordcount table so far.

python barplot_top20.py

Alternatively, you can log into table Tcount in psql and run the following query to retrieve the top 20 words and frequency from tweetwordcount table

SELECT word, count FROM tweetwordcount ORDER by COUNT DESC LIMIT 20;

You can capture the result in a python 2-dimensional array and then plot the horizontal bar diagram of the result to view inline and also save to a png file.



