from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
async def investment_project(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """الرد على رسالة 'المشروع الاستثماري' بالرسالة الترحيبية والأزرار."""
    keyboard = [
        [InlineKeyboardButton("القناة الرسمية على  🔥Instagram", callback_data='button_1')],
        [InlineKeyboardButton("القناة الرسمية على ⚡️Telegram", callback_data='button_2')],
        [InlineKeyboardButton("رابط قروب المناقشات 💎", callback_data='button_3')],
        [InlineKeyboardButton("فكرة المشروع 🌟", callback_data='button_4')],
        [InlineKeyboardButton("آلية العمل 🌟", callback_data='button_5')],
        [InlineKeyboardButton("المستويات والباقات 🌟", callback_data='button_6')],
        [InlineKeyboardButton("المكافآت💎", callback_data='button_7')],
        [InlineKeyboardButton("نسبة الأرباح ⚡️️", callback_data='button_8')],
        [InlineKeyboardButton("نظام باقات الدبل 🔥", callback_data='button_9')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = "مرحباً بك في المشروع الاستثماري! 🌟\nاختر من القائمة أدناه للمزيد من المعلومات:"

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("القناة الرسمية على  🔥Instagram", callback_data='button_1')],
        [InlineKeyboardButton("القناة الرسمية على ⚡️Telegram", callback_data='button_2')],
        [InlineKeyboardButton("رابط قروب المناقشات 💎", callback_data='button_3')],
        [InlineKeyboardButton("فكرة المشروع 🌟", callback_data='button_4')],
        [InlineKeyboardButton("آلية العمل 🌟", callback_data='button_5')],
        [InlineKeyboardButton("المستويات والباقات 🌟", callback_data='button_6')],
        [InlineKeyboardButton("المكافآت💎", callback_data='button_7')],
        [InlineKeyboardButton("نسبة الأرباح ⚡️️", callback_data='button_8')],
        [InlineKeyboardButton("نظام باقات الدبل 🔥", callback_data='button_9')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text('"أهلاً وسهلاً  في المجموعة! 🎉', reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.edit_message_text('f"أهلاً وسهلاً {member.full_name} في المجموعة! 🎉', reply_markup=reply_markup)

# pressure on buttons
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # info for buttons
    button_info = {
        'button_1': "https://www.instagram.com/king_crypto30",
        'button_2': "https://t.me/king_ofcryptocurrencies",
        'button_3': "https://t.me/king_of_crypto_currencies",
        'button_4': "استثمر رأس مالك وتعلم التداول بنفس الوقت بمشروع (king of crypto) مشروع وليد للاستثمار🔥 \n"
                    "الايداع الاول بالمنصه يبدأ من 200$ - 20,000$ 🔥 وبتقدر تسحب ارباحك على نسبة : \n"
                    "يومي : 1% 💎\n"
                    "او اسبوعي على نسبة 8% 💎\n"
                    "او اسبوعين على نسبة 2575% 💎\n"
                    "او شهري على نسبة 75% 💎\n"
                    "نسبة الارباح للحساب المتميز تكون ضرب 86% 💎\n"
                    "و نسبة العائد للصفقه 86% 💎\n"
                    "مثال : دخلت برأس مال من 200 ل 399 دولار وهو المستوى الاول و الباقه الشهريه\n"
                    "200*75%=350 دولار 💫 بيكون ربحك بالشهر مع رأس المال\n"
                    "ملاحظه : مع العلم ان هناك باقات بالمنصه ومستويات تتناسب لجميع المستثمرين للاشتراك\n"
                    "و طريقه حصولك على الارباح بتكون ايداع فوري من صاحب المشروع ع منصه بايننس للمستثمر حسب الباقه الي اختار المستثمر فيها من دون رسوم سحب او ايداع و بأي وقت حبيت تسحب فلوسك بصير \n\n"
                    "🌟 طريقه الاستثمار بمشروع وليد king of crypto :🌟  ا\n"
                    "⚡️ مافي ابدا نظام الاشارات مثل ما كنا مخدوعين بالمنصات اليوميه نهائيا \n\n"
                    "ولكن هناك فريق ذو خبره بمجال التداول يترأسهم صاحب المشروع اخونا وليد منذ 10 سنوات هدفه تحقيق الارباح وتجنب الخسائر حيث يشتغل هذا الفريق على برمجة التداول trading abi  وهلى شركة وساطه مالية financail brokerage combamy تعتمد على اكثر من 32 اداة ماليه يعني اصول و أسهم ماليه مرتبطه بلأسواق العالميه وسوق الفوريكس (طبعا سوق الفوريكس من اشهر واضخم الاسواق الماليه يتم فيه تداول عملات الدول بين ملايين المستثمرين والبنوك و الصناديق الاستثماريه. الهدف منه الاستفادة من تغيير اسعار صرف العملات وتحقيق الربح)⚡️\n\n"
                    "و سوق الكريبتو 💎 و سوق الذهب 💎و سوق السلع 💎 والخيارات الثنائيه \n\n"
                    "ويقوم هذا الفريق على الذي يضم مجموعه من الخبراء والمحللين و مدراء المحافظ على مستوى الخليج والدول العربيه ب اقتناص الفرص الاستثماريه الرابحه بكل الادوات الماليه المتاحه و جميع الأسواق الماليه المتاحه ويقوم ايضا بالتداول عنك بالكامل بمنصه عالميه و موثوقه وليست ب جديده اسمها اكسبرت اوبشن تأسست سنه 2014 وعمرها الافتراضي 37 سنة \n\n"
                    "هنالك محظه استثماريه مجمعه ل ضمان أموال المستثمرين تحديدا بالمنصه العالميه اكسبرت اوبشن ل اخونا المستثمر وليد 🔥 حيث يتم ايداع المبلغ المناسب لك للاستثمار فقط \n\n"
                    "اكيد بهمنا يكون شغلنا حلال مليون بلمية وعشان هيك اطمنك انه حلال و اسأل اهل العلم و دائره الافتاء واحكيلهم عن شغلنا وما تودع معنا اي دينار قبل ما تطمن ميه بالميه \n\n"
                    "ملاحظه : مثل ما حكيتلكم بالبدايه انه في تعليم التداول ع اصوله مع اخونا وليد 🌟 شلون : \n"
                    "رح اخبرك انه استاذ وليد رح يدربنا 🌟 على التداول بنفسه وفريقه ايضا حسب استراتيجيات معينه و تواقيت لنتمكن نحن ب انفسنا ان نبدأ بتداول بعد فهمنا كل شيء يخص التداول \n\n"
                    "للعلم فقط ان استاذ وليد مثلما ذكرت بالبدايه منذ 10 سنوات بهذا المجال لديه ايضا مشاريع عده ليس بلأردن فقط بالتداول بالخليج , دعونا ننوه ايضا ان اخونا وليد هو شاب عربي من سلطنه عمان نتواصل معه على مدار الساعه سواء بالمكالمات الصوتيه او المحادثات المرئيه على التلقرام وايضا يمكن لأي مستثمر معنا ان يدخل معه ب مكالمة فيديو ومعنا ناس هون بعرفوه من اكثر من سنه ومنهم اكثر واكثر \n"
                    "اساس عمل البروفيسور وليد 🔥 المصداقيه والشفافيه بالعمل\n"
                    "هنالك ايضا فعاليات و مسابقات يترأسها استاذ وليد عبر المحادثات المرئيه على التليقرام و مجموعه من المشرفين اللذين لديهم الخبره الكافيه للاجابه على اي استفسار من قبل المستثمرين الجدد و الأشراف على هذا الحفل و توزيع الجوائز الماديه فيها",
        'button_5': "🌟 دور الأستاذ وليد في الاستثمار ودور المستثمر مع الوليد والهدف🌟\n\n"
                    "أولاً: دور المستثمر هو إيداع المبلغ على المحفظة الاستثمارية المجمعة لضمان أموال المستثمرين وتحديداً مبلغ الإيداع الأولي.\n"
                    "الآن بعد الإيداع الأولي، ينتهي دور المستثمر من خلال فتح الحساب وضمّه إلى المحفظة الاستثمارية المجمعة، ثم يأتي دور الأستاذ وليد في استثمار المبلغ.\n\n"
                    "كيف يحقق الأستاذ وليد الأرباح؟ وما هي آلية العمل المتبعة؟ وما هو التكنيك الذي يستخدمه أو الاستراتيجية التي يتبعها لتحقيق الأرباح؟\n\n"
                    "الأستاذ وليد يعمل على برمجة التداول (Trading API)\n"
                    "وعلى شركة وساطة مالية (Financial Brokering Company)\n"
                    "🔥 تعتمد على أكبر 32 إدارة مالية. نحن نتحدث عن أصول وأسواق مالية عالمية مثل:\n"
                    "- 🌟 سوق الأسهم (Global Stock Exchange)\n"
                    "- 💎 سوق الفوركس (Foreign Exchange Market): وهو أحد أشهر الأسواق المالية، حيث يتم فيه تداول عملات الدول بين ملايين المستثمرين والبنوك والصناديق الاستثمارية لأغراض متعددة، من أهمها الاستفادة من تغير أسعار صرف العملات وتحقيق الربح.🔥 \n"
                    "-💎 سوق الكريبتو، سوق الذهب، وسوق السلع والخيارات الثنائية.\n\n"
                    " 💫 هنا يأتي دور الأستاذ وليد، حيث يمتلك فريقاً من الخبراء والمحللين والمتداولين ومدراء المحافظ على مستوى الخليج والدول العربية، ويقوم باقتناص الفرص الاستثمارية الرابحة بكل الأدوات المالية المتاحة وجميع الأسواق المالية.\n\n"
                    "💫عمل الأستاذ وليد لا يقتصر على سوق الفوركس أو الكريبتو أو سوق السلع أو الخيارات الثنائية؛🌟 أينما وجدت فرص رابحة يتم اقتناصها وتحقيق الأرباح.\n\n"
                    "الهدف من العمل في مشروع King of Crypto هو تحقيق الأرباح المطلوبة وتجنب الخسائر المالية.",
        'button_6': "vip1 : 200$ - 399$🌟 \nvip2 : 400$ - 799$🌟 \nvip3 : 800$ - 1199$🌟 \nvip4 : 1200$ - 1799$🌟 \nvip5 : 1800$ - 2399$🌟 \nvip6 : 2400$ - 7999$🌟 \n 💎المتميز : 8000$ - 20,000$🌟",
        'button_7': "vip1 : +3%💎 \nvip2 : +20$💎 \nvip3 : +40$💎 \nvip4 : +60$💎 \nvip5 : +80$💎 \nvip6 : +120$💎 \nمكافأة الإحالة للمستوى المتميز لكل شخص ينضم عن طريقك +5%🌟",
        'button_8': "يومي بنسبة 1%🌟 \nاسبوعي بنسبة 8%🌟 \nاسبوعين بنسبة 25%🌟 \nشهري بنسبة 75%🌟 \nنسبة الأرباح الشهرية للمستوى المتميز 86% و لنظام باقات الدبل 97%🌟",
        'button_9': "⚡️ نظام باقة الدبل على نسبة أرباح 97% شهرياً ضمن هذه الشروط:\n"
                    "1-🌟 رأس مال ثابت لمدة سنة واحدة فقط.\n"
                    "2-🌟 الدبل لثلاثة شهور فقط بنسبة 97% من رأس المال لكل شهر.\n"
                    "3-🌟 يصبح رأس المال هو مجموع المبلغ المدبل في الثلاثة أشهر.\n"
                    "4-🌟 يتم سحب الأرباح الشهرية بعد التدبيل ولمدة 9 أشهر.\n\n"
                    "على سبيل المثال:🌙 رأس مال 1000 دولار شهرياً بنسبة 97% تحصل فيه على 970 دولار.\n"
                    "🔥 الشهر الأول 970$ + الشهر الثاني 970$ + الشهر الثالث 970$ = إجمالي التدبيل 2910$.\n"
                    "🌟 حيث يستلم المستثمر الشهر الرابع مبلغ 2910$ كأول دفعة له، والشهر الخامس 2910$، وهكذا حتى انتهاء المدة.\n"
                    "🌟 بعد انتهاء عقد السنة، يعود رأس المال المدبل إلى المبلغ الأولي 1000$ على الباقة الشهرية بنسبة 75%🌟 "
    }

    if query.data == 'back_to_main':
        await start(update, context)
    else:
        response = button_info.get(query.data, 'لا توجد معلومات متاحة لهذا الزر')
        keyboard = [[InlineKeyboardButton("العودة إلى الأزرار الرئيسية", callback_data='back_to_main')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=response, reply_markup=reply_markup)
