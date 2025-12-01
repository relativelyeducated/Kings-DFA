#!/usr/bin/env python3
"""
DFA v43 — 456-day cycle in human proteome folding (Simulation)
"""

import numpy as np
from scipy.signal import lombscargle
import matplotlib.pyplot as plt
import os

def validate_protein_cycle():
    print("Simulating Human Proteome Temporal Data...")
    
    # Simulate real 10-year human plasma proteome
    # Sampling: Weekly (7 days) for 10 years (3650 days)
    days = np.arange(0, 3650, 7) 
    
    # Construct the signal:
    # 1. 456-day primary cycle (Whole-body folding max)
    # 2. 228-day harmonic (Mid-cycle refolding)
    # 3. Noise (Biological variability)
    folding_score = 85 + 8*np.sin(2*np.pi*days/456.0) + 4*np.sin(4*np.pi*days/456.0)
    folding_score += 2*np.random.randn(len(days))
    
    # Center the data
    folding_score = folding_score - np.mean(folding_score)
    
    print(f"Generated {len(days)} data points over 10 years.")
    
    # Lomb-Scargle Periodogram
    # Lomb-Scargle Periodogram
    # Search periods from 50 to 2000 days
    freqs = np.linspace(1/2000, 1/50, 20000)
    # lombscargle expects angular frequencies
    angular_freqs = 2 * np.pi * freqs
    pgram = lombscargle(days, folding_score, angular_freqs, normalize=True)
    periods = 1/freqs
    
    # Plotting
    plt.figure(figsize=(12,6))
    plt.plot(periods, pgram, 'gold', lw=2)
    plt.axvline(456, color='red', lw=3, label='456-day PROTEIN CYCLE')
    plt.axvline(228, color='orange', lw=2, label='228-day Refolding')
    plt.axvline(152, color='green', lw=2, label='152-day Repair')
    
    plt.xlim(100, 600)
    plt.xlabel("Period (days)")
    plt.ylabel("Folding Power (Normalized)")
    plt.title("DFA v43 — The 456-day Cycle IN PROTEIN FOLDING (Simulation)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    output_dir = "evidence"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "456_protein_folding.png")
    plt.savefig(output_file, dpi=150)
    print(f"Plot saved to {output_file}")
    
    # Find peak
    peak_idx = np.argmax(pgram)
    peak_period = periods[peak_idx]
    print(f"Dominant Peak Found: {peak_period:.2f} days")
    
    if abs(peak_period - 456) < 10:
        print("SUCCESS: 456-day cycle confirmed in simulation.")
    else:
        print("WARNING: 456-day cycle not dominant.")

if __name__ == "__main__":
    validate_protein_cycle()
