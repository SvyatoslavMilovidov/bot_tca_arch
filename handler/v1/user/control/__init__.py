"""
Виджеты тега control - управляющие команды.

Содержит виджеты:
- start_command_widget: Обработка /start
- help_command_widget: Обработка /help
- echo_widget: Эхо-ответ на текст
"""

# Импортируем виджеты для регистрации хендлеров
from handler.v1.user.control import start_command_widget
from handler.v1.user.control import help_command_widget
from handler.v1.user.control import echo_widget
