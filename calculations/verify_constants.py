#!/usr/bin/env python3
"""
Prime 19 Mathematical System - Verification Script
المنظومة الرياضية للعدد الأولي 19 - برنامج التحقق

This script verifies all mathematical relationships between
the prime number 19 and fundamental physical constants.

Author: Mathematical Research Conversation
License: MIT
"""

import math
from dataclasses import dataclass
from typing import Tuple

# =============================================================================
# CODATA 2022 Reference Values (Latest Official Values)
# القيم المرجعية من CODATA 2022
# =============================================================================

CONSTANTS = {
    'e': 2.718281828459045,           # Euler's number
    'pi': 3.141592653589793,          # Pi
    'alpha_inv': 137.035999177,       # 1/α (Fine structure constant inverse)
    'c': 299792458,                   # Speed of light (m/s)
    'e_charge': 1.602176634e-19,      # Electron charge (C)
    'm_e': 9.1093837139e-31,          # Electron mass (kg)
    'm_p': 1.67262192595e-27,         # Proton mass (kg)
    'h': 6.62607015e-34,              # Planck constant (J·s)
    'hbar': 1.054571817e-34,          # Reduced Planck constant (J·s)
    'G': 6.67430e-11,                 # Gravitational constant (m³·kg⁻¹·s⁻²)
    'k_B': 1.380649e-23,              # Boltzmann constant (J/K)
    'E_hoyle': 7.6549,                # Hoyle resonance energy (MeV)
    'mass_ratio': 1836.152673426,     # Proton to electron mass ratio
}

# =============================================================================
# Prime 19 System Definitions
# تعريفات منظومة العدد 19
# =============================================================================

p = 19  # The prime number
e_p = p / 7  # e_p = 19/7

# =============================================================================
# Calculation Functions
# دوال الحساب
# =============================================================================

@dataclass
class CalculationResult:
    """Result of a calculation with error analysis"""
    name: str
    name_ar: str
    formula: str
    calculated: float
    actual: float
    error_percent: float
    unit: str = ""

def calculate_error(calculated: float, actual: float) -> float:
    """Calculate percentage error"""
    return abs((calculated - actual) / actual) * 100

def verify_euler_number() -> CalculationResult:
    """Verify e = e_p / ln(e_p)"""
    calculated = e_p / math.log(e_p)
    actual = CONSTANTS['e']
    return CalculationResult(
        name="Euler's Number",
        name_ar="العدد النيبري",
        formula="e = e_p / ln(e_p) = 19 / (7 × ln(19/7))",
        calculated=calculated,
        actual=actual,
        error_percent=calculate_error(calculated, actual)
    )

def verify_pi() -> CalculationResult:
    """Verify π = e_p + 3/7 = 22/7"""
    calculated = e_p + 3/7  # = 22/7
    actual = CONSTANTS['pi']
    return CalculationResult(
        name="Pi",
        name_ar="النسبة الدائرية",
        formula="π = e_p + 3/7 = (19+3)/7 = 22/7",
        calculated=calculated,
        actual=actual,
        error_percent=calculate_error(calculated, actual)
    )

def verify_fine_structure_simple() -> CalculationResult:
    """Verify 1/α = 7p + 4 = 137 (simple approximation)"""
    calculated = 7 * p + 4
    actual = CONSTANTS['alpha_inv']
    return CalculationResult(
        name="Fine Structure (Simple)",
        name_ar="ثابت البنية الدقيقة (بسيط)",
        formula="1/α = 7p + 4 = 7×19 + 4 = 137",
        calculated=calculated,
        actual=actual,
        error_percent=calculate_error(calculated, actual)
    )

def verify_fine_structure_precise() -> CalculationResult:
    """Verify 1/α = 7p + 4 + 7/(10p) (precise approximation)"""
    calculated = 7 * p + 4 + 7 / (10 * p)
    actual = CONSTANTS['alpha_inv']
    return CalculationResult(
        name="Fine Structure (Precise)",
        name_ar="ثابت البنية الدقيقة (دقيق)",
        formula="1/α = 7p + 4 + 7/(10p) = 137 + 7/190",
        calculated=calculated,
        actual=actual,
        error_percent=calculate_error(calculated, actual)
    )

def verify_electron_charge() -> CalculationResult:
    """Verify e_q = (√e_p - 1/(7π)) × 10^(-p)"""
    pi_approx = 22/7
    calculated = (math.sqrt(e_p) - 1/(7 * pi_approx)) * 10**(-p)
    actual = CONSTANTS['e_charge']
    return CalculationResult(
        name="Electron Charge",
        name_ar="شحنة الإلكترون",
        formula="e_q = (√e_p - 1/(7π)) × 10^(-19)",
        calculated=calculated,
        actual=actual,
        error_percent=calculate_error(calculated, actual),
        unit="C"
    )

def verify_speed_of_light_simple() -> CalculationResult:
    """Verify c = e^(p + 0.5) (simple approximation)"""
    e_val = CONSTANTS['e']
    calculated = e_val ** (p + 0.5)
    actual = CONSTANTS['c']
    return CalculationResult(
        name="Speed of Light (Simple)",
        name_ar="سرعة الضوء (بسيط)",
        formula="c = e^(19.5)",
        calculated=calculated,
        actual=actual,
        error_percent=calculate_error(calculated, actual),
        unit="m/s"
    )

def verify_speed_of_light_precise() -> CalculationResult:
    """Verify c = e^(p + 0.5) × (7π + sin(e_p))/(7π) (precise)"""
    e_val = CONSTANTS['e']
    pi_approx = 22/7
    correction = (7 * pi_approx + math.sin(e_p)) / (7 * pi_approx)
    calculated = e_val ** (p + 0.5) * correction
    actual = CONSTANTS['c']
    return CalculationResult(
        name="Speed of Light (Precise)",
        name_ar="سرعة الضوء (دقيق)",
        formula="c = e^(19.5) × (7π + sin(e_p))/(7π)",
        calculated=calculated,
        actual=actual,
        error_percent=calculate_error(calculated, actual),
        unit="m/s"
    )

def verify_electron_mass() -> CalculationResult:
    """Verify m_e = (p×7×5)/(4p-3) × 10^(-(2p-7))"""
    numerator = p * 7 * 5  # = 665
    denominator = 4 * p - 3  # = 73
    exponent = -(2 * p - 7)  # = -31
    calculated = (numerator / denominator) * 10**(exponent)
    actual = CONSTANTS['m_e']
    return CalculationResult(
        name="Electron Mass",
        name_ar="كتلة الإلكترون",
        formula="m_e = (19×7×5)/(4×19-3) × 10^(-31) = 665/73 × 10^(-31)",
        calculated=calculated,
        actual=actual,
        error_percent=calculate_error(calculated, actual),
        unit="kg"
    )

def verify_proton_mass() -> CalculationResult:
    """Verify m_p = p²/6³ × 10^(-(p+8))"""
    numerator = p ** 2  # = 361
    denominator = 6 ** 3  # = 216
    exponent = -(p + 8)  # = -27
    calculated = (numerator / denominator) * 10**(exponent)
    actual = CONSTANTS['m_p']
    return CalculationResult(
        name="Proton Mass",
        name_ar="كتلة البروتون",
        formula="m_p = 19²/6³ × 10^(-27) = 361/216 × 10^(-27)",
        calculated=calculated,
        actual=actual,
        error_percent=calculate_error(calculated, actual),
        unit="kg"
    )

def verify_mass_ratio() -> CalculationResult:
    """Verify m_p/m_e = 2×7²×p - (p+7)"""
    calculated = 2 * (7**2) * p - (p + 7)
    actual = CONSTANTS['mass_ratio']
    return CalculationResult(
        name="Mass Ratio (m_p/m_e)",
        name_ar="نسبة الكتل",
        formula="m_p/m_e = 2×7²×19 - (19+7) = 1862 - 26 = 1836",
        calculated=calculated,
        actual=actual,
        error_percent=calculate_error(calculated, actual)
    )

def verify_planck_constant() -> CalculationResult:
    """Verify h = 44×p²/7⁴ × 10^(-(p+15))"""
    numerator = 44 * (p ** 2)  # = 44 × 361 = 15884
    denominator = 7 ** 4  # = 2401
    exponent = -(p + 15)  # = -34
    calculated = (numerator / denominator) * 10**(exponent)
    actual = CONSTANTS['h']
    return CalculationResult(
        name="Planck Constant",
        name_ar="ثابت بلانك",
        formula="h = 44×19²/7⁴ × 10^(-34)",
        calculated=calculated,
        actual=actual,
        error_percent=calculate_error(calculated, actual),
        unit="J·s"
    )

def verify_reduced_planck() -> CalculationResult:
    """Verify ℏ = p²/7³ × 10^(-(p+15))"""
    numerator = p ** 2  # = 361
    denominator = 7 ** 3  # = 343
    exponent = -(p + 15)  # = -34
    calculated = (numerator / denominator) * 10**(exponent)
    actual = CONSTANTS['hbar']
    return CalculationResult(
        name="Reduced Planck Constant",
        name_ar="ثابت بلانك المخفض",
        formula="ℏ = 19²/7³ × 10^(-34) = 361/343 × 10^(-34)",
        calculated=calculated,
        actual=actual,
        error_percent=calculate_error(calculated, actual),
        unit="J·s"
    )

def verify_gravitational_constant() -> CalculationResult:
    """Verify G = 4p·e_p/(2p-7) × 10^(-(p-8))"""
    numerator = 4 * p * e_p  # = 4 × 19 × (19/7) = 76 × 19/7
    denominator = 2 * p - 7  # = 31
    exponent = -(p - 8)  # = -11
    calculated = (numerator / denominator) * 10**(exponent)
    actual = CONSTANTS['G']
    return CalculationResult(
        name="Gravitational Constant",
        name_ar="ثابت الجاذبية",
        formula="G = 4×19×e_p/(2×19-7) × 10^(-11) = 76×e_p/31 × 10^(-11)",
        calculated=calculated,
        actual=actual,
        error_percent=calculate_error(calculated, actual),
        unit="m³·kg⁻¹·s⁻²"
    )

def verify_boltzmann_constant() -> CalculationResult:
    """Verify k_B = √(p/10) × 10^(-(p+4))"""
    calculated = math.sqrt(p / 10) * 10**(-(p + 4))
    actual = CONSTANTS['k_B']
    return CalculationResult(
        name="Boltzmann Constant",
        name_ar="ثابت بولتزمان",
        formula="k_B = √(19/10) × 10^(-23)",
        calculated=calculated,
        actual=actual,
        error_percent=calculate_error(calculated, actual),
        unit="J/K"
    )

def verify_hoyle_resonance() -> CalculationResult:
    """Verify E_Hoyle = 7 + p/29"""
    calculated = 7 + p / 29
    actual = CONSTANTS['E_hoyle']
    return CalculationResult(
        name="Hoyle Resonance",
        name_ar="رنين هويل",
        formula="E_H = 7 + 19/29",
        calculated=calculated,
        actual=actual,
        error_percent=calculate_error(calculated, actual),
        unit="MeV"
    )

# =============================================================================
# Additional Verifications
# تحققات إضافية
# =============================================================================

def verify_digital_root_property():
    """Verify that Digital Root(k × 19) = k for k ∈ {1,...,9}"""
    print("\n" + "="*70)
    print("DIGITAL ROOT PROPERTY | خاصية الجذر الرقمي")
    print("="*70)
    print(f"{'k':<5} {'k×19':<10} {'Sum':<15} {'Digital Root':<15} {'Valid':<10}")
    print("-"*70)
    
    all_valid = True
    for k in range(1, 10):
        product = k * 19
        # Calculate digital root
        digit_sum = sum(int(d) for d in str(product))
        digital_root = digit_sum
        while digital_root >= 10:
            digital_root = sum(int(d) for d in str(digital_root))
        
        valid = digital_root == k
        all_valid = all_valid and valid
        
        print(f"{k:<5} {product:<10} {digit_sum:<15} {digital_root:<15} {'✓' if valid else '✗':<10}")
    
    print("-"*70)
    print(f"Property verified: {'✓ YES' if all_valid else '✗ NO'}")
    return all_valid

def verify_digit_multiplication_property():
    """Verify 19 = 1×9 + 1 + 9"""
    print("\n" + "="*70)
    print("DIGIT MULTIPLICATION PROPERTY | خاصية ضرب الأرقام")
    print("="*70)
    
    digit_1 = 1
    digit_2 = 9
    product = digit_1 * digit_2
    sum_digits = digit_1 + digit_2
    result = product + sum_digits
    
    print(f"19 = {digit_1} × {digit_2} + {digit_1} + {digit_2}")
    print(f"19 = {product} + {sum_digits}")
    print(f"19 = {result}")
    print(f"Verified: {'✓ YES' if result == 19 else '✗ NO'}")
    
    # Check that both digits are non-prime
    print(f"\nDigit 1 = {digit_1} (non-prime: {'✓' if digit_1 == 1 else '✗'})")
    print(f"Digit 9 = {digit_2} (non-prime: {'✓' if digit_2 not in [2,3,5,7] else '✗'})")
    
    return result == 19

def verify_key_relationships():
    """Verify key mathematical relationships"""
    print("\n" + "="*70)
    print("KEY RELATIONSHIPS | العلاقات الأساسية")
    print("="*70)
    
    pi_approx = 22/7
    
    relations = [
        ("π - e_p = 3/7", pi_approx - e_p, 3/7),
        ("7π = 22", 7 * pi_approx, 22),
        ("7e_p + 3 = 22", 7 * e_p + 3, 22),
        ("π + e_p = 41/7", pi_approx + e_p, 41/7),
        ("1/α ≈ 7×19 + 4 = 137", 7*19 + 4, 137),
    ]
    
    for name, calculated, expected in relations:
        valid = abs(calculated - expected) < 1e-10
        print(f"{name:<25} : {calculated:.10f} = {expected:.10f} {'✓' if valid else '✗'}")

def verify_exponent_structure():
    """Verify that all exponents derive from p = 19"""
    print("\n" + "="*70)
    print("EXPONENT STRUCTURE | بنية الأُسس")
    print("="*70)
    print(f"{'Constant':<20} {'Exponent':<12} {'Expression':<20} {'Value':<10} {'Valid':<10}")
    print("-"*70)
    
    exponents = [
        ("G", -11, "-(p-8)", -(p-8)),
        ("e_q", -19, "-p", -p),
        ("k_B", -23, "-(p+4)", -(p+4)),
        ("m_p", -27, "-(p+8)", -(p+8)),
        ("m_e", -31, "-(2p-7)", -(2*p-7)),
        ("h, ℏ", -34, "-(p+15)", -(p+15)),
    ]
    
    for name, expected, expr, calculated in exponents:
        valid = calculated == expected
        print(f"{name:<20} {expected:<12} {expr:<20} {calculated:<10} {'✓' if valid else '✗':<10}")

# =============================================================================
# Main Execution
# التنفيذ الرئيسي
# =============================================================================

def main():
    print("="*70)
    print("THE MATHEMATICAL SYSTEM OF PRIME NUMBER 19")
    print("المنظومة الرياضية للعدد الأولي 19")
    print("="*70)
    print(f"\nBase Definition: p = {p}, e_p = p/7 = {e_p:.10f}")
    print("="*70)
    
    # Run all verifications
    results = [
        verify_euler_number(),
        verify_pi(),
        verify_fine_structure_simple(),
        verify_fine_structure_precise(),
        verify_electron_charge(),
        verify_speed_of_light_simple(),
        verify_speed_of_light_precise(),
        verify_electron_mass(),
        verify_proton_mass(),
        verify_mass_ratio(),
        verify_planck_constant(),
        verify_reduced_planck(),
        verify_gravitational_constant(),
        verify_boltzmann_constant(),
        verify_hoyle_resonance(),
    ]
    
    # Print results table
    print("\n" + "="*70)
    print("PHYSICAL CONSTANTS VERIFICATION | التحقق من الثوابت الفيزيائية")
    print("="*70)
    
    print(f"\n{'Constant':<30} {'Calculated':<20} {'Actual':<20} {'Error %':<12}")
    print("-"*70)
    
    for r in results:
        calc_str = f"{r.calculated:.6e}" if abs(r.calculated) < 0.01 or abs(r.calculated) > 1000 else f"{r.calculated:.6f}"
        act_str = f"{r.actual:.6e}" if abs(r.actual) < 0.01 or abs(r.actual) > 1000 else f"{r.actual:.6f}"
        print(f"{r.name:<30} {calc_str:<20} {act_str:<20} {r.error_percent:<12.6f}")
    
    # Sort by error and show ranking
    print("\n" + "="*70)
    print("ACCURACY RANKING | ترتيب الدقة")
    print("="*70)
    
    sorted_results = sorted(results, key=lambda x: x.error_percent)
    
    medals = ['🥇', '🥈', '🥉'] + [str(i) for i in range(4, 20)]
    
    print(f"\n{'Rank':<6} {'Constant':<35} {'Error %':<15}")
    print("-"*70)
    
    for i, r in enumerate(sorted_results):
        print(f"{medals[i]:<6} {r.name:<35} {r.error_percent:.6f}%")
    
    # Additional verifications
    verify_digital_root_property()
    verify_digit_multiplication_property()
    verify_key_relationships()
    verify_exponent_structure()
    
    # Summary statistics
    print("\n" + "="*70)
    print("SUMMARY STATISTICS | إحصائيات ملخصة")
    print("="*70)
    
    below_001 = sum(1 for r in results if r.error_percent < 0.01)
    below_01 = sum(1 for r in results if r.error_percent < 0.1)
    below_025 = sum(1 for r in results if r.error_percent < 0.25)
    
    print(f"\nConstants with error < 0.01%:  {below_001}")
    print(f"Constants with error < 0.1%:   {below_01}")
    print(f"Constants with error < 0.25%:  {below_025}")
    print(f"Total constants verified:      {len(results)}")
    
    avg_error = sum(r.error_percent for r in results) / len(results)
    min_error = min(r.error_percent for r in results)
    max_error = max(r.error_percent for r in results)
    
    print(f"\nMinimum error: {min_error:.6f}%")
    print(f"Maximum error: {max_error:.6f}%")
    print(f"Average error: {avg_error:.6f}%")
    
    print("\n" + "="*70)
    print("VERIFICATION COMPLETE | اكتمل التحقق")
    print("="*70)
    print("\nAll calculations can be independently verified using CODATA reference values.")
    print("جميع الحسابات يمكن التحقق منها بشكل مستقل باستخدام القيم المرجعية من CODATA.")
    print("\n" + "="*70)

if __name__ == "__main__":
    main()