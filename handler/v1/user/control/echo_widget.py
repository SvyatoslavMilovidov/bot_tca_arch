"""
Виджет: Эхо-ответ.

Повторяет текстовое сообщение пользователя.

Доступен из:
1. любое состояние (обрабатывает любой текст)
   - Из какого state: любое (*)
   - Из какого answer: — (текстовое сообщение)

Переводит в:
- Не меняет состояние
"""

from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import F

from handler.v1.user.router import control_router
from core.vocab import DEFAULT_LANGUAGE

# Импортируем компоненты из node
from node.control.trigger import EchoTrigger
from node.control.code import EchoCode
from node.control.answer import EchoAnswer

# Реестр Answer-ов для этого виджета
ANSWER_REGISTRY = {
    "echo": EchoAnswer(),
}


@control_router.message(F.text)
async def handle_echo(
    message: Message,
    state: FSMContext,
) -> None:
    """
    Главный хендлер эхо-ответа.

    Входные состояния: любое (*)
    Выходные состояния: не меняет

    FSM на входе:
    - нет обязательных полей

    FSM на выходе:
    - нет записей

    Возможные Answer:
    - echo (EchoAnswer) - всегда
      Показывает: эхо-ответ с текстом пользователя
      Компонент: node/control/answer/echo_answer.py

    Архитектура:
    1. EchoTrigger - извлечение текста сообщения
    2. EchoCode - подготовка данных для эхо
    3. EchoAnswer - отправка эхо-ответа
    """
    # Шаг 1: Trigger
    trigger = EchoTrigger()
    trigger_data = await trigger.run(message, state)

    # Шаг 2: Code
    code = EchoCode()
    code_result = await code.run(trigger_data, state)

    # Шаг 3: Answer
    answer = ANSWER_REGISTRY[code_result["answer_name"]]
    await answer.run(
        event=message,
        user_lang="ru",
        data=code_result["data"],
    )
