from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import logging

TOKEN = "8070321774:AAGCiVU-eh5ncuOBs-KH_5E7WECb1R4Z2bg"
LINK_KIRVANO = "https://preview--lucro-inteligente.lovable.app/"

logging.basicConfig(level=logging.INFO)

# Respostas para dúvidas frequentes
respostas = {
    "valor": f"O investimento no Renda Inteligente está com um desconto especial! Clique no link para ver o preço atualizado: {LINK_KIRVANO}",
    "como funciona": "O curso ensina passo a passo como usar inteligência artificial para criar renda extra real, mesmo sem experiência.",
    "vale a pena": "Sim! Muitas pessoas já transformaram suas vidas usando nosso método e começaram a faturar online.",
    "o que tem no produto": "Você terá aulas práticas, acesso ao nosso grupo exclusivo, suporte e ferramentas para começar a ganhar dinheiro com IA.",
    "sim": f"Perfeito! Então vou te mandar o link, mas guarde para você, é um segredo poderoso. 😉\n{LINK_KIRVANO}",
    "não": "Tudo bem, se mudar de ideia, é só me chamar. Estou aqui para ajudar você a mudar sua vida.",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['aguardando_confirmacao'] = True  # Ativa flag para esperar resposta "sim" ou "não"
    await update.message.reply_text(
        "Olá! Você tem mesmo interesse em mudar de vida e começar a ganhar dinheiro com inteligência artificial? Responda com *sim* ou *não*.",
        parse_mode="Markdown"
    )

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if context.user_data.get('aguardando_confirmacao', False):
        # Está esperando a confirmação inicial
        if "sim" in texto:
            context.user_data['aguardando_confirmacao'] = False
            await update.message.reply_text(
                f"Que ótimo! Vou te mandar o link, mas por favor, não compartilhe com muita gente — esse é um segredo para poucos que querem realmente mudar de vida. 😉\n\n{LINK_KIRVANO}"
            )
            return
        elif "não" in texto:
            context.user_data['aguardando_confirmacao'] = False
            await update.message.reply_text(
                "Entendo. Se mudar de ideia, estarei aqui para ajudar você a transformar sua vida!"
            )
            return
        else:
            await update.message.reply_text(
                "Por favor, responda apenas *sim* ou *não* para continuarmos.",
                parse_mode="Markdown"
            )
            return

    # Responder dúvidas frequentes
    for palavra, resposta in respostas.items():
        if palavra in texto:
            await update.message.reply_text(resposta)
            return

    # Se não reconheceu, tenta guiar para clicar no link
    await update.message.reply_text(
        f"Não entendi muito bem. Se quiser saber mais, é só perguntar sobre *valor*, *como funciona*, *vale a pena* ou *o que tem no produto*.\n\n"
        f"Ou clique no link para garantir sua vaga e mudar sua vida agora:\n{LINK_KIRVANO}",
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    app.run_polling()

