import matplotlib.pyplot as plt
import numpy as np

def plot_packing_conflict():
    # Data
    prediction_ratio = 13/19  # 0.68421...
    planck_mean = 0.6847
    planck_error = 0.0073
    
    # Setup plot
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Plot Planck Measurement (Error Bar)
    ax.errorbar(planck_mean, 0, xerr=planck_error, fmt='o', color='black', 
                capsize=10, elinewidth=3, markeredgewidth=2, label='Planck 2018 (Ω_DE)')
    
    # Plot Prediction (Line)
    ax.axvline(prediction_ratio, color='red', linestyle='-', linewidth=3, 
               label=f'Packing Conflict Prediction (13/19 ≈ {prediction_ratio:.5f})')
    
    # Annotations
    ax.text(prediction_ratio, 0.2, f'Prediction: {prediction_ratio:.5f}', 
            color='red', ha='center', fontweight='bold')
    ax.text(planck_mean, -0.2, f'Planck: {planck_mean} ± {planck_error}', 
            color='black', ha='center')
    
    # Formatting
    ax.set_xlim(0.65, 0.72)
    ax.set_ylim(-0.5, 0.5)
    ax.set_xlabel('Dark Energy Density Parameter (Ω_DE)', fontsize=12)
    ax.set_title('Packing Conflict Hypothesis vs. Planck 2018 Data', fontsize=14)
    ax.get_yaxis().set_visible(False)
    ax.legend(loc='upper right')
    ax.grid(True, axis='x', alpha=0.3)
    
    # Save
    output_path = 'figures/packing_conflict_prediction.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    plot_packing_conflict()
