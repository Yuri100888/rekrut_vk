import vk_api

session = vk_api.VkApi(
    token='введите токен')
vk = session.get_api()


def get_dialogs_list():
    '''возвращает список словарей непрочитанных сообщений {имя_пользователя:текст_сообщения}'''
    dialogs_list = vk.messages.getConversations(count=10, filter='unread')
    it = dialogs_list['items']
    dialogs = []
    for i in it:
        user_id = i['conversation']['peer']['local_id']
        user_info = get_users_info(user_id)
        user_name = f"{user_info[0]['last_name']} {user_info[0]['first_name']}"
        text_mess = i['last_message']['text']
        dict_ev = {user_name: text_mess}
        dialogs.append(dict_ev)
    return dialogs


def send_message(id, msg):
    '''отправляет сообщения msg пользователю id'''
    vk.messages.send(user_id=id, message=msg, random_id=0)


def get_friends(id):
    '''принимает id интересующего нас человека и возвращает список ID его друзей'''
    friends_list = vk.friends.get(user_id=id)
    return friends_list


def get_users_info(id):
    '''принимает id интересующего нас человека и возвращает информацию о нем'''
    idies_info = vk.users.get(user_ids=id)
    return idies_info

#___________Проверки исправности________
# send_message('ку-ку')
# print(get_friends())
# print(get_users_info())
# print(get_dialogs_list())
# print(get_users_info(get_dialogs_list()))
# get_dialogs_list()
