from telegram import Update, ChatPermissions
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
from telegram.constants import ChatMemberStatus

OWNER_ID = 6531482773 , -1002333813177
ADMINS = [OWNER_ID] , 5959345285 , -1002333813177 , 6531482773 , 5030849305 , 7586528405 , 6160808673

async def ban_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """BAN USER"""
    if update.message.chat.type != "supergroup":
        await update.message.reply_text("هذه الأوامر متاحة فقط في المجموعات من نوع سوبر جروب.")
        return

    if update.effective_user.id not in ADMINS:
        await update.message.reply_text("عذراً، هذه الصلاحية مخصصة للأدمن فقط.")
        return

    if not update.message.reply_to_message:
        await update.message.reply_text("يرجى الرد على الرسالة الخاصة بالشخص الذي ترغب في حظره.")
        return

    user_id = update.message.reply_to_message.from_user.id
    if user_id == OWNER_ID:
        await update.message.reply_text("لا يمكن حظر مالك المجموعة.")
        return

    await context.bot.ban_chat_member(update.message.chat.id, user_id)
    await update.message.reply_text(f"تم حظر المستخدم {update.message.reply_to_message.from_user.first_name} بنجاح.")

async def unban_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """UN BAN THE USER"""
    if update.message.chat.type != "supergroup":
        await update.message.reply_text("هذه الأوامر متاحة فقط في المجموعات من نوع سوبر جروب.")
        return

    if update.effective_user.id not in ADMINS:
        await update.message.reply_text("عذراً، هذه الصلاحية مخصصة للأدمن فقط.")
        return

    if not update.message.reply_to_message:
        await update.message.reply_text("يرجى الرد على الرسالة الخاصة بالشخص الذي ترغب في إلغاء حظره.")
        return

    user_id = update.message.reply_to_message.from_user.id
    await context.bot.unban_chat_member(update.message.chat.id, user_id)
    await update.message.reply_text(f"تم إلغاء حظر المستخدم {update.message.reply_to_message.from_user.first_name} بنجاح.")

async def mute_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """MUTE THE USER"""
    if update.message.chat.type != "supergroup":
        await update.message.reply_text("هذه الأوامر متاحة فقط في المجموعات من نوع سوبر جروب.")
        return

    if update.effective_user.id not in ADMINS:
        await update.message.reply_text("عذراً، هذه الصلاحية مخصصة للأدمن فقط.")
        return

    if not update.message.reply_to_message:
        await update.message.reply_text("يرجى الرد على الرسالة الخاصة بالشخص الذي ترغب في كتمه.")
        return

    user_id = update.message.reply_to_message.from_user.id
    permissions = ChatPermissions(can_send_messages=False)
    await context.bot.restrict_chat_member(update.message.chat.id, user_id, permissions=permissions)
    await update.message.reply_text(f"تم كتم المستخدم {update.message.reply_to_message.from_user.first_name} بنجاح.")

async def unmute_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """UN MUTE THE USER."""
    if update.message.chat.type != "supergroup":
        await update.message.reply_text("هذه الأوامر متاحة فقط في المجموعات من نوع سوبر جروب.")
        return

    if update.effective_user.id not in ADMINS:
        await update.message.reply_text("عذراً، هذه الصلاحية مخصصة للأدمن فقط.")
        return

    if not update.message.reply_to_message:
        await update.message.reply_text("يرجى الرد على الرسالة الخاصة بالشخص الذي ترغب في إلغاء كتمه.")
        return

    user_id = update.message.reply_to_message.from_user.id
    permissions = ChatPermissions(can_send_messages=True)
    await context.bot.restrict_chat_member(update.message.chat.id, user_id, permissions=permissions)
    await update.message.reply_text(f"تم إلغاء كتم المستخدم {update.message.reply_to_message.from_user.first_name} بنجاح.")

async def clear_muted(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """UN MUTE FOR ALL"""
    if update.message.chat.type != "supergroup":
        await update.message.reply_text("هذه الأوامر متاحة فقط في المجموعات من نوع سوبر جروب.")
        return

    if update.effective_user.id not in ADMINS:
        await update.message.reply_text("عذراً، هذه الصلاحية مخصصة للأدمن فقط.")
        return

    chat = await context.bot.get_chat(update.message.chat.id)
    members = await chat.get_administrators()

    for member in members:
        if member.status == ChatMemberStatus.RESTRICTED:
            permissions = ChatPermissions(can_send_messages=True)
            await context.bot.restrict_chat_member(update.message.chat.id, member.user.id, permissions=permissions)
    await update.message.reply_text("تم مسح جميع المكتومين بنجاح.")

async def clear_banned(update: Update , context: ContextTypes.DEFAULT_TYPE) -> None:
   #un ban for all
    if update.message.chat.type != "supergroup":
        await update.message.reply_text("هذه الأوامر متاحة فقط في المجموعات من نوع سوبر جروب.")
        return

    if update.effective_user.id not in ADMINS:
        await update.message.reply_text("عذراً، هذه الصلاحية مخصصة للأدمن فقط.")
        return

    # get the list of baned users
    banned_users = await context.bot.get_chat_administrators(update.message.chat.id)
    for user in banned_users:
        if user.status == ChatMemberStatus.BANNED:
            await context.bot.unban_chat_member(update.message.chat.id, user.user.id)
    await update.message.reply_text("تم مسح جميع المحظورين بنجاح.")

# try the code super groube or not
async def lock_chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """قفل الشات (تعطيل إرسال الرسائل للأعضاء العاديين)"""
    user = update.effective_user
    chat = update.effective_chat

    #if the user is admin or owner
    member = await chat.get_member(user.id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        await update.message.reply_text("عذراً، هذا الأمر متاح فقط للمشرفين والمالك.")
        return

    # close the chat
    permissions = ChatPermissions(can_send_messages=False)
    await context.bot.set_chat_permissions(chat.id, permissions)
    await update.message.reply_text("تم قفل الشات. الأعضاء العاديون لا يمكنهم إرسال الرسائل الآن.")


async def unlock_chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """open the chat"""
    user = update.effective_user
    chat = update.effective_chat

    # if the user is admin or owner
    member = await chat.get_member(user.id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        await update.message.reply_text("عذراً، هذا الأمر متاح فقط للمشرفين والمالك.")
        return

    # open the chat
    permissions = ChatPermissions(can_send_messages=True)
    await context.bot.set_chat_permissions(chat.id, permissions)
    await update.message.reply_text("تم فتح الشات. يمكن للأعضاء العاديين إرسال الرسائل الآن.")