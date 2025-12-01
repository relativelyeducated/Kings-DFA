import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

def plot_vesica_corrected():
    # Parameters
    R = 1.0
    d = 0.5 * R  # Virial Equilibrium
    
    # Setup plot
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Circles
    circle1 = plt.Circle((-d/2, 0), R, color='blue', alpha=0.2, label='Structure (S)')
    circle2 = plt.Circle((d/2, 0), R, color='red', alpha=0.2, label='Relation (R)')
    
    # Outlines
    circle1_line = plt.Circle((-d/2, 0), R, color='blue', fill=False, linewidth=2)
    circle2_line = plt.Circle((d/2, 0), R, color='red', fill=False, linewidth=2)
    
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle1_line)
    ax.add_patch(circle2_line)
    
    # Centers
    ax.plot(-d/2, 0, 'bo', markersize=8)
    ax.plot(d/2, 0, 'ro', markersize=8)
    
    # Annotations
    # d/R = 0.5
    ax.annotate(f'Separation d = {d}R', xy=(0, 0), xytext=(0, -0.2),
                arrowprops=dict(arrowstyle='<->', color='black'),
                ha='center', fontsize=12)
    
    # Overlap Area
    ax.text(0, 0.5, r'$\Omega_{DE} \approx 0.685$', ha='center', fontsize=14, fontweight='bold')
    ax.text(0, 0.35, '(Overlap Area)', ha='center', fontsize=10)
    
    # Non-Overlap
    ax.text(-1.2, 0, r'$\Omega_{M} \approx 0.315$', ha='center', fontsize=12)
    ax.text(1.2, 0, r'$\Omega_{M} \approx 0.315$', ha='center', fontsize=12)
    
    # Formatting
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(r'Vesica Piscis at Virial Equilibrium ($d/R=0.5$)', fontsize=16)
    
    # Save
    output_path = 'figures/vesica_piscis_corrected.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    plot_vesica_corrected()
