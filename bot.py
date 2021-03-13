API_KEY = "NA"
API_SECRET_KEY = "NA"
BEARER_TOKEN = "NA"
ACCESS_TOKEN = "NA"
ACCESS_TOKEN_SECRET = "NA"

import tweepy


def update_bot(cur_v, cur_date, cur_v2, prev_v, prev_date, prev_v2):

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    increase_1 = cur_v - prev_v
    increase_2 = cur_v2 - prev_v2

    p1 = 100 * (cur_v / 4900000)
    p2 = 100 * (cur_v2 / 4900000)

    MESSAGE = """{:,} people ({:0.2f}% of the population) have received their first dose. (+{:,} since {})
    
{:,} people ({:0.2f}% of the population) have received their second dose. (+{:,} since {})

               """.format(cur_v, p1, increase_1, prev_date, cur_v2, p2, increase_2, prev_date)

    api.update_status(MESSAGE)

