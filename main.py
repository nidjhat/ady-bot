import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Bot token
TOKEN = os.getenv("TOKEN")  # Render / Replit variable-da TOKEN əlavə olunmalıdır

# /start command cavabı
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salam 👋 Bot işləyir! ADY bilet monitor üçün hazırdır.")

# burda gələcəkdə ADY biletləri yoxlama funksiyası əlavə olunacaq
async def check_tickets():
    while True:
        # buraya real ADY API yoxlama kodu gələcək
        # hal-hazırda sadəcə test loop
        await asyncio.sleep(60)  # hər 1 dəqiqə yoxlayır (test)
        
def main():
    app = Application.builder().token(TOKEN).build()
    
    # Telegram /start handler
    app.add_handler(CommandHandler("start", start))
    
    # Async background task
    app.job_queue.run_repeating(lambda ctx: asyncio.create_task(check_tickets()), interval=60, first=10)
    
    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
