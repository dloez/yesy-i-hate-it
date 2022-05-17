"""Tests for main.py"""
import pytest
import tweepy

from yes_i_hate_it.main import get_tweets
from yes_i_hate_it.main import load_env
from yes_i_hate_it.main import TWITTER_API_KEY, TWITTER_API_SECRET
from yes_i_hate_it.main import TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET, TWITTER_BEARER_TOKEN

from yes_i_hate_it.exceptions import ValueExceeded, ValueInferior


def test_load_env():
    """Test main.load_env function"""
    tokens = load_env()
    assert isinstance(tokens, dict)

    assert TWITTER_API_KEY in tokens
    assert isinstance(tokens[TWITTER_API_KEY], str)

    assert TWITTER_API_SECRET in tokens
    assert isinstance(tokens[TWITTER_API_SECRET], str)

    assert TWITTER_ACCESS_TOKEN in tokens
    assert isinstance(tokens[TWITTER_ACCESS_TOKEN], str)

    assert TWITTER_ACCESS_SECRET in tokens
    assert isinstance(tokens[TWITTER_ACCESS_SECRET], str)

    assert TWITTER_BEARER_TOKEN in tokens
    assert isinstance(tokens[TWITTER_BEARER_TOKEN], str)


def test_get_tweets():
    """Test main.get_tweets"""
    max_results = 10
    user_name = 'javieff16YT'
    tweets = get_tweets(user_name, max_results)

    assert isinstance(tweets, list)
    assert len(tweets) == max_results - 1
    assert isinstance(tweets[0], tweepy.tweet.Tweet)

    with pytest.raises(ValueExceeded):
        get_tweets(user_name, 102)

    with pytest.raises(ValueInferior):
        get_tweets(user_name, 1)
