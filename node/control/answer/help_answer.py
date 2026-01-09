"""
Answer: Экран справки.

Состояние экрана: Показывается после команды /help.
Отображение: Справочное сообщение с описанием команд.

Используется в виджетах:
- handler/v1/user/control/help_command_widget.py (всегда)
"""

from aiogram.types import Message

from core.vocab import MESSAGES


class HelpAnswer:
    """
    Answer для экрана справки.
    
    Бизнес-логика Answer:
    - нет (только отрисовка)
    
    Используемые тексты:
    - MESSAGES["help"] - справочное сообщение
    """
    
    async def run(
        self,
        event: Message,
        user_lang: str,
        data: dict,
        **kwargs
    ) -> None:
        """
        Отрисовать экран справки.
        
        Args:
            event: Message для отправки ответа
            user_lang: Язык пользователя
            data: Данные от Code
            {
                "telegram_id": int - ID пользователя,
                "user_lang": str - язык пользователя
            }
            **kwargs: Дополнительные параметры
        """
        text = self._build_text(data, user_lang)
        await event.answer(text=text)
    
    def _build_text(self, data: dict, user_lang: str) -> str:
        """
        Построить текст сообщения.
        
        Args:
            data: Данные от Code
            user_lang: Язык пользователя
            
        Returns:
            str: Текст сообщения
        """
        return MESSAGES["help"][user_lang]
