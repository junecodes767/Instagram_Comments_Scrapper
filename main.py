from instagrapi import Client
import os
import json

username=os.getenv("NAME") 
password=os.getenv("PASSWORD")
cl = Client() # instagram object

#login to api
cl.login(username, password)

#used to access the clients fitness account
user_id = cl.user_id_from_username("growwithjo")

#list that contains the id of the each post
last_ten_post=[]

#accesses the last three posts from the clients fitness account
medias = cl.user_medias(user_id, 3)

#post number 1
media_object =medias[0]

#post number 1 media id
mo_id =media_object.id
last_ten_post.append(mo_id) #appends to list

#post number 2
media_object_2 =medias[1]

#post number 2 media id
mo_id_2 = media_object_2.id
last_ten_post.append(mo_id_2) #appends to list

#post number 3
media_object_3 =medias[2]

#post number 3 media id
mo_id_3 =media_object_3.id
last_ten_post.append(mo_id_3) #appends to list

 
 
for ids in last_ten_post:
    print(ids)
 

#list that contains the media id of 10 posts


# media_id = media_object.id
# comment_count =media_object.comment_count
# comments =cl.media_comments(media_id,comment_count)

# comment_list =[]

# for comment in comments:
#     comment_text=comment.text
#     comment_text.rstrip()
#     comment_list.append(comment_text)
#     print("Comments appened!")


# for comment in comment_list:
#     with open ('comments.json','a') as comments :
#         json.dump(comment,comments,indent=4)
#         comments.write("\n")