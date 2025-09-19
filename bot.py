# -*- coding: utf-8 -*-
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

# ─────────────── 🔐 الإعدادات ───────────────
TELEGRAM_TOKEN = "7685861730:AAGn4h7VL8T55kjXrRED5lqdFs8oz7n8W78"

# 🔗 الروابط القابلة للتعديل (حط روابطك هنا)
REGISTER_ADVANCED = "https://smartincome-17.com/xvvXKYw"      # سجّل الآن - برنامج الاستراتيجيات المتقدمة
REGISTER_BASIC    = "https://smartincome-17.com"      # سجّل الآن - البداية من الصفر
REGISTER_WEEKLY   = "https://smartincome-17.com/gydpAVV"      # سجّل الآن - مشاركة الفرص الأسبوعية
NATIONAL_REGISTER = "https://smartincome-17.com"      # سجّل الآن - عروض اليوم الوطني
FREE_GROUP_LINK   = "https://t.me/+HM9i6LEZsUZhZDRk"
SUPPORT_LINK      = "https://t.me/ecombassam"

LINK_COVER_CALL   = "https://t.me/smart1in/1226"
LINK_SNAP         = "https://t.snapchat.com/6MzlRYhF"
LINK_YOUTUBE      = "https://youtube.com/channel/UCGqRv9hWPDNvbI1Y-83D4bw"
LINK_FAQ          = "https://t.me/smart1in/1149"
LINK_7PCT_DEMO    = "https://t.me/smart1in/1161"

# ─────────────── 🧭 المفاتيح (callback_data) ───────────────
CB_MORE_INFO        = "more_info"
CB_PROGRAMS         = "programs"
CB_NATIONAL_OFFER   = "national_offer"
CB_IMPORTANT_LINKS  = "important_links"
CB_GROUP            = "group"
CB_SUPPORT          = "support"
CB_BACK_MAIN        = "back_main"

CB_PROG_ADVANCED    = "prog_advanced"
CB_PROG_BASIC       = "prog_basic"
CB_PROG_WEEKLY      = "prog_weekly"

# ─────────────── 🧩 قائمة رئيسية ───────────────
def main_menu_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("ℹ️ معرفة المزيد", callback_data=CB_MORE_INFO)],
        [InlineKeyboardButton("📚 أنواع البرامج التدريبية", callback_data=CB_PROGRAMS)],
        [InlineKeyboardButton("🎉 عروض اليوم الوطني", callback_data=CB_NATIONAL_OFFER)],
        [InlineKeyboardButton("📌 روابط مهمة", callback_data=CB_IMPORTANT_LINKS)],
        [InlineKeyboardButton("👥 الانضمام إلى قروب مجاني", callback_data=CB_GROUP)],
        [InlineKeyboardButton("🤖 الدعم الفني", callback_data=CB_SUPPORT)],
    ])

# ─────────────── 🚀 /start ───────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "مرحباً 👋\n"
        "أهلاً بك في بوت برنامج الاستراتيجيات المتقدمة 🚀\n\n"
        "📈 خطوتك لبناء دخل شهري مستقر من سوق الأوبشن\n"
        "🎥 الدورة مسجّلة بالكامل – تبدأ وقت ما تحب"
    )
    if update.message:
        await update.message.reply_text(text, reply_markup=main_menu_markup())
    else:
        await update.callback_query.edit_message_text(text, reply_markup=main_menu_markup())

# ─────────────── 🎛️ التعامل مع الأزرار ───────────────
async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    # ℹ️ معرفة المزيد
    if q.data == CB_MORE_INFO:
        text = (
            "🚀 البرنامج التدريبي للاستراتيجيات المتقدمة\n\n"
            "📌 المميزات:\n"
            "• 🎥 11 درس مسجّل خطوة بخطوة.\n"
            "• 📈 4 استراتيجيات عملية لتحقيق عوائد 8–15% شهريًا.\n"
            "• 🔒 تطوير الكوفر كول كدخل ثابت.\n"
            "• ⚡️ شرح الكريدت (كول + بوت).\n"
            "• 🛡️ حماية رأس المال.\n\n"
            "🎯 النتيجة:\n"
            "✅ محفظة دخل شهرية ثابتة.\n"
            "✅ وضوح متى وأين تستخدم كل استراتيجية.\n"
            "✅ خطة مدروسة بدل العشوائية."
        )
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("📚 أنواع البرامج التدريبية", callback_data=CB_PROGRAMS)],
            [InlineKeyboardButton("⬅️ رجوع", callback_data=CB_BACK_MAIN)],
        ])
        await q.edit_message_text(text, reply_markup=kb)

    # 📚 أنواع البرامج التدريبية
    elif q.data == CB_PROGRAMS:
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("📈 برنامج الاستراتيجيات المتقدمة", callback_data=CB_PROG_ADVANCED)],
            [InlineKeyboardButton("📊 البداية من الصفر للأوبشن", callback_data=CB_PROG_BASIC)],
            [InlineKeyboardButton("📅 مشاركة الفرص الأسبوعية", callback_data=CB_PROG_WEEKLY)],
            [InlineKeyboardButton("⬅️ رجوع", callback_data=CB_BACK_MAIN)],
        ])
        await q.edit_message_text("📚 اختر البرنامج التدريبي 👇", reply_markup=kb)

    # 📈 برنامج الاستراتيجيات المتقدمة
    elif q.data == CB_PROG_ADVANCED:
        text = "📈 تفاصيل برنامج الاستراتيجيات المتقدمة:\n- شرح استراتيجيات عملية لبناء دخل شهري.\n- محتوى مسجّل كامل."
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("📌 سجّل الآن", url=REGISTER_ADVANCED)],
            [InlineKeyboardButton("⬅️ رجوع", callback_data=CB_PROGRAMS)],
        ])
        await q.edit_message_text(text, reply_markup=kb)

    # 📊 البداية من الصفر
    elif q.data == CB_PROG_BASIC:
        text = "📊 البداية من الصفر للأوبشن:\n- تأسيس كامل للمبتدئين.\n- تبسيط حتى أول صفقة."
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("📌 سجّل الآن", url=REGISTER_BASIC)],
            [InlineKeyboardButton("⬅️ رجوع", callback_data=CB_PROGRAMS)],
        ])
        await q.edit_message_text(text, reply_markup=kb)

    # 📅 مشاركة الفرص الأسبوعية
    elif q.data == CB_PROG_WEEKLY:
        text = "📅 مشاركة الفرص الأسبوعية:\n- ترشيحات جاهزة أسبوعيًا.\n- تحديثات مستمرة."
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("📌 سجّل الآن", url=REGISTER_WEEKLY)],
            [InlineKeyboardButton("⬅️ رجوع", callback_data=CB_PROGRAMS)],
        ])
        await q.edit_message_text(text, reply_markup=kb)

    # 🎉 عروض اليوم الوطني
    elif q.data == CB_NATIONAL_OFFER:
        text = (
            "🎉 عروض اليوم الوطني 🇸🇦\n\n"
            "- العرض ساري حتى نهاية الأسبوع ✅"
        )
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("📌 سجّل الآن", url=NATIONAL_REGISTER)],
            [InlineKeyboardButton("⬅️ رجوع", callback_data=CB_BACK_MAIN)],
        ])
        await q.edit_message_text(text, reply_markup=kb)

    # 📌 روابط مهمة
    elif q.data == CB_IMPORTANT_LINKS:
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("📌 شرح الكوفر كول", url=LINK_COVER_CALL)],
            [InlineKeyboardButton("👻 سناب شات", url=LINK_SNAP)],
            [InlineKeyboardButton("▶️ يوتيوب", url=LINK_YOUTUBE)],
            [InlineKeyboardButton("❓ الأسئلة الشائعة", url=LINK_FAQ)],
            [InlineKeyboardButton("💹 تجربة الاستراتيجية 7%", url=LINK_7PCT_DEMO)],
            [InlineKeyboardButton("⬅️ رجوع", callback_data=CB_BACK_MAIN)],
        ])
        await q.edit_message_text("📚 روابط مهمة 👇", reply_markup=kb)

    # 👥 الانضمام إلى قروب مجاني
    elif q.data == CB_GROUP:
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("📌 انضم الآن", url=FREE_GROUP_LINK)],
            [InlineKeyboardButton("⬅️ رجوع", callback_data=CB_BACK_MAIN)],
        ])
        await q.edit_message_text("👥 انضم إلى القروب المجاني:", reply_markup=kb)

    # 🤖 الدعم الفني
    elif q.data == CB_SUPPORT:
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("📞 تواصل مع الدعم", url=SUPPORT_LINK)],
            [InlineKeyboardButton("⬅️ رجوع", callback_data=CB_BACK_MAIN)],
        ])
        await q.edit_message_text("🤖 للتواصل مع الدعم الفني:", reply_markup=kb)

    # رجوع للقائمة الرئيسية
    elif q.data == CB_BACK_MAIN:
        await start(update, context)

# ─────────────── ▶️ التشغيل ───────────────
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(on_button))
    print("✅ البوت شغال...")
    app.run_polling()

if __name__ == "__main__":
    main()
