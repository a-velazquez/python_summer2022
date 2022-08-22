#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 3

Created on Tue Aug 16 14:59:55 2022

@author: Alma Velazquez
"""

import os
import importlib
import tweepy
import pandas as pd
import random
import time

twitter = importlib.import_module("start_twitter")
api = twitter.client


# inner loop
def get_info(id_list, part_1=True):
    """For a list of user ids, gather user attributes for each and return them
    in a list of dictionaries."""

    # instantiate empty list
    all_users = []

    # store total and define counter
    total = len(id_list)
    counter = 0

    for uid in id_list:

        counter += 1

        print(f"Now on user {counter} of {total}")

        # instantiate empty dict per user
        users = {}

        try:
            usr = api.get_user(user_id=uid)

            # these attributes are needed for both parts of the hw
            users["screen_name"] = usr.screen_name
            users["user_id"] = usr.id
            users["n_tweets"] = usr.statuses_count

            if part_1:
                # these attributes are only needed for the first part of the hw
                users["n_followers"] = usr.followers_count
                users["n_friends"] = usr.friends_count

                if usr.followers_count < 100:
                    # layman
                    users["layman"] = True
                    users["expert"] = False
                    users["celebrity"] = False
                elif usr.followers_count > 1000:
                    # celebrity
                    users["layman"] = False
                    users["expert"] = False
                    users["celebrity"] = True
                else:
                    # expert
                    users["layman"] = False
                    users["expert"] = True
                    users["celebrity"] = False

            # add dict to list
            all_users.append(users)

            # sleeping avoids hitting the rate limit
            time.sleep(random.uniform(5, 10))

        except tweepy.errors.TwitterServerError:
            # if one of the above iterations hits an error, return the list up
            # to that point
            return all_users

    return all_users


def one_degree_separation(screen_nm):

    # instantiate the dict that will contain the answers
    answers = {
        "most_active_follower": {},
        "most_popular_follower": {},
        "most_active_friends": {"layman": {}, "celebrity": {}, "expert": {}},
        "most_popular_friend": {},
    }

    # get lists of ids for followers and friends
    print("On Followers List")
    follower_ids = api.get_follower_ids(screen_name=screen_nm)

    print("On Friends List")
    friend_ids = api.get_friend_ids(screen_name=screen_nm)

    # use the above defined get_info function for followers
    # store in a dataframe for easier sorting later
    followers = pd.DataFrame(get_info(follower_ids))
    print("Followers DF: ", followers.shape, " out of", len(follower_ids))

    # repeat for friends
    friends = pd.DataFrame(get_info(friend_ids))
    print("Friends DF: ", friends.shape, " out of", len(friend_ids))

    # use sort_values by n_tweets to get the username and number of tweets
    # of the most active follower
    answers["most_active_follower"]["user"] = followers.sort_values(
        "n_tweets", ascending=False
    ).iloc[0]["screen_name"]
    answers["most_active_follower"]["tweets"] = followers.sort_values(
        "n_tweets", ascending=False
    ).iloc[0]["n_tweets"]

    # get the most popular friend and follower using both dataframes
    for df, nm in zip((friends, followers), ("friend", "follower")):

        key = f"most_popular_{nm}"

        answers[key]["user"] = df.sort_values("n_followers", ascending=False).iloc[0][
            "screen_name"
        ]
        answers[key]["followers"] = df.sort_values("n_followers", ascending=False).iloc[
            0
        ]["n_followers"]

    for var in ("layman", "celebrity", "expert"):
        # get most active friends by category
        answers["most_active_friends"][var]["user"] = (
            friends.loc[friends[var]]
            .sort_values("n_tweets", ascending=False)
            .iloc[0]["screen_name"]
        )
        answers["most_active_friends"][var]["tweets"] = (
            friends.loc[friends[var]]
            .sort_values("n_tweets", ascending=False)
            .iloc[0]["n_tweets"]
        )
    # return the dictionary and both dataframes, which are needed in part 2
    return answers, followers, friends


# fuunction call
part_1_results, followers_df, friends_df = one_degree_separation("@WUSTLPoliSci")


# part 1 answers
""" {'most_active_follower': {'user': 'TheNjoroge', 'tweets': 171008},
 'most_popular_follower': {'user': 'mariapaularomo', 'followers': 357041},
 'most_active_friends': {'layman': {'user': 'usmanfalalu1', 'tweets': 1440},
  'celebrity': {'user': 'nytimes', 'tweets': 481384},
  'expert': {'user': 'prof_nokken', 'tweets': 20334}},
 'most_popular_friend': {'user': 'BarackObama', 'followers': 132544268}} """


# outer loop
def f_of_f(id_list, user_type):
    """Given a list of ids, and a user type (friend or follower), apply the get info 
    function to each of THEIR [user type]."""

    total = len(id_list)
    counter = 0

    more_users = pd.DataFrame()
    # instantiate empy list to which append error-causing ids are appended
    bad_ids = []

    for uid in id_list:
        counter += 1
        # informative outer-level print statement
        print(f"Now on user {counter} out of {total}")

        try:
            # run the appropriate tweepy function by user type
            if user_type == "friend":
                temp = api.get_friend_ids(user_id=uid)
            else:
                temp = api.get_follower_ids(user_id=uid)

            time.sleep(random.uniform(5, 10))
            # use get_info to get all the information of the individuals
            # in 'temp'
            more_users = pd.concat(
                [more_users, pd.DataFrame(get_info(temp, part_1=False))]
            )

        except:
            bad_ids.append(uid)
            pass

    # return the dataframe and the list of bad ids
    return more_users, bad_ids


# call the above function for friends and followers, using filtering and pandas Series tolist()
# function; both calls will return dataframes of the 2-degree separated users to append to the originals

"""Neither of the next two lines finished in time; the first one (friends of friends) was called
Friday at 7pm and by Sunday night had only reached 60 out of 101 direct WashU PoliSci friends. """

friends_of_friends, bad_friends = f_of_f(
    friends_df.loc[friends_df.layman | friends_df.expert]["user_id"].tolist(), "friend"
)

followers_of_followers, bad_followers = f_of_f(
    followers_df.loc[followers_df.layman | followers_df.expert]["user_id"].tolist(),
    "follower",
)

# Store part 2 results in a dictionary
part_2_results = {
    "most_active_friend_of_friends": {},
    "most_active_follower_of_followers": {},
}

# sort the dataframes and then isolate the record with the highest tweet number
part_2_results["most_active_friend_of_friends"]["tweets"] = (
    pd.concat([friends_df, friends_of_friends[["screen_name", "user_id", "n_tweets"]]])
    .sort_values("n_tweets", ascending=False)
    .iloc[0]["n_tweets"]
)


part_2_results["most_active_friend_of_friends"]["user"] = (
    pd.concat([friends_df, friends_of_friends[["screen_name", "user_id", "n_tweets"]]])
    .sort_values("n_tweets", ascending=False)
    .iloc[0]["screen_name"]
)


part_2_results["most_active_follower_of_followers"]["tweets"] = (
    pd.concat(
        [followers_df, followers_of_followers[["screen_name", "user_id", "n_tweets"]]]
    )
    .sort_values("n_tweets", ascending=False)
    .iloc[0]["n_tweets"]
)


part_2_results["most_active_follower_of_followers"]["user"] = (
    pd.concat(
        [followers_df, followers_of_followers[["screen_name", "user_id", "n_tweets"]]]
    )
    .sort_values("n_tweets", ascending=False)
    .iloc[0]["screen_name"]
)
