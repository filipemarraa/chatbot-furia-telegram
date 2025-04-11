from telegram import Update
from telegram.ext import ContextTypes

async def lineup_furia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "🧠 <b>Lineup atual da FURIA (CS2):</b>\n\n"
        "🇧🇷 <b>Gabriel \"FalleN\" Toledo</b> – IGL / AWP\n"
        "🇧🇷 <b>Yuri \"yuurih\" Santos</b> – Rifler\n"
        "🇧🇷 <b>Kaike \"KSCERATO\" Cerato</b> – Rifler\n"
        "🇧🇷 <b>Marcelo \"chelo\" Cespedes</b> – Entry Fragger\n"
        "🇧🇷 <b>Felipe \"skullz\" Medeiros</b> – Rifler\n\n"
        "🎯 <b>Treinador:</b> 🇧🇷 Sidnei \"sidde\" Macedo\n"
        "🧠 <b>Treinador Assistente:</b> 🇪🇸 Juan \"Hepa\" Borges"
    )
    await update.message.reply_text(mensagem, parse_mode='HTML')
