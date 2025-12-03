#!/usr/bin/env python3
"""
KDFA Reference Charts Generator
Generates publication-quality figures for framework documentation
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patches as mpatches

# Set publication quality defaults
plt.rcParams.update({
    'font.size': 12,
    'font.family': 'serif',
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 11,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.grid': True,
    'grid.alpha': 0.3
})

def create_kappa_zones_chart(output_path):
    """Create the κ coupling zones visualization"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Define zones
    zones = [
        (0.00, 0.25, '#8B0000', 'COLLAPSED\nκ < 0.25', 'Failed State'),
        (0.25, 0.333, '#FF6B6B', 'SUBCRITICAL\n0.25 < κ < 0.33', 'Rigid/Fragile'),
        (0.333, 0.45, '#4ECDC4', 'CRITICAL\n0.33 < κ < 0.45', 'Life Zone'),
        (0.45, 0.55, '#45B7D1', 'OPTIMAL\n0.45 < κ < 0.55', 'Generative'),
        (0.55, 0.65, '#F9C74F', 'SUPERCRITICAL\n0.55 < κ < 0.65', 'Abundance Crushing'),
        (0.65, 1.00, '#FF6B6B', 'TERMINAL\nκ > 0.65', 'Collapse Imminent')
    ]
    
    for x0, x1, color, label, desc in zones:
        rect = FancyBboxPatch((x0, 0), x1-x0, 1, 
                               boxstyle="round,pad=0.02",
                               facecolor=color, alpha=0.7,
                               edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text((x0+x1)/2, 0.7, label, ha='center', va='center', 
                fontsize=10, fontweight='bold', color='black')
        ax.text((x0+x1)/2, 0.3, desc, ha='center', va='center',
                fontsize=9, style='italic', color='black')
    
    # Mark critical values
    critical_points = [
        (0.333, 'κ = 1/3\n(Virial)', 'red'),
        (0.35, 'κ = 0.35\n(Life)', 'green'),
        (0.342, 'κ = ∛0.04\n(Cosmo)', 'blue')
    ]
    
    for x, label, color in critical_points:
        ax.axvline(x, color=color, linestyle='--', linewidth=2, alpha=0.8)
        ax.text(x, 1.05, label, ha='center', va='bottom', fontsize=9, 
                color=color, fontweight='bold')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.2)
    ax.set_xlabel(r'Coupling Ratio $\kappa = R/(R+S)$', fontsize=14)
    ax.set_title(r'L-Spark Coupling Zones: $\mathcal{L}_{Spark}(\kappa)$', fontsize=16, fontweight='bold')
    ax.set_yticks([])
    
    # Add S and R axis labels
    ax.text(0.1, -0.1, r'← S-dominated (Constraint)', fontsize=11, ha='center', transform=ax.transAxes)
    ax.text(0.9, -0.1, r'R-dominated (Dynamics) →', fontsize=11, ha='center', transform=ax.transAxes)
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Created: {output_path}")


def create_d2_validation_chart(output_path):
    """Create D₂ validation across systems"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Data: (system, D₂, error, color)
    systems = [
        ('KDFA Prediction', 1.46, 0.10, '#FF6B6B', '*'),
        ('IceCube Neutrinos', 1.495, 0.144, '#4ECDC4', 'o'),
        ('Fermi GCE', 1.635, 0.10, '#45B7D1', 's'),
        ('Nepal Earthquake', 1.65, 0.02, '#F9C74F', '^'),
        ('Coral Reefs (Surface)', 1.60, 0.05, '#96CEB4', 'D'),
        ('Earthquake (b=1)', 1.45, 0.10, '#DDA0DD', 'p'),
        ('Global Seismicity', 2.20, 0.05, '#FFB6C1', 'h'),
    ]
    
    y_positions = np.arange(len(systems))
    
    for i, (name, d2, err, color, marker) in enumerate(systems):
        ax.errorbar(d2, i, xerr=err, fmt=marker, markersize=12, 
                   color=color, capsize=5, capthick=2, linewidth=2,
                   label=name)
    
    # Add critical zone
    ax.axvspan(1.36, 1.56, alpha=0.2, color='green', label='Critical Zone (1.46±0.10)')
    ax.axvline(1.46, color='red', linestyle='--', linewidth=2, label=r'$D_2 = 1.46$')
    
    ax.set_yticks(y_positions)
    ax.set_yticklabels([s[0] for s in systems])
    ax.set_xlabel(r'Correlation Dimension $D_2$', fontsize=14)
    ax.set_title(r'Universal $D_2 \approx 1.46$ at Criticality', fontsize=16, fontweight='bold')
    ax.set_xlim(1.0, 2.5)
    ax.legend(loc='upper right', fontsize=9)
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Created: {output_path}")


def create_b_value_precursor_chart(output_path):
    """Create b-value precursor timeline example"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    
    # Simulated Wenchuan-like data
    months = np.arange(-24, 1, 0.5)  # 24 months before mainshock
    
    # b-value: stable then drops
    b_baseline = 1.47
    b_values = np.ones_like(months) * b_baseline
    drop_start = -6  # 6 months before
    mask = months > drop_start
    b_values[mask] = b_baseline - (months[mask] - drop_start) * 0.175
    b_values = np.clip(b_values, 0.42, 1.47)
    b_values += np.random.normal(0, 0.05, len(months))
    
    # κ estimate from b
    kappa = 1 - (b_values / 2)
    
    # Plot b-value
    ax1.plot(months, b_values, 'b-', linewidth=2, label='b-value')
    ax1.axhline(0.7, color='orange', linestyle='--', linewidth=2, label='Warning threshold (b=0.7)')
    ax1.axhline(0.5, color='red', linestyle='--', linewidth=2, label='Critical threshold (b=0.5)')
    ax1.axvline(0, color='black', linestyle='-', linewidth=3, label='MAINSHOCK')
    ax1.fill_between(months, 0.5, 0.7, alpha=0.2, color='orange')
    ax1.fill_between(months, 0, 0.5, alpha=0.2, color='red')
    ax1.set_ylabel(r'Gutenberg-Richter $b$-value', fontsize=12)
    ax1.set_ylim(0.3, 1.7)
    ax1.legend(loc='upper right')
    ax1.set_title('Earthquake Precursor: Wenchuan-type Pattern', fontsize=14, fontweight='bold')
    
    # Plot κ estimate
    ax2.plot(months, kappa, 'g-', linewidth=2, label=r'$\kappa \approx 1 - b/2$')
    ax2.axhline(0.65, color='orange', linestyle='--', linewidth=2, label=r'$\kappa = 0.65$ (Supercritical)')
    ax2.axhline(0.75, color='red', linestyle='--', linewidth=2, label=r'$\kappa = 0.75$ (Terminal)')
    ax2.axvline(0, color='black', linestyle='-', linewidth=3)
    ax2.fill_between(months, 0.65, 0.75, alpha=0.2, color='orange')
    ax2.fill_between(months, 0.75, 1.0, alpha=0.2, color='red')
    ax2.set_ylabel(r'Coupling Ratio $\kappa$', fontsize=12)
    ax2.set_xlabel('Months Before Mainshock', fontsize=12)
    ax2.set_ylim(0.2, 0.85)
    ax2.legend(loc='upper left')
    
    # Add alert level annotations
    ax2.annotate('GREEN', xy=(-20, 0.27), fontsize=10, color='green', fontweight='bold')
    ax2.annotate('YELLOW', xy=(-8, 0.60), fontsize=10, color='orange', fontweight='bold')
    ax2.annotate('ORANGE', xy=(-4, 0.70), fontsize=10, color='darkorange', fontweight='bold')
    ax2.annotate('RED', xy=(-1, 0.78), fontsize=10, color='red', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Created: {output_path}")


def create_lspark_equation_chart(output_path):
    """Create L-Spark equation visualization"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Panel 1: κ dependence
    ax1 = axes[0]
    kappa = np.linspace(0.01, 0.99, 100)
    L_kappa = kappa  # Simplified: just the coupling term
    
    ax1.plot(kappa, L_kappa, 'b-', linewidth=3)
    ax1.axvline(0.333, color='red', linestyle='--', linewidth=2, label=r'$\kappa_{virial} = 1/3$')
    ax1.axvline(0.35, color='green', linestyle='--', linewidth=2, label=r'$\kappa_{critical} = 0.35$')
    ax1.axvspan(0.35, 0.55, alpha=0.2, color='green', label='Optimal Zone')
    ax1.set_xlabel(r'$\kappa = R/(R+S)$', fontsize=12)
    ax1.set_ylabel(r'$\kappa$ term', fontsize=12)
    ax1.set_title(r'Coupling: $\kappa = \frac{R}{R+S}$', fontsize=14)
    ax1.legend(fontsize=9)
    ax1.set_xlim(0, 1)
    
    # Panel 2: Damping term for different D₂
    ax2 = axes[1]
    n = np.linspace(0, 1000, 500)
    
    for d2, color, label in [(1.3, 'blue', r'$D_2=1.3$'), 
                              (1.46, 'red', r'$D_2=1.46$'), 
                              (1.7, 'green', r'$D_2=1.7$')]:
        alpha = np.exp(-(n/456)**(2-d2))
        ax2.plot(n, alpha, color=color, linewidth=2, label=label)
    
    ax2.axvline(456, color='purple', linestyle='--', linewidth=2, label=r'$n = 456$')
    ax2.set_xlabel(r'Scale $n$', fontsize=12)
    ax2.set_ylabel(r'Damping $\alpha(n)$', fontsize=12)
    ax2.set_title(r'Damping: $\exp\left[-\left(\frac{n}{456}\right)^{2-D_2}\right]$', fontsize=14)
    ax2.legend(fontsize=9)
    ax2.set_xlim(0, 1000)
    
    # Panel 3: Full L-Spark surface
    ax3 = axes[2]
    kappa_grid = np.linspace(0.1, 0.9, 50)
    n_grid = np.linspace(1, 500, 50)
    K, N = np.meshgrid(kappa_grid, n_grid)
    D2 = 1.46
    L = K * np.exp(-(N/456)**(2-D2))
    
    contour = ax3.contourf(K, N, L, levels=20, cmap='viridis')
    plt.colorbar(contour, ax=ax3, label=r'$\mathcal{L}_{Spark}$')
    ax3.set_xlabel(r'$\kappa$', fontsize=12)
    ax3.set_ylabel(r'Scale $n$', fontsize=12)
    ax3.set_title(r'$\mathcal{L}_{Spark}(\kappa, n)$ at $D_2=1.46$', fontsize=14)
    
    # Add optimal zone marker
    ax3.axvline(0.35, color='white', linestyle='--', linewidth=2)
    ax3.axvline(0.55, color='white', linestyle='--', linewidth=2)
    
    plt.suptitle(r'L-Spark Equation: $\mathcal{L}_{Spark}(n, \kappa, D_2) = \frac{R}{R+S} \cdot \exp\left[-\left(\frac{n}{456}\right)^{2-D_2}\right]$', 
                 fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Created: {output_path}")


def create_sr_mapping_chart(output_path):
    """Create S-R axis mapping visualization"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Domain data
    domains = [
        ('Stellar', 'Gravitational PE\n(binding)', 'Thermal KE\n(expansion)', '0.333', 'Virial theorem'),
        ('Quantum', 'Position uncertainty\nΔx', 'Momentum uncertainty\nΔp', '~0.35', 'Heisenberg'),
        ('Protein', 'Bond network\n(structure)', 'Folding dynamics\n(conformational)', '~0.35', 'Flexible residues'),
        ('Cellular', 'Membrane structure\n(containment)', 'Metabolic flux\n(throughput)', '0.35-0.38', 'ATP efficiency'),
        ('Ecosystem', 'Structural complexity\n(habitat)', 'Energy flow\n(productivity)', '~0.35', 'Trophic efficiency'),
        ('Earthquake', 'Fault friction\n(locking)', 'Strain energy\n(loading)', '0.35', 'Nucleation threshold'),
        ('Economy', 'Production capacity\n(real output)', 'Coordination load\n(overhead)', '0.35', 'Venezuela κ=0.70'),
        ('Civilization', 'Infrastructure\n(physical capital)', 'Social complexity\n(coordination)', '~0.35', 'Collapse threshold'),
    ]
    
    # Create table-like visualization
    ax.set_xlim(0, 10)
    ax.set_ylim(0, len(domains) + 1)
    ax.axis('off')
    
    # Headers
    headers = ['Domain', 'S-Axis\n(Constraint/HOW)', 'R-Axis\n(Dynamics/WHAT)', 'κ_optimal', 'Evidence']
    x_positions = [0.5, 2.5, 5.0, 7.5, 9.0]
    
    for x, header in zip(x_positions, headers):
        ax.text(x, len(domains) + 0.5, header, ha='center', va='center', 
                fontsize=11, fontweight='bold', 
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
    
    # Data rows
    for i, (domain, s_axis, r_axis, kappa, evidence) in enumerate(domains):
        y = len(domains) - i - 0.5
        
        # Alternating row colors
        if i % 2 == 0:
            rect = Rectangle((0, y-0.4), 10, 0.8, facecolor='lightgray', alpha=0.3)
            ax.add_patch(rect)
        
        ax.text(x_positions[0], y, domain, ha='center', va='center', fontsize=10, fontweight='bold')
        ax.text(x_positions[1], y, s_axis, ha='center', va='center', fontsize=9)
        ax.text(x_positions[2], y, r_axis, ha='center', va='center', fontsize=9)
        ax.text(x_positions[3], y, kappa, ha='center', va='center', fontsize=10, 
                color='darkgreen', fontweight='bold')
        ax.text(x_positions[4], y, evidence, ha='center', va='center', fontsize=9, style='italic')
    
    # Title and caption
    ax.set_title(r'Universal S-R Mapping: $\kappa = \frac{R}{R+S} \approx 0.35$ Across Domains', 
                 fontsize=16, fontweight='bold', pad=20)
    
    ax.text(5, -0.5, 
            r'S = Constraint (the HOW) | R = Dynamics (the WHAT) | $\kappa_{critical} \approx 0.35 \approx 1/e$',
            ha='center', va='center', fontsize=12, style='italic')
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Created: {output_path}")


def create_456_derivation_chart(output_path):
    """Create 456 harmonic derivation visualization"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Panel 1: Hoyle State derivation
    ax1 = axes[0, 0]
    ax1.text(0.5, 0.9, r'$\mathbf{456\ Harmonic\ Derivation}$', ha='center', fontsize=14, fontweight='bold', transform=ax1.transAxes)
    
    derivation_text = r'''
$E_{Hoyle} = 7.656$ MeV (Carbon-12 resonance)

$7.656^3 = 449.2 \approx 456$

Alternative:
$456 = \frac{4}{3} \times 0.342 \times 1000$

where $0.342 = \sqrt[3]{0.04}$ (cosmological)

$\frac{456}{1000} = 0.456 \approx \frac{1}{e} + 0.09$
'''
    ax1.text(0.1, 0.5, derivation_text, ha='left', va='center', fontsize=11, 
             transform=ax1.transAxes, family='monospace')
    ax1.axis('off')
    
    # Panel 2: 456 appearances
    ax2 = axes[0, 1]
    appearances = [
        ('Stellar oscillations', '456/k harmonics'),
        ('Sleep cycle', '456 min ≈ 7.6 hr'),
        ('Cardiac rhythm', '456/7 ≈ 65 bpm'),
        ('Carbon fusion', '7.656³ ≈ 456'),
        ('Collapse timescale', 't = 456/Δκ'),
        ('Recovery period', 'T = 456 × (2-D₂)'),
    ]
    
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, len(appearances) + 1)
    ax2.axis('off')
    ax2.text(0.5, len(appearances) + 0.5, '456 Appearances', ha='center', fontsize=12, fontweight='bold')
    
    for i, (system, formula) in enumerate(appearances):
        y = len(appearances) - i - 0.3
        ax2.text(0.1, y, f'• {system}:', fontsize=10, fontweight='bold')
        ax2.text(0.55, y, formula, fontsize=10, family='monospace')
    
    # Panel 3: Damping curves at n=456
    ax3 = axes[1, 0]
    n = np.linspace(1, 1000, 500)
    
    for d2 in [1.2, 1.46, 1.7, 1.9]:
        alpha = np.exp(-(n/456)**(2-d2))
        ax3.plot(n, alpha, linewidth=2, label=f'$D_2 = {d2}$')
    
    ax3.axvline(456, color='red', linestyle='--', linewidth=2, label='$n = 456$')
    ax3.axhline(1/np.e, color='gray', linestyle=':', linewidth=1, label='$1/e$')
    ax3.set_xlabel('Scale $n$')
    ax3.set_ylabel(r'$\alpha(n) = \exp[-(n/456)^{2-D_2}]$')
    ax3.set_title('Damping Term at Different $D_2$')
    ax3.legend()
    ax3.set_xlim(0, 1000)
    
    # Panel 4: At n=456, α = 1/e for various D₂
    ax4 = axes[1, 1]
    d2_range = np.linspace(1.0, 2.0, 100)
    alpha_at_456 = np.exp(-(1)**(2-d2_range))  # n/456 = 1 when n=456
    
    ax4.plot(d2_range, alpha_at_456, 'b-', linewidth=3)
    ax4.axhline(1/np.e, color='red', linestyle='--', linewidth=2, label='$1/e \\approx 0.368$')
    ax4.axvline(1.46, color='green', linestyle='--', linewidth=2, label='$D_2 = 1.46$')
    
    ax4.set_xlabel(r'Fractal Dimension $D_2$')
    ax4.set_ylabel(r'$\alpha(456)$')
    ax4.set_title(r'At $n=456$: $\alpha = e^{-1} = 1/e$ for all $D_2$')
    ax4.legend()
    
    plt.suptitle('The 456 Universal Harmonic', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Created: {output_path}")


def create_earthquake_alert_flowchart(output_path):
    """Create earthquake alert system flowchart"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Define boxes
    boxes = [
        (1, 8.5, 3, 1, 'Seismic Network\n(Real-time data)', 'lightblue'),
        (5.5, 8.5, 3, 1, 'b-Value Calculation\n(100-event window)', 'lightyellow'),
        (10, 8.5, 3, 1, r'$\kappa$ Estimation' + '\n' + r'$\kappa = 1 - b/2$', 'lightgreen'),
        (1, 6, 3, 1, r'$D_2$ Calculation' + '\n(Spatial clustering)', 'lightyellow'),
        (5.5, 6, 3, 1, 'Pattern Recognition\n(Foreshock detection)', 'lightpink'),
        (10, 6, 3, 1, 'Alert Level\nDetermination', 'moccasin'),
        (3.25, 3.5, 2.5, 0.8, 'GREEN\nκ < 0.55', 'lightgreen'),
        (5.75, 3.5, 2.5, 0.8, 'YELLOW\n0.55 < κ < 0.65', 'yellow'),
        (8.25, 3.5, 2.5, 0.8, 'ORANGE\n0.65 < κ < 0.75', 'orange'),
        (10.75, 3.5, 2.5, 0.8, 'RED\nκ > 0.75', 'red'),
        (7, 1, 4, 1.2, 'Community Alert System\n(Mobile, Sirens, Broadcast)', 'lightcyan'),
    ]
    
    for x, y, w, h, text, color in boxes:
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                               facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=9, fontweight='bold')
    
    # Arrows
    arrows = [
        (4, 9, 1.5, 0),      # Network -> b-value
        (8.5, 9, 1.5, 0),    # b-value -> kappa
        (2.5, 8.5, 0, -1.5), # Network -> D2
        (4, 6.5, 1.5, 0),    # D2 -> Pattern
        (8.5, 6.5, 1.5, 0),  # Pattern -> Alert
        (11.5, 8.5, 0, -1.5),# kappa -> Alert
        (7, 6, 0, -0.7),     # Pattern -> levels
        (4.5, 4.3, 0, -0.5), # to GREEN
        (7, 4.3, 0, -0.5),   # to YELLOW
        (9.5, 4.3, 0, -0.5), # to ORANGE
        (12, 4.3, 0, -0.5),  # to RED
        (9, 3.5, 0, -1.3),   # to Community
    ]
    
    for x, y, dx, dy in arrows:
        ax.annotate('', xy=(x+dx, y+dy), xytext=(x, y),
                   arrowprops=dict(arrowstyle='->', color='black', lw=2))
    
    ax.set_title('L-Spark Earthquake Alert System Architecture', fontsize=16, fontweight='bold', pad=20)
    
    # Add formula box
    formula_text = r'''
Core Formulas:
$\kappa = 1 - \frac{b}{2}$
$D_2 = 1.45 \times b$
Alert when $\kappa > 0.55$
'''
    ax.text(0.5, 2, formula_text, fontsize=10, family='monospace',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Created: {output_path}")


if __name__ == "__main__":
    import os
    
    output_dir = "/mnt/user-data/outputs/kdfa_charts"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating KDFA reference charts...")
    
    create_kappa_zones_chart(f"{output_dir}/kappa_zones.png")
    create_d2_validation_chart(f"{output_dir}/d2_validation.png")
    create_b_value_precursor_chart(f"{output_dir}/b_value_precursor.png")
    create_lspark_equation_chart(f"{output_dir}/lspark_equation.png")
    create_sr_mapping_chart(f"{output_dir}/sr_mapping.png")
    create_456_derivation_chart(f"{output_dir}/456_derivation.png")
    create_earthquake_alert_flowchart(f"{output_dir}/earthquake_alert_system.png")
    
    print(f"\nAll charts saved to: {output_dir}/")
