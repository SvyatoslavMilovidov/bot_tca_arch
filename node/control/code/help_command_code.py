"""
Code для команды /help.

Задача: Подготовить данные для справочного сообщения.

Используется в виджетах:
- handler/v1/user/control/help_command_widget.py
"""

from aiogram.fsm.context import FSMContext

from core.vocab import DEFAULT_LANGUAGE


class HelpCommandCode:
    """
    Класс для бизнес-логики команды /help.
    
    ⚠️ ВАЖНО: Подготавливает данные для показа справки.
    
    Бизнес-логика:
    1. Получить данные от Trigger
    2. Определить язык пользователя
    3. Подготовить данные для Answer
    
    Используемые сервисы:
    - нет (простая логика)
    
    Условия роутинга к Answer:
    - всегда → "help" (HelpAnswer)
    """
    
    async def run(self, trigger_data: dict, state: FSMContext, **kwargs) -> dict:
        """
        Выполнить бизнес-логику и выбрать Answer.
        
        Args:
            trigger_data: Данные от Trigger
            {
                "telegram_id": int - ID пользователя в Telegram,
                "event": Message - оригинальное событие
            }
            state: FSM контекст
            **kwargs: Дополнительные параметры
            
        Returns:
            dict: Название Answer + данные для него
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
        
        Returns:
            dict: Результат обработки
        """
        telegram_id = trigger_data["telegram_id"]
        user_lang = kwargs.get("user_lang", DEFAULT_LANGUAGE)
        
        return {
            "telegram_id": telegram_id,
            "user_lang": user_lang,
        }
    
    async def _route_to_answer(self, result: dict) -> dict:
        """
        Определить какой Answer использовать.
        
        Returns:
            dict: Название Answer + данные
        """
        return {"answer_name": "help", "data": result}
