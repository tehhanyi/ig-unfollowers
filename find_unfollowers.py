import instaloader
import getpass

username = input("Username: ")
password = getpass.getpass("Password: ")
try:
    instaloader.Instaloader().login(username, password)
except instaloader.TwoFactorAuthRequiredException:
    two_factor_code = input("Enter the 2FA code: ")
    instaloader.Instaloader().two_factor_login(two_factor_code)
# except instaloader.WrongPasswordException:
#     print("Wrong password")
#     password = input("Password: ")
#     L.login(username, password)

profile = instaloader.Profile.from_username(L.context, username)

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

