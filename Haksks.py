استيراد  نظام التشغيل

فئة  Var ( كائن ):
    APP_ID  =  كثافة العمليات ( نظام التشغيل . البيئى . الحصول على ( "APP_ID" ، 6 ))
    # 6 عنصر نائب
    API_HASH  =  نظام التشغيل . بيئة . الحصول على ( "API_HASH" ، "eb06d4abfb49dc3eeb1aeb98ae0f581e" )
    STRING_SESSION  =  نظام التشغيل . بيئة . الحصول على ( "STRING_SESSION" ، لا يوجد )
    DB_URI  =  نظام التشغيل . بيئة . الحصول على ( "DATABASE_URL" ، لا يوجد )
    TEMP_DOWNLOAD_DIRECTORY  =  نظام التشغيل . بيئة . الحصول على ( "TEMP_DOWNLOAD_DIRECTORY" ، لا يوجد )
    LOGGER  =  صحيح
    GITHUB_ACCESS_TOKEN  =  نظام التشغيل . بيئة . الحصول على ( "GITHUB_ACCESS_TOKEN" ، لا يوجد )
    GIT_REPO_NAME  =  نظام التشغيل . بيئة . الحصول على ( "GIT_REPO_NAME" ، لا يوجد )
    # هنا لأغراض لاحقة
    SUDO_USERS  =  مجموعة ( كثافة العمليات ( س ) ل  س  في  نظام التشغيل . البيئى . الحصول على ( "SUDO_USERS" ، "967883138" ). انقسام ())
    LYDIA_API_KEY  =  نظام التشغيل . بيئة . الحصول على ( "LYDIA_API_KEY" ، لا يوجد )
    LESS_SPAMMY  =  نظام التشغيل . بيئة . احصل على ( "LESS_SPAMMY" ، لا يوجد )
    HEROKU_API_KEY  =  نظام التشغيل . بيئة . الحصول على ( "HEROKU_API_KEY" ، لا يوجد )
    HEROKU_APP_NAME  =  نظام التشغيل . بيئة . الحصول على ( "HEROKU_APP_NAME" ، لا يوجد )
    TG_BOT_TOKEN_BF_HER  =  نظام التشغيل . بيئة . الحصول على ( "TG_BOT_TOKEN_BF_HER" ، لا يوجد )
    # إرسال .get_id في أي قناة لملء هذه القيمة.
    PLUGIN_CHANNEL  =  كثافة العمليات ( نظام التشغيل . البيئى . الحصول على ( "PLUGIN_CHANNEL" ، - 100 ))
    TG_BOT_USER_NAME_BF_HER  =  نظام التشغيل . بيئة . الحصول على ( "TG_BOT_USER_NAME_BF_HER" ، لا يوجد )
    NO_SONGS  =  منطقي ( نظام التشغيل . البيئى . الحصول على ( "NO_SONGS" ، خطأ ))
    DOWNLOAD_PFP_URL_CLOCK  =  نظام التشغيل . بيئة . الحصول على ( "DOWNLOAD_PFP_URL_CLOCK" ، لا يوجد )
    G_DRIVE_CLIENT_ID  =  نظام التشغيل . بيئة . الحصول على ( "G_DRIVE_CLIENT_ID" ، لا يوجد )
    G_DRIVE_CLIENT_SECRET  =  نظام التشغيل . بيئة . الحصول على ( "G_DRIVE_CLIENT_SECRET" ، لا يوجد )
    GDRIVE_FOLDER_ID  =  نظام التشغيل . بيئة . الحصول على ( "GDRIVE_FOLDER_ID" ، "root" )
    AUTH_TOKEN_DATA  =  نظام التشغيل . بيئة . الحصول على ( "AUTH_TOKEN_DATA" ، لا يوجد )
    MAX_FLOOD_IN_P_M_s  =  كثافة العمليات ( نظام التشغيل . البيئى . الحصول على ( "MAX_FLOOD_IN_P_M_s" ، 3 ))
    إذا  AUTH_TOKEN_DATA  ! =  لا شيء :
        إن  لم يكن  نظام التشغيل . المسار . إسدير ( TEMP_DOWNLOAD_DIRECTORY ):
            نظام التشغيل . صوريات ( TEMP_DOWNLOAD_DIRECTORY )
        t_file  =  فتح ( TEMP_DOWNLOAD_DIRECTORY + "auth_token.txt" ، "w" )
        t_file . اكتب ( AUTH_TOKEN_DATA )
        t_file .إغلاق ()
    PRIVATE_GROUP_ID  =  نظام التشغيل . بيئة . الحصول على ( "PRIVATE_GROUP_ID" ، لا يوجد )
    إذا كان  PRIVATE_GROUP_ID  ! =  لا يوجد :
        محاولة :
            PRIVATE_GROUP_ID  =  int ( PRIVATE_GROUP_ID )
        إلا  ValueError :
            رفع  ValueError ( "معرف المجموعة الخاصة غير صالح. تأكد من أن المعرف يبدأ بـ -100 وتأكد من أنه أرقام فقط." )

 تطوير الفصل ( Var ):
    المسجل  = صحيح
    # هنا لأغراض لاحقة
