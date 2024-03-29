from aiogram import Dispatcher

from handlers.user.handlers import (
    group_select_handler,
    handle_group_callback,
    next_handler,
    now_handler,
    search_day_handler,
    search_week_handler,
    today_handler,
    tomorrow_handler,
    wait_for_group_handler,
    week_handler,
)
from states.default import GroupSelect


def setup(dispatcher: Dispatcher):
    dispatcher.register_message_handler(group_select_handler, commands=["group"])
    dispatcher.register_message_handler(wait_for_group_handler, state=GroupSelect.waiting_for_group)
    dispatcher.register_callback_query_handler(handle_group_callback, state=GroupSelect.waiting_for_group)
    dispatcher.register_message_handler(now_handler, commands=["now"])
    dispatcher.register_message_handler(next_handler, commands=["next"])
    dispatcher.register_message_handler(today_handler, commands=["today"])
    dispatcher.register_message_handler(tomorrow_handler, commands=["tomorrow"])
    dispatcher.register_message_handler(week_handler, commands=["week"])
    dispatcher.register_message_handler(search_day_handler, commands=["search_day"])
    dispatcher.register_message_handler(search_week_handler, commands=["search_week"])
