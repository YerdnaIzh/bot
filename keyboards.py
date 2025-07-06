from pyrogram.types import ReplyKeyboardMarkup
import buttons

# Главная клавиатура
main_keyboard = ReplyKeyboardMarkup(
	keyboard = [
		[buttons.time_button, buttons.help_button], # первый ряд клавиатуры
		[buttons.search_films, buttons.random_films],
		[buttons.settings_button] # второй ряд клавиатуры
	], resize_keyboard = True)

# Клавиатура настроек
settings_keyboard = ReplyKeyboardMarkup(
	keyboard = [
		[buttons.back_button]
	], resize_keyboard = True
)

# Домашнее задание/TODO:
# кнопки для /search_films и /random_films также должны быть в какой-то клавиатуре
