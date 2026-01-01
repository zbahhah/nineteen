#!/usr/bin/env python3
"""
التحليل العلمي الصارم: هل العدد 19 مميز في تقريبات الثوابت الرياضية؟

المنهجية:
1. حساب الكسور المستمرة (Continued Fractions) للثوابت
2. إيجاد أفضل التقريبات الكسرية (Best Rational Approximations)
3. مقارنة إحصائية مع أعداد أولية أخرى
4. اختبار الفرضية الصفرية: هل 19 عشوائي أم مميز؟

الثوابت المدروسة:
- e (عدد أويلر)
- π (باي)  
- δ (ثابت فيغنباوم الأول)
- α (ثابت فيغنباوم الثاني)
- φ (النسبة الذهبية)
"""

import math
from fractions import Fraction
from typing import List, Tuple, Dict
from dataclasses import dataclass

# ═══════════════════════════════════════════════════════════════
# الثوابت الرياضية
# ═══════════════════════════════════════════════════════════════

CONSTANTS = {
    'e': 2.718281828459045,
    'π': 3.141592653589793,
    'δ (Feigenbaum 1)': 4.669201609102990,
    'α (Feigenbaum 2)': 2.502907875095893,
    'φ (Golden Ratio)': 1.618033988749895,
    'ln(2)': 0.693147180559945,
    'sqrt(2)': 1.414213562373095,
    'sqrt(π)': 1.772453850905516,
}

# الأعداد الأولية للمقارنة
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# ═══════════════════════════════════════════════════════════════
# الجزء 1: الكسور المستمرة
# ═══════════════════════════════════════════════════════════════

def continued_fraction(x: float, max_terms: int = 20) -> List[int]:
    """حساب الكسر المستمر لعدد حقيقي"""
    cf = []
    for _ in range(max_terms):
        a = int(x)
        cf.append(a)
        frac = x - a
        if frac < 1e-10:
            break
        x = 1.0 / frac
    return cf

def convergents_from_cf(cf: List[int]) -> List[Tuple[int, int]]:
    """حساب المتقاربات من الكسر المستمر"""
    convergents = []
    h_prev, h_curr = 0, 1
    k_prev, k_curr = 1, 0
    
    for a in cf:
        h_new = a * h_curr + h_prev
        k_new = a * k_curr + k_prev
        convergents.append((h_new, k_new))
        h_prev, h_curr = h_curr, h_new
        k_prev, k_curr = k_curr, k_new
    
    return convergents

def analyze_continued_fraction(name: str, value: float):
    """تحليل الكسر المستمر لثابت معين"""
    print(f"\n{'='*60}")
    print(f"الكسر المستمر لـ {name} = {value}")
    print('='*60)
    
    cf = continued_fraction(value, 15)
    print(f"CF: [{cf[0]}; {', '.join(map(str, cf[1:]))}]")
    
    convergents = convergents_from_cf(cf)
    
    print(f"\nالمتقاربات (Convergents):")
    print(f"{'n':>3} | {'p/q':>15} | {'القيمة':>12} | {'الخطأ':>12} | {'المقام أولي؟':>12}")
    print("-" * 65)
    
    for i, (p, q) in enumerate(convergents[:10]):
        approx = p / q
        error = abs(value - approx)
        is_prime = is_prime_number(q)
        prime_mark = "✓ أولي" if is_prime else ""
        print(f"{i:>3} | {p:>7}/{q:<7} | {approx:>12.8f} | {error:>12.2e} | {prime_mark}")
    
    return cf, convergents

# ═══════════════════════════════════════════════════════════════
# الجزء 2: أفضل التقريبات تحت قيد المقام
# ═══════════════════════════════════════════════════════════════

def is_prime_number(n: int) -> bool:
    """اختبار أولية العدد"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def best_rational_approximation(x: float, max_denom: int) -> Tuple[int, int, float]:
    """إيجاد أفضل تقريب كسري تحت قيد المقام"""
    best_p, best_q = 0, 1
    best_error = abs(x)
    
    for q in range(1, max_denom + 1):
        p = round(x * q)
        error = abs(x - p/q)
        if error < best_error:
            best_error = error
            best_p, best_q = p, q
    
    return best_p, best_q, best_error

def best_approximation_with_prime_denom(x: float, max_denom: int) -> Dict:
    """إيجاد أفضل تقريب بمقام أولي"""
    results = {}
    
    for p in PRIMES:
        if p > max_denom:
            break
        numerator = round(x * p)
        error = abs(x - numerator/p)
        relative_error = error / x * 100
        results[p] = {
            'numerator': numerator,
            'fraction': f"{numerator}/{p}",
            'value': numerator/p,
            'error': error,
            'relative_error': relative_error
        }
    
    return results

def compare_prime_denominators(name: str, value: float, max_denom: int = 50):
    """مقارنة أداء المقامات الأولية المختلفة"""
    print(f"\n{'='*70}")
    print(f"مقارنة المقامات الأولية لـ {name} = {value}")
    print(f"(المقام الأقصى: {max_denom})")
    print('='*70)
    
    results = best_approximation_with_prime_denom(value, max_denom)
    
    # ترتيب حسب الخطأ النسبي
    sorted_primes = sorted(results.items(), key=lambda x: x[1]['relative_error'])
    
    print(f"\n{'المقام':>8} | {'الكسر':>12} | {'القيمة':>10} | {'الخطأ المطلق':>14} | {'الخطأ %':>10} | {'الترتيب':>8}")
    print("-" * 80)
    
    rank_of_19 = None
    for rank, (prime, data) in enumerate(sorted_primes, 1):
        marker = " ◄◄◄" if prime == 19 else ""
        print(f"{prime:>8} | {data['fraction']:>12} | {data['value']:>10.6f} | {data['error']:>14.2e} | {data['relative_error']:>9.4f}% | {rank:>8}{marker}")
        if prime == 19:
            rank_of_19 = rank
    
    return sorted_primes, rank_of_19

# ═══════════════════════════════════════════════════════════════
# الجزء 3: التحليل الإحصائي الشامل
# ═══════════════════════════════════════════════════════════════

@dataclass
class StatisticalResult:
    constant_name: str
    rank_of_19: int
    total_primes: int
    best_prime: int
    is_19_best: bool
    is_19_top3: bool
    percentile: float

def comprehensive_statistical_analysis(max_denom: int = 50) -> List[StatisticalResult]:
    """تحليل إحصائي شامل لجميع الثوابت"""
    print("\n" + "═"*80)
    print("التحليل الإحصائي الشامل: هل 19 مميز؟")
    print("═"*80)
    
    results = []
    primes_in_range = [p for p in PRIMES if p <= max_denom]
    total_primes = len(primes_in_range)
    
    for name, value in CONSTANTS.items():
        sorted_primes, rank_of_19 = compare_prime_denominators(name, value, max_denom)
        
        best_prime = sorted_primes[0][0]
        is_19_best = (best_prime == 19)
        is_19_top3 = rank_of_19 is not None and rank_of_19 <= 3
        percentile = (rank_of_19 / total_primes * 100) if rank_of_19 else None
        
        results.append(StatisticalResult(
            constant_name=name,
            rank_of_19=rank_of_19 if rank_of_19 else -1,
            total_primes=total_primes,
            best_prime=best_prime,
            is_19_best=is_19_best,
            is_19_top3=is_19_top3,
            percentile=percentile if percentile else 100
        ))
    
    return results

def print_summary(results: List[StatisticalResult]):
    """طباعة ملخص التحليل"""
    print("\n" + "═"*80)
    print("الملخص النهائي: أداء العدد 19 كمقام")
    print("═"*80)
    
    print(f"\n{'الثابت':<20} | {'ترتيب 19':>10} | {'أفضل مقام':>10} | {'19 الأفضل؟':>12} | {'19 ضمن أفضل 3؟':>15}")
    print("-" * 80)
    
    count_best = 0
    count_top3 = 0
    
    for r in results:
        is_best = "✓ نعم" if r.is_19_best else "✗ لا"
        is_top3 = "✓ نعم" if r.is_19_top3 else "✗ لا"
        print(f"{r.constant_name:<20} | {r.rank_of_19:>10} | {r.best_prime:>10} | {is_best:>12} | {is_top3:>15}")
        
        if r.is_19_best:
            count_best += 1
        if r.is_19_top3:
            count_top3 += 1
    
    print("\n" + "─"*80)
    print(f"عدد المرات التي كان فيها 19 الأفضل: {count_best}/{len(results)}")
    print(f"عدد المرات التي كان فيها 19 ضمن أفضل 3: {count_top3}/{len(results)}")
    
    # الحكم النهائي
    print("\n" + "═"*80)
    print("الحكم العلمي:")
    print("═"*80)
    
    expected_best = 1 / len([p for p in PRIMES if p <= 50])  # احتمال عشوائي
    expected_top3 = 3 / len([p for p in PRIMES if p <= 50])
    
    actual_best = count_best / len(results)
    actual_top3 = count_top3 / len(results)
    
    print(f"\nالاحتمال المتوقع (عشوائياً) أن يكون 19 الأفضل: {expected_best*100:.1f}%")
    print(f"النسبة الفعلية: {actual_best*100:.1f}%")
    print(f"النسبة: {actual_best/expected_best:.2f}x")
    
    print(f"\nالاحتمال المتوقع (عشوائياً) أن يكون 19 ضمن أفضل 3: {expected_top3*100:.1f}%")
    print(f"النسبة الفعلية: {actual_top3*100:.1f}%")
    print(f"النسبة: {actual_top3/expected_top3:.2f}x")
    
    if actual_best > expected_best * 2:
        print("\n⚠️  العدد 19 يظهر كأفضل مقام بنسبة أعلى من المتوقع عشوائياً!")
    elif actual_best < expected_best * 0.5:
        print("\n📊 العدد 19 لا يتفوق - أداؤه عادي أو أقل من المتوقع")
    else:
        print("\n📊 العدد 19 يؤدي ضمن النطاق العشوائي المتوقع")

# ═══════════════════════════════════════════════════════════════
# الجزء 4: تحليل خاص لـ e و δ
# ═══════════════════════════════════════════════════════════════

def special_analysis_e_and_delta():
    """تحليل خاص للعلاقة بين e و δ و 19"""
    print("\n" + "═"*80)
    print("تحليل خاص: العلاقة المزعومة e ≈ 19/7 و δ ≈ 89/19")
    print("═"*80)
    
    e = CONSTANTS['e']
    delta = CONSTANTS['δ (Feigenbaum 1)']
    
    # تحليل e ≈ 19/7
    print("\n1. تحليل e ≈ 19/7:")
    print("-" * 40)
    
    # أفضل تقريب بمقام 7
    best_with_7 = round(e * 7)
    error_7 = abs(e - best_with_7/7)
    print(f"   أفضل تقريب بمقام 7: {best_with_7}/7 = {best_with_7/7:.6f}")
    print(f"   الخطأ: {error_7:.6f} ({error_7/e*100:.4f}%)")
    
    # المنافسون
    competitors = [(15, 11), (19, 7), (87, 32), (106, 39), (193, 71)]
    print(f"\n   المنافسون:")
    for p, q in competitors:
        err = abs(e - p/q)
        print(f"   {p}/{q} = {p/q:.6f}, خطأ = {err:.6f} ({err/e*100:.4f}%)")
    
    # تحليل δ ≈ 89/19
    print("\n2. تحليل δ ≈ 89/19:")
    print("-" * 40)
    
    # أفضل تقريب بمقام 19
    best_with_19 = round(delta * 19)
    error_19 = abs(delta - best_with_19/19)
    print(f"   أفضل تقريب بمقام 19: {best_with_19}/19 = {best_with_19/19:.6f}")
    print(f"   الخطأ: {error_19:.6f} ({error_19/delta*100:.4f}%)")
    
    # هل 89/19 من المتقاربات؟
    cf_delta = continued_fraction(delta, 15)
    conv_delta = convergents_from_cf(cf_delta)
    
    print(f"\n   الكسر المستمر لـ δ: [{cf_delta[0]}; {', '.join(map(str, cf_delta[1:8]))}...]")
    print(f"\n   المتقاربات الأولى لـ δ:")
    for i, (p, q) in enumerate(conv_delta[:8]):
        err = abs(delta - p/q)
        marker = " ◄◄◄ (89/19)" if (p == 89 and q == 19) else ""
        print(f"   {p}/{q} = {p/q:.6f}, خطأ = {err:.2e}{marker}")
    
    # هل 89/19 متقارب؟
    is_convergent = any(p == 89 and q == 19 for p, q in conv_delta)
    print(f"\n   هل 89/19 من متقاربات δ؟ {'نعم ✓' if is_convergent else 'لا ✗'}")

# ═══════════════════════════════════════════════════════════════
# الجزء 5: مقارنة شاملة للأعداد الأولية
# ═══════════════════════════════════════════════════════════════

def prime_performance_ranking():
    """ترتيب الأعداد الأولية حسب أدائها الكلي"""
    print("\n" + "═"*80)
    print("ترتيب الأعداد الأولية حسب الأداء الكلي")
    print("═"*80)
    
    # حساب متوسط الترتيب لكل عدد أولي
    prime_scores = {p: [] for p in PRIMES if p <= 50}
    
    for name, value in CONSTANTS.items():
        results = best_approximation_with_prime_denom(value, 50)
        sorted_results = sorted(results.items(), key=lambda x: x[1]['relative_error'])
        
        for rank, (prime, _) in enumerate(sorted_results, 1):
            prime_scores[prime].append(rank)
    
    # حساب متوسط الترتيب
    avg_ranks = {}
    for prime, ranks in prime_scores.items():
        avg_ranks[prime] = sum(ranks) / len(ranks)
    
    # ترتيب حسب المتوسط
    sorted_primes = sorted(avg_ranks.items(), key=lambda x: x[1])
    
    print(f"\n{'العدد الأولي':>12} | {'متوسط الترتيب':>15} | {'الأفضل':>10}")
    print("-" * 50)
    
    for i, (prime, avg) in enumerate(sorted_primes, 1):
        marker = " ◄◄◄" if prime == 19 else ""
        best_mark = "🥇" if i == 1 else ("🥈" if i == 2 else ("🥉" if i == 3 else ""))
        print(f"{prime:>12} | {avg:>15.2f} | {best_mark:>10}{marker}")
    
    # موقع 19
    rank_of_19 = next(i for i, (p, _) in enumerate(sorted_primes, 1) if p == 19)
    print(f"\n→ ترتيب العدد 19 الكلي: {rank_of_19} من {len(sorted_primes)}")

# ═══════════════════════════════════════════════════════════════
# التنفيذ الرئيسي
# ═══════════════════════════════════════════════════════════════

def main():
    print("╔" + "═"*78 + "╗")
    print("║" + " التحليل العلمي الصارم: هل العدد 19 مميز في تقريبات الثوابت الرياضية؟ ".center(78) + "║")
    print("╚" + "═"*78 + "╝")
    
    # 1. تحليل الكسور المستمرة للثوابت الرئيسية
    print("\n" + "█"*80)
    print("الجزء الأول: تحليل الكسور المستمرة")
    print("█"*80)
    
    for name in ['e', 'π', 'δ (Feigenbaum 1)', 'α (Feigenbaum 2)']:
        analyze_continued_fraction(name, CONSTANTS[name])
    
    # 2. التحليل الإحصائي الشامل
    print("\n" + "█"*80)
    print("الجزء الثاني: مقارنة المقامات الأولية")
    print("█"*80)
    
    results = comprehensive_statistical_analysis(max_denom=50)
    print_summary(results)
    
    # 3. التحليل الخاص
    print("\n" + "█"*80)
    print("الجزء الثالث: التحليل الخاص لـ e و δ")
    print("█"*80)
    
    special_analysis_e_and_delta()
    
    # 4. الترتيب الكلي للأعداد الأولية
    print("\n" + "█"*80)
    print("الجزء الرابع: الترتيب الكلي للأعداد الأولية")
    print("█"*80)
    
    prime_performance_ranking()
    
    # الخلاصة النهائية
    print("\n" + "╔" + "═"*78 + "╗")
    print("║" + " الخلاصة النهائية ".center(78) + "║")
    print("╚" + "═"*78 + "╝")
    
    print("""
    هذا التحليل يجيب على السؤال: "هل 19 مميز إحصائياً؟"
    
    المنهجية المستخدمة:
    ────────────────────
    1. حساب الكسور المستمرة (الطريقة الرياضية الصحيحة لإيجاد أفضل التقريبات)
    2. مقارنة أداء 19 مع أعداد أولية أخرى (7, 11, 13, 17, 23, 29...)
    3. حساب النسب المئوية والترتيب
    4. مقارنة مع التوقع العشوائي
    
    النتيجة العلمية:
    ────────────────────
    - إذا كان 19 يتفوق بنسبة > 2x من المتوقع → قد يكون هناك نمط حقيقي
    - إذا كان أداؤه عادياً → النتائج السابقة كانت "cherry-picking"
    - الحكم النهائي يعتمد على البيانات أعلاه
    """)

if __name__ == "__main__":
    main()
