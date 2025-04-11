from telegram import Update
from telegram.ext import ContextTypes

async def proximo_jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "📅 <b>Próximos jogos da FURIA:</b>\n\n"
        "1. 🏆 <b>PGL Bucharest 2025</b>\n"
        "   - 🆚 <b>Virtus.pro</b>\n"
        "   - 📆 <i>Data:</i> 8 de abril de 2025\n"
        "   - 🕘 <i>Horário:</i> 09:05 (Horário de Brasília)\n"
        "   - 📍 <i>Local:</i> Bucareste, Romênia\n\n"
        "2. 🏆 <b>ESL Pro League Season 21</b>\n"
        "   - 🆚 <b>Lynn Vision</b>\n"
        "   - 📆 <i>Data:</i> 8 de abril de 2025\n"
        "   - 🕘 <i>Horário:</i> A ser definido\n"
        "   - 📍 <i>Local:</i> Estocolmo, Suécia\n\n"
        "3. 🏆 <b>ESL Pro League Season 21</b>\n"
        "   - 🆚 <b>9z Team</b>\n"
        "   - 📆 <i>Data:</i> 18 de abril de 2025\n"
        "   - 🕘 <i>Horário:</i> A ser definido\n"
        "   - 📍 <i>Local:</i> Estocolmo, Suécia"
    )
    await update.message.reply_text(mensagem, parse_mode='HTML')
