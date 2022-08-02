import instaloader
from instaloader import Profile,Post

instance=instaloader.Instaloader()

usersearch=input("Enter the username of the account you want to search :")
instance.login(user="",passwd="")
profile = instaloader.Profile.from_username(instance.context, usersearch)

# Print list of followees
for followee in profile.get_followers():
    print(followee)
    
instance.download_profile(profile_name=usersearch)