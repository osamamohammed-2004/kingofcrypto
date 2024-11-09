from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from admin import ban_user, unban_user, mute_user, unmute_user, clear_muted, clear_banned, lock_chat, unlock_chat

from buttons import button, start
from buttons import investment_project
from handlers import start, welcome, handle_links, get_admins
from project_buttons_screen import project_keywords_handler, project_button_callback
from interactions import setup_interactions, show_top_interactors
import asyncio

TOKEN = "8070460438:AAHAceu93ThnI5y4MfGBQupGJnKGfyuB3PI"


async def main() -> None:
    # إنشاء التطبيق
    application = ApplicationBuilder().token(TOKEN).build()

    #  admin.py
    application.add_handler(CommandHandler('ban', ban_user))
    application.add_handler(CommandHandler('unban', unban_user))
    application.add_handler(CommandHandler('mute', mute_user))
    application.add_handler(CommandHandler('unmute', unmute_user))
    application.add_handler(CommandHandler('clearmuted', clear_muted))
    application.add_handler(CommandHandler('clearbanned', clear_banned))

    #  admin.py
    application.add_handler(MessageHandler(filters.Text(['حظر']), ban_user))
    application.add_handler(MessageHandler(filters.Text(['الغاء الحظر']), unban_user))
    application.add_handler(MessageHandler(filters.Text(['كتم']), mute_user))
    application.add_handler(MessageHandler(filters.Text(['الغاء الكتم']), unmute_user))
    application.add_handler(MessageHandler(filters.Text(['مسح المكتومين']), clear_muted))
    application.add_handler(MessageHandler(filters.Text(['مسح المحظورين']), clear_banned))
    application.add_handler(MessageHandler(filters.Text(['قفل الشات']), lock_chat))
    application.add_handler(MessageHandler(filters.Text(['فتح الشات']), unlock_chat))

    #  handlers.py
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex(r'http[s]?://'), handle_links))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex(r'^الادمن$'), get_admins))

    #  buttons.py
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^المشروع الاستثماري$'), investment_project))

    # project keywords
    application.add_handler(project_keywords_handler)

    # project buttons
    application.add_handler(CallbackQueryHandler(project_button_callback, pattern='^project_.*'))
    setup_interactions(application)
    application.add_handler(CommandHandler('top_interactors', show_top_interactors))


    # run the bot
    await application.run_polling()


if __name__ == "__main__":
    import nest_asyncio

    nest_asyncio.apply()
    loop = asyncio.get_event_loop()
    if not loop.is_running():
        loop.run_until_complete(main())