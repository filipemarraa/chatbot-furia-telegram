from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from handlers.jogos import proximo_jogos
from handlers.resultados import resultados_recentes
from handlers.lineup import lineup_furia
from handlers.ia import perguntar_ia
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz
import sys

# Carrega variáveis do .env (ou da aba Variables no Railway)
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Mensagem de boas-vindas
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Fala, FURIOSO!\n\n"
        "Eu sou a Pantera 🐆, o bot oficial da FURIA!\n\n"
        "📆 /jogos - Ver os próximos jogos\n"
        "📊 /resultados - Ver os resultados mais recentes\n"
        "🧠 /lineup - Ver a line atual da FURIA\n"
        "🤖 /perguntar - Perguntar algo pra IA da Pantera"
    )

# Função principal
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jogos", proximo_jogos))
    app.add_handler(CommandHandler("resultados", resultados_recentes))
    app.add_handler(CommandHandler("lineup", lineup_furia))
    app.add_handler(CommandHandler("perguntar", perguntar_ia))

    print("🚀 Bot da Pantera rodando...")
    app.run_polling()

if __name__ == '__main__':
    main()
