من userbot import bot
من sys import argv
استيراد النظم
من telethon.errors.rpcerrorlist استيراد PhoneNumberInvalidError
استيراد نظام التشغيل
من تيليثون استيراد TelegramClient
من var استيراد Var
من userbot.utils استيراد load_module
من استيراد userbot LOAD_PLUG ، BOTLOG_CHATID ، LOGS
من مسار استيراد pathlib
استيراد asyncio
استيراد telethon.utils
استيراد heroku3


غير متزامن def add_bot ():
    ((await bot.start ()) إذا كانت os.environ.get ("PHONE") لا شيء آخر (في انتظار bot.start (phone = os.environ.get ("PHONE"))))
    bot.me = انتظار bot.get_me () 
    bot.uid = telethon.utils.get_peer_id (bot.me)



إذا لم يكن len (argv) في (1 ، 3 ، 4):
    bot.disconnect ()
آخر:
    bot.tgbot = لا شيء
    إذا لم يكن Var.TG_BOT_USER_NAME_BF_HER بلا:
        طباعة ("بدء تشغيل الروبوت المضمن")
        # لأعظم الخير للتجميل
        bot.tgbot = TelegramClient (
            "TG_BOT_TOKEN" ،
            api_id = Var.APP_ID ،
            api_hash = Var.API_HASH
        ) .start (bot_token = Var.TG_BOT_TOKEN_BF_HER)
        طباعة ("انتهت التهيئة بدون أخطاء")
        طباعة ("بدء Userbot")
        bot.loop.run_until_complete (add_bot ())
        إذا لم يكن Var.HEROKU_APP_NAME و Var.HEROKU_API_KEY بلا:
            Heroku = heroku3.from_key (Var.HEROKU_API_KEY)
            التطبيق = Heroku.app (Var.HEROKU_APP_NAME)
            heroku_var = app.config ()
            متغير = "SUDO_USERS"
            إذا كان متغيرًا في heroku_var:
                del heroku_var [متغير]
            آخر:
                طباعة ("كل خير!")
        طباعة ("اكتمل بدء التشغيل")
    آخر:
        ((bot.start ()) إذا كان os.environ.get ("PHONE") لا شيء آخر (bot.start (phone = os.environ.get ("PHONE"))))
    

استيراد الكرة الأرضية
المسار = 'userbot / plugins / *. py'
الملفات = glob.glob (المسار)
للاسم في الملفات:
    مع (الاسم) المفتوح كـ f:
        path1 = المسار (f.name)
        الاسم المختصر = path1.stem
        load_module (shortname.replace (". py"، ""))

استيراد userbot._core

print ("شكرًا لك على استخدام Telethon KSA. يعمل الروبوت الآن. تابع قناتنا: T.me/KSATHON")

إذا لم يكن len (argv) في (1 ، 3 ، 4):
    bot.disconnect ()
آخر:
    bot.run_until_disconnected ()
