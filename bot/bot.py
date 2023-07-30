import telebot
from telebot import types
import mail
import connector

# import composer_table
# from composer_table import *

bot = telebot.TeleBot('6212331908:AAHaPNBTXNvvhXJty5tWQc0ih6_3Y8m48PQ')
info = {}
groups = ["Admins", "Buh", "CEO", "Crimea", "Fired", "Fired", "Guest", "HoDep", "HR", "Msk", "Prog", "Reception", "Sales", "Sklad", "Tech", "Zakupki"]
rightgroup = 1
@bot.message_handler(commands=['start', 'help', 'support', 'create', 'tips'])
def handle_output(message):
    if message.text == "/start":
        hello_text = "☀️Добрый день!☀️\n\nЯ полноправный помощник компании <b>Bazis Telecom</b>!\n\nМне понятны только команды, а также я реагирую на нажатие кнопок.\n\nНажмите на 👉 /help для вывода более подробной информации о командах."
        remove_keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, hello_text, parse_mode="html", reply_markup=remove_keyboard)
    elif message.text == "/help":
        remove_keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "<b>Вам доступны следующие команды:</b>\n\n 👤 /create - Создать учётную запись\n 👽 /tips - Полезные советы по пользованию ботом\n 🆘 /support - Нашли ошибку? Сообщите, пожалуйста, поддержке!", parse_mode="html", reply_markup=remove_keyboard)
    elif message.text == "/support":
        remove_keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id,"Если вы обнаружили ошибку в работе бота, напишите @Barbarian_dm. Так же можете предлагать свои варианты по улучшению функционала!", reply_markup=remove_keyboard)
    elif message.text == "/create":
        remove_keyboard = types.ReplyKeyboardRemove()
        info = {}
        bot.send_message(message.from_user.id, "<b>👤Создание учётной записи👤</b>\n\nВы начали создание учётной записи Windows для компании <b>Bazis Telecom</b>!\n\n<u>Исходные данные:\n</u>Домен - bazis.local\n\n<b>Необходимо заполнить:</b> \n• Подразделение, в котором будет создан пользователь.\n• Имя\n• Фамилия\n• Логин для входа\n• Пароль\n• Почта(необязательно)", parse_mode='html', reply_markup=remove_keyboard)

        bot.send_message(message.from_user.id, "<b>Давайте начнём!</b>\n\nВведите имя пользователя на английском 👇",
                         parse_mode="html")
        bot.register_next_step_handler(message, handle_name)
    elif message.text == "/tips":
        tips = "💥<b>Полезные советы</b>💥\n\n1. Вместо того чтобы вписывать команды самостоятельно, вы можете нажать на интересующую команду, если увидите её в тексте. Она выполнится автоматически.\n2. Вы можете выбирать команды в <b>меню</b>, а также нажимать на появляющиеся под клавиатурой кнопки для выбора каких-либо дополнительных параметров в зависимости от команды.\n\n⏳ Количество полезных советов скоро вырастет :)"
        bot.send_message(message.from_user.id, tips, parse_mode='html')

def handle_name(message):
    info['name'] = message.text

    bot.send_message(message.from_user.id, "<b>Введите фамилию пользователя на английском 👇</b>",parse_mode="html")
    bot.register_next_step_handler(message, handle_surename)

def handle_surename(message):
    info['surename'] = message.text.upper()

    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    for i in groups:
        keyboard.add(types.KeyboardButton(i))

    bot.send_message(message.from_user.id,
                     "<b>Нажмите на кнопку с подраздрелением, в которое хотите поместить пользователя👇</b>",
                     parse_mode="html", reply_markup=keyboard)
    bot.register_next_step_handler(message, handle_group)

def handle_group(message):
    if message.text in groups:
        info['group'] = message.text
        remove_keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "<b>Введите логин пользователя👇</b>", parse_mode="html", reply_markup=remove_keyboard)
        bot.register_next_step_handler(message, handle_login)
    else:
        rightgroup = 0
        bot.send_message(message.from_user.id, "<b>Упс!</b>\n\nТакого подразделения не существует. Введите название подразделения ещё раз 👇", parse_mode="html")
        bot.register_next_step_handler(message, handle_group)

def handle_login(message):
    info['login'] = message.text

    bot.send_message(message.from_user.id, "<b>Введите пароль пользователя 👇</b>", parse_mode="html")
    bot.register_next_step_handler(message, handle_password)

def handle_password(message):
    info['password'] = message.text

    bot.send_message(message.from_user.id, "<b>Повторите пароль пользователя 👇</b>", parse_mode="html")
    bot.register_next_step_handler(message, handle_repeat_password)

def handle_repeat_password(message):
    info['password_repeat'] = message.text

    if info['password_repeat'] == info['password']:

        keyboard = types.ReplyKeyboardMarkup(row_width=1)
        keyboard.add(types.KeyboardButton("Да"))
        keyboard.add(types.KeyboardButton("Нет"))

        bot.send_message(message.from_user.id, "<b>Будете ли вы создавать почту для пользователя? </b>\n\nНажмите на соответствующую кнопку 👇", parse_mode="html", reply_markup=keyboard)
        bot.register_next_step_handler(message, handle_mail)
    else:
        bot.send_message(message.from_user.id, "<b>Упс!</b>\n\nПароли не совпадают. Введите пароль пользователя ещё раз 👇",
                         parse_mode="html")
        bot.register_next_step_handler(message, handle_password)

def handle_mail(message):

    remove_keyboard = types.ReplyKeyboardRemove()
    if (message.text == "Да"):
        bot.send_message(message.from_user.id, "<b>Введите почту пользователя:</b>👇\n\n*почта должна оканчиваться на @bztel.ru или @bztel.store", parse_mode="html", reply_markup=remove_keyboard)
        bot.register_next_step_handler(message, handle_itogo)
    elif (message.text == "Нет"):
        info['mail'] = 0

        text = f"<b>Будет создан пользователь:</b>\n\nИмя: {info['name']}\nФамилия: {info['surename']}\n<b>Подразделение:</b> {info['group']}\n<b>Логин для входа:</b> {info['login']}\n<b>Пароль:</b> {info['password']}\n\n⚠Подтвердите создание.\nВ случае подтверждения будет создана учётная запись, под которой можно зайти на любой компьютер в офисе."
        bot.send_message(message.from_user.id, text, parse_mode='html')
        bot.register_next_step_handler(message, create_user)
def handle_itogo(message):
    if "@b" in message.text:
        info['mail'] = message.text

        keyboard = types.ReplyKeyboardMarkup(row_width=1)
        keyboard.add(types.KeyboardButton("Да"))
        keyboard.add(types.KeyboardButton("Нет"))
        text = f"<b>Будет создан пользователь:</b>\n\nИмя: {info['name']}\nФамилия: {info['surename']}\n<b>Подразделение:</b> {info['group']}\n<b>Логин для входа:</b> {info['login']}\n<b>Пароль:</b> {info['password']}\n<b>Почтовый ящик:</b> {info['mail']} \n\n⚠Подтвердите создание.\nВ случае подтверждения будет создана учётная запись, под которой можно зайти на любой компьютер в офисе."
        bot.send_message(message.from_user.id, text, parse_mode='html', reply_markup=keyboard)
        bot.register_next_step_handler(message, create_user)
        print(info)
    else:
        bot.send_message(message.from_user.id, "⚠Почта записана в неправильном формате.\nВведите почту ещё раз: ", parse_mode='html')
        bot.register_next_step_handler(message, handle_itogo)
def create_user(message):
    remove_keyboard = types.ReplyKeyboardRemove()
    if message.text == "Да":

        bot.send_message(message.from_user.id, "Создание пользователя...\nЭто может занять до минуты, ждите!",
                         parse_mode='html', reply_markup=remove_keyboard)


        if info['mail'] != 0:
            email = mail.execute_command_with_sudo(info['mail'])

        request = connector.put(info)

        if request and info['mail'] != 0:
            # bot.send_message(message.from_user.id, f"✅Учётная запись создана✅\n\n<b>Логин для входа:</b> {info['login']}\n<b>Пароль:</b> {info['password']}\nПочтовый ящик: {email_creditials[0]}\nПароль от почты: {email_creditials[1]}",
            #              parse_mode='html')
            bot.send_message(message.from_user.id,
                             f"✅Учётная запись создана✅\n\n<b>Подразделение:</b> {info['group']}\n<b>Логин для входа:</b> {info['login']}\n<b>Пароль:</b> {info['password']}\n\n<b>Почта:</b>\n{email}",
                          parse_mode='html')
        elif request and info['mail'] == 0:
            bot.send_message(message.from_user.id,
                             f"✅Учётная запись создана✅\n\n<b>Логин для входа:</b> {info['login']}\n<b>Пароль:</b> {info['password']}\n\n<b>Подразделение:</b> {info['group']}",
                             parse_mode='html')
        else:
            bot.send_message(message.from_user.id, "<b>Что-то пошло не так...</b>", parse_mode='html')


        # bot.send_message(message.from_user.id,
        #                  f"✅Учётная запись создана✅\n\n<b>Логин для входа:</b> {info['login']}\n<b>Пароль:</b> {info['password']}\nПочтовый ящик: {email_creditials[0]}\nПароль от почты: {email_creditials[1]}",
        #                   parse_mode='html')

    elif message.text == "Нет":
        remove_keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "Ладно... Приходите в другой раз",
                         parse_mode='html', reply_markup=remove_keyboard)
    else:
        bot.send_message(message.from_user.id, "Ничего не понял... Запускайте создание пользователя заново с помощью /create",
                         parse_mode='html')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    remove_keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "⚠ Мне понятны только команды, а также я реагирую на нажатие кнопок.\n\nНажмите на 👉 /help для вывода более подробной информации о командах.", reply_markup=remove_keyboard)

bot.polling(none_stop=True, interval=0)