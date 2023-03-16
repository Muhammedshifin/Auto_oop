from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client as bot
from plugins.function import make_carbon
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
aiohttpsession = ClientSession()

C = "Successfully Created Your Carbon"
F = InlineKeyboardMarkup(
[[
     InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/myownbots")
]]
)




@bot.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Replay To A Text Message to Make Carbon Image."
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "Replay To A Text."
        )
    user_id = message.from_user.id
    m = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("ᴜᴘʟᴏᴀᴅɪɴɢ..")
    await message.reply_photo(
        photo=carbon,
        caption=C,
        reply_markup=F)
    await m.delete()
    carbon.close()
