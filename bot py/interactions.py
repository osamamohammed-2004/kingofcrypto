import sqlite3
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
from telegram.constants import ChatMemberStatus

# CREAR DATA BASE
def init_db():
    conn = sqlite3.connect('interactions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS interactions
                 (user_id INTEGER PRIMARY KEY, username TEXT, interaction_count INTEGER)''')
    conn.commit()
    conn.close()

# UPDATE THR NUMBER OF INTERACTIONS FOR YHE USER
def update_interaction(user_id, username):
    conn = sqlite3.connect('interactions.db')
    c = conn.cursor()
    c.execute("SELECT * FROM interactions WHERE user_id=?", (user_id,))
    user = c.fetchone()
    if user:
        c.execute("UPDATE interactions SET interaction_count = interaction_count + 1 WHERE user_id=?", (user_id,))
    else:
        c.execute("INSERT INTO interactions (user_id, username, interaction_count) VALUES (?, ?, 1)",
                  (user_id, username))
    conn.commit()
    conn.close()

# TOP 10
def get_top_interactors():
    conn = sqlite3.connect('interactions.db')
    c = conn.cursor()
    c.execute("SELECT username, interaction_count FROM interactions ORDER BY interaction_count DESC LIMIT 10")
    top_users = c.fetchall()
    conn.close()
    return top_users

# SHOW TOP INTERACTORS
async def show_top_interactors(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat

    # IF THE USER ARE ADMIN OR OWNER
    member = await chat.get_member(user.id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        await update.message.reply_text("عذراً، هذا الأمر متاح فقط للمشرفين والمالك.")
        return

    top_users = get_top_interactors()
    if not top_users:
        await update.message.reply_text("لا يوجد متفاعلين حتى الآن.")
        return

    message = "أكثر 10 أشخاص متفاعلين في المجموعة:\n\n"
    for i, (username, count) in enumerate(top_users, 1):
        message += f"{i}. {username}: {count} تفاعل\n"

    await update.message.reply_text(message)

#record interaction
async def record_interaction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    update_interaction(user.id, user.username or user.first_name)

# setup interactions
def setup_interactions(application):
    init_db()
    application.add_handler(CommandHandler('top_interactors', show_top_interactors))
    application.add_handler(MessageHandler(filters.ALL, record_interaction))