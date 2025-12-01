# Validation Protocol: Blind Spot Search & Deviation Handling

## Objective
To systematically identify data that *does not* fit the predicted geometric or theoretical models ("Blind Spots") and determine whether this represents a falsification or a **misapplication of the theory**.

## 1. Definition of a Blind Spot
A "Blind Spot" is defined as a dataset or system that:
1.  **Deviates significantly** (>3\(\sigma\)) from the predicted Power Law or Geometric Node.
2.  **Does not fit** the standard Null Hypothesis (randomness/normal distribution) either.
3.  appears to be "invisible" or "outlier" data in standard analyses.

## 2. Search Methodology
For every claim validation (Vesica, Biology, etc.), we will:
1.  **Residual Analysis**: Plot the residuals of the best-fit model. Look for systematic structure in the errors.
2.  **Outlier Mapping**: Identify specific systems that fall outside the prediction interval.
3.  **Constraint Check**: Verify if the *assumed* active constraint (S) is actually the *dominant* constraint for that specific system.

## 3. The "Misapplication Check" (CRITICAL)
**IF** a system fails the prediction, we do **NOT** immediately mark the claim as falsified.
**INSTEAD**, we trigger a **User Review** to check for **Misapplied Theory**:

### Procedure:
1.  **Pause Validation**: Stop processing that specific dataset.
2.  **Compile Deviation Report**:
    - What is the system?
    - What was the predicted value?
    - What is the actual value?
    - What is the active constraint we *assumed*?
3.  **Notify User**: "Validation failed for [System]. Deviation: [Details]. Is this a misapplication of the theory (e.g., wrong scale, wrong active constraint)?"

## 4. Classification of Results
- **Type A: Validated**: Data fits prediction.
- **Type B: Misapplication**: Data failed initially, but fits after User corrects the theoretical application (e.g., "That system is R-dominant, not S-dominant").
- **Type C: True Anomaly**: Data consistently fails even after theoretical correction. This is a **Discovery** (new physics/biology).
