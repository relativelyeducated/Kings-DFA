#!/usr/bin/env python3
"""
Test Born Rule Deviation with Coherent States

This script fixes the bug in reproduce_30pct_deviation.py by using
a COHERENT superposition state instead of an incoherent mixed state.

Key fix: Initial state must have off-diagonal terms (R-axis present)
for the DA modification to apply.

Author: Jason A King (with KDFA analysis)
Date: 2025-11-24
"""

import numpy as np
import sys
sys.path.append('/home/king/ai-workspace/DFA-AI-Training/simulations/quantums')

# Import qutip from venv
import qutip as qt

# Import the DA framework from original simulation
from reproduce_30pct_deviation import DialecticArchestructure, create_apparatus


def create_coherent_state(p_up: float = 0.6) -> qt.Qobj:
    """
    Create COHERENT superposition state (PURE state, not mixed).

    |ψ⟩ = √p_up |↑⟩ + √(1-p_up) |↓⟩

    This has OFF-DIAGONAL terms (R-axis present) unlike the
    mixed state used in the original simulation.

    Parameters
    ----------
    p_up : float
        Probability of measuring spin-up (default: 0.6)

    Returns
    -------
    rho : qutip.Qobj
        Density matrix with coherence terms
    """
    # Amplitudes (not probabilities!)
    alpha = np.sqrt(p_up)
    beta = np.sqrt(1 - p_up)

    # Pure state
    psi = alpha * qt.basis(2, 0) + beta * qt.basis(2, 1)

    # Density matrix
    rho = psi * psi.dag()

    print(f"\n📐 State prepared:")
    print(f"   |ψ⟩ = {alpha:.4f}|↑⟩ + {beta:.4f}|↓⟩")
    print(f"\n   Density matrix:")
    print(rho.full())
    print(f"\n   ✓ Off-diagonal terms: {rho[0,1]:.4f} (R-axis present!)")

    return rho


def analyze_sr_decomposition(da: DialecticArchestructure, rho: qt.Qobj):
    """Analyze S-R decomposition of state."""
    rho_S, rho_R = da.sr_decompose(rho)

    S_strength = da.structural_strength(rho)
    R_strength = da.relational_strength(rho)

    print(f"\n🔬 S-R Decomposition:")
    print(f"   S-axis (diagonal):")
    print(rho_S.full())
    print(f"   Strength: {S_strength:.4f}")
    print(f"\n   R-axis (off-diagonal):")
    print(rho_R.full())
    print(f"   Strength: {R_strength:.4f}")
    print(f"\n   Ratio R/S: {R_strength/S_strength if S_strength > 0 else 0:.4f}")


def test_born_deviation(config='balanced', n_trials=100):
    """
    Test Born rule deviation with coherent state.

    Parameters
    ----------
    config : str
        'balanced' or 'strong'
    n_trials : int
        Number of trials
    """
    print("="*70)
    print("KDFA BORN RULE DEVIATION TEST (FIXED)")
    print("="*70)

    # Initialize DA framework with α = 0.35
    da = DialecticArchestructure(alpha=0.35)
    print(f"\n⚙️  DA coupling constant α = {da.alpha}")

    # Create COHERENT state (FIX!)
    print(f"\n📋 Creating coherent superposition state...")
    rho_sys = create_coherent_state(p_up=0.6)

    # Analyze S-R decomposition
    analyze_sr_decomposition(da, rho_sys)

    # Create apparatus
    print(f"\n🔧 Creating apparatus (config: {config})...")
    rho_app = create_apparatus(config)
    print(f"   Apparatus matrix:")
    print(rho_app.full())

    # Check Arch formation
    arch_forms = da.check_arch_formation(rho_sys, rho_app)
    print(f"\n🏗️  Arch formation: {'✓ YES' if arch_forms else '✗ NO'}")

    if arch_forms:
        # Calculate modification parameters
        _, rho_R = da.sr_decompose(rho_sys)
        C_emergent = np.linalg.norm(rho_R.full(), ord='fro')
        H_initial = da.structural_strength(rho_sys)

        print(f"   C_emergent (R-axis coherence): {C_emergent:.4f}")
        print(f"   H_initial (S-axis entropy): {H_initial:.4f}")
        print(f"   Ratio C/H: {C_emergent/H_initial:.4f}")
        print(f"   Modification factor: 1 + α(C/H) = {1 + da.alpha * C_emergent/H_initial:.4f}")

    # Measurement operator
    P_up = qt.basis(2, 0) * qt.basis(2, 0).dag()

    # Calculate Born rule prediction
    P_born = (rho_sys * P_up).tr().real
    print(f"\n📊 Born Rule Prediction: P(↑) = {P_born:.4f}")

    # Run trials
    print(f"\n🔬 Running {n_trials} trials...")
    P_up_values = []
    arch_count = 0

    for i in range(n_trials):
        P_da, arch = da.measure(rho_sys, rho_app, P_up)
        P_up_values.append(P_da)
        if arch:
            arch_count += 1

    # Statistics
    P_mean = np.mean(P_up_values)
    P_std = np.std(P_up_values)
    deviation_pct = ((P_mean - P_born) / P_born) * 100

    print(f"\n" + "="*70)
    print("RESULTS")
    print("="*70)
    print(f"\nBorn Rule:        P(↑) = {P_born:.4f}")
    print(f"DA Framework:     P(↑) = {P_mean:.4f} ± {P_std:.4f}")
    print(f"\n📈 Deviation:      {deviation_pct:+.2f}%")
    print(f"🏗️  Arch rate:      {arch_count/n_trials*100:.1f}%")

    if abs(deviation_pct) > 1.0:
        print(f"\n✅ SUCCESS: Significant deviation observed!")
        print(f"   This is the KDFA signature at κ ≈ 0.35")
    else:
        print(f"\n⚠️  No significant deviation (expected for this configuration)")

    print("\n" + "="*70)

    return {
        'P_born': P_born,
        'P_mean': P_mean,
        'P_std': P_std,
        'deviation_pct': deviation_pct,
        'arch_rate': arch_count / n_trials
    }


if __name__ == '__main__':
    print("\n" + "🔬"*35)
    print("TESTING KDFA BORN RULE DEVIATION")
    print("Momentum (R-axis) vs Structure (S-axis) Interference")
    print("🔬"*35 + "\n")

    print("\n" + "-"*70)
    print("TEST 1: BALANCED APPARATUS (κ ≈ 0.35, critical coupling)")
    print("-"*70)
    results_balanced = test_born_deviation(config='balanced', n_trials=100)

    print("\n\n" + "-"*70)
    print("TEST 2: STRONG APPARATUS (κ < 0.35, S-dominant)")
    print("-"*70)
    results_strong = test_born_deviation(config='strong', n_trials=100)

    print("\n\n" + "="*70)
    print("COMPARISON")
    print("="*70)
    print(f"\nBalanced (κ≈0.35):  Deviation = {results_balanced['deviation_pct']:+.2f}%")
    print(f"Strong (κ<0.35):    Deviation = {results_strong['deviation_pct']:+.2f}%")
    print(f"\nΔ(Balanced - Strong) = {results_balanced['deviation_pct'] - results_strong['deviation_pct']:+.2f}%")

    if results_balanced['deviation_pct'] > 20:
        print(f"\n🎯 KDFA PREDICTION CONFIRMED!")
        print(f"   Born rule deviates by ~30% at critical coupling κ ≈ 0.35")
        print(f"   This is S-R interference - momentum vs structure!")

    print("\n" + "="*70 + "\n")
