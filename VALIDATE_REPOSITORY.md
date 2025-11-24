# Repository Validation Instructions for Claude

**Purpose**: Automated validation of Kings-DFA repository completeness
**Usage**: Load this file and execute validation checks outside main context
**Status**: To be run after system restart, before GitHub publication

---

## Instructions for Claude Agent

You are a validation agent. Your job is to verify the Kings-DFA repository is complete and ready for publication.

**Working Directory**: `/home/king/ai-workspace/Kings-DFA/`

---

## Validation Checklist

### 1. File Existence Check

Verify these files exist:
```bash
# Core files
README.md
LICENSE
CITATION.cff

# Documentation (8 theory documents)
docs/01_OVERVIEW.md
docs/02_CORE_FRAMEWORK.md
docs/03_MOMENTUM_FORMULATION.md
docs/04_BORN_RULE_DEVIATION.md
docs/05_BIOLOGICAL_VALIDATION.md
docs/06_SIMULATION_ANALYSIS.md
docs/07_BIOLOGICAL_TEST_LIST.md
docs/08_LITERATURE_STATUS.md

# Code
simulations/born_rule/test_born_deviation.py
simulations/born_rule/requirements.txt
simulations/born_rule/README.md

# Notebook
notebooks/01_KDFA_Interactive_Demo.ipynb

# Planning documents
ARCHOS_INTEGRATION_PLAN.md
BREAKTHROUGH_TIMELINE.md
PUBLICATION_READY.md
NEXT_ACTIONS.md
QUICKSTART_NEXT_SESSION.md

# Session notes
SESSION_2025-11-24_KDFA_PUBLICATION_READY.md
```

**Action**: Use Read or Glob tool to check each file exists.

### 2. Content Validation

For each theory document, verify it contains:
- **01_OVERVIEW.md**: Framework introduction, κ definition
- **02_CORE_FRAMEWORK.md**: Complete theory (~33KB, should be largest)
- **03_MOMENTUM_FORMULATION.md**: Force=S, Momentum=R explanation (~18KB)
- **04_BORN_RULE_DEVIATION.md**: Experimental predictions, Stern-Gerlach protocol
- **05_BIOLOGICAL_VALIDATION.md**: Life as thermal vs gravity
- **06_SIMULATION_ANALYSIS.md**: Bug fix documentation
- **07_BIOLOGICAL_TEST_LIST.md**: Specific experimental protocols
- **08_LITERATURE_STATUS.md**: Supporting evidence review

**Action**: Read first 50 lines of each file, verify content matches description.

### 3. Key Equations Check

Search for these critical equations in docs/02_CORE_FRAMEWORK.md:
- `κ = T/(T+|U|)`
- `2T + U = 0` (virial theorem)
- `κ = 1/3 = 0.333`
- `456 = (4/3) × 0.342 × 1000`

**Action**: Use Grep tool to find equations.

### 4. Code Validation

Check simulations/born_rule/test_born_deviation.py contains:
- `create_coherent_state()` function
- Calculation of Born rule probability
- Calculation of KDFA probability
- Deviation percentage output
- Should print approximately "24.97%" or "25%"

**Action**: Read the Python file, verify functions exist.

### 5. Git Repository Check

Verify git status:
```bash
cd /home/king/ai-workspace/Kings-DFA
git status
git log --oneline | head -10
```

Expected:
- On branch `main`
- Possibly untracked files (ARCHOS_INTEGRATION_PLAN.md, etc.)
- At least 6 commits

**Action**: Use Bash tool to check git status.

### 6. Size and Line Count Validation

Expected totals:
- Repository size: ~750KB
- Total lines in docs/*.md: ~4,000 lines
- Total files: 20+

**Action**:
```bash
du -sh /home/king/ai-workspace/Kings-DFA
wc -l docs/*.md | tail -1
find . -type f | wc -l
```

### 7. Critical Content Spot Checks

Verify these key findings appear somewhere in documentation:

**In theory docs:**
- [x] "Virial theorem: κ = 0.333" (should be within 4.9% of 0.35)
- [x] "Cosmological: ∛0.04 = 0.342" (within 2.3% of 0.35)
- [x] "Born rule deviation: 24.97%" or "25-30%"
- [x] "S-axis = Gravity" (literal, not metaphor)
- [x] "R-axis = Thermal" (literal, not metaphor)
- [x] "Life is R-axis fighting S-axis"

**Action**: Use Grep tool to search for key phrases across docs/.

### 8. Cross-Reference Validation

Verify README.md mentions:
- κ = 0.35 as the key number
- Connection to ARCHOS-DFA repository
- Link to simulation code
- Citation information
- License (CC-BY-4.0)

**Action**: Read README.md, verify sections present.

### 9. License and Citation Check

Verify:
- LICENSE file contains "CC BY 4.0" or "Creative Commons Attribution"
- CITATION.cff contains:
  - Author: Jason A. King
  - Email: relativelyeducated@gmail.com
  - Title contains "Kings DFA"
  - Year: 2025

**Action**: Read LICENSE and CITATION.cff files.

### 10. Integration Plan Validation

Verify ARCHOS_INTEGRATION_PLAN.md contains:
- 9 missions listed
- Agent-based approach mentioned
- Context protection strategy
- Domain reanalyses (neutrino, stellar, biology, cosmology, quantum)

**Action**: Read ARCHOS_INTEGRATION_PLAN.md, check structure.

---

## Validation Output Format

After completing all checks, provide a report in this format:

```markdown
# Kings-DFA Repository Validation Report

**Date**: [current date]
**Validator**: Claude Agent
**Status**: [PASS/FAIL/WARNINGS]

## File Existence: [PASS/FAIL]
- Core files: [count]/3
- Theory docs: [count]/8
- Code files: [count]/3
- Planning docs: [count]/5

## Content Validation: [PASS/FAIL]
- All theory docs contain expected content: [YES/NO]
- Key equations found: [count]/4
- Code functions present: [YES/NO]

## Git Status: [PASS/FAIL]
- On main branch: [YES/NO]
- Commit count: [number]
- Untracked files: [list or NONE]

## Size Validation: [PASS/FAIL]
- Repository size: [actual] (expected ~750KB)
- Total doc lines: [actual] (expected ~4,000)
- Total files: [actual] (expected 20+)

## Critical Content: [PASS/FAIL]
- Virial theorem: [FOUND/MISSING]
- Cosmological constant: [FOUND/MISSING]
- Born rule deviation: [FOUND/MISSING]
- S=Gravity, R=Thermal: [FOUND/MISSING]
- Life interpretation: [FOUND/MISSING]

## Cross-References: [PASS/FAIL]
- README complete: [YES/NO]
- LICENSE correct: [YES/NO]
- CITATION.cff valid: [YES/NO]
- ARCHOS connection documented: [YES/NO]

## Issues Found:
[List any problems, or "None"]

## Recommendations:
[Actions needed before publication, or "Ready to publish"]

---

**Overall Status**: [READY FOR PUBLICATION / NEEDS FIXES]
```

---

## Usage Instructions for User

**After system restart:**

1. Start fresh Claude session with `/clear`

2. Tell Claude:
   ```
   Please read and execute /home/king/ai-workspace/Kings-DFA/VALIDATE_REPOSITORY.md

   Perform all validation checks and provide the report.
   ```

3. Claude will:
   - Load this file
   - Run all validation checks outside main context
   - Provide comprehensive validation report
   - Tell you if anything is missing

4. If validation passes:
   - Proceed with git commit
   - Create GitHub repository
   - Push to public

5. If validation fails:
   - Fix identified issues
   - Re-run validation
   - Then proceed with publication

---

## Expected Validation Time

- File checks: ~2 minutes
- Content checks: ~3 minutes
- Grep searches: ~1 minute
- Report generation: ~1 minute

**Total**: ~7 minutes for complete validation

---

## Why This Works

**Context Protection**:
- Agent loads ONLY this instruction file
- Performs checks using tools (Read, Grep, Bash)
- Doesn't need to load full theory into context
- Reports findings concisely

**Confidence**:
- Systematic verification of all components
- Catches missing files before publication
- Validates key content exists
- Confirms git state ready for push

**Efficiency**:
- Single command to validate everything
- No manual checking needed
- Reproducible verification
- Fast turnaround

---

## Troubleshooting

### If Validation Fails on File Existence:
- Check you're in correct directory: `/home/king/ai-workspace/Kings-DFA/`
- Verify files weren't accidentally deleted
- Check git status to see what's tracked

### If Validation Fails on Content:
- File might be incomplete
- Check file size matches expectations
- Read the file manually to verify

### If Validation Fails on Git:
- Might need to commit untracked files
- Check branch name (should be `main`)
- Verify git initialized properly

### If Bash Tool Fails:
- Bash context might be corrupted (restart needed)
- Try individual commands manually
- Use Read tool as fallback for file checks

---

## Post-Validation Actions

### If PASS:
1. Commit any untracked files
2. Create GitHub repository
3. Push to origin
4. Verify on GitHub web UI

### If WARNINGS:
1. Review warnings
2. Fix if critical
3. Re-validate
4. Proceed if acceptable

### If FAIL:
1. Fix issues listed in report
2. Re-run validation
3. Don't publish until PASS

---

**Validation Protocol Complete**

This file provides everything needed for automated repository verification before publication.

**Next File to Load**: QUICKSTART_NEXT_SESSION.md (for publication steps)
