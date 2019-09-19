

import praw



reddit = praw.Reddit(
    user_agent="something",
    client_id="yOlYpKnddCn91A",
    client_secret="gTGKq-42UTCQeBI2MbxTXIVQV2E",
    username="",
    password="",
)

subreddit = reddit.subreddit("all")

keywords = ['what is', 'who is' , 'how is']
replyText = 'look at this cool citation generator[citethis.net](https://citethis.net/)!'



for comment in reddit.subreddit('all').stream.comments():
	for word in keywords:
		if word in comment.body:
			comment.reply(replyText)

			print(comment.body)