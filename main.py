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
comments =cl.media_comments(media_id,comment_count)

comment_list =[]

for comment in comments:
    comment_text=comment.text
    comment_text.rstrip()
    comment_list.append(comment_text)
    print("Comments appened!")


for comment in comment_list:
    with open ('comments.json','a') as comments :
        json.dump(comment,comments,indent=4)
        comments.write("\n")