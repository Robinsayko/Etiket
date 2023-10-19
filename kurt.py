import heroku3
import random, os, logging, asyncio
import time
import os
import heroku3
import logging 
from mesaj.kurtmesaj import koyluu, sarhoss, gozcuu, yancii, seyircii, silahsorr, kmelekk, aptall, masonn, dedektiff, gozcucc, tavcii, eross, avcii, beceriksizz, demircii, karakk, prenss, bbaskanii, kahinn, hukumdarr, bariscill, ybilgee, uyutucuu, kurdumsuu, sehitt, simyacii, efendii, guzell, fgetirenn, hainn, ycocukk, lanetli
from mesaj.kurtmesaj import kurtadamm, alfakurtt, falcii, yavrukurtt, lycann, haydutt, mistikk, duzenbazz, karmelekk, ibliss, tarikatcii, rahipp, hirsizz, kustasii, cgidenn, skatill, kundakcii, necromancerr, rols, bilgis
from telethon import TelegramClient, events
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import StopPropagation
from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters



api_id = int(os.environ.get("APP_ID","26573250"))
api_hash = os.environ.get("API_HASH","6306d2d23b1083a6f757f64f0b0c609c")
bot_token = os.environ.get("TOKEN","6559325433:AAHRdRuS7agUSYXIYpQPfS7gYvLO5tXNPyY")

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)



@client.on(events.NewMessage(pattern="^/kurt$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     await event.reply(f"{rols}", buttons=(
                      [
                       Button.inline('👱 Köylü Takımı', data='koylutakim')
                      ],
                      [
                       Button.inline('🐺 Kurtlar & Müttefikleri', data='kurttakim')
                      ],
                      [
                       Button.inline('👤 Diğer Düşmanlar', data='bireysel')
                      ],
                    ),
                    link_preview=False)

  if event.is_group:
    return await client.send_message(event.chat_id, f"{rols}", buttons=(
                      [
                       Button.inline('👱 Köylü Takımı', data='koylutakim')
                      ],
                      [
                       Button.inline('🐺 Kurtlar & Müttefikleri', data='kurttakim')
                      ],
                      [
                       Button.inline('👤 Diğer Düşmanlar', data='bireysel')
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="grstart"))
async def start(event):
    async for usr in client.iter_participants(event.chat_id):
     await event.edit(f"{rols}",
                    buttons=(
                      [
                       Button.inline('👱 Köylü Takımı', data='koylutakim')
                      ],
                      [
                       Button.inline('🐺 Kurtlar & Müttefikleri', data='kurttakim')
                      ],
                      [
                       Button.inline('👤 Diğer Düşmanlar', data='bireysel')
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="koylutakim"))
async def handler(event):
    await event.edit(f"{bilgis}", buttons=(
                      [
                      Button.inline("Köylü 👱", data="koylu"),
                      Button.inline("Sarhoş 🍻", data="sarhos")
                      ],
                      [
                      Button.inline("Gözcü 👳", data="gozcu"),
                      Button.inline("Yancı 💋", data="yanci")
                      ],
                      [
                      Button.inline("Seyirci 👁", data="seyirci"),
                      Button.inline("Silahşör 🔫", data="silahsor")
                      ],
                      [
                      Button.inline("Koruyucu Melek 👼", data="kmelek"),
                      Button.inline("Aptal 🃏", data="aptal")
                      ],
                      [
                      Button.inline("Mason 👷", data="mason"),
                      Button.inline("Dedektif 🕵", data="dedektif")
                      ],
                      [
                      Button.inline("Gözcü Çırağı 🙇", data="gozcuc"),
                      Button.inline("Tarikatçı Avcı 💂", data="tavci")
                      ],
                      [
                      Button.inline("Eros 🏹", data="eros"),
                      Button.inline("Avcı 🎯", data="avci")
                      ],
                      [
                      Button.inline("Beceriksiz 🤕", data="beceriksiz"),
                      Button.inline("Demirci ⚒", data="demirci")
                      ],
                      [
                      Button.inline("Kara kurt 🐺🌑", data="karak")
                      ],
                      [
                      Button.inline("Prens 💍", data="prens"),
                      Button.inline("Belediye Başkanı 🎖", data="bbaskani")
                      ],
                      [
                      Button.inline("Kahin 🌀", data="kahin"),
                      Button.inline("Hükümdar 👑", data="hukumdar")
                      ],
                      [
                      Button.inline("Barışçıl ☮️", data="bariscil"),
                      Button.inline("Yaşlı Bilge 📚", data="ybilge")
                      ],
                      [
                      Button.inline("Uyutucu 💤", data="uyutucu"),
                      Button.inline("Kurdumsu 👱‍🌚", data="kurdumsu")
                      ],
                      [
                      Button.inline("Şehit 🔰", data="sehit"),
                      Button.inline("Simyacı 🍵", data="simyaci")
                      ],
                      [
                      Button.inline("Efendi 🛡", data="efendi"),
                      Button.inline("Güzel 💅", data="guzel")
                      ],
                      [
                      Button.inline("Fırtına Getiren 🌩", data="fgetiren"),
                      Button.inline("Hain 🖕", data="hain")
                      ],
                      [
                      Button.inline("Yabani Çocuk 👶", data="ycocuk"),
                      Button.inline("Lanetli 😾", data="lanetli")
                      ],
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kurttakim"))
async def handler(event):
    await event.edit(f"{bilgis}", buttons=(
                      [
                      Button.inline("Kurtadam 🐺", data="kurtadam"),
                      Button.inline("Alfa Kurt ⚡️", data="alfakurt")
                      ],
                      [
                      Button.inline("Falcı 🔮", data="falci"),
                      Button.inline("Yavru Kurt 🐶", data="yavrukurt")
                      ],
                      [
                      Button.inline("Lycan 🐺🌝", data="lycan")
                      ],
                      [
                      Button.inline("Haydut 🦉", data="haydut"),
                      Button.inline("Mistik ☄️", data="mistik")
                      ],
                      [
                      Button.inline("Düzenbaz Kurt 🐑", data="duzenbaz"),
                      Button.inline("Kara Melek 👼🐺", data="karmelek")
                      ],
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="bireysel"))
async def handler(event):
    await event.edit(f"{bilgis}", buttons=(
                      [
                      Button.inline("İblis 👺", data="iblis"),
                      Button.inline("Tarikatçı 👤", data="tarikatci")
                      ],
                      [
                      Button.inline("Rahip ✝️", data="rahip"),
                      Button.inline("Hırsız 😈", data="hirsiz")
                      ],
                      [
                      Button.inline("Çift - Giden 🎭", data="cgiden")
                      ],
                      [
                      Button.inline("Kukla ustası 🕴", data="kustasi"),
                      Button.inline("Seri Katil 🔪", data="skatil")
                      ],
                      [
                      Button.inline("Kundakçı 🔥", data="kundakci"),
                      Button.inline("Necromancer ⚰️", data="necromancer")
                      ],
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ]
                    ),
                    link_preview=False)




@client.on(events.callbackquery.CallbackQuery(data="koylu"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Köylü 👱\n\n🗯️ Hakkında :\n**{koyluu}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="sarhos"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Sarhoş 🍻\n\n🗯️ Hakkında :\n**{sarhoss}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="gozcu"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Gözcü 👳\n\n🗯️ Hakkında :\n**{gozcuu}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="yanci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Yancı 💋\n\n🗯️ Hakkında :\n**{yancii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="seyirci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Seyirci 👁\n\n🗯️ Hakkında :\n**{seyircii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="silahsor"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Silahşör 🔫\n\n🗯️ Hakkında :\n**{silahsorr}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kmelek"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Koruyucu Melek 👼\n\n🗯️ Hakkında :\n**{kmelekk}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="aptal"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Aptal 🃏\n\n🗯️ Hakkında :\n**{aptall}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="mason"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Mason 👷\n\n🗯️ Hakkında :\n**{masonn}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="dedektif"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Dedektif 🕵\n\n🗯️ Hakkında :\n**{dedektiff}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="gozcuc"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Gözcü Çırağı 🙇\n\n🗯️ Hakkında :\n**{gozcucc}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="tavci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Tarikatçı Avcı 💂\n\n🗯️ Hakkında :\n**{tavcii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="eros"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Eros 🏹\n\n🗯️ Hakkında :\n**{eross}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="avci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Avcı 🎯\n\n🗯️ Hakkında :\n**{avcii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="beceriksiz"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Beceriksiz 🤕\n\n🗯️ Hakkında :\n**{beceriksizz}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="demirci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Demirci ⚒\n\n🗯️ Hakkında :\n**{demircii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="karak"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Kara kurt 🐺🌑\n\n🗯️ Hakkında :\n**{karakk}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="prens"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Prens 💍\n\n🗯️ Hakkında :\n**{prenss}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="bbaskani"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Belediye Başkanı 🎖\n\n🗯️ Hakkında :\n**{bbaskanii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kahin"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Kahin 🌀\n\n🗯️ Hakkında :\n**{kahinn}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="hukumdar"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Hükümdar 👑\n\n🗯️ Hakkında :\n**{hukumdarr}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="bariscil"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Barışçıl ☮️\n\n🗯️ Hakkında :\n**{bariscill}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="ybilge"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Yaşlı Bilge 📚\n\n🗯️ Hakkında :\n**{ybilgee}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="uyutucu"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Uyutucu 💤\n\n🗯️ Hakkında :\n**{uyutucuu}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kurdumsu"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Kurdumsu 👱‍🌚\n\n🗯️ Hakkında :\n**{kurdumsuu}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="sehit"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Şehit 🔰\n\n🗯️ Hakkında :\n**{sehitt}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="simyaci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Simyacı 🍵\n\n🗯️ Hakkında :\n**{simyacii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="efendi"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Efendi 🛡\n\n🗯️ Hakkında :\n**{efendii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="guzel"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Güzel 💅\n\n🗯️ Hakkında :\n**{guzell}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="fgetiren"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Fırtına Getiren 🌩\n\n🗯️ Hakkında :\n**{fgetirenn}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="hain"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Hain 🖕\n\n🗯️ Hakkında :\n**{hainn}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="ycocuk"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Yabani Çocuk 👶\n\n🗯️ Hakkında :\n**{ycocukk}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="lanetli"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Lanetli 😾\n\n🗯️ Hakkında :\n**{lanetlii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

################################

@client.on(events.callbackquery.CallbackQuery(data="kurtadam"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Kurtadam 🐺\n\n🗯️ Hakkında :\n**{kurtadamm}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="alfakurt"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Alfa Kurt ⚡️\n\n🗯️ Hakkında :\n**{alfakurtt}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="falci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Falcı 🔮\n\n🗯️ Hakkında :\n**{falcii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="yavrukurt"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Yavru Kurt 🐶\n\n🗯️ Hakkında :\n**{yavrukurtt}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="lycan"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Lycan 🐺🌝\n\n🗯️ Hakkında :\n**{lycann}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="haydut"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Haydut 🦉\n\n🗯️ Hakkında :\n**{haydutt}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="mistik"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Mistik ☄️\n\n🗯️ Hakkında :\n**{mistikk}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="duzenbaz"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Düzenbaz Kurt 🐑\n\n🗯️ Hakkında :\n**{duzenbazz}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="karmelek"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Kara Melek 👼🐺\n\n🗯️ Hakkında :\n**{karmelekk}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

################################

@client.on(events.callbackquery.CallbackQuery(data="iblis"))
async def handler(event):
    await event.edit(f"**🌟 Rol : İblis 👺\n\n🗯️ Hakkında :\n**{ibliss}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="tarikatci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Tarikatçı 👤\n\n🗯️ Hakkında :\n**{tarikatcii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="rahip"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Rahip ✝️\n\n🗯️ Hakkında :\n**{rahipp}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="hirsiz"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Hırsız 😈\n\n🗯️ Hakkında :\n**{hirsizz}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kustasi"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Kukla ustası 🕴\n\n🗯️ Hakkında :\n**{kustasii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="cgiden"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Çift - Giden 🎭\n\n🗯️ Hakkında :\n**{cgidenn}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="skatil"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Seri Katil 🔪\n\n🗯️ Hakkında :\n**{skatill}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kundakci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Kundakçı 🔥\n\n🗯️ Hakkında :\n**{kundakcii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="necromancer"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Necromancer ⚰️\n\n🗯️ Hakkında :\n**{necromancerr}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)
    
client.run_until_disconnected()
