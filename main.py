from instagrapi import Client
import os
import json

username=os.getenv("NAME") 
password=os.getenv("PASSWORD")
cl = Client()
cl.login(username, password)
user_id = cl.user_id_from_username("growwithjo")

medias = cl.user_medias(user_id, 1)
media_object =medias[0]
#for post_id in medias:
 
media_id = media_object.id
comment_count =media_object.comment_count
commments =cl.media_comments(media_id,comment_count)

for comment in commments:
    print("Comment inserted!")

    with open ('comments.json','w') as comments :
        json.dump(f"{comment.text}\n",comments)