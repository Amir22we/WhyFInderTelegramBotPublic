from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from keep_alive import keep_alive
import asyncio

keep_alive()

API_TOKEN = ""

bot = Bot(token=API_TOKEN)

dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer(f"Привет {message.from_user.full_name}! Каждая проблема имеет решение, нужно только найти её корень. Напиши, что тебя беспокоит, и мы начнем поиск вместе! Для подробной информации можешь прочитать этот пост: https://t.me/bunkeramira/1952 ")
    sticker_id = "CAACAgIAAxkBAANmZ1bdaImWNUoBhyy8JiGJKUUuARcAAvEQAAJHNzhJzmVlPiO9EzM2BA"
    await bot.send_sticker(chat_id=message.chat.id, sticker=sticker_id)

@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "👋 Привет!\n\n"
        "Меня зовут Амир, я 17-летний программист, и это мой первый проект на aiogram. Надеюсь, вам понравится пользоваться этим ботом! 😊\n\n"
        "💡 Если разобрались с вашей проблемой, просто напишите: /stop и бот остановится.\n"
        "Если нужна дополнительная поддержка — пропишите команду /need_help, и бот снова начнет сеанс!\n\n"
        "📢 Не забудьте подписаться на мой канал! Там я делюсь своими проектами, мыслями и полезными материалами: @bunkeramira. Поддержите меня, это очень важно для меня! 🙏\n\n"
        "И напоследок:\n"
        "✨ Счастья, мира и добра вам! ✨\n"
        "Помните, что всё будет хорошо, даже если сейчас кажется иначе. Просто идите вперёд и верьте в себя! 💪"
    )

@dp.message(Command("need_help"))
async def more_why_help_command(message: Message):
    await message.reply(
        "Что произошло?\n\n"
        "Пожалуйста, поделись со мной своей проблемой, и я постараюсь тебе помочь! 🛠\n\n"
        "Не стесняйся, вместе мы обязательно найдём решение! 💡"
    )

@dp.message(Command("stop"))
async def stop_why_help_command(message: Message):
    await message.reply("Рад был помочь, если нужна еще помощь то /need_help")

@dp.message()
async def why_command(message: Message):
    await message.reply(f"Почему вы были в таком состояние: {message.text}?")

async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
