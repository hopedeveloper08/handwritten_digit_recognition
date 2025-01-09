from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from get_token import TOKEN
import numpy as np
import tensorflow as tf
from PIL import Image
import os
import requests
from io import BytesIO

model = tf.keras.models.load_model(os.path.join(os.getcwd(), 'handwritten_digit_recognition', 'best_model.keras'))

def preprocess_image(img):
    img = img.resize((28, 28))
    img = img.convert('L')
    img_array = np.array(img)
    img_array = 255 - img_array
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=(0, -1))
    return img_array


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="یک عکس با پس زمینه سفید و یک رقم انگلیسی دست نویس برام ارسال کن تا بهت بگم چه عددی هست.")


async def image_process(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    url = await photo.get_file()
    img = Image.open(BytesIO(requests.get(url.file_path).content))
    image = preprocess_image(img)
    prediction = model.predict(image)
    digit = np.argmax(prediction)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=str(digit))


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.PHOTO, image_process))

    application.run_polling()
    