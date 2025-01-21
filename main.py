from instagrapi import Client
import os
import json
import time

username = os.getenv("USER_NAME")
password = os.getenv("PASS_WORD")
cl = Client()

# Attempt to load or create session
session_file = "session.json"
if os.path.exists(session_file):
    try:
        cl.load_settings(session_file)
        cl.login(username, password)
    except Exception:
        os.remove(session_file)
        cl.login(username, password)
        cl.dump_settings(session_file)
else:
    cl.login(username, password)
    cl.dump_settings(session_file)

# Fetch user ID
try:
    user_id = cl.user_id_from_username("trainwithjoan")
except Exception as e:
    print(f"Failed to fetch user ID: {e}")
    exit()

# Fetch the last 10 media posts
medias = cl.user_medias(user_id, 10)
last_ten_post_id = [(media, media.id) for media in medias]

# Save comments for each post
for index, (post, post_id) in enumerate(last_ten_post_id):
    comments = cl.media_comments(post_id, post.comment_count)
    comment_list = [comment.text for comment in comments]

    file_name = f"media_post{index + 1}.json"
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            json.dump(comment_list, file, indent=4)
    else:
        with open(file_name, "r+") as file:
            existing_comments = json.load(file)
            existing_comments.extend(comment_list)
            file.seek(0)
            json.dump(existing_comments, file, indent=4)

time.sleep(120)
