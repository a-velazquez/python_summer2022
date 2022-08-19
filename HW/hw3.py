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

# Create user objects
wps_user = api.get_user(screen_name="@WUSTLPoliSci")
wps_user  # biiiig object

type(wps_user)
dir(wps_user)


wps_user.followers_count
wps_user_5000 = api.get_follower_ids(
    user_id=wps_user.id
)  # creates a list of user ids - up to 5000
len(wps_user_5000)
wps_user_5000[0]


wps_user_friends = api.get_friend_ids(
    user_id=wps_user.id
)  # creates a list of user ids - up to 5000
len(wps_user_friends)


def get_info(id_list):
    all_users = []

    total = len(id_list)
    counter = 0

    for uid in id_list:

        counter += 1

        print(f"Now on user {counter} of {total}")

        users = {}
        try:
            usr = api.get_user(user_id=uid)

            users["screen_name"] = usr.screen_name
            users["user_id"] = usr.id
            users["n_tweets"] = usr.statuses_count
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

            all_users.append(users)

            time.sleep(random.uniform(5, 10))

        except tweepy.errors.TwitterServerError:

            return all_users

    return all_users


def one_degree_separation(screen_nm):

    answers = {
        "most_active_follower": {},
        "most_popular_follower": {},
        "most_active_friends": {"layman": {}, "celebrity": {}, "expert": {}},
        "most_popular_friend": {},
    }

    print("On Followers List")
    follower_ids = api.get_follower_ids(screen_name=screen_nm)

    print("On Friends List")
    friend_ids = api.get_friend_ids(screen_name=screen_nm)

    followers = pd.DataFrame(get_info(follower_ids))
    print("Followers DF: ", followers.shape, " out of", len(follower_ids))

    friends = pd.DataFrame(get_info(friend_ids))
    print("Friends DF: ", friends.shape, " out of", len(friend_ids))

    answers["most_active_follower"]["user"] = followers.sort_values(
        "n_tweets", ascending=False
    ).iloc[0]["screen_name"]
    answers["most_active_follower"]["tweets"] = followers.sort_values(
        "n_tweets", ascending=False
    ).iloc[0]["n_tweets"]

    for df, nm in zip((friends, followers), ("friend", "follower")):

        key = f"most_popular_{nm}"

        answers[key]["user"] = df.sort_values("n_followers", ascending=False).iloc[0][
            "screen_name"
        ]
        answers[key]["followers"] = df.sort_values("n_followers", ascending=False).iloc[
            0
        ]["n_followers"]

    for var in ("layman", "celebrity", "expert"):

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

    return answers, followers, friends


results, followers_df, friends_df = one_degree_separation("@WUSTLPoliSci")

""" {'most_active_follower': {'user': 'TheNjoroge', 'tweets': 171008},
 'most_popular_follower': {'user': 'mariapaularomo', 'followers': 357041},
 'most_active_friends': {'layman': {'user': 'usmanfalalu1', 'tweets': 1440},
  'celebrity': {'user': 'nytimes', 'tweets': 481384},
  'expert': {'user': 'prof_nokken', 'tweets': 20334}},
 'most_popular_friend': {'user': 'BarackObama', 'followers': 132544268}} """
