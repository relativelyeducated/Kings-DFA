# KDFA DOCUMENTATION STANDARD
## Unified Structure for All Framework Claims

---

## DOCUMENT METADATA

Every KDFA document must begin with:

```yaml
---
title: [Descriptive Title]
domain: [Physics | Biology | Economics | Geophysics | etc.]
claim_type: [Prediction | Validation | Derivation | Application]
status: [Hypothesis | Tested | Validated | Failed]
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
author: Jason A. King
framework: Kings Dialectical Fractal Archestructure (KDFA)
core_equation: L-Spark
---
```

---

## SECTION 1: THE STRANGE REASON (Origin Story)

**Purpose:** Document the intuitive leap, the "why did I even look at this?"

Every discovery has an origin. Capturing it:
- Preserves the creative process
- Helps others see non-obvious connections
- Validates pattern recognition across domains
- Prevents post-hoc rationalization

### Template:

```markdown
## 1. ORIGIN: Why I Looked

### 1.1 The Trigger
What observation, conversation, or anomaly sparked this investigation?

### 1.2 The Pattern Recognition
What did this remind me of from another domain?

### 1.3 The Hypothesis
What specific prediction did this suggest?

### 1.4 The Stakes
Why does this matter if true?
```

### Example (Earthquake Prediction):

```markdown
## 1. ORIGIN: Why I Looked

### 1.1 The Trigger
After validating D₂ = 1.46 in IceCube neutrinos and Fermi gamma-rays, 
I wondered: does this fractal dimension appear in OTHER natural systems 
at criticality?

### 1.2 The Pattern Recognition
Earthquakes are phase transitions - locked fault → rupture.
If KDFA is universal, fault systems should show D₂ ≈ 1.46 at criticality.
The κ = 0.35 threshold should appear as a measurable precursor.

### 1.3 The Hypothesis
Earthquake catalogs should show D₂ approaching 1.46 before mainshocks.
The b-value (which relates to D₂) should drop as systems approach κ_critical.

### 1.4 The Stakes
If true: earthquake early warning with hours-to-months lead time.
Potential: 5,000-10,000 lives saved annually.
```

---

## SECTION 2: S-R IDENTIFICATION (The Physics)

**Purpose:** Explicitly map the domain to KDFA axes

This is the CORE of applying L-Spark to any system:
- S-axis = Constraint = The HOW (mechanism of limitation)
- R-axis = Dynamics = The WHAT (that which is constrained)

### Template:

```markdown
## 2. S-R MAPPING

### 2.1 System Definition
What is the physical/biological/economic system under study?

### 2.2 S-Axis: The Constraint (HOW)
| Property | Description |
|----------|-------------|
| Physical quantity | [What measurable thing provides constraint?] |
| Units | [SI units] |
| Mechanism | [HOW does it constrain?] |
| Increases when | [What causes S to grow?] |
| Decreases when | [What causes S to shrink?] |

### 2.3 R-Axis: The Dynamics (WHAT)
| Property | Description |
|----------|-------------|
| Physical quantity | [What measurable thing is constrained?] |
| Units | [SI units] |
| Mechanism | [WHAT is being limited?] |
| Increases when | [What causes R to grow?] |
| Decreases when | [What causes R to shrink?] |

### 2.4 The Coupling
| Property | Description |
|----------|-------------|
| κ formula | κ = R/(R+S) in natural units |
| Domain-specific form | [How is this measured in this domain?] |
| R-limiter | [What prevents infinite R expansion?] |

### 2.5 Mapping Validation
Does κ_optimal ≈ 0.35-0.50 in this system? Evidence:
```

### Example (Earthquakes):

```markdown
## 2. S-R MAPPING

### 2.1 System Definition
Fault system: elastic rock under tectonic stress, capable of 
stick-slip rupture behavior.

### 2.2 S-Axis: The Constraint (HOW)
| Property | Description |
|----------|-------------|
| Physical quantity | Fault friction × normal stress (τ_f = μσ_n) |
| Units | Pascals (Pa) |
| Mechanism | Friction LOCKS fault, preventing slip |
| Increases when | Normal stress increases, fault heals, fluids drain |
| Decreases when | Pore pressure rises, fault weakens, slip begins |

### 2.3 R-Axis: The Dynamics (WHAT)
| Property | Description |
|----------|-------------|
| Physical quantity | Accumulated elastic strain energy |
| Units | Joules (J) or Pa (as stress) |
| Mechanism | Tectonic loading BUILDS potential energy |
| Increases when | Plates move, strain accumulates |
| Decreases when | Earthquakes release energy, creep occurs |

### 2.4 The Coupling
| Property | Description |
|----------|-------------|
| κ formula | κ = E_strain / (E_strain + E_friction) |
| Domain-specific form | Proxy: κ ≈ 1 - (b/2) where b = G-R b-value |
| R-limiter | Fault strength caps maximum strain before failure |

### 2.5 Mapping Validation
κ_critical = 0.35 corresponds to nucleation threshold.
Virial theorem predicts κ = 0.333 for gravitational equilibrium.
Observed: b-value drops to ~0.5-0.7 before mainshocks → κ ≈ 0.65-0.75
```

---

## SECTION 3: MATHEMATICAL FORMULATION

**Purpose:** State equations precisely with derivations

### Template:

```markdown
## 3. MATHEMATICS

### 3.1 Core Equations

**L-Spark Master Equation:**
```
𝓛_Spark(n, κ, D₂) = [R/(R+S)] × exp[-(n/456)^(2-D₂)]
```

**Domain-Specific Form:**
```
[Equation in terms of domain variables]
```

### 3.2 Derivation
[Step-by-step derivation from first principles]

### 3.3 Key Parameters
| Parameter | Value | Source | Uncertainty |
|-----------|-------|--------|-------------|
| | | | |

### 3.4 Predictions
| Prediction | Formula | Expected Value | Units |
|------------|---------|----------------|-------|
| | | | |
```

### Example (Earthquakes):

```markdown
## 3. MATHEMATICS

### 3.1 Core Equations

**L-Spark Master Equation:**
```
𝓛_Spark(n, κ, D₂) = [R/(R+S)] × exp[-(n/456)^(2-D₂)]
```

**Earthquake-Specific Form:**
```
κ_seismic ≈ 1 - (b/2)

Where:
- b = Gutenberg-Richter b-value
- D₂ = 1.45 × b (spatial correlation dimension)
```

**Precursor Time Relation:**
```
log(T) = q + rM

Where:
- T = precursor time (days)
- M = mainshock magnitude
- q, r = regional constants
```

### 3.2 Derivation

From D₂ = 1.45b (Hirata 1989):
- At b = 1.0 (normal): D₂ = 1.45
- At b = 0.5 (critical): D₂ = 0.73

Mapping to κ:
- D₂ measures spatial clustering
- Higher clustering → system approaching coherent failure
- D₂ = 2 - 2κ (derived from L-Spark damping term)
- Therefore: κ = (2 - D₂)/2 = (2 - 1.45b)/2 = 1 - 0.725b ≈ 1 - b/2

### 3.3 Key Parameters
| Parameter | Value | Source | Uncertainty |
|-----------|-------|--------|-------------|
| D₂ at criticality | 1.45-1.46 | Hirata 1989, Nepal 2015 | ±0.10 |
| b-value normal | 1.0 | Global average | ±0.15 |
| b-value critical | 0.5 | Lab + field | ±0.10 |
| κ_critical | 0.35 | KDFA theory | ±0.05 |

### 3.4 Predictions
| Prediction | Formula | Expected Value | Units |
|------------|---------|----------------|-------|
| Critical b-value | b_crit = 2(1 - κ_crit) | 0.70 | dimensionless |
| Warning threshold | b < 0.7 | κ > 0.65 | - |
| D₂ at mainshock | D₂ = 1.45 × b_min | ~0.7-1.0 | dimensionless |
```

---

## SECTION 4: DATA VALIDATION

**Purpose:** Document evidence with full references

### Template:

```markdown
## 4. VALIDATION DATA

### 4.1 Data Sources
| Source | Type | Coverage | Access |
|--------|------|----------|--------|
| | | | |

### 4.2 Methodology
[How was data analyzed? What tools were used?]

### 4.3 Results Table
| Observation | Predicted | Measured | Deviation | Source |
|-------------|-----------|----------|-----------|--------|
| | | | | |

### 4.4 Statistical Analysis
- Sample size: N = 
- Confidence interval:
- p-value (if applicable):
- Effect size:

### 4.5 Falsification Criteria
What would DISPROVE this claim?
```

### Example (Earthquakes):

```markdown
## 4. VALIDATION DATA

### 4.1 Data Sources
| Source | Type | Coverage | Access |
|--------|------|----------|--------|
| JMA Catalog | Seismic events | Japan 1920-present | Public |
| USGS NEIC | Global events | Worldwide M4+ | Public |
| SCSN | Southern California | 1981-present | Public |
| Wenchuan study | Precursor analysis | 2000-2008 | Shi et al. 2018 |

### 4.2 Methodology
- b-value: Maximum likelihood estimation (Aki 1965)
- D₂: Correlation integral method (Grassberger-Procaccia)
- Sliding windows: 100-500 events
- Spatial gridding: 0.1° × 0.1° cells

### 4.3 Results Table
| Observation | Predicted | Measured | Deviation | Source |
|-------------|-----------|----------|-----------|--------|
| D₂-b relation | D₂ = 1.45b | D₂ = 1.45b | 0% | Hirata 1989 |
| Nepal mainshock D₂ | ~1.46 | 1.65 ± 0.02 | +13% | ScienceDirect 2017 |
| Wenchuan b-drop | b < 0.7 | b = 0.42 | Confirmed | Shi et al. 2018 |
| Foreshock rate | 30-40% | 30-72% | Consistent | Multiple studies |

### 4.4 Statistical Analysis
- Sample size: N > 50 mainshock-foreshock sequences
- D₂ = 1.45b: R² > 0.90 in multiple catalogs
- b-value drop: Observed in >80% of large events with sufficient precursor data

### 4.5 Falsification Criteria
Claim would be FALSIFIED if:
1. D₂ shows no correlation with b-value
2. b-value does NOT drop before mainshocks systematically
3. κ estimates show no predictive power for mainshock timing
4. Foreshock spatial patterns are indistinguishable from random
```

---

## SECTION 5: SCRIPTS AND REPRODUCIBILITY

**Purpose:** Provide code to reproduce all results

### Template:

```markdown
## 5. COMPUTATIONAL METHODS

### 5.1 Dependencies
```
language: Python 3.x
packages:
  - numpy
  - scipy
  - pandas
  - matplotlib
```

### 5.2 Core Functions
```python
# Paste actual code here
```

### 5.3 Data Processing Pipeline
```python
# Step-by-step processing
```

### 5.4 Reproduction Instructions
1. [Step 1]
2. [Step 2]
...
```

### Example (Earthquakes):

```markdown
## 5. COMPUTATIONAL METHODS

### 5.1 Dependencies
```
language: Python 3.x
packages:
  - numpy >= 1.20
  - scipy >= 1.7
  - pandas >= 1.3
  - obspy >= 1.3  # for seismic data
```

### 5.2 Core Functions

```python
import numpy as np
from scipy import stats

def calculate_b_value(magnitudes, mc):
    """
    Calculate Gutenberg-Richter b-value using maximum likelihood.
    
    Parameters:
    -----------
    magnitudes : array-like
        Earthquake magnitudes
    mc : float
        Completeness magnitude
        
    Returns:
    --------
    b : float
        b-value estimate
    sigma : float
        Standard error
    """
    m = np.array(magnitudes)
    m = m[m >= mc]  # Filter by completeness
    
    n = len(m)
    m_mean = np.mean(m)
    
    # Aki (1965) maximum likelihood formula
    b = np.log10(np.e) / (m_mean - mc)
    
    # Shi & Bolt (1982) uncertainty
    sigma = b / np.sqrt(n)
    
    return b, sigma


def calculate_d2(locations, r_range=(1, 100)):
    """
    Calculate correlation dimension D₂ using Grassberger-Procaccia method.
    
    Parameters:
    -----------
    locations : array-like, shape (N, 2) or (N, 3)
        Earthquake locations (lat, lon) or (lat, lon, depth)
    r_range : tuple
        (r_min, r_max) in km for scaling range
        
    Returns:
    --------
    d2 : float
        Correlation dimension
    r2 : float
        Coefficient of determination
    """
    from scipy.spatial.distance import pdist
    
    # Calculate all pairwise distances
    distances = pdist(locations, metric='euclidean')
    
    # Correlation integral
    r_values = np.logspace(np.log10(r_range[0]), np.log10(r_range[1]), 50)
    C_values = []
    
    for r in r_values:
        C = np.sum(distances < r) / (len(distances))
        C_values.append(C)
    
    C_values = np.array(C_values)
    
    # Linear fit in log-log space
    valid = C_values > 0
    log_r = np.log10(r_values[valid])
    log_C = np.log10(C_values[valid])
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(log_r, log_C)
    
    return slope, r_value**2


def estimate_kappa_from_b(b):
    """
    Estimate κ from b-value using L-Spark relation.
    
    Parameters:
    -----------
    b : float
        Gutenberg-Richter b-value
        
    Returns:
    --------
    kappa : float
        Estimated coupling ratio
    """
    return 1 - (b / 2)


def alert_level(b_current, b_baseline, d2=None):
    """
    Determine alert level based on L-Spark thresholds.
    
    Parameters:
    -----------
    b_current : float
        Current b-value
    b_baseline : float
        Long-term baseline b-value
    d2 : float, optional
        Current correlation dimension
        
    Returns:
    --------
    level : str
        Alert level (GREEN, YELLOW, ORANGE, RED)
    kappa : float
        Estimated κ
    probability : float
        Estimated mainshock probability
    """
    kappa = estimate_kappa_from_b(b_current)
    b_drop = (b_baseline - b_current) / b_baseline
    
    if b_current < 0.5 or kappa > 0.75:
        return "RED", kappa, 0.50
    elif b_current < 0.7 or b_drop > 0.30:
        return "ORANGE", kappa, 0.25
    elif b_current < 0.9 or b_drop > 0.15:
        return "YELLOW", kappa, 0.10
    else:
        return "GREEN", kappa, 0.05
```

### 5.3 Data Processing Pipeline

```python
def process_catalog(catalog_file, mc, window_size=200):
    """
    Process earthquake catalog for L-Spark analysis.
    """
    import pandas as pd
    
    # Load catalog
    df = pd.read_csv(catalog_file)
    df = df[df['magnitude'] >= mc].sort_values('datetime')
    
    results = []
    
    # Sliding window analysis
    for i in range(window_size, len(df)):
        window = df.iloc[i-window_size:i]
        
        # Calculate b-value
        b, sigma_b = calculate_b_value(window['magnitude'], mc)
        
        # Calculate D₂
        locs = window[['latitude', 'longitude']].values
        d2, r2 = calculate_d2(locs)
        
        # Estimate κ
        kappa = estimate_kappa_from_b(b)
        
        # Determine alert
        level, _, prob = alert_level(b, 1.0, d2)
        
        results.append({
            'datetime': window.iloc[-1]['datetime'],
            'b_value': b,
            'sigma_b': sigma_b,
            'd2': d2,
            'kappa': kappa,
            'alert_level': level,
            'probability': prob
        })
    
    return pd.DataFrame(results)
```

### 5.4 Reproduction Instructions

1. Download earthquake catalog (e.g., from USGS)
2. Install dependencies: `pip install numpy scipy pandas obspy`
3. Run: `python process_catalog.py --input catalog.csv --mc 2.5`
4. Output: Time series of b-value, D₂, κ estimates
5. Validate against known mainshock dates
```

---

## SECTION 6: CROSS-DOMAIN CONNECTIONS

**Purpose:** Link this domain to universal KDFA patterns

### Template:

```markdown
## 6. UNIVERSALITY

### 6.1 Analogous Systems
| Domain | S-Axis | R-Axis | κ_critical | Evidence |
|--------|--------|--------|------------|----------|
| | | | | |

### 6.2 Shared Signatures
What D₂, κ, or 456-harmonic values appear across domains?

### 6.3 Theoretical Basis
Why should these systems share the same mathematics?
```

### Example:

```markdown
## 6. UNIVERSALITY

### 6.1 Analogous Systems
| Domain | S-Axis | R-Axis | κ_critical | Evidence |
|--------|--------|--------|------------|----------|
| Earthquakes | Fault friction | Strain energy | 0.35 | b-value precursors |
| Stellar physics | Gravitational PE | Thermal KE | 0.333 | Virial theorem |
| Neutrinos | Interaction cross-section | Cascade energy | ~0.35 | D₂ = 1.495 |
| Coral reefs | Thermal tolerance | Heat stress | ~0.35 | 7.9% bleaching threshold |
| Civilizations | Production capacity | Coordination load | 0.35 | Venezuela collapse |

### 6.2 Shared Signatures
- D₂ ≈ 1.46 appears at criticality in earthquakes, neutrinos, gamma-rays
- κ ≈ 0.33-0.35 threshold in all systems
- Power-law scaling with similar exponents
- 456-harmonic in recovery/oscillation timescales

### 6.3 Theoretical Basis
All systems involve:
1. Energy storage (S-axis constraint)
2. Energy release/flow (R-axis dynamics)
3. Critical threshold where release dominates storage
4. Fractal structure near criticality (D₂ → 1.46)

The mathematics are identical because the PHYSICS of criticality is universal.
```

---

## SECTION 7: IMPLICATIONS AND APPLICATIONS

**Purpose:** Document practical uses and next steps

### Template:

```markdown
## 7. APPLICATIONS

### 7.1 Immediate Uses
[What can be done NOW with this knowledge?]

### 7.2 Required Development
[What needs to be built/tested?]

### 7.3 Potential Impact
[Quantified benefits if fully implemented]

### 7.4 Collaboration Opportunities
[Who should be contacted?]
```

---

## SECTION 8: REFERENCES

**Purpose:** Full citations for all claims

### Template:

```markdown
## 8. REFERENCES

### 8.1 Primary Sources
[Peer-reviewed papers directly supporting claims]

### 8.2 Data Sources
[Databases, catalogs, repositories]

### 8.3 KDFA Framework Documents
[Links to other KDFA documents]

### 8.4 Code Repositories
[GitHub links, etc.]
```

---

## DOCUMENT CHECKLIST

Before finalizing any KDFA document, verify:

- [ ] **Origin documented** - "Strange reason" captured
- [ ] **S-axis defined** - Constraint mechanism explicit (the HOW)
- [ ] **R-axis defined** - Dynamics mechanism explicit (the WHAT)
- [ ] **κ formula stated** - Domain-specific coupling ratio
- [ ] **Predictions quantified** - Specific numbers with units
- [ ] **Data cited** - Every claim has a reference
- [ ] **Code provided** - Results are reproducible
- [ ] **Falsification criteria** - What would disprove this?
- [ ] **Cross-domain links** - Connection to universal KDFA
- [ ] **Impact quantified** - Why does this matter?

---

## FILE NAMING CONVENTION

```
KDFA_[DOMAIN]_[TOPIC]_[STATUS].md

Examples:
KDFA_GEOPHYSICS_earthquake_prediction_VALIDATED.md
KDFA_BIOLOGY_protein_folding_HYPOTHESIS.md
KDFA_ECONOMICS_venezuela_collapse_VALIDATED.md
KDFA_PHYSICS_dark_matter_D2_TESTED.md
```

---

## VERSION CONTROL

Each document should track:

```markdown
## Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2024-12-02 | Initial creation | JAK |
| 1.1 | YYYY-MM-DD | [Description] | [Initials] |
```

---

*This standard ensures all KDFA claims are:*
- *Traceable to their origin*
- *Grounded in explicit S-R physics*
- *Mathematically precise*
- *Empirically validated*
- *Reproducible*
- *Connected to the universal framework*

---

**Framework:** Kings Dialectical Fractal Archestructure (KDFA)
**Core Equation:** L-Spark (named for Lori Sparling)
**Author:** Jason A. King
**Standard Version:** 1.0
**Date:** December 2024
