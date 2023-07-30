import paramiko
import time

def replace_first_occurrence(text, word_to_replace, replacement):
    index = text.find(word_to_replace)
    if index != -1:
        new_text = text[:index] + text[index:].replace(word_to_replace, replacement, 1)
        return new_text
    else:
        return text

def execute_command_with_sudo(email):
    try:
        # Создаем объект клиента SSH
        client = paramiko.SSHClient()
        # Устанавливаем политику подтверждения хоста (WARNING: это делается исключительно в целях примера и может быть небезопасно)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Подключаемся к удаленному хосту
        client.connect("198.18.37.3", username="bzadmin", password="maz0uK")

        # Создаем интерактивный сеанс
        channel = client.invoke_shell()

        # Отправляем команду "sudo -s"
        channel.send('sudo -s\n')
        time.sleep(1)

       # Отправляем пароль
        channel.send('maz0uK' + '\n')
        time.sleep(1)

        # Запускаем скрипт "mail" с вводом "1" и адресом почты
        channel.send(f'mail\n')
        time.sleep(1)
        output1 = channel.recv(1024).decode('utf-8')
        channel.send('1\n')  # Вводим "1"
        time.sleep(1)

        channel.send(f'{email}\n')  # Вводим адрес почты
        output1 = channel.recv(1024).decode('utf-8')
        time.sleep(1)

        # Читаем результаты выполнения скрипта
        output = channel.recv(1024).decode('utf-8')

        output = output.replace(output1, "")
        output = replace_first_occurrence(output, email, "")
        output = output.replace("Этого ты добивался?", "")
        try:
            output = output.replace("[?2004h", "")
        except:
            print("[?2004h не нашлось")
        output = output.replace("root@mail:/home/bzadmin#", "").strip()
        # Закрываем соединение
        channel.close()
        client.close()


        return output
    except paramiko.AuthenticationException:
        print("Ошибка аутентификации. Проверьте имя пользователя и пароль.")
    except paramiko.SSHException as e:
        print(f"Ошибка при подключении или выполнении команды: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")
