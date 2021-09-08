# حقوق النشر 2019-2020 DarkPrinc3

# مرخص بموجب ترخيص أباتشي ، الإصدار 2.0 ("الترخيص") ؛
# لا يجوز لك استخدام هذا الملف إلا بما يتوافق مع الترخيص.
# يمكنك الحصول على نسخة من الترخيص على

# http://www.apache.org/licenses/LICENSE-2.0

# ما لم يكن مطلوبًا بموجب القانون المعمول به أو تم الاتفاق عليه كتابةً ، البرنامج
# موزعة بموجب الترخيص يتم توزيعها على أساس "كما هي" ،
# بدون ضمانات أو شروط من أي نوع ، سواء كانت صريحة أو ضمنية.
# راجع الترخيص للحصول على أذونات تحكم لغة معينة و
# قيود بموجب الترخيص.

من  userbot  import  bot
من  أحداث الاستيراد telethon  
من  userbot . utils  import  command ، remove_plugin ، load_module
من  var  استيراد  Var
استيراد  importlib
من  مسار استيراد pathlib  
من  userbot  استيراد  LOAD_PLUG
استيراد  النظم
استيراد  asyncio
استيراد  traceback
استيراد  نظام التشغيل
استيراد برنامج  userbot . المرافق
من  تاريخ  استيراد  ووقت وتاريخ

DELETE_TIMEOUT  =  5

@ أمر ( النمط = "^ .install" ، الصادر = صحيح )
 تثبيت مواطن غير  متزامن ( حدث ):
    إذا  حدث . fwd_from :
        إرجاع
    إذا  حدث . reply_to_msg_id :
        جرب :
            download_file_name  =  انتظار  الحدث . العميل . download_media (   # pylint: تعطيل = E0602
                انتظر  الحدث . get_reply_message () ،
                "userbot / plugins /"   # pylint: تعطيل = E0602
            )
            إذا كان  "("  ليس  في  download_file_name :
                path1  =  مسار ( downloaded_file_name )
                الاسم المختصر  =  المسار 1 . إيقاف
                load_module ( SHORTNAME . محل ( ".py" ، "" ))
                انتظر  الحدث . تحرير ( "تثبيت البرنامج المساعد` `{}" . شكل ( نظام التشغيل . الطريق . basename ( downloaded_file_name )))
            آخر :
                نظام التشغيل . إزالة ( download_file_name )
                انتظر  الحدث . تحرير ( "أخطاء! هذا البرنامج المساعد مثبت بالفعل / مثبت مسبقًا." )
        باستثناء  استثناء  مثل  e :   # pylint: disable = C0103 ، W0703
            انتظر  الحدث . تحرير ( شارع ( هـ ))
            نظام التشغيل . إزالة ( download_file_name )
    في انتظار  أسينسيو . النوم ( DELETE_TIMEOUT )
    انتظر  الحدث . حذف ()

@ الأمر ( النمط = "^. إرسال (؟ P <shortname> \ w +) $" ، الصادر = صحيح )
 إرسال مواطن غير  متزامن ( حدث ):
    إذا  حدث . fwd_from :
        إرجاع
    message_id  =  حدث . رسالة . هوية شخصية
    input_str  =  حدث . pattern_match [ " الاسم المختصر " ]
    the_plugin_file  =  "./userbot/plugins/{}.py" . تنسيق ( input_str )
    البدء  =  التاريخ والوقت . الآن ()
    انتظر  الحدث . العميل . send_file (   # pylint: تعطيل = E0602
        حدث . chat_id ،
        the_plugin_file ،
        force_document = صحيح ،
        allow_cache = خطأ ،
        reply_to = message_id
    )
    النهاية  =  التاريخ والوقت . الآن ()
    time_taken_in_ms  = ( نهاية  -  البداية ). ثواني
    انتظر  الحدث . تحرير ( "تم التحميل {} في {} ثانية" . تنسيق ( input_str ، time_taken_in_ms ))
    في انتظار  أسينسيو . النوم ( DELETE_TIMEOUT )
    انتظر  الحدث . حذف ()

@ الأمر ( النمط = "^ .unload (؟ P <shortname> \ w +) $" ، الصادر = صحيح )
غير متزامن  def  unload ( حدث ):
    إذا  حدث . fwd_from :
        إرجاع
    الاسم المختصر  =  حدث . pattern_match [ " الاسم المختصر " ]
    جرب :
        remove_plugin ( SHORTNAME )
        انتظر  الحدث . تحرير ( f "تم تفريغ { shortname } بنجاح" )
    باستثناء  الاستثناء  كـ  e :
        انتظر  الحدث . تحرير ( "بنجاح إلغاء تحميل {shortname} \ n {}" . تنسيق (اسم قصير ، str ( e )))

@ الأمر ( النمط = "^ .load (؟ P <shortname> \ w +) $" ، الصادر = صحيح )
 تحميل غير متزامن def  load ( event ):
    إذا  حدث . fwd_from :
        إرجاع
    الاسم المختصر  =  حدث . pattern_match [ " الاسم المختصر " ]
    جرب :
        جرب :
            remove_plugin ( SHORTNAME )
        باستثناء :
            يمر
        load_module ( SHORTNAME )
        انتظر  الحدث . تحرير ( f "تم تحميل { shortname } بنجاح " )
    باستثناء  الاستثناء  كـ  e :
        انتظر  الحدث . تحرير ( f "تعذر تحميل { shortname } بسبب الخطأ التالي. \ n { str ( e ) } " )
