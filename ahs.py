import instaloader
from instaloader import Profile,Post

instance=instaloader.Instaloader()

usersearch=input("Enter the username of the account you want to search :")#enter username of id you want to download and 
instance.login(user="",passwd="")  #write username and password there of Your id
profile = instaloader.Profile.from_username(instance.context, usersearch)

# Print list of followees
for followee in profile.get_followers():
    print(followee)
    
instance.download_profile(profile_name=usersearch)
