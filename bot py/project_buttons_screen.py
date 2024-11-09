from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, MessageHandler, filters


async def show_project_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """SHOW PROJECT PUTTONS"""
    project_buttons = [
        [InlineKeyboardButton("💎 طريقه الاستثمار'", url="https://t.me/king_ofcryptocurrencies/69")],
        [InlineKeyboardButton("🌟 المستويات و الباقات المتوفرة للاستثمار ", url="https://t.me/king_ofcryptocurrencies/72")],
        [InlineKeyboardButton("💫 نسبة الارباح", url="https://t.me/king_ofcryptocurrencies/73")],
        [InlineKeyboardButton("⭐️ المكافأت", url="https://t.me/king_ofcryptocurrencies/74")],
        [InlineKeyboardButton("🌙 توضيح باقات مستويات vip", url="https://t.me/king_ofcryptocurrencies/93l")],
        [InlineKeyboardButton("⚡️ صورة توضيحيه ل نسب الارباح", url="https://t.me/king_ofcryptocurrencies/94")],
        [InlineKeyboardButton("🔥 صورة توضيحيه لنظام باقات الدبل", url="https://t.me/king_ofcryptocurrencies/95")],
        [InlineKeyboardButton("💫مكافأت الاحالة لمستويات الvip", url="https://t.me/king_ofcryptocurrencies/97")],
        [InlineKeyboardButton("🌟 مكافأت الاحاله للمستوى المتميز", url="https://t.me/king_ofcryptocurrencies/98")],
        [InlineKeyboardButton("💎 Instagram", url="https://www.instagram.com/king_crypto30")],
        [InlineKeyboardButton("⚡️telegram channel", url="https://t.me/king_ofcryptocurrencies")]
    ]

    reply_markup = InlineKeyboardMarkup(project_buttons)

    await update.message.reply_text(
        "🌟 مرحباً بك في قائمة مشاريعنا\n",
        reply_markup=reply_markup
    )


async def project_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()


#KEYWORDS FOR THE PROJECT BUTTONS
project_keywords_handler = MessageHandler(
    filters.TEXT & (filters.Regex(r"المشروع|king of crypto")),
    show_project_buttons
)