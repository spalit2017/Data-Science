# import libraries
import sys
import psycopg2
 
# get words from command line
args = sys.argv[1:]
args = [x.strip(',') for x in args]

# error handling: more than two inputs receive
if len(args) != 2:
    print "Only two inputs accepted and received {}".format(len(args))
    print "Please enter two input numbers, seperated by a space"
    sys.exit()
    
# error handling: inputs are not numbers
if not(args[0].isdigit() and args[1].isdigit()):
    print "Numeric inputs needed. Digit test on inputs return {}".format(map(str.isdigit, args))
    print "Please enter two input numbers, seperated by a space"
    sys.exit()

# convert args to digits
args = [int(x) for x in args]

# connect to postgres
conn = psycopg2.connect(database="Tcount",
                        user="postgres",
                        password="pass",
                        host="localhost",
                        port="5432")

# create a cursor
cur = conn.cursor()

# query words and counts
cur.execute("SELECT word, count FROM tweetwordcount WHERE count BETWEEN %s and %s", (min(args), max(args)) )
results = {rec[0]: rec[1] for rec in cur.fetchall()}

# if results are returned, print words and counts
if results:
    for word in sorted(results, key=results.__getitem__, reverse = True):
        print "Word:{:<12} Count:{:<4}".format(word, results[word])

# if no results were returned
else:
    print "No words found with those counts"
    
conn.close()
