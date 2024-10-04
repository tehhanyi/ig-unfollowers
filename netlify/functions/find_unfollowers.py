import json
import instaloader

def handler(event, context):
    body = json.loads(event['body'])
    username = body['username']
    password = body['password']
    two_factor_code = body.get('twoFactorCode')

    loader = instaloader.Instaloader()

    try:
        loader.login(username, password)
    except instaloader.TwoFactorAuthRequiredException:
        if two_factor_code:
            loader.two_factor_login(two_factor_code)
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({"error": "2FA code required"})
            }

    profile = instaloader.Profile.from_username(loader.context, username)

    followers = profile.get_followers()
    followings = profile.get_followees()

    followers_set = {follower.username for follower in followers}
    followings_set = {following.username for following in followings}

    if username == "tehhanyi":
        with open('influencers.txt', 'r') as file:
            influencers = {line.strip() for line in file}
    else:
        influencers = set()

    non_follow_back = followings_set - followers_set - influencers

    result = {
        "total_followers": len(followers_set),
        "total_followings": len(followings_set),
        "unfollowers": list(non_follow_back)
    }

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }