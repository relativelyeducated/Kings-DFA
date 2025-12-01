import matplotlib.pyplot as plt
import numpy as np

def plot_neutrino_mass_prediction():
    # Data
    prediction = 0.028  # eV (DFA Prediction)
    planck_bound = 0.12 # eV (Planck 2018 95% CL)
    katrin_bound = 0.8  # eV (KATRIN Upper Limit per flavor, approx sum > 2.4, but we use Planck for sum)
    
    # Setup plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot Regions
    # Allowed Region (Green)
    ax.axvspan(0, planck_bound, color='green', alpha=0.1, label='Allowed Region (Planck 2018)')
    
    # Excluded Region (Red)
    ax.axvspan(planck_bound, 1.0, color='red', alpha=0.1, label='Excluded by Cosmology')
    
    # Plot Lines
    ax.axvline(planck_bound, color='red', linestyle='--', linewidth=2, label=f'Planck Limit (< {planck_bound} eV)')
    ax.axvline(prediction, color='blue', linestyle='-', linewidth=3, label=f'DFA Prediction ({prediction} eV)')
    
    # Annotations
    ax.text(prediction + 0.005, 0.5, 'DFA Prediction\n(0.028 eV)', color='blue', fontweight='bold')
    ax.text(planck_bound + 0.01, 0.5, 'Planck Limit\n(0.12 eV)', color='red', fontweight='bold')
    
    # Formatting
    ax.set_xlim(0, 0.2)
    ax.set_ylim(0, 1)
    ax.set_xlabel('Sum of Neutrino Masses (eV)', fontsize=12)
    ax.set_title('DFA Neutrino Mass Prediction vs. Cosmological Bounds', fontsize=14)
    ax.get_yaxis().set_visible(False)
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    # Save
    output_path = 'figures/neutrino_mass_prediction.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    plot_neutrino_mass_prediction()
