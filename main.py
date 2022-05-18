from instagrapi import Client
from login import ACCOUNT_USERNAME, ACCOUNT_PASSWORD
import json

# Instagram login

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)


# Get and post the data

with open('posts/posts.json', 'r') as data_file:
    data = json.load(data_file) # Get the info from json

for i in data: # Post the first file in json
    media = cl.photo_upload(
        data[str(i)]["PATH"],
        data[str(i)]["TEXT"] 
    )

    data.pop(str(i)) # Delete already used data
    with open('posts/posts.json', 'w') as data_file:
        data = json.dump(data, data_file, indent=4) # Commit the changes!

    break

print('Done!!')