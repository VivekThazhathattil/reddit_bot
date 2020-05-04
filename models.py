import praw
import random
import requests
import time
import os

class reddit_bot(object):
    insult_list = [ "dumb", 
            "shit", 
            "asshole", 
            "fuck", 
            "bitch", 
            "piss", 
            "drunk", 
            "bastard", 
            "dick", 
            "cunt", 
            "FUCK", 
            "Fuck", 
            "poo", 
            "stfu",
            "Stfu",
            "STFU",
            "gtfo",
            "GTFO",
            "Gtfo" ]

    def get_num_lines_in_file(self) -> int:
        print("get number of lines in filtered_insults.txt")
        return sum(1 for line in open('filtered_insults.txt'))

    def get_nth_line_in_file(self) -> str:
        print("get nth line from filtered_insults.txt")
        with open("filtered_insults.txt") as f:
            for i, line in enumerate(f):
                if i == self.n_for_file-1:
                    return line

    def authenticate_bot(self) -> None:
        self.reddit = praw.Reddit("cuck_simulator",
                user_agent = "a really really toxic bot")
        print("authenticated the bot")

    def delete_downvoted_comments(self) -> None:
        for com in self.reddit.user.me().comments.new(limit=300):
            if com.score < 0:
                com.delete()

    def get_list_of_already_replied(self) -> None:
        if not os.path.isfile("already_replied.txt"):
            self.already_replied = []
        else:
            with open("already_replied.txt", "r") as f:
                self.already_replied = f.read()
                self.already_replied = self.already_replied.split("\n")
                self.already_replied = filter(None, self.already_replied)

    def check_trigger_comments(self) -> bool:
        print(f"Obtaining {self.comment_num} comments ...")
        self.get_list_of_already_replied()
        for comment in self.reddit.subreddit('all').comments(limit=self.comment_num):
            com_body = comment.body
            if any(word in com_body for word in self.insult_list) \
            and comment.id not in self.already_replied \
            and comment.author != self.reddit.user.me():
                self.target_comment = comment
                return True
        return False

    def reply_to_trigger_comment(self) -> None:
        self.target_comment.reply(self.insult_text)
        print("replied to {}".format(str(self.target_comment.author)))

    def get_my_insult(self) -> str:
        self.num_lines = self.get_num_lines_in_file()
        self.n_for_file = random.randrange(1,self.num_lines)
        reply_text = self.get_nth_line_in_file()
        return reply_text

    def mark_replied(self) -> None:
        with open ("already_replied.txt", "a") as f:
            f.write(self.target_comment.id + "\n")

    def run_bot(self) -> None:
        try:
            self.comment_num = 25
            found_trigger_comment = self.check_trigger_comments()
            if found_trigger_comment:
                self.insult_text = self.get_my_insult()
                self.reply_to_trigger_comment()
                self.mark_replied()
        except Exception as e:
#            if e == praw.exceptions.APIException:
                print("waiting for a minute")
                time.sleep(60)
                pass

    def reply_to_inbox(self) -> None:
        for reply in self.reddit.inbox.comment_replies():
            try:
                reply.reply("You just replied to a bot. Congrats!")
                reply.mark_replied()
            except Exception as e:
#                if e == praw.exceptions.APIException:
                    print("waiting for a minute")
                    time.sleep(60)
                    pass
