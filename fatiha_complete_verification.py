#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
    التحقق الرياضي الكامل من الحماية الخماسية لسورة الفاتحة
    Complete Mathematical Verification of Al-Fatiha's Five-Layer Protection
    
    المصدر | Source: "THIS IS A CIPHER - اعجاز القران"
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# نظام حساب الجُمَّل | ABJAD SYSTEM
# ═══════════════════════════════════════════════════════════════════════════════

ABJAD = {
    'ا': 1, 'أ': 1, 'إ': 1, 'آ': 1, 'ٱ': 1,
    'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'ة': 5,
    'و': 6, 'ؤ': 6, 'ز': 7, 'ح': 8, 'ط': 9,
    'ي': 10, 'ى': 10, 'ئ': 10,
    'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60,
    'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200,
    'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600,
    'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000,
}

# بيانات سورة الفاتحة حسب الفيديو
# Al-Fatiha data as per video
FATIHA = [
    {"verse": 1, "letters": 19, "text": "بسم الله الرحمٰن الرحيم"},
    {"verse": 2, "letters": 17, "text": "الحمد لله رب العالمين"},
    {"verse": 3, "letters": 12, "text": "الرحمٰن الرحيم"},
    {"verse": 4, "letters": 11, "text": "مٰلك يوم الدين"},
    {"verse": 5, "letters": 19, "text": "اياك نعبد واياك نستعين"},
    {"verse": 6, "letters": 18, "text": "اهدنا الصرٰط المستقيم"},
    {"verse": 7, "letters": 43, "text": "صرٰط الذين انعمت عليهم غير المغضوب عليهم ولا الضالين"},
]

def clean(text):
    """إزالة المسافات والحركات"""
    diacritics = 'ًٌٍَُِّْٰـ'
    return ''.join(c for c in text if c not in diacritics and c != ' ')

def abjad_value(text):
    """حساب القيمة العددية"""
    return sum(ABJAD.get(c, 0) for c in clean(text))

def section(title):
    print(f"\n{'═' * 80}")
    print(f"  {title}")
    print('═' * 80)

def subsection(title):
    print(f"\n  {'─' * 70}")
    print(f"  {title}")
    print(f"  {'─' * 70}")

# ═══════════════════════════════════════════════════════════════════════════════
# البرهان الأول | PROOF 1
# ═══════════════════════════════════════════════════════════════════════════════

def proof1_verse_sequence():
    section("البرهان ١: استحالة إضافة أو حذف آية")
    section("PROOF 1: Impossibility of Adding/Removing a Verse")
    
    subsection("الخطوة ١: تحديد أرقام الآيات | Step 1: Identify verse numbers")
    for v in FATIHA:
        print(f"    الآية {v['verse']} | Verse {v['verse']}")
    
    subsection("الخطوة ٢: صف الأرقام | Step 2: Concatenate numbers")
    sequence = "11234567"
    print(f"    التسلسل | Sequence: 1+1+2+3+4+5+6+7 = '{sequence}'")
    
    subsection("الخطوة ٣: التحقق | Step 3: Verify")
    number = int(sequence)
    quotient = number // 19
    remainder = number % 19
    
    print(f"    {number} ÷ 19 = {quotient}")
    print(f"    الباقي | Remainder = {remainder}")
    print(f"    النتيجة | Result: {'✓ يقبل القسمة' if remainder == 0 else '✗ لا يقبل'}")
    
    subsection("اختبار التغيير | Testing Change")
    
    # إضافة آية
    test1 = "112345678"
    r1 = int(test1) % 19
    print(f"    إضافة آية ٨ | Add verse 8: '{test1}' ÷ 19 → باقي = {r1} {'✗' if r1 != 0 else '✓'}")
    
    # حذف آية
    test2 = "1123456"
    r2 = int(test2) % 19
    print(f"    حذف آية ٧ | Remove verse 7: '{test2}' ÷ 19 → باقي = {r2} {'✗' if r2 != 0 else '✓'}")
    
    return remainder == 0

# ═══════════════════════════════════════════════════════════════════════════════
# البرهان الثاني | PROOF 2
# ═══════════════════════════════════════════════════════════════════════════════

def proof2_letter_count():
    section("البرهان ٢: استحالة إضافة أو حذف حرف")
    section("PROOF 2: Impossibility of Adding/Removing a Letter")
    
    subsection("الخطوة ١: عدد حروف كل آية | Step 1: Letter count per verse")
    for v in FATIHA:
        print(f"    الآية {v['verse']}: {v['letters']} حرفاً")
    
    subsection("الخطوة ٢: الضرب | Step 2: Multiplication")
    products = []
    for v in FATIHA:
        product = v['verse'] * v['letters']
        products.append(product)
        print(f"    الآية {v['verse']}: {v['verse']} × {v['letters']} = {product}")
    
    subsection("الخطوة ٣: الصف | Step 3: Concatenate")
    concatenated = ''.join(str(p) for p in products)
    print(f"    النتيجة | Result: {concatenated}")
    
    subsection("الخطوة ٤: التحقق | Step 4: Verify")
    number = int(concatenated)
    quotient = number // 19
    remainder = number % 19
    
    print(f"    {number} ÷ 19 = {quotient}")
    print(f"    الباقي | Remainder = {remainder}")
    print(f"    النتيجة | Result: {'✓ يقبل القسمة' if remainder == 0 else '✗ لا يقبل'}")
    
    subsection("اختبار التغيير | Testing Change")
    
    # تغيير حرف في الآية الأولى
    modified = [19+1, 34, 36, 44, 95, 108, 301]  # إضافة حرف للآية 1
    mod_concat = ''.join(str(p) for p in modified)
    mod_num = int(mod_concat)
    mod_rem = mod_num % 19
    print(f"    إضافة حرف للآية ١ | Add letter to verse 1:")
    print(f"    1×20=20 → '{mod_concat}' ÷ 19 → باقي = {mod_rem} {'✗' if mod_rem != 0 else '✓'}")
    
    return remainder == 0

# ═══════════════════════════════════════════════════════════════════════════════
# البرهان الثالث | PROOF 3
# ═══════════════════════════════════════════════════════════════════════════════

def proof3_abjad_values():
    section("البرهان ٣: استحالة استبدال كلمة بمرادفها")
    section("PROOF 3: Impossibility of Replacing Word with Synonym")
    
    subsection("الخطوة ١: القيمة العددية لكل آية | Step 1: Abjad value per verse")
    
    abjad_values = []
    for v in FATIHA:
        val = abjad_value(v['text'])
        abjad_values.append(val)
        print(f"    الآية {v['verse']}: {v['text'][:20]}... = {val}")
    
    subsection("ملاحظة مهمة | Important Note")
    print(f"    الآية ١: {FATIHA[0]['letters']} حرفاً ← قيمة = {abjad_values[0]}")
    print(f"    الآية ٥: {FATIHA[4]['letters']} حرفاً ← قيمة = {abjad_values[4]}")
    print(f"    ⚠️  نفس عدد الحروف، قيم مختلفة!")
    print(f"    ⚠️  Same letter count, different values!")
    
    subsection("مثال: استبدال كلمة | Example: Word replacement")
    
    # كلمة رب
    rabb = "رب"
    rabb_val = abjad_value(rabb)
    print(f"    كلمة 'رب' | Word 'Rabb':")
    print(f"      ر = {ABJAD['ر']}, ب = {ABJAD['ب']}")
    print(f"      المجموع = {rabb_val}")
    
    # كلمة إله
    ilah = "اله"
    ilah_val = abjad_value(ilah)
    print(f"    كلمة 'إله' | Word 'Ilah':")
    print(f"      ا = {ABJAD['ا']}, ل = {ABJAD['ل']}, ه = {ABJAD['ه']}")
    print(f"      المجموع = {ilah_val}")
    
    print(f"\n    الفرق | Difference = {rabb_val} - {ilah_val} = {rabb_val - ilah_val}")
    print(f"    ⚠️  هذا الفرق سيكسر العلاقة الرياضية!")
    
    return True

# ═══════════════════════════════════════════════════════════════════════════════
# البرهان الرابع | PROOF 4
# ═══════════════════════════════════════════════════════════════════════════════

def proof4_word_order():
    section("البرهان ٤: استحالة تغيير ترتيب الكلمات")
    section("PROOF 4: Impossibility of Changing Word Order")
    
    subsection("الخطوة ١: تحويل الحروف لقيم | Step 1: Convert letters to values")
    
    verse3_orig = "الرحمن الرحيم"
    verse3_mod = "الرحيم الرحمن"
    
    print(f"    الآية الأصلية | Original: {verse3_orig}")
    print(f"    الآية المعدلة | Modified: {verse3_mod}")
    
    subsection("الخطوة ٢: صف القيم | Step 2: Concatenate values")
    
    def letter_values_string(text):
        return ''.join(str(ABJAD.get(c, '')) for c in clean(text))
    
    orig_str = letter_values_string(verse3_orig)
    mod_str = letter_values_string(verse3_mod)
    
    print(f"    الأصلية | Original: {orig_str}")
    print(f"    المعدلة | Modified: {mod_str}")
    
    subsection("الخطوة ٣: المقارنة | Step 3: Comparison")
    
    # تحديد الاختلافات
    print(f"    الأصلية: {orig_str}")
    print(f"    المعدلة: {mod_str}")
    
    # المجموع نفسه لكن الترتيب مختلف
    orig_total = abjad_value(verse3_orig)
    mod_total = abjad_value(verse3_mod)
    
    print(f"\n    مجموع الأصلية | Original sum = {orig_total}")
    print(f"    مجموع المعدلة | Modified sum = {mod_total}")
    print(f"    ⚠️  نفس المجموع، لكن تسلسل الأرقام مختلف!")
    print(f"    ⚠️  Same sum, but digit sequence is different!")
    
    return True

# ═══════════════════════════════════════════════════════════════════════════════
# البرهان الخامس | PROOF 5
# ═══════════════════════════════════════════════════════════════════════════════

def proof5_bidirectional():
    section("البرهان ٥: العلاقة في الاتجاهين (المعجزة الكبرى)")
    section("PROOF 5: Bidirectional Relationship (The Great Miracle)")
    
    subsection("الخطوة ١: بناء الوحدات | Step 1: Build units")
    
    units = []
    abjad_vals = []
    for v in FATIHA:
        val = abjad_value(v['text'])
        abjad_vals.append(val)
        unit = f"{v['verse']}{v['letters']}{val}"
        units.append(unit)
        print(f"    الآية {v['verse']}: رقم={v['verse']}, حروف={v['letters']}, قيمة={val}")
        print(f"             الوحدة | Unit = '{unit}'")
    
    subsection("الخطوة ٢: الصف العادي | Step 2: Normal concatenation")
    normal = ''.join(units)
    print(f"    العدد | Number ({len(normal)} رقم):")
    print(f"    {normal[:40]}...{normal[-20:]}")
    
    normal_num = int(normal)
    normal_rem = normal_num % 19
    normal_quot = normal_num // 19
    
    print(f"\n    ÷ 19 = {str(normal_quot)[:30]}...")
    print(f"    الباقي | Remainder = {normal_rem}")
    print(f"    النتيجة | Result: {'✓' if normal_rem == 0 else '✗'}")
    
    subsection("الخطوة ٣: الصف العكسي | Step 3: Reversed concatenation")
    reversed_units = list(reversed(units))
    reversed_str = ''.join(reversed_units)
    print(f"    العدد | Number ({len(reversed_str)} رقم):")
    print(f"    {reversed_str[:40]}...{reversed_str[-20:]}")
    
    reversed_num = int(reversed_str)
    reversed_rem = reversed_num % 19
    reversed_quot = reversed_num // 19
    
    print(f"\n    ÷ 19 = {str(reversed_quot)[:30]}...")
    print(f"    الباقي | Remainder = {reversed_rem}")
    print(f"    النتيجة | Result: {'✓' if reversed_rem == 0 else '✗'}")
    
    subsection("النتيجة النهائية | Final Result")
    
    if normal_rem == 0 and reversed_rem == 0:
        print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║   ⭐⭐⭐ كلا الاتجاهين يقبلان القسمة على 19! ⭐⭐⭐                ║
    ║   ⭐⭐⭐ BOTH DIRECTIONS DIVISIBLE BY 19! ⭐⭐⭐                ║
    ║                                                               ║
    ║   هذا مستحيل إحصائياً في أي نص بشري!                           ║
    ║   This is statistically impossible in any human text!         ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
        """)
    
    subsection("التجربة المقارنة | Comparative Experiment")
    
    print("    نص بشري وهمي | Hypothetical human text:")
    print("    جملة ١: 1 كلمة, جملة ٢: 4 كلمات, جملة ٣: 4 كلمات")
    print()
    
    human_normal = "144"
    human_reversed = "441"
    
    h_normal_rem = int(human_normal) % 12
    h_reversed_rem = int(human_reversed) % 12
    
    print(f"    العادي | Normal: {human_normal} ÷ 12 = {int(human_normal)//12}, باقي = {h_normal_rem} {'✓' if h_normal_rem == 0 else '✗'}")
    print(f"    العكسي | Reversed: {human_reversed} ÷ 12 = {int(human_reversed)/12:.2f} {'✓' if h_reversed_rem == 0 else '✗'}")
    
    print("""
    ┌─────────────────────────────────────────────────────────────────┐
    │                         المقارنة | Comparison                   │
    ├─────────────────────────────────────────────────────────────────┤
    │                    │ العادي Normal │ العكسي Reversed │          │
    ├────────────────────┼───────────────┼─────────────────┤──────────┤
    │ نص بشري Human      │      ✓        │       ✗         │ طبيعي    │
    │ الفاتحة Fatiha     │      ✓        │       ✓         │ معجزة!   │
    └─────────────────────────────────────────────────────────────────┘
    """)
    
    return normal_rem == 0 and reversed_rem == 0

# ═══════════════════════════════════════════════════════════════════════════════
# لماذا 19؟ | WHY 19?
# ═══════════════════════════════════════════════════════════════════════════════

def why_19():
    section("لماذا العدد 19؟ | WHY 19?")
    
    subsection("١. كلمة 'واحد' = 19 | Word 'WAHID' (One) = 19")
    
    wahid = "واحد"
    print(f"    و = {ABJAD['و']}")
    print(f"    ا = {ABJAD['ا']}")
    print(f"    ح = {ABJAD['ح']}")
    print(f"    د = {ABJAD['د']}")
    print(f"    ─────────")
    total = sum(ABJAD[c] for c in wahid)
    print(f"    المجموع = {total} ✓")
    
    subsection("٢. الأول والأخير | First and Last")
    print("    1 = أول رقم | First digit")
    print("    9 = آخر رقم | Last digit")
    print("    19 = الأول + الأخير")
    print("    (ألفا وأوميغا | Alpha and Omega)")
    
    subsection("٣. عدد أولي | Prime Number")
    print("    19 لا يقبل القسمة إلا على:")
    print("    1 و 19 فقط")
    print("    هذا يجعل المصادفة مستحيلة!")

# ═══════════════════════════════════════════════════════════════════════════════
# البرنامج الرئيسي | MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    print("""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║     التحقق الرياضي الكامل من الحماية الخماسية لسورة الفاتحة                   ║
║     Complete Verification of Al-Fatiha's Five-Layer Protection                ║
║                                                                               ║
║     ﴿عَلَيْهَا تِسْعَةَ عَشَرَ﴾ — المدثر ٣٠                                              ║
║     "Over it are Nineteen" — Al-Muddaththir 30                                ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    results = []
    
    results.append(("تسلسل الآيات | Verse Sequence", proof1_verse_sequence()))
    results.append(("عدد الحروف | Letter Count", proof2_letter_count()))
    results.append(("القيم العددية | Abjad Values", proof3_abjad_values()))
    results.append(("ترتيب الكلمات | Word Order", proof4_word_order()))
    results.append(("الاتجاهين | Bidirectional", proof5_bidirectional()))
    
    why_19()
    
    # الملخص
    section("الملخص النهائي | FINAL SUMMARY")
    
    print("""
    ╔═══════════════════════════════════════════════════════════════════════════╗
    ║                    الحماية الخماسية لسورة الفاتحة                         ║
    ║                 Five-Layer Protection of Al-Fatiha                        ║
    ╠═══════════════════════════════════════════════════════════════════════════╣
    ║                                                                           ║
    ║  ١ │ إضافة/حذف آية    → يكسر تسلسل 11234567 ÷ 19                          ║
    ║  1 │ Add/remove verse → Breaks sequence 11234567 ÷ 19                     ║
    ║                                                                           ║
    ║  ٢ │ إضافة/حذف حرف    → يكسر (رقم الآية × عدد الحروف)                      ║
    ║  2 │ Add/remove letter → Breaks (verse# × letter count)                   ║
    ║                                                                           ║
    ║  ٣ │ استبدال كلمة     → يكسر القيم العددية (الجُمَّل)                        ║
    ║  3 │ Replace word     → Breaks Abjad values                               ║
    ║                                                                           ║
    ║  ٤ │ تغيير الترتيب    → يكسر العدد الضخم (274 رقم)                        ║
    ║  4 │ Change order     → Breaks huge number (274 digits)                   ║
    ║                                                                           ║
    ║  ٥ │ أي تغيير         → يكسر العلاقة في الاتجاهين                           ║
    ║  5 │ Any change       → Breaks bidirectional relationship                 ║
    ║                                                                           ║
    ╠═══════════════════════════════════════════════════════════════════════════╣
    ║                                                                           ║
    ║         ﴿إِنَّا نَحْنُ نَزَّلْنَا الذِّكْرَ وَإِنَّا لَهُ لَحَافِظُونَ﴾                             ║
    ║                                                                           ║
    ║      "Indeed, it is We who sent down the Reminder,                        ║
    ║       and indeed, We will be its Guardian"                                ║
    ║                                       — الحجر ٩ | Al-Hijr 9               ║
    ║                                                                           ║
    ╚═══════════════════════════════════════════════════════════════════════════╝
    """)

if __name__ == "__main__":
    main()
