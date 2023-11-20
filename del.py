import telebot
import requests
from datetime import datetime
import random
import time

TOKEN = '6923679994:AAFN1YVRdcZm-jtv3aYyORkyZgMRsiRB-_M'
bot = telebot.TeleBot(TOKEN)

target_number = None
start_time = None

@bot.message_handler(commands=['sayi'])
def start(message):
    if message.chat.type == 'private':
        bot.reply_to(message, "✦ <b>Sadece gruplarda kullanılabilir .</b>", parse_mode="HTML")
        return
    global target_number
    global start_time

    if target_number is not None:
        bot.reply_to(message, "✦ <b>Zaten aktif oyun var .\n✦ İptal etmek için ➡️ /iptal</b>", parse_mode="HTML")
        return

    bot.reply_to(message, "✦ <b>Aklımda 1 - 1000 arasında bir sayı tuttum , hadi tahmin et !</b>", parse_mode="HTML")

    target_number = random.randint(1, 1000)

@bot.message_handler(commands=['iptal'])
def cancel(message):
    global target_number
    global start_time

    if target_number is None:
        return
    else:
        bot.reply_to(message, "✦ <b>Sayı Tahmin Oyunu iptal edildi .</b>", parse_mode="HTML")
        target_number = None
        start_time = None

@bot.message_handler(func=lambda message: True)
def guess(message):
    global target_number
    global start_time
    global guess_count

    guess_count = 0

    try:
        guess_number = int(message.text)
    except ValueError:
        return

    if target_number is None:
        return

    guess_count += 1

    if guess_number < target_number:
        bot.reply_to(message, "🔺<b> Daha büyük bir sayı tahmin edin .</b>", parse_mode="HTML")
    elif guess_number > target_number:
        bot.reply_to(message, "🔻<b> Daha küçük bir sayı tahmin edin .</b>", parse_mode="HTML")
    else:
        bot.reply_to(message, f"✦<b> Tebrikler , Doğru sayıyı buldunuz .\n✦ Bulunan Sayı : {guess_number} </b>", parse_mode="HTML")
        target_number = None
        guess_count = 0
        return

    start_time = time.time()
    
    
print("Telebot Aktif !")
bot.polling()


@app.on_message(filters.command(["bul", "song"]) & ~filters.edited)
async def bul(_, message):
    try:
        await message.delete()
    except:
        pass
    query = " ".join(message.command[1:])
    m = await message.reply("**__✦ şᴀʀᴋɪ ᴀʀᴀɴɪʏᴏʀ !__**")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
    
    except Exception as e:
        await m.edit("**__✦ şᴀʀᴋɪ ʙᴜʟᴜɴᴀᴍᴀᴅɪ !__**")
        print(str(e))
        return
    await m.edit("**__✦ şᴀʀᴋɪ ɪɴᴅɪʀɪʟɪʏᴏʀ !__**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**__✦ ᴘᴀʀᴄ̧ᴀ__ : {title[:35]}\n__✦ sᴜ̈ʀᴇ__ : {duration}\n\n__✦ ɪsᴛᴇʏᴇɴ__ : {message.from_user.mention}**"
        res = f"**__✦ ᴘᴀʀᴄ̧ᴀ__ : {title[:35]}\n__✦ sᴜ̈ʀᴇ__ : {duration}\n\n__✦ ɪsᴛᴇʏᴇɴ__ : {message.from_user.mention}**"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        await m.edit("**__✦ şᴀʀᴋɪ ʏᴜ̈ᴋʟᴇɴɪʏᴏʀ !__**")
        await message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="✦  𝐌𝐮̈𝐳𝐢𝐤 𝐁𝐨𝐭  ✦", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✦  𝖬𝗎̈𝗓𝗂𝗄 𝖪𝖺𝗒ı𝗍  ✦", url=f"t.me/{MCHANNEL}")]]))
        await m.delete()
        await _.send_audio(chat_id=PLAYLIST_ID, audio=audio_file, caption=res, performer="✦  𝐌𝐮̈𝐳𝐢𝐤 𝐁𝐨𝐭  ✦", parse_mode='md', title=title, duration=dur, thumb=thumb_name)
    except Exception as e:
        await m.edit("**__✦ ʙᴇɴɪ ʏᴏɴᴇᴛɪᴄɪ ʏᴀᴘɪɴ !__**")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

@app.on_message(filters.command(["vbul", "vsong"]) & ~filters.edited)
async def vsong(client, message):
    try:
        await message.delete()
    except:
        pass
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
        views = results[0]["views"]
        mention = message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("**__✦ ᴠɪᴅᴇᴏ ᴀʀᴀɴɪʏᴏʀ !__**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"**__✦ ᴠɪᴅᴇᴏ ʙᴜʟᴜɴᴀᴍᴀᴅɪ !__**")
    preview = wget.download(thumbnail)
    await msg.edit("**__✦ ᴠɪᴅᴇᴏ ɪɴᴅɪʀɪʟɪʏᴏʀ !__**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=f"**__✦ ᴘᴀʀᴄ̧ᴀ__ : {ytdl_data['title']}\n__✦ sᴜ̈ʀᴇ__ : {duration}\n\n__✦ ɪsᴛᴇʏᴇɴ__ : {message.from_user.mention}**",
    )
    try:
        os.remove(file_name)
        os.remove(thumb_name)
        await msg.delete()
    except Exception as e:
        print(e)

@app.on_message(filters.command(["ara", "search"]) & ~filters.edited)
async def ytsearch(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        if len(message.command) < 2:
            return await message.reply_text("**__✦ sᴏɴᴜᴄ̧ ʙᴜʟᴜɴᴀᴍᴀᴅɪ !**")
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("**__✦ ᴀʀɪʏᴏʀᴜᴍ !__**")
        results = YoutubeSearch(query, max_results=6).to_dict()
        i = 0
        text = ""
        while i < 6:
            text += f"**__💬 ᴘᴀʀᴄ̧ᴀ__ : {results[i]['title']}**\n"
            text += f"**__⌚ sᴜ̈ʀᴇ__ : {results[i]['duration']}**\n"
            text += f"**__🔗 ʟɪɴᴋ__ : [ ʏᴏᴜᴛᴜʙᴇ'ᴅᴇɴ ɪᴢʟᴇ ](https://youtube.com{results[i]['url_suffix']})**\n\n"
            i += 1
        await m.edit_text(
            text=text,
            disable_web_page_preview=True,
        )
    except Exception as e:
        await message.reply_text(str(e))


bot_token = '6404904263:AAHP25SjaF85qCncHTq5NE9zA4A-ASD5XNA'

bot_active = False

bot = telebot.TeleBot(bot_token)

# /yas komutuna yanıt veren bir işlev
@bot.message_handler(commands=['yas'])
def calculate_age(message):
    try:
        # Komutu kullanan kullanıcının doğum tarihini alın
        birthday_str = message.text.split()[-1]
        birthday = datetime.strptime(birthday_str, "%d.%m.%Y")

        # Şu anki tarihi alın
        current_date = datetime.now()

        # Kullanıcının yaşını hesaplayın
        age = current_date.year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))

        # Doğum gününün ne kadar zaman sonra olduğunu hesaplayın
        next_birthday = datetime(current_date.year, birthday.month, birthday.day)
        if current_date > next_birthday:
            next_birthday = datetime(current_date.year + 1, birthday.month, birthday.day)
        days_until_birthday = (next_birthday - current_date).days

        # Kullanıcıya cevap verin
        reply_message = f"🎉 sᴇᴠɢɪʟɪ {message.from_user.first_name}\n"
        reply_message += f"💭 şᴜᴀɴᴅᴀ {age} ʏᴀşɪɴᴅᴀsɪɴ .\n\n"
        reply_message += f"🎂 ᴅᴏɢ̆ᴜᴍ ɢᴜ̈ɴᴜ̈ɴ {days_until_birthday} ɢᴜ̈ɴ sᴏɴʀᴀ ."
        bot.reply_to(message, reply_message)
    except ValueError:
        bot.reply_to(message, "🗒️ ɢᴇᴄ̧ᴇʀsɪᴢ ᴛᴀʀɪʜ .\nᴅᴏɢ̆ʀᴜ ʙɪʀ ᴛᴀʀɪʜ ɢɪʀɪɴ .\nᴏ̈ʀɴᴇᴋ : 30.01.2000")
    except Exception as e:
        bot.reply_to(message, "🗒️ ʙɪʀ ʜᴀᴛᴀ ᴏʟᴜşᴛᴜ .\nsᴏɴʀᴀ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇʏɪɴ .")

# /burc komutuna yanıt veren bir işlev
@bot.message_handler(commands=['burc'])
def calculate_zodiac_sign(message):
    try:
        # Komutu kullanan kullanıcının doğum tarihini alın
        birthday_str = message.text.split()[-1]
        birthday = datetime.strptime(birthday_str, "%d.%m.%Y")

        # Burçları ve tarih aralıklarını tanımlayın
        zodiac_signs = [
            {"name": "𝗄𝗈𝖼̧", "start_date": datetime(birthday.year, 3, 21), "end_date": datetime(birthday.year, 4, 19)},
            {"name": "𝖻𝗈𝗀̆𝖺", "start_date": datetime(birthday.year, 4, 20), "end_date": datetime(birthday.year, 5, 20)},
            {"name": "𝗂𝗄𝗂𝗓𝗅𝖾𝗋", "start_date": datetime(birthday.year, 5, 21), "end_date": datetime(birthday.year, 6, 20)},
            {"name": "𝗒𝖾𝗇𝗀𝖾𝖼̧", "start_date": datetime(birthday.year, 6, 21), "end_date": datetime(birthday.year, 7, 22)},
            {"name": "𝖺𝗌𝗅𝖺𝗇", "start_date": datetime(birthday.year, 7, 23), "end_date": datetime(birthday.year, 8, 22)},
            {"name": "𝖻𝖺𝗌̧𝖺𝗄", "start_date": datetime(birthday.year, 8, 23), "end_date": datetime(birthday.year, 9, 22)},
            {"name": "𝗍𝖾𝗋𝖺𝗓𝗂", "start_date": datetime(birthday.year, 9, 23), "end_date": datetime(birthday.year, 10, 22)},
            {"name": "𝖺𝗄𝗋𝖾𝗉", "start_date": datetime(birthday.year, 10, 23), "end_date": datetime(birthday.year, 11, 21)},
            {"name": "𝗒𝖺𝗒", "start_date": datetime(birthday.year, 11, 22), "end_date": datetime(birthday.year, 12, 21)},
            {"name": "𝗈𝗀̆𝗅𝖺𝗄", "start_date": datetime(birthday.year, 12, 22), "end_date": datetime(birthday.year, 1, 19)},
            {"name": "𝗄𝗈𝗏𝖺", "start_date": datetime(birthday.year, 1, 20), "end_date": datetime(birthday.year, 2, 18)},
            {"name": "𝖻𝖺𝗅ı𝗄", "start_date": datetime(birthday.year, 2, 19), "end_date": datetime(birthday.year, 3, 20)},
        ]

        # Kullanıcının burcunu bulun
        zodiac_sign = None
        for sign in zodiac_signs:
            if sign["start_date"] <= birthday <= sign["end_date"]:
                zodiac_sign = sign["name"]
                break

        if zodiac_sign:
            bot.reply_to(message, f"💭 {birthday_str} ᴛᴀʀɪʜɪɴᴅᴇ \n🌟 ᴅᴏɢ̆ᴅᴜɢ̆ᴜɴᴜᴢᴀ ɢᴏ̈ʀᴇ ...\n\n✓ ʙᴜʀᴄᴜɴᴜᴢ : {zodiac_sign}")
        else:
            bot.reply_to(message, "🗒️ ɢᴇᴄ̧ᴇʀsɪᴢ ᴛᴀʀɪʜ ᴠᴇʏᴀ ʙᴜʀᴄ̧ ʜᴇsᴀᴘʟᴀɴᴀᴍᴀᴅɪ ...")
    except ValueError:
        bot.reply_to(message, "🗒️ ɢᴇᴄ̧ᴇʀsɪᴢ ᴛᴀʀɪʜ .\nᴅᴏɢ̆ʀᴜ ʙɪʀ ᴛᴀʀɪʜ ɢɪʀɪɴ .\nᴏ̈ʀɴᴇᴋ : 30.01.2000")
    except Exception as e:
        bot.reply_to(message, "🗒️ ʙɪʀ ʜᴀᴛᴀ ᴏʟᴜşᴛᴜ .\nsᴏɴʀᴀ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇʏɪɴ .")

# SUS KOMUTUNA YANIT VEREN BİR İŞLEV
@bot.message_handler(commands=['susjdkrkr'])
def deactivate_bot(message):
    global bot_active
    bot_active = False
    bot.reply_to(message, "Bot şu an pasif.")

# KONUS KOMUTUNA YANIT VEREN BİR İŞLEV
@bot.message_handler(commands=['konuskdjdk'])
def activate_bot(message):
    global bot_active
    bot_active = True
    bot.reply_to(message, "Bot şu an aktif.")

# İP KOMUTUNA YANIT VEREN BİR İŞLEV
@bot.message_handler(commands=['ipdndjr'])
def ip_sorgu(message):
    try:
        ip = message.text.split()[-1]

        # IP sorgusu işlemi
        response = requests.get(f"http://ip-api.com/json/{ip}").json()

        if response["status"] == "success":
            # IP sorgusu başarılı ise sonucu özelleştirin
            result = "🌐 IP Bilgileri 🌐\n\n"
            result += f"🔹 **IP Adresi:** `{response['query']}`\n"
            result += f"🔹 **Ülke:** `{response['country']}`\n"
            result += f"🔹 **Şehir:** `{response['city']}`\n"
            result += f"🔹 **Posta Kodu:** `{response['zip']}`\n"
            result += f"🔹 **Koordinatlar:** `{response['lat']}, {response['lon']}`\n"

            bot.reply_to(message, result)
        else:
            bot.reply_to(message, "IP sorgusu başarısız oldu.")
    except IndexError:
        bot.reply_to(message, "❌ İşlem Başarısız\n❗️ Lütfen Geçerli Bir IP Adresi Giriniz!\n\nÖrnek: /ip 8.8.8.8")
    except Exception as e:
        bot.reply_to(message, "❌ Bir Hata Oluştu\n\nLütfen Daha Sonra Tekrar Deneyin. . .⏳")

# DNS KOMUTUNU İŞLEYİN
@bot.message_handler(commands=['dnsjsdjkd'])
def dns_sorgu(message):
    try:
        domain = message.text.split()[-1]

        # DNS sorgusu işlemi
        response = requests.get(f"http://ip-api.com/json/{domain}").json()

        if response["status"] == "success":
            # DNS sorgusu başarılı ise sonucu özelleştirin
            result = "🌐 DNS Sorgusu 🌐\n\n"
            result += f"🔹 **Domain Adı:** `{domain}`\n"
            result += f"🔹 **IP Adresi:** `{response['query']}`\n"

            bot.reply_to(message, result, parse_mode='Markdown')
        else:
            bot.reply_to(message, "❌ DNS sorgusu başarısız oldu veya bu domain için herhangi bir IP adresi bulunamadı.")
    except IndexError:
        bot.reply_to(message, "❌ İşlem Başarısız\n❗️ Lütfen Geçerli Bir Domain Adı Giriniz!\n\nÖrnek: /dns example.com")
    except Exception as e:
        bot.reply_to(message, f"❌ Bir Hata Oluştu\n\nHata Detayı: {str(e)}")

# Bot'u çalıştırın
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        pass
'''
