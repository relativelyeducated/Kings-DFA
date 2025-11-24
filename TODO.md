# Kings-DFA Task Tracker

**Last Updated**: 2025-11-24
**Current Focus**: Get website live with pictures/graphs

---

## 🚨 NEXT SESSION: Do These Steps

### Step 1: Make Repo Private (if not already)
1. Go to: https://github.com/relativelyeducated/Kings-DFA
2. Click **Settings** (top right)
3. Scroll to bottom → **Danger Zone**
4. Click **Change visibility** → Select **Private**
5. Confirm

### Step 2: Merge the Branch to Main
1. Go to: https://github.com/relativelyeducated/Kings-DFA/pulls
2. You should see a PR for `claude/code-review-...`
3. Click it → Click **Merge pull request** → **Confirm merge**
4. This puts all the new stuff (SVG graphics, TODO, index.html) onto main

### Step 3: Enable GitHub Pages
1. Go to: https://github.com/relativelyeducated/Kings-DFA/settings/pages
2. Under **Source**: Select **Deploy from a branch**
3. Under **Branch**: Select **main** and folder **/docs**
4. Click **Save**
5. Wait 1-2 minutes
6. Your site will be at: `https://relativelyeducated.github.io/Kings-DFA/`

### Step 4: Generate the Graphs (Optional - makes notebook show plots)
Run this in terminal or Google Colab:
```bash
cd Kings-DFA/notebooks
pip install qutip matplotlib numpy scipy
jupyter notebook 01_KDFA_Interactive_Demo.ipynb
```
Then: Run all cells → PNGs save to `figures/` → commit & push them

**OR** just use Google Colab:
1. Go to: https://colab.research.google.com
2. File → Open → GitHub tab
3. Paste: `https://github.com/relativelyeducated/Kings-DFA`
4. Open the notebook
5. Add cell at top: `!pip install qutip`
6. Run all cells - graphs appear!

---

## Active Work

| Priority | Task | Status | Notes |
|----------|------|--------|-------|
| P1 | Merge PR to main | 🔴 Not Started | Gets SVG graphics onto main branch |
| P1 | Enable GitHub Pages | 🔴 Not Started | Settings → Pages → main /docs |
| P1 | Import ARCHOS docs 10-15 | 🔴 Not Started | Human science, religious texts, consciousness |
| P1 | Clean up planning/ folder | 🔴 Not Started | Remove from public, keep locally |
| P1 | Remove emojis from docs | 🔴 Not Started | Make academic-ready |
| P2 | Reorganize docs by domain | 🔴 Not Started | See structure below |
| P2 | Generate notebook graphs | 🔴 Not Started | Run notebook in Colab or locally |

---

## Missing Docs to Import from ARCHOS-DFA

| Doc | File | Size | Content |
|-----|------|------|---------|
| 10 | 10_SOCIAL_SYSTEMS.md | 31KB | Civilizational κ, Rome/Maya collapse |
| 11 | 11_NEUTRINO_PHYSICS.md | 37KB | Neutrino cascades, D₂ validation |
| 12 | 12_STELLAR_OSCILLATIONS.md | 32KB | Reed et al., 456 harmonic |
| 13 | 13_ANCIENT_DATA_PATTERNS.md | 63KB | Religious texts, Jubilee cycles, 456 in Bible/Quran |
| 14 | 14_CONSCIOUSNESS_PHYSICS.md | 37KB | κ > 0.45 consciousness, AI analysis |
| 15 | 15_FERTILITY_HEALTH_COLLAPSE.md | 25KB | Fertility crisis, generational decay |

**Total missing: ~225KB of human science content**

---

## Proposed Doc Organization (by domain)

```
docs/
├── index.html                    ← Website landing page
├── overview.md                   ← Start here
│
├── theory/
│   ├── core-framework.md         ← κ = T/(T+|U|)
│   └── momentum-formulation.md   ← S=Gravity, R=Thermal
│
├── quantum/
│   ├── born-rule-deviation.md
│   └── stern-gerlach.md
│
├── biology/
│   ├── validation.md
│   └── test-protocols.md
│
├── physics/
│   ├── neutrino-cascades.md      ← from ARCHOS 11
│   └── stellar-oscillations.md   ← from ARCHOS 12
│
├── civilization/
│   ├── social-systems.md         ← from ARCHOS 10
│   └── fertility-collapse.md     ← from ARCHOS 15
│
├── consciousness/
│   └── consciousness-physics.md  ← from ARCHOS 14
│
├── wisdom/
│   └── ancient-patterns.md       ← from ARCHOS 13 (Bible, Quran, 456)
│
└── meta/
    ├── literature-status.md
    └── simulation-analysis.md
```

---

## Breakthroughs Being Applied

### Breakthrough 1: S/R Physical Identification
- **Date Discovered**: 2025-11-24
- **Core Insight**: S = GRAVITY (least action, constraint) | R = THERMODYNAMICS (entropy, relations)
- **Key Claim**: Life = Thermal fighting Gravity. All living systems are R-axis pushing against S-axis collapse.
- **Mathematical Form**:
  - S-axis: Gravity, Force, Potential Energy, Least Action Principle
  - R-axis: Thermal, Momentum, Kinetic Energy, Entropy Maximization
- **Documents to Update**: MATHEMATICS.md, docs/02_CORE_FRAMEWORK.md, docs/03_MOMENTUM_FORMULATION.md
- **Status**: 🟡 In Progress

### Breakthrough 2: [Name]
- **Date Discovered**:
- **Core Insight**:
- **Documents to Update**:
- **Status**: 🔴 Not Started

---

## Completed

| Date | Task | Result |
|------|------|--------|
| 2025-11-24 | Repository creation | ✅ Complete framework documented |
| 2025-11-24 | Born rule simulation | ✅ 24.97% deviation validated |
| 2025-11-24 | Force=S, Momentum=R | ✅ Derived κ = 1/3 from virial theorem |
| 2025-11-24 | SVG visualizations | ✅ Created 4 diagrams in index.html |
| 2025-11-24 | GitHub Pages setup | ✅ docs/index.html ready |

---

## What's Already Done

✅ **index.html has SVG graphics** - no Python needed, they just work:
- κ coupling scale (gradient bar)
- S-R axis diagram (Gravity vs Thermal circles)
- Phase space ellipse
- Born rule deviation chart

✅ **MathJax equations** - render beautifully

✅ **Notebook embedded** - via nbviewer iframe

**Once you merge the PR and enable Pages, the site will be live with all the visuals.**

---

## Priority Legend
- **P1**: Critical - do this now
- **P2**: Important - do this soon
- **P3**: Nice to have - when time permits

## Status Legend
- 🔴 Not Started
- 🟡 In Progress
- 🟢 Complete
- ⏸️ Blocked
