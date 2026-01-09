"""
Trigger для команды /start.

Используется в виджетах:
- handler/v1/user/control/start_command_widget.py
"""

from aiogram.types import Message
from aiogram.fsm.context import FSMContext


class StartCommandTrigger:
    """
    Trigger для обработки команды /start.

    Выполняет визуальные операции:
    - Сброс FSM состояния (если было)
    - Извлечение базовых данных пользователя
    """

    async def run(self, event: Message, state: FSMContext) -> dict:
        """
        Выполнить визуальные операции.

        Args:
            event: Message событие от Telegram
            state: FSM контекст

        Returns:
            dict: Данные для передачи в Code
            {
                "telegram_id": int - ID пользователя в Telegram,
                "username": str | None - username пользователя,
                "event": Message - оригинальное событие
            }
        """
        telegram_id = event.from_user.id
        username = event.from_user.username

        return {
            "telegram_id": telegram_id,
            "username": username,
            "event": event,
        }
