"""
Trigger для эхо-ответа на текстовое сообщение.

Используется в виджетах:
- handler/v1/user/control/echo_widget.py
"""

from aiogram.types import Message
from aiogram.fsm.context import FSMContext


class EchoTrigger:
    """
    Trigger для обработки текстового сообщения (эхо).
    
    Выполняет визуальные операции:
    - Извлечение текста сообщения
    - Извлечение данных пользователя
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
                "text": str - текст сообщения пользователя,
                "event": Message - оригинальное событие
            }
        """
        telegram_id = event.from_user.id
        text = event.text or ""
        
        return {
            "telegram_id": telegram_id,
            "text": text,
            "event": event,
        }
