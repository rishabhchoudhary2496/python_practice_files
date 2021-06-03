import instapy


accounts = ['rishabh.2496','robin.benjamin.125','amit.kumar.230',]
comments = ['Awesome', 'Really Cool', 'I like your stuff','Nice Shot','This post is 🔥']



session = instapy.InstaPy(username="idont_wantit",password="pupeeteer")
session.login()
session.set_skip_users(skip_private=False)
# session.set_quota_supervisor(enabled=True,
#                             sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
#                             sleepyhead=True,
#                             stochastic_flow=True,
#                             notify_me=True,
#                             peak_likes_hourly=57,
#                             peak_likes_daily=300,
#                             peak_comments_hourly=15,
#                             peak_comments_daily=180,
#                             peak_follows_hourly=30,
#                             peak_follows_daily=None,
#                             peak_server_calls_hourly=None,
#                             peak_server_calls_daily=4700)
# session.set_do_follow(enabled=True,percentage=10,times=2)
# session.follow_by_list(followlist=accounts, times=1,sleep_delay=600,interact=True)
# session.follow_user_followers(accounts,amount=15,randomize=True,sleep_delay=60)
# session.set_do_like(enabled=True, percentage=90)
# session.set_do_comment(enabled=True, percentage=25)
# session.like_by_feed(amount=100, randomize=True, unfollow=True, interact=True)


# session.set_do_like(True, percentage=70)
# session.interact_by_users(accounts,amount=10,randomize=True,media='Photo')