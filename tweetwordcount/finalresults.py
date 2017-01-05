# import libraries
import sys
import psycopg2

def get_counts(args = None):
 
    # connect to postgres
    conn = psycopg2.connect(database="Tcount",
                            user="postgres",
                            password="pass",
                            host="localhost",
                            port="5432")

    # create a cursor
    cur = conn.cursor()
 
    # query words and counts
    cur.execute("SELECT word, count FROM tweetwordcount")
    results = {rec[0]: rec[1] for rec in cur.fetchall()}

    # close the connection
    conn.close

    # return found word counts
    return results

# get words from command line
args = sys.argv[1:]

# retrieve words from database
results = get_counts(args = args)

# If no words given, return all words and counts, sorted alphabetically
if args:

    # print words and counts, one per line
    for word in args:
	#set initial word count to 0
	cnt = 0

	# if word found, update ocunt
	if word in results.keys():
		cnt = results[word]

        print "Total number of occurences of {}: {}".format(word, cnt)
        
# otherwise, return total number of word occurances for specific words 
else:

    # print words and counts, one per line
    for word in sorted(results, key=str.lower):
        print "Word:{:<12} Count:{:<4}".format(word, results[word])
