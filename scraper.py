import configparser
import praw
from submissions import SubmissionModel, Classification

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("reddit.ini")
    client_id = config["reddit"]["client_id"]
    secret = config["reddit"]["secret"]
    user_agent = config["reddit"]["user_agent"]

    reddit = praw.Reddit(
        client_id=client_id, client_secret=secret, user_agent=user_agent
    )

    feed = reddit.subreddit("3Dprinting").hot(limit=10)
    for submission in feed:
        SubmissionModel(
            Classification.sexual, submission.selftext, submission.title, submission.id
        ).save()
