from models import reddit_bot
if __name__ == "__main__":
    obj = reddit_bot()
    obj.authenticate_bot()
    while True:
            obj.run_bot()
            #obj.reply_to_inbox()
            obj.delete_downvoted_comments()
