"""
Code для команды /start.

Задача: Подготовить данные для приветственного сообщения.

Используется в виджетах:
- handler/v1/user/control/start_command_widget.py
"""

from aiogram.fsm.context import FSMContext

from core.vocab import DEFAULT_LANGUAGE


class StartCommandCode:
    """
    Класс для бизнес-логики команды /start.
    
    ⚠️ ВАЖНО: Определяет язык пользователя и подготавливает данные для приветствия.
    
    Бизнес-логика:
    1. Получить данные от Trigger
    2. Определить язык пользователя (по умолчанию)
    3. Подготовить данные для Answer
    
    Используемые сервисы:
    - нет (простая логика)
    
    Условия роутинга к Answer:
    - всегда → "welcome" (WelcomeAnswer)
    """
    
    async def run(self, trigger_data: dict, state: FSMContext, **kwargs) -> dict:
        """
        Выполнить бизнес-логику и выбрать Answer.
        
        Бизнес-логика:
        1. Извлечь telegram_id из trigger_data
        2. Определить язык (по умолчанию ru)
        3. Вернуть answer_name = "welcome"
        
        Args:
            trigger_data: Данные от Trigger
            {
                "telegram_id": int - ID пользователя в Telegram,
                "username": str | None - username пользователя,
                "event": Message - оригинальное событие
            }
            state: FSM контекст
            **kwargs: Дополнительные параметры
            
        Returns:
            dict: Название Answer + данные для него
            {
                "answer_name": str,  # "welcome"
                "data": dict         # Данные для Answer
            }
        """
        result = await self._execute_business_logic(trigger_data, state, **kwargs)
        return await self._route_to_answer(result)
    
    async def _execute_business_logic(
        self, 
        trigger_data: dict, 
        state: FSMContext,
        **kwargs
    ) -> dict:
        """
        Выполнить всю бизнес-логику.
        
        Бизнес-логика:
        1. Получить telegram_id
        2. Определить язык пользователя
        
        Returns:
            dict: Результат обработки
            {
                "telegram_id": int - ID пользователя,
                "user_lang": str - язык пользователя
            }
        """
        telegram_id = trigger_data["telegram_id"]
        
        # Определяем язык (можно расширить логикой из БД)
        user_lang = kwargs.get("user_lang", DEFAULT_LANGUAGE)
        
        return {
            "telegram_id": telegram_id,
            "user_lang": user_lang,
        }
    
    async def _route_to_answer(self, result: dict) -> dict:
        """
        Определить какой Answer использовать.
        
        Всегда возвращает "welcome" - приветственный экран.
        
        Args:
            result: Результат бизнес-логики
            
        Returns:
            dict: Название Answer + данные
        """
        return {"answer_name": "welcome", "data": result}
