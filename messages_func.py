from tok import tok
import vk_api

session = vk_api.VkApi(token='введите токен')
vk = session.get_api()


def send_message(msg):
    vk.messages.send(user_id="", message=msg, random_id=0)





def get_friends(id):
    friends_list = vk.friends.get(user_id=id)
    return friends_list


def get_users_info(id):
    idies_info = vk.users.get(user_ids=id, fields="country, city")
    return idies_info


# send_message('ку-ку')
# print(get_friends())
print(get_users_info())
