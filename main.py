from instagrapi import Client
import os
import json
import time
from instagrapi.exceptions import LoginRequired


username=os.getenv("USER_NAME") 
password=os.getenv("PASS_WORD") 
cl = Client() # instagram object

# Attempt to load session settings from a file
session_file = "session.json"
if os.path.exists(session_file):
    try:
        cl.load_settings(session_file)
    except Exception as e:
        print("Session file is invalid, logging in again.")
        cl.login(username, password)
        cl.dump_settings(session_file)
else:
    
    cl.login(username, password)
    cl.dump_settings(session_file)

#used to access the clients fitness account
user_id = cl.user_id_from_username("trainwithjoan")

#list that contains the id of the each post
last_ten_post_id=[]

#accesses the last three posts from the clients fitness account
medias = cl.user_medias(user_id, 10)

#loops through 10 media post and appends id and object to list in the form of a tuple
for i,media_obj in enumerate(medias):
    t_media= media_obj,media_obj.id
    last_ten_post_id.append(t_media)
    
for index, (post, post_id) in enumerate(last_ten_post_id):
    #number of comments for that post
    comment_count =post.comment_count

    #list of comments for a given post
    comments =cl.media_comments(post_id,comment_count)

#Extract comments into the list
    comment_list =[ comment.text for comment in comments]
    
    file_name = f"media_post{index+1}.json"


    # Check if the file exists; if not, create and write comments
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            json.dump(comment_list, file, indent=4)
    else:
        # If the file exists, append new comments
        with open(file_name, 'r+') as file:
            existing_comments = json.load(file)
            existing_comments.extend(comment_list)
            file.seek(0)
            json.dump(existing_comments, file, indent=4)      
time.sleep(120)  