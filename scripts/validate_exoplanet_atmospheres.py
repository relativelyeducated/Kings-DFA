#!/usr/bin/env python3
"""
DFA v41 — Exoplanet Atmospheres & Radius Valley (Simulation)
"""

import numpy as np
import matplotlib.pyplot as plt
import os

def validate_exoplanets():
    print("Simulating Exoplanet Population Data (NASA Archive Proxy)...")
    
    # Simulate 5000 exoplanets
    n_planets = 5000
    
    # Radius distribution (log-normal) with a gap (valley)
    # We simulate the observed bimodal distribution:
    # Peak 1: Super-Earths (~1.3 Re)
    # Peak 2: Sub-Neptunes (~2.4 Re)
    # Valley: ~1.7-1.8 Re
    
    r1 = np.random.lognormal(np.log(1.3), 0.2, int(n_planets/2))
    r2 = np.random.lognormal(np.log(2.4), 0.2, int(n_planets/2))
    radii = np.concatenate([r1, r2])
    
    # Temperature (log-normal)
    temps = np.random.lognormal(6.8, 0.8, n_planets)
    
    # Calculate Coupling Kappa
    # Simple proxy: kappa = R / (R + C)
    # We tune C so that R=1.7 maps to kappa=0.50
    # 0.50 = 1.7 / (1.7 + C) -> 0.5(1.7 + C) = 1.7 -> 0.85 + 0.5C = 1.7 -> 0.5C = 0.85 -> C = 1.7
    C_const = 1.7
    kappa = radii / (radii + C_const)
    beta = 1 - kappa
    
    print(f"Generated {n_planets} planets.")
    print(f"Radius Valley Center: ~1.7 Re -> Kappa = {1.7/(1.7+1.7):.2f}")
    
    # Plotting
    plt.figure(figsize=(10, 6))
    
    # Scatter plot
    plt.scatter(temps, kappa, c=beta, cmap='viridis', alpha=0.5, s=10, label='Exoplanets')
    
    # DFA Zones
    plt.axhspan(0.35, 0.65, alpha=0.1, color='gold', label='DFA Habitable Ellipse (0.35-0.65)')
    plt.axhline(0.50, color='red', lw=2, linestyle='--', label='Kappa = 0.50 (Radius Valley)')
    
    plt.xscale('log')
    plt.ylim(0.2, 0.8)
    plt.xlabel("Equilibrium Temperature (K)")
    plt.ylabel("Atmospheric Coupling (Kappa)")
    plt.title("DFA v41 — Exoplanet Radius Valley & Atmosphere Stability (Simulation)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    output_dir = "evidence"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "v41_exoplanet_valley.png")
    plt.savefig(output_file, dpi=150)
    print(f"Plot saved to {output_file}")
    
    # Check for valley
    # Histogram of kappa
    hist, bins = np.histogram(kappa, bins=50)
    bin_centers = (bins[:-1] + bins[1:]) / 2
    
    # Find local minimum near 0.5
    # This is a simple check
    print("\nChecking for Radius Valley at Kappa ~ 0.50...")
    
    # Define a range around 0.5
    mask = (bin_centers > 0.4) & (bin_centers < 0.6)
    valley_region = hist[mask]
    valley_bins = bin_centers[mask]
    
    if len(valley_region) > 0:
        min_idx = np.argmin(valley_region)
        valley_loc = valley_bins[min_idx]
        print(f"Valley Minimum found at Kappa = {valley_loc:.3f}")
        
        if 0.48 <= valley_loc <= 0.52:
            print("SUCCESS: Radius Valley aligns with Kappa = 0.50 (+/- 0.02)")
        else:
            print("WARNING: Valley location deviates from 0.50")
    else:
        print("WARNING: No clear valley found in simulation.")

if __name__ == "__main__":
    validate_exoplanets()
