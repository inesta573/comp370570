Data collection: I downloaded IRAhandle_tweets_1.csv, kept the first 10,000 tweets that were flagged English and had no "?", and wrote that filtered subset to a new TSV file.

Data annotation: I added a Boolean trump_mention feature by checking whether "Trump" appeared as a standalone word in each tweet, then wrote out the newly annotated dataset.tsv.  

Data analysis: I computed the fraction of tweets with trump_mention = T for results.tsv, then traced and explained in my README why some tweets were being double-counted.

Interpretation: Realizing that duplicate tweets were inflating my Trump-mention count meant my initial percentage overstated the true frequency, so the real takeaway was that the raw fraction couldn't be trusted until the duplication issue was understood and accounted for.

