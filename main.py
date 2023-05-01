import asyncio
import os

import pandas as pd
import telebot
from load_dotenv import load_dotenv

import exceptions
import utils
import webparser

load_dotenv()

BOT_TOKEN = os.getenv('bot_token')
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        text=utils.START_MESSAGE,
        parse_mode='HTML',
    )


@bot.message_handler(commands=['excel'])
def handle_excel(message):
    bot.send_message(
        message.chat.id,
        text=utils.SEND_FILE,
        parse_mode='HTML',
    )
    bot.register_next_step_handler(message, handle_excel_file)


async def async_handle_excel_file(message):
    file = message.document

    if not file:
        bot.send_message(
            message.chat.id,
            utils.NOT_FILE_SENT,
            parse_mode='HTML',
        )
        bot.register_next_step_handler(message, handle_excel_file)
        return

    if not file.file_name.endswith('.xlsx'):
        bot.reply_to(message, utils.WRONG_FILE_FORMAT)
        bot.register_next_step_handler(message, handle_excel_file)
        return

    file_info = bot.get_file(file.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open('file.xlsx', 'wb') as f:
        f.write(downloaded_file)

    xl = pd.read_excel('file.xlsx', names=None)

    try:
        all_rows = await webparser.get_and_create_in_db_all_products(xl)
        content_file_as_message = utils.make_message_with_file_content(all_rows)
        bot.send_message(
            message.chat.id,
            text=f'Содержимое файла:\n{content_file_as_message}',
            parse_mode='HTML',
        )

    except exceptions.EmptyTableValueExceprion:
        bot.send_message(message.chat.id, text=utils.EMPTY_CELL)
        bot.register_next_step_handler(message, handle_excel_file)
        return

    except TypeError and IndexError:
        bot.send_message(message.chat.id, text=utils.WRONG_XPATH)
        return

    except exceptions.NotNumberInXPathException:
        bot.send_message(message.chat.id, text=utils.NOT_NUMBER_IN_XPATH)
        return


def handle_excel_file(message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(async_handle_excel_file(message))
    loop.close()


if __name__ == '__main__':
    # try:
        bot.polling()
    # except Exception as e:
    #     print(f'Ошибка бота - {e}')
    #     bot.polling()
