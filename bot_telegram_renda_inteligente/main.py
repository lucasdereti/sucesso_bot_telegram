from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import logging

TOKEN = "8070321774:AAGCiVU-eh5ncuOBs-KH_5E7WECb1R4Z2bg"
LINK_KIRVANO = "https://pay.kirvano.com/353273fb-3cb8-4b83-ab2c-7f387198101d"

logging.basicConfig(level=logging.INFO)

# Respostas automáticas por palavra-chave
respostas = {
    "funciona": "Sim! O método Renda Inteligente foi feito para quem quer ganhar dinheiro com inteligência artificial mesmo começando do zero. 💸",
    "quero": "Você está no lugar certo! Com o Renda Inteligente, qualquer pessoa pode começar a faturar online com a ajuda da IA. 🤖",
    "preço": "O curso está com DESCONTO por tempo limitado! Acesse aqui e confira: " + LINK_KIRVANO,
    "garantia": "Sim! Você tem 7 dias de garantia para testar tudo sem risco.",
    "seguro": "Sim! O curso é seguro e já ajudou muitas pessoas a começarem online com IA.",
    "dinheiro": "Com a estratégia certa e IA, sim, é possível fazer uma renda extra real. Veja aqui: " + LINK_KIRVANO,
    "zero": "Mesmo sem experiência, o curso ensina tudo passo a passo!"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = context.args
    if args and args[0].lower() == "quero":
        await update.message.reply_text("Quero saber mais")  # Mensagem automática sugerida
        return

    keyboard = [[InlineKeyboardButton("Acessar Renda Inteligente 👇", url=LINK_KIRVANO)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    mensagem = (
        "Descubra como ganhar dinheiro com inteligência artificial usando o método *Renda Inteligente*.\n\n"
        "Clique no botão abaixo para saber mais 👇"
    )

    await update.message.reply_text(
        mensagem,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()
    for palavra, resposta in respostas.items():
        if palavra in texto:
            await update.message.reply_text(resposta)
            return

    # Resposta padrão
    await update.message.reply_text(
        "Me explica melhor sua dúvida? Ou clique aqui e conheça o método: " + LINK_KIRVANO
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    app.run_polling()
