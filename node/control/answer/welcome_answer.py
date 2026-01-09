"""
Answer: Приветственный экран.

Состояние экрана: Показывается после команды /start.
Отображение: Приветственное сообщение с описанием функционала бота.

Используется в виджетах:
- handler/v1/user/control/start_command_widget.py (всегда)
"""

from aiogram.types import Message

from core.vocab import MESSAGES


class WelcomeAnswer:
    """
    Answer для приветственного экрана.
    
    Бизнес-логика Answer:
    - нет (только отрисовка)
    
    Используемые тексты:
    - MESSAGES["welcome"] - приветственное сообщение
    """
    
    async def run(
        self,
        event: Message,
        user_lang: str,
        data: dict,
        **kwargs
    ) -> None:
        """
        Отрисовать приветственный экран.
        
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
        # Формируем текст
        text = self._build_text(data, user_lang)
        
        # Отправляем сообщение
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
        return MESSAGES["welcome"][user_lang]
