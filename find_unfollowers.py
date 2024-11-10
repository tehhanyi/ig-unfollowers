import instaloader
from firefox_session import loginFromSession

def find_unfollowers(loader, username):
    profile = instaloader.Profile.from_username(loader.context, username)

    print ("loading followers...")
    followers = profile.get_followers()
    print ("now loading followees...")
    followings = profile.get_followees()

    followers_set = {follower.username for follower in followers}
    print("Total followers:", len(followers_set))
    followings_set = {following.username for following in followings}
    print("Total followee:", len(followings_set))

    if username == "tehhanyi":
        with open('influencers.txt', 'r') as file:
            influencers = {line.strip() for line in file}
    else:
        influencers = set()

    non_follow_back = followings_set - followers_set - influencers
    print("\nUsers who don't follow you back:")
    for user in non_follow_back:
        print(user)

def loginWithCredentials():
    import getpass

    loader = instaloader.Instaloader()

    username = input("Username: ")
    password = getpass.getpass("Password: ")
    try:
        loader.login(username, password)
    except instaloader.TwoFactorAuthRequiredException:
        two_factor_code = input("Enter the 2FA code: ")
        loader.two_factor_login(two_factor_code)
    except instaloader.WrongPasswordException:
        print("Wrong password")
        password = input("Password: ")
        loader.login(username, password)

if __name__ == "__main__":
    loader, username = loginFromSession() #loginWithCredentials() when instaloader.exceptions.BadCredentialsException fixed
    find_unfollowers(loader, username)