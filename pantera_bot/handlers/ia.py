import requests
from telegram import Update
from telegram.ext import ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

# 🧠 Persona da Pantera
PERSONA = """
Você é a Pantera 🐆, mascote oficial da FURIA Esports.
Fale como uma torcedora empolgada, confiante, com linguagem descontraída e cheia de emoção!
Use emojis, exclamações e frases de impacto quando possível. Sempre defenda a FURIA!
Se alguém perguntar quem é o melhor, fale bem dos jogadores da FURIA.
Seu tom é como o de um fã que entende muito de CS:GO.
Limite suas respostas a no máximo 5 linhas.

Você pode usar frases como:
- 'AQUI É FURIA, MEU PARCEIRO! 🔥'
- 'KSCERATO tá jogando o fino do fino!'
- 'FalleN é o professor, respeita! 👊'
- 'Quem vem contra a FURIA, volta pra casa chorando!'
"""

# 📊 Contexto (pode ser dinâmico futuramente)
FURIA_CONTEXT = """
Time: FURIA Esports 🇧🇷
Lineup atual:
- KSCERATO (rifler)
- yuurih (rifler)
- FalleN (IGL / AWP)
- chelo (entry)
- skullz (support)

Últimos jogos:
- Vitória 2x0 vs MOUZ (Ancient, Nuke)
- Derrota 1x2 vs NAVI (Mirage, Inferno, Overpass)

Próximo jogo:
- vs FaZe - 12/04 às 15h (BRT)

História:
A FURIA é uma equipe brasileira fundada em 2017. Chegou ao top 5 do ranking mundial da HLTV em 2020.

🏆 Conquistas Notáveis:
- Campeã da ESL Pro League Season 12 North America (2020)
- Campeã do Elisa Masters Espoo (2023)
- 3º–4º lugar no IEM Rio Major (2022)
- 5º–8º lugar no PGL Major Stockholm (2021)
- 5º–8º lugar no PGL Major Antwerp (2022)

📈 Estatísticas Recentes:
- Taxa de vitórias nos últimos 3 meses: 65%
- Total de partidas disputadas: 525
- Total de torneios disputados: 129
- Prêmios acumulados: $2.283.872

📊 Desempenho Recente:
- Últimos 5 confrontos: 4 vitórias (80%)
- Últimos 10 confrontos: 7 vitórias (70%)

📅 Próximos Jogos:
- 🆚 Lynn Vision – 8 de abril de 2025
- 🆚 9z Team – 18 de abril de 2025

🔍 Curiosidades:
- Fundada em 2017, a FURIA rapidamente se destacou no cenário internacional de CS:GO.
- Em 2020, venceu a ESL Pro League Season 12 North America.
- Em 2022, alcançou as semifinais do IEM Rio Major, sua melhor colocação em Majors até então.
- Em 2024, participou do PGL Major Copenhagen e do Perfect World Shanghai Major.

💬 Frases Icônicas:
- "AQUI É FURIA, MEU PARCEIRO! 🔥"
- "KSCERATO tá jogando o fino do fino!"
- "FalleN é o professor, respeita! 👊"
- "Quem vem contra a FURIA, volta pra casa chorando!"
"""

async def perguntar_ia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pergunta = " ".join(context.args)

    if not pergunta:
        await update.message.reply_text("❓ Manda a pergunta, tipo: `/perguntar Quem é o IGL da FURIA?`")
        return

    await update.message.reply_text("🐆 A Pantera tá pensando... segura aí!")

    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mistralai/mixtral-8x7b-instruct",
            "messages": [
                {"role": "system", "content": f"{PERSONA}\n\n{FURIA_CONTEXT}"},
                {"role": "user", "content": pergunta}
            ],
            "max_tokens": 600
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        resposta = result["choices"][0]["message"]["content"]

        await update.message.reply_text(resposta)

    except requests.exceptions.HTTPError as err:
        await update.message.reply_text(f"⚠️ Erro da IA: {err.response.text}")
    except Exception as e:
        await update.message.reply_text(f"❌ Erro inesperado com a IA: {str(e)}")
