from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    input_str = event.pattern_match.group(1)
    if input_str == "صمون":
        await event.edit(input_str)
        animation_chars = [
            "عشره بالف 🥖🥖",
            "صمون",
            "عشره بالف 🥖🥖🥖🥖",
            "صمون",
            "عشره بالف 🥖🥖🥖🥖🥖🥖",
            "صمون",
            "عشره بالف 🥖🥖🥖🥖🥖🥖🥖🥖",
            "عشره بالف 🥖🥖🥖🥖",
            "صمون",
            "عشره بالف 🥖🥖🥖🥖🥖🥖",
            "صمون",
            "عشره بالف 🥖🥖🥖🥖🥖🥖🥖🥖",
            "صمون",
            "عشره بالف 🥖🥖🥖🥖",
            "صمون",
            "عشره بالف 🥖🥖🥖🥖🥖🥖",
            "صمون",
            "عشره بالف 🥖🥖🥖🥖🥖🥖🥖🥖",
            "صمون",
            "عشره بالف 🥖🥖🥖🥖🥖🥖\nhttps://telegra.ph/file/4473182ac153401d32d61.jpg"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %5 ])

            
@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    input_str = event.pattern_match.group(1)
    if input_str == "كلاوات":
        await event.edit(input_str)
        animation_chars = [
            "لك انت",
            "لك انت وين",
            "لك انت وين لكيت",
            "لك انت وين لكيت هاي",
            "الكلاوات",
            "الكلاوات",
            "الكلاوات",
            "الكلاوات",
            "الكلاوات",
            "الكلاوات",
            "الكلاوات",
            "لك انت وين لكيت هاي الكلاوات\nhttps://telegra.ph/file/7490f0c3515dd9cd6e9db.jpg"
            
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %5 ])
