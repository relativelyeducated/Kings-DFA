# KDFA Core Rules

## File Naming Convention
- Format: `{topic}_{stage}.md`
- Stages:
  - `claim`: Initial extraction of a claim.
  - `search`: Search results and raw data.
  - `evidence`: Compiled evidence from search.
  - `test`: Test protocols and execution logs.
  - `result`: Final result of the validation.
  - `validated`: Successfully validated claim (with data).
  - `pending`: Claim awaiting further validation.

## Constants & Thresholds
- **κ (Kappa) Threshold**: `0.35` (Survival Floor, NOT optimum).
- **Threshold Zone**: `[0.33, 0.38]`
  - Derived from: Virial (1/3 ≈ 0.333), 1/e (≈ 0.368), Golden Ratio (≈ 0.382).
- **Upper Bound**: `0.65` (THEORETICAL - always flag as unvalidated).

## Validation Categories
- **Validated**: Claims supported by empirical data (e.g., PDB structures, IceCube data).
- **Proposed**: Claims that are theoretically consistent but lack direct empirical verification.
- **Theoretical**: Speculative claims or those in domains without hard measurements (e.g., Social Science).
