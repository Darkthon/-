استيراد  نظام التشغيل
من  تاريخ  استيراد  ووقت وتاريخ
من  استيراد صورة PIL  ، ImageDraw ، ImageFont 
من  pySmartDL  استيراد  SmartDL
من  telethon . وظائف استيراد TL  
استيراد  asyncio
استيراد  شيل

FONT_FILE_TO_USE  =  "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

@ الأمر ( النمط = "^ .autopic" ، الصادر = صحيح )
غير متزامن  def  autopic ( حدث ):
    download_file_name  =  "userbot / original_pic.png"
    downloader  =  SmartDL ( Var . DOWNLOAD_PFP_URL_CLOCK ، download_file_name ، progress_bar = False )
    تنزيل . بدء ( منع = خطأ )
    الصورة  =  "userbot / photo_pfp.png"
    أثناء  عدم  التنزيل . منتهي ():
        place_holder  =  لا يوجد
    العداد  =  - 30
    بينما  صحيح :
        شوتيل . نسخ ( download_file_name ، photo )
        im  =  صورة . فتح ( صورة )
        file_test  =  im . استدارة ( عداد ، توسيع = خطأ ). حفظ ( الصورة ، "PNG" )
        current_time  =  datetime . الآن (). strftime ( "⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ \ n   الوقت:٪ H:٪ M \ n   التاريخ:٪ d.٪ m.٪ y \ n ⚡⚡⚡⚡ ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ " )
        img  =  صورة . افتح ( صورة )
        draw_text  =  ImageDraw . ارسم ( img )
        FNT  =  ImageFont . تروتايب ( FONT_FILE_TO_USE ، 30 )
        draw_text . نص (( 95 ، 250 )، current_time ، font = fnt ، fill = ( 255 ، 255 ، 255 ))
        IMG . حفظ ( صورة )
        ملف  =  انتظار  البوت . upload_file ( الصورة )   # pylint: تعطيل = E0602
        جرب :
            في انتظار  بوت ( وظائف . صور . UploadProfilePhotoRequest (   # pylint: تعطيل = E0602
                ملف
            ))
            نظام التشغيل . إزالة ( الصورة )
            العداد  - =  30
            في انتظار  أسينسيو . النوم ( 60 )
        باستثناء :
            إرجاع
