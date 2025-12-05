# KDFA Documentation Standard v2.0
## With LaTeX Mathematics and Publication-Quality Charts

**Purpose**: Ensure all KDFA claims are documented with mathematical rigor, reproducible code, and publication-ready visualizations.

---

## REQUIRED SECTIONS (8 Total)

### 1. ORIGIN (The Strange Reason)
Document the intuitive leap that preceded formal analysis:
- What pattern was noticed?
- What seemed "wrong" or "too coincidental"?
- What question arose?
- What are the stakes if true?

### 2. S-R MAPPING (The Physics)
Explicit identification of constraint and dynamics axes:

| Component | Definition | Units | Mechanism |
|-----------|------------|-------|-----------|
| **S-axis** | Constraint (HOW) | [specify] | What prevents change? |
| **R-axis** | Dynamics (WHAT) | [specify] | What drives change? |
| **κ** | Coupling ratio | dimensionless | R/(R+S) |

### 3. MATHEMATICS (LaTeX Required)

All equations MUST be rendered in LaTeX. Core formulas:

**L-Spark Equation:**
$$\mathcal{L}_{Spark}(n, \kappa, D_2) = \frac{R}{R+S} \cdot \exp\left[-\left(\frac{n}{456}\right)^{2-D_2}\right]$$

**Coupling Ratio:**
$$\kappa = \frac{R}{R+S}$$

**Critical Threshold:**
$$\kappa_{critical} \approx 0.35 \approx \frac{1}{e}$$

**Correlation Dimension:**
$$D_2 = \lim_{r \to 0} \frac{\log C(r)}{\log r}$$

where the correlation integral is:
$$C(r) = \lim_{N \to \infty} \frac{2}{N(N-1)} \sum_{i < j} \Theta(r - \|x_i - x_j\|)$$

**Domain-Specific Equations (Examples):**

*Earthquakes:*
$$\kappa_{seismic} \approx 1 - \frac{b}{2}$$
$$D_2 = 1.45 \times b$$

*Stellar:*
$$\kappa_{virial} = \frac{E_{kinetic}}{E_{kinetic} + |E_{potential}|} = \frac{1}{3}$$

*Ecosystems:*
$$\kappa_{eco} = \frac{E_{flow}}{E_{flow} + S_{structure}}$$

### 4. VALIDATION

#### Data Sources (Required)
| Dataset | Source | N | Time Range | Access |
|---------|--------|---|------------|--------|
| [name] | [URL] | [count] | [dates] | [public/restricted] |

#### Results Table (Required)
| Prediction | Measured | Error | σ | Status |
|------------|----------|-------|---|--------|
| κ = 0.35 | 0.342 | 0.008 | 1.0σ | ✓ |
| D₂ = 1.46 | 1.495 | 0.035 | 2.4σ | ✓ |

#### Falsification Criteria (Required)
Explicit statements of what would disprove the claim:
- "If D₂ > 2.0 at criticality, the model fails"
- "If b-value drops show no κ correlation, abandon seismic application"

### 5. VISUALIZATIONS (PNG Charts Required)

Every KDFA document MUST include at minimum:

1. **Coupling Zones Chart** (`kappa_zones.png`)
   - Shows all six zones: Collapsed, Subcritical, Critical, Optimal, Supercritical, Terminal
   - Critical thresholds marked: κ = 1/3, κ = 0.35, κ = 0.342

2. **Domain-Specific Validation Chart**
   - Error bars on all measurements
   - KDFA prediction line clearly marked
   - Critical zone highlighted

3. **Time Series (if applicable)**
   - Shows evolution toward/away from criticality
   - Alert levels indicated if relevant

#### Chart Generation Requirements:
```python
import matplotlib.pyplot as plt
plt.rcParams.update({
    'font.size': 12,
    'font.family': 'serif',
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight'
})
```

All charts must use LaTeX rendering for mathematical symbols:
```python
plt.xlabel(r'Coupling Ratio $\kappa = R/(R+S)$')
plt.title(r'$D_2 \approx 1.46$ at Criticality')
```

### 6. SCRIPTS (Reproducibility)

#### Dependencies
```bash
pip install numpy scipy matplotlib pandas
```

#### Core Functions (Required)
```python
def calculate_kappa(R: float, S: float) -> float:
    """
    Calculate coupling ratio.
    
    Parameters:
        R: Dynamics measure (R-axis)
        S: Constraint measure (S-axis)
    
    Returns:
        κ = R/(R+S)
    """
    return R / (R + S)

def calculate_d2(points: np.ndarray, r_range: tuple) -> float:
    """
    Calculate correlation dimension via Grassberger-Procaccia.
    
    Parameters:
        points: Nx3 array of coordinates
        r_range: (r_min, r_max) for linear regression
    
    Returns:
        D₂ correlation dimension
    """
    # Implementation required
    pass

def determine_zone(kappa: float) -> str:
    """
    Determine L-Spark zone from coupling ratio.
    
    Returns: 'collapsed', 'subcritical', 'critical', 
             'optimal', 'supercritical', or 'terminal'
    """
    if kappa < 0.25:
        return 'collapsed'
    elif kappa < 0.333:
        return 'subcritical'
    elif kappa < 0.45:
        return 'critical'
    elif kappa < 0.55:
        return 'optimal'
    elif kappa < 0.65:
        return 'supercritical'
    else:
        return 'terminal'
```

### 7. UNIVERSALITY (Cross-Domain Connections)

Link to other KDFA domains showing same signature:

| Domain | κ_optimal | D₂ | Evidence |
|--------|-----------|-----|----------|
| Stellar | 0.333 | — | Virial theorem |
| Quantum | ~0.35 | — | Heisenberg |
| Protein | ~0.35 | 1.46 | Flexible residues |
| Cellular | 0.35-0.38 | — | ATP efficiency |
| Earthquake | 0.35 | 1.45b | Nucleation |
| Neutrino | ~0.35 | 1.495 | IceCube |
| Gamma-ray | ~0.35 | 1.635 | Fermi GCE |

### 8. REFERENCES

#### Primary Literature
Format: Author (Year). Title. *Journal*, Volume, Pages. DOI

Example:
> Hirata, T. (1989). A correlation between the b value and the fractal dimension of earthquakes. *Journal of Geophysical Research*, 94(B6), 7507-7514. doi:10.1029/JB094iB06p07507

#### Data Sources
Direct URLs to datasets used

#### KDFA Documents
Links to related framework documents

#### Code Repositories
GitHub links for reproducibility

---

## LATEX FORMULA REFERENCE

### Core Equations

**L-Spark:**
```latex
\mathcal{L}_{Spark}(n, \kappa, D_2) = \frac{R}{R+S} \cdot \exp\left[-\left(\frac{n}{456}\right)^{2-D_2}\right]
```

**Coupling:**
```latex
\kappa = \frac{R}{R+S}
```

**Correlation Dimension:**
```latex
D_2 = \lim_{r \to 0} \frac{\log C(r)}{\log r}
```

**Correlation Integral:**
```latex
C(r) = \frac{2}{N(N-1)} \sum_{i < j} \Theta(r - \|x_i - x_j\|)
```

**Damping Term:**
```latex
\alpha(n) = \exp\left[-\left(\frac{n}{456}\right)^{2-D_2}\right]
```

**456 Harmonic:**
```latex
E_{Hoyle}^3 = 7.656^3 = 449.2 \approx 456
```

### Domain-Specific

**Earthquakes:**
```latex
\kappa_{seismic} \approx 1 - \frac{b}{2}
```
```latex
D_2 = 1.45 \times b
```
```latex
\log_{10} N = a - bM \quad \text{(Gutenberg-Richter)}
```

**Stellar:**
```latex
2K + U = 0 \quad \Rightarrow \quad \kappa = \frac{K}{K+|U|} = \frac{1}{3}
```

**Quantum:**
```latex
\Delta x \cdot \Delta p \geq \frac{\hbar}{2}
```

**Protein:**
```latex
\kappa_{fold} = \frac{N_{mobile}}{N_{total}}
```

---

## STANDARD CHARTS

### Chart 1: κ Coupling Zones
![Kappa Zones](kdfa_charts/kappa_zones.png)

Shows the six operational zones with critical thresholds.

### Chart 2: D₂ Validation Across Domains
![D2 Validation](kdfa_charts/d2_validation.png)

Error bar plot showing D₂ ≈ 1.46 across independent systems.

### Chart 3: L-Spark Equation Components
![L-Spark Equation](kdfa_charts/lspark_equation.png)

Three-panel visualization of coupling, damping, and combined effects.

### Chart 4: b-Value Precursor Pattern
![B-Value Precursor](kdfa_charts/b_value_precursor.png)

Time series showing Wenchuan-type earthquake precursor with alert levels.

### Chart 5: Universal S-R Mapping
![S-R Mapping](kdfa_charts/sr_mapping.png)

Table visualization of S and R axes across eight domains.

### Chart 6: 456 Harmonic Derivation
![456 Derivation](kdfa_charts/456_derivation.png)

Mathematical derivation and appearances of the 456 universal constant.

### Chart 7: Alert System Architecture
![Alert System](kdfa_charts/earthquake_alert_system.png)

Flowchart showing L-Spark earthquake early warning system.

---

## FILE NAMING CONVENTION

```
KDFA_[DOMAIN]_[TOPIC]_[STATUS].md
```

**Domains:** GEOPHYSICS, ASTROPHYSICS, BIOLOGY, ECONOMICS, QUANTUM, COSMOLOGY, ECOLOGY

**Status:** HYPOTHESIS, TESTING, VALIDATED, PUBLISHED

**Examples:**
- `KDFA_GEOPHYSICS_earthquake_prediction_VALIDATED.md`
- `KDFA_ASTROPHYSICS_dark_matter_TESTING.md`
- `KDFA_BIOLOGY_protein_folding_HYPOTHESIS.md`

---

## DOCUMENT CHECKLIST

Before submission, verify:

- [ ] Origin documented ("strange reason" captured)
- [ ] S-axis defined (constraint mechanism explicit - the HOW)
- [ ] R-axis defined (dynamics mechanism explicit - the WHAT)
- [ ] κ formula stated with LaTeX (domain-specific coupling ratio)
- [ ] L-Spark equation adapted to domain
- [ ] Predictions quantified (specific numbers with units and errors)
- [ ] Data cited (every claim has reference)
- [ ] Code provided (results reproducible)
- [ ] Charts generated (PNG at 300 DPI minimum)
- [ ] LaTeX formulas render correctly
- [ ] Falsification criteria explicit (what would disprove this?)
- [ ] Cross-domain links (connection to universal KDFA)
- [ ] Impact quantified (why does this matter?)

---

## CHART GENERATION SCRIPT

Save as `generate_kdfa_charts.py`:

```python
#!/usr/bin/env python3
"""
KDFA Standard Chart Generator
Creates publication-quality figures with LaTeX math
"""

import numpy as np
import matplotlib.pyplot as plt

# Enable LaTeX rendering
plt.rcParams.update({
    'font.size': 12,
    'font.family': 'serif',
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'text.usetex': False,  # Set True if LaTeX installed
    'axes.grid': True,
    'grid.alpha': 0.3
})

# See /home/claude/generate_kdfa_charts.py for full implementation
```

---

## VERSION HISTORY

- **v1.0** (2024-12-02): Initial standard with 8 sections
- **v2.0** (2024-12-02): Added LaTeX requirements, chart specifications, formula reference

---

*"The same mathematics governs stars and earthquakes, proteins and civilizations. Document it rigorously so others can verify."*

— KDFA Documentation Principle
