"""
Виджет: Команда /help.

Показывает справочную информацию о боте.

Доступен из:
1. любое состояние (команда /help доступна всегда)
   - Из какого state: любое (*)
   - Из какого answer: — (команда)

Переводит в:
- Не меняет состояние
"""

from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from handler.v1.user.router import control_router
from core.vocab import COMMANDS, DEFAULT_LANGUAGE

# Импортируем компоненты из node
from node.control.trigger import HelpCommandTrigger
from node.control.code import HelpCommandCode
from node.control.answer import HelpAnswer

# Реестр Answer-ов для этого виджета
ANSWER_REGISTRY = {
    "help": HelpAnswer(),
}


@control_router.message(Command(COMMANDS["help"]))
async def handle_help_command(
    message: Message,
    state: FSMContext,
) -> None:
    """
    Главный хендлер команды /help.

    Входные состояния: любое (*)
    Выходные состояния: не меняет

    FSM на входе:
    - нет обязательных полей

    FSM на выходе:
    - нет записей

    Возможные Answer:
    - help (HelpAnswer) - всегда
      Показывает: справочное сообщение
      Компонент: node/control/answer/help_answer.py

    Архитектура:
    1. HelpCommandTrigger - извлечение данных
    2. HelpCommandCode - подготовка данных
    3. HelpAnswer - отображение справки
    """
    # Шаг 1: Trigger
    trigger = HelpCommandTrigger()
    trigger_data = await trigger.run(message, state)

    # Шаг 2: Code
    code = HelpCommandCode()
    code_result = await code.run(trigger_data, state)

    # Шаг 3: Answer
    answer = ANSWER_REGISTRY[code_result["answer_name"]]
    await answer.run(
        event=message,
        user_lang="ru",
        data=code_result["data"],
    )
