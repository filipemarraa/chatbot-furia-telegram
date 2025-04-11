from telegram import Update
from telegram.ext import ContextTypes

async def resultados_recentes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "📊 *Últimos resultados da FURIA (CS2):*\n\n"
        "1. 🆚 *The MongolZ* – ❌ Derrota por 0x2\n"
        "   📅 9 de abril de 2025 – PGL Bucharest 2025\n\n"
        "2. 🆚 *Virtus.pro* – ❌ Derrota por 0x2\n"
        "   📅 8 de abril de 2025 – PGL Bucharest 2025\n\n"
        "3. 🆚 *Complexity* – ❌ Derrota por 1x2\n"
        "   📅 7 de abril de 2025 – PGL Bucharest 2025\n\n"
        "4. 🆚 *Apogee* – ✅ Vitória por 2x0\n"
        "   📅 6 de abril de 2025 – PGL Bucharest 2025\n\n"
        "5. 🆚 *M80* – ❌ Derrota por 1x2\n"
        "   📅 22 de março de 2025 – BLAST Open Spring 2025"
    )
    await update.message.reply_text(mensagem, parse_mode='Markdown')
