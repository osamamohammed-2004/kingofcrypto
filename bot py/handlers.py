# handlers.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ChatMember
from telegram.ext import ContextTypes
from telegram.error import BadRequest
import re
from collections import defaultdict

# قاموس لتتبع التحذيرات لكل عضو
warnings = defaultdict(int)


async def get_admins(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """the list of the admins"""
    if update.message.text.lower() == 'الادمن':
        chat_id = update.effective_chat.id
        admins = await context.bot.get_chat_administrators(chat_id)

        admin_list = "قائمة الأدمن:\n\n"
        for admin in admins:
            if admin.user.username:
                admin_list += f"@{admin.user.username}\n"
            else:
                admin_list += f"{admin.user.first_name}\n"

        await update.message.reply_text(admin_list)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """repley wen the bot start"""
    await update.message.reply_text("بوت الترحيب جاهز!")


async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """welcome for new members in the groube"""
    try:
        for member in update.message.new_chat_members:
            # نص الترحيب
            welcome_text = f"أهلاً وسهلاً {member.full_name} في المجموعة! 🎉\nنرجو منك قراءة قوانين المجموعة وإعدادات الخصوصية"

            # تعريف الأزرار
            buttons = [
                [InlineKeyboardButton("القناة الرسمية على 🔥Instagram", callback_data='button_1')],
                [InlineKeyboardButton("القناة الرسمية على ⚡️Telegram", callback_data='button_2')],
                [InlineKeyboardButton("رابط قروب المناقشات 💎", callback_data='button_3')],
                [InlineKeyboardButton("فكرة المشروع 🌟", callback_data='button-4')],
                [InlineKeyboardButton("الية العمل 🌟", callback_data='button_5')],
                [InlineKeyboardButton("الباقات 🌟", callback_data='button-6')],
                [InlineKeyboardButton("المستويات 🌟", callback_data='button_7')],
                [InlineKeyboardButton("المكافآت 💎", callback_data='button_8')],
                [InlineKeyboardButton("نسبة الأرباح ⚡️", callback_data='button_9')],
                [InlineKeyboardButton("العودة إلى القائمة الرئيسية 🔥", callback_data='main_menu')]
            ]

            # welcome massege
            await update.message.reply_text(
                welcome_text,
                reply_markup=InlineKeyboardMarkup(buttons)
            )
    except Exception as e:
        print(f"Error in welcome function: {str(e)}")


async def handle_links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """the url send by the users"""
    user_id = update.message.from_user.id
    chat_id = update.message.chat.id
    message_text = update.message.text
    user_name = update.message.from_user.full_name

    # if the user is admin or owner
    chat_member = await context.bot.get_chat_member(chat_id, user_id)
    if chat_member.status in [ChatMember.ADMINISTRATOR, ChatMember.OWNER]:
        # exception the admin and owner
        return

    # التحقق مما إذا كانت الرسالة تحتوي على أي نوع من الروابط
    if re.search(r'http[s]?://|www\.|t\.me|@', message_text):
        warnings[user_id] += 1
        remaining_warnings = 3 - warnings[user_id]

        #delete the url
        try:
            await update.message.delete()
        except BadRequest:
            pass  #ignore the eror

        # send the warning
        await update.effective_chat.send_message(
            f"تحذير! {user_name}, لقد قمت بمشاركة رابط. "
            f"عدد التحذيرات: {warnings[user_id]}. "
            f"المتبقي: {remaining_warnings} تحذيرات قبل الحظر التلقائي من المجموعة."
        )

        # if the warning 3 ban
        if warnings[user_id] >= 3:
            await context.bot.ban_chat_member(chat_id, user_id)
            await update.effective_chat.send_message(
                f"تم حظر {user_name} بسبب تجاوز عدد التحذيرات (3)!"
            )