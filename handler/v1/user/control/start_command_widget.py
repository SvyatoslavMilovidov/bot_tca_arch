"""
Виджет: Команда /start.

Точка входа в бота. Показывает приветственное сообщение.

Доступен из:
1. entry (команда /start)
   - Из какого state: любое (*)
   - Из какого answer: — (команда)

Переводит в:
- Остается в idle состоянии, ожидая текстовое сообщение
"""

from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from handler.v1.user.router import control_router
from core.vocab import COMMANDS, DEFAULT_LANGUAGE

# Импортируем компоненты из node
from node.control.trigger import StartCommandTrigger
from node.control.code import StartCommandCode
from node.control.answer import WelcomeAnswer

# Реестр Answer-ов для этого виджета
ANSWER_REGISTRY = {
    "welcome": WelcomeAnswer(),
}


@control_router.message(Command(COMMANDS["start"]))
async def handle_start_command(
    message: Message,
    state: FSMContext,
) -> None:
    """
    Главный хендлер команды /start.

    Входные состояния: любое (*)
    Выходные состояния: None (idle)

    FSM на входе:
    - нет обязательных полей

    FSM на выходе (Code записывает):
    - нет записей (FSM очищается в Trigger)

    FSM на выходе (Answer записывает):
    - нет записей

    Возможные Answer:
    - welcome (WelcomeAnswer) - всегда
      Показывает: приветственное сообщение
      Компонент: node/control/answer/welcome_answer.py

    Архитектура:
    1. StartCommandTrigger - сброс FSM, извлечение данных
    2. StartCommandCode - подготовка данных для приветствия
    3. WelcomeAnswer - отображение приветствия
    """
    # Шаг 1: Trigger (визуальные операции)
    trigger = StartCommandTrigger()
    trigger_data = await trigger.run(message, state)

    # Шаг 2: Code (бизнес-логика)
    code = StartCommandCode()
    code_result = await code.run(trigger_data, state)

    # Шаг 3: Answer (отрисовка экрана)
    answer = ANSWER_REGISTRY[code_result["answer_name"]]
    await answer.run(
        event=message,
        user_lang="ru",
        data=code_result["data"],
    )
