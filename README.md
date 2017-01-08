# Transforming-data-with-Python
Transform and work with data by writing Python scripts.

Introduction:-

In this project, I have been working with a dataset of submissions to Hacker News from 2006 to 2015. Hacker News is a site where users can submit articles from across the internet (usually about technology and startups), and others can "upvote" the articles, signifying that they like them. The more upvotes a submission gets, the more popular it was in the community. Popular articles get to the "front page" 
of Hacker News, where they're more likely to be seen by others.

The dataset have been using was compiled by Arnaud Drizard using the Hacker News API, and can be found here. We've sampled 10000 rows from the data randomly, and removed all extraneous columns. Our dataset only has four columns:

1. submission_time -- when the story was submitted.
2. upvotes -- number of upvotes the submission got.
3. url -- the base domain of the submission.
4. headline -- the headline of the submission. Users can edit this, and it doesn't have to match the headline of the original article.

I have written scripts to answer some main questions:

1. What words appear most often in the headlines?
2. What domains were submitted most often to Hacker News?
3. At what times are the most articles submitted?

I have answered these questions by writing command line scripts, instead of using IPython notebook. IPython notebooks are great for quick data visualization and exploration, but Python scripts are the way to put anything we learn into production. Let's say you want to make a website to help people write headlines that get as many upvotes as possible, and submit articles at the right time. To do this, you'll need scripts.
