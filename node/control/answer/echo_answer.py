"""
Answer: Экран эхо-ответа.

Состояние экрана: Показывается после получения текстового сообщения.
Отображение: Эхо-ответ с префиксом и текстом пользователя.

Используется в виджетах:
- handler/v1/user/control/echo_widget.py (всегда)
"""

from aiogram.types import Message

from core.vocab import MESSAGES


class EchoAnswer:
    """
    Answer для эхо-ответа.
    
    Бизнес-логика Answer:
    - нет (только отрисовка)
    
    Используемые тексты:
    - MESSAGES["echo_prefix"] - префикс для эхо
    """
    
    async def run(
        self,
        event: Message,
        user_lang: str,
        data: dict,
        **kwargs
    ) -> None:
        """
        Отрисовать эхо-ответ.
        
        Args:
            event: Message для отправки ответа
            user_lang: Язык пользователя
            data: Данные от Code
            {
                "telegram_id": int - ID пользователя,
                "text": str - текст для эхо,
                "user_lang": str - язык пользователя
            }
            **kwargs: Дополнительные параметры
        """
        text = self._build_text(data, user_lang)
        await event.answer(text=text)
    
    def _build_text(self, data: dict, user_lang: str) -> str:
        """
        Построить текст эхо-сообщения.
        
        Args:
            data: Данные от Code
            user_lang: Язык пользователя
            
        Returns:
            str: Текст эхо-сообщения с префиксом
        """
        prefix = MESSAGES["echo_prefix"][user_lang]
        user_text = data["text"]
        return f"{prefix}{user_text}"
