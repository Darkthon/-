# (ج) كساثون
# الأصل بقلمKSATHON تحرير بواسطةBERLIV

من أحداث الاستيراد telethon
استيراد asyncio
من مجموعات استيراد deque


@ borg.on (events.NewMessage (pattern = r "\. earth" ، الصادرة = True))
غير متزامن def _ (حدث):
	إذا event.fwd_from:
		إرجاع
	deq = deque (list ("🌏🌍🌎🌎🌍🌏🌍🌎"))
	لـ _ في النطاق (48):
		انتظر asyncio.sleep (0.1)
		انتظار الحدث. تحرير ("". انضم (deq))
		ديق.روت (1)
