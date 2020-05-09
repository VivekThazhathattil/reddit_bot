from models import reddit_bot
import nltk
if __name__ == "__main__":
    nltk.download('vader_lexicon')
    obj = reddit_bot()
    obj.authenticate_bot()
    while True:
            obj.run_bot()
            #obj.reply_to_inbox()
            obj.delete_downvoted_comments()
