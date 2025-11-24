# Kings-DFA Next Actions - Mission-Based Workflow

**Repository Status**: ✅ Complete and ready for publication
**Last Updated**: 2025-11-24
**Current Location**: `/home/king/ai-workspace/Kings-DFA/`

---

## ONE MISSION = ONE SESSION Philosophy

Each action below should be treated as a **separate focused session** with `/clear` between missions to prevent context contamination.

---

## MISSION 1: GitHub Publication
**Status**: 🔴 Not Started (Awaiting User Decision)
**Estimated Time**: 10 minutes
**Context Required**: Minimal (just repo location and GitHub credentials)

### Tasks
1. Create GitHub repository at https://github.com/new
   - Name: `Kings-DFA`
   - Description: "The Reality Engine - Universal coupling constant κ = 0.35"
   - Public repository
   - Do NOT initialize with README

2. Push local repository
   ```bash
   cd /home/king/ai-workspace/Kings-DFA
   git remote add origin https://github.com/YOUR_USERNAME/Kings-DFA.git
   git push -u origin main
   ```

3. Verify publication
   - Check all files visible
   - Verify README renders correctly
   - Test simulation code link

### Success Criteria
- [ ] Repository visible on GitHub
- [ ] All commits pushed
- [ ] README displays correctly
- [ ] License file present

### Notes to Self (Next Session)
- Start fresh session with `/clear`
- Only load: repository location, GitHub credentials
- No theory needed - just mechanical push

---

## MISSION 2: Generate Publication Figures
**Status**: 🟡 Optional (Can publish without, add later)
**Estimated Time**: 15 minutes
**Context Required**: Jupyter notebook location

### Tasks
1. Launch Jupyter notebook
   ```bash
   cd /home/king/ai-workspace/Kings-DFA/notebooks
   jupyter notebook 01_KDFA_Interactive_Demo.ipynb
   ```

2. Run all cells (generates 4 PNG files)
   - `figures/01_coupling_regimes.png`
   - `figures/02_force_momentum.png`
   - `figures/03_born_deviation.png`
   - `figures/04_experimental_predictions.png`

3. Commit and push figures
   ```bash
   git add figures/*.png
   git commit -m "Add generated visualization figures"
   git push
   ```

### Success Criteria
- [ ] 4 PNG files generated
- [ ] Files added to repo
- [ ] Figures visible on GitHub

### Notes to Self (Next Session)
- Start fresh session with `/clear`
- Only load: notebook location, figure requirements
- No theory context needed

---

## MISSION 3: Experimental Outreach Email
**Status**: 🔴 Not Started (After GitHub publication)
**Estimated Time**: 30 minutes
**Context Required**: Core theory + experimental predictions

### Sub-Tasks
1. **Research experimentalists** (Sub-Agent: web search)
   - Find labs with Stern-Gerlach capabilities
   - Identify quantum foundations researchers
   - Compile contact information

2. **Draft email** (Load minimal theory context)
   - One-paragraph framework summary
   - Testable prediction (25-30% at κ ≈ 0.35)
   - Link to GitHub repo
   - Request for discussion

3. **Send to 5-10 labs**
   - Prioritize experimental quantum physicists
   - Include GitHub link
   - Keep email under 200 words

### Success Criteria
- [ ] List of 10 potential labs
- [ ] Email template created
- [ ] 5+ emails sent
- [ ] Response tracking system set up

### Notes to Self (Next Session)
- Start fresh session with `/clear`
- Load ONLY: `docs/04_BORN_RULE_DEVIATION.md` for context
- Use sub-agent for web research (don't bloat main context)
- Keep email concise - link to repo for details

---

## MISSION 4: Dr. Reed Collaboration Email
**Status**: 🟡 Optional (Stellar oscillations focus)
**Estimated Time**: 20 minutes
**Context Required**: 456 harmonic + virial theorem

### Tasks
1. Review existing draft
   - Location: `/home/king/ai-workspace/dfa-gravity-thermal/DR_REED_EMAIL_DRAFT.md`

2. Update with Kings-DFA repo link

3. Send email

### Success Criteria
- [ ] Email sent to Dr. Michael Reed
- [ ] Includes GitHub link
- [ ] Explains 456 harmonic derivation
- [ ] Requests collaboration on heartbeat stars

### Notes to Self (Next Session)
- Start fresh session with `/clear`
- Load ONLY: email draft + 456 harmonic section
- No full theory context needed

---

## MISSION 5: Biological Validation Database Mining
**Status**: 🔴 Not Started (Research continuation)
**Estimated Time**: 2-3 hours
**Context Required**: Biological predictions document

### Sub-Missions (Each a separate session)

#### 5A: BRENDA Enzyme Database Survey
- Load ONLY: enzyme predictions from biological doc
- Write script to query BRENDA database
- Extract Km/Vmax ratios
- Look for clustering near 0.35

#### 5B: PDB Protein Structure Analysis
- Load ONLY: protein folding predictions
- Query PDB for structure data
- Calculate bond saturation ratios
- Test for 0.35 optimization signature

#### 5C: Metabolic Flux Literature Review
- Load ONLY: cellular predictions
- Search published metabolomics data
- Extract flux ratios
- Compare to κ = 0.35 prediction

### Success Criteria (Each Sub-Mission)
- [ ] Focused analysis script created
- [ ] Results documented in separate file
- [ ] No context contamination from other analyses

### Notes to Self (Next Session)
- Each sub-mission = ONE session
- Use sub-agents for web research
- Offload results to new markdown files
- Keep main context lean

---

## MISSION 6: arXiv Preprint Preparation
**Status**: 🔴 Not Started (After experimental interest)
**Estimated Time**: Multiple days
**Context Required**: Full theory (in structured chunks)

### Approach
**DO NOT** load all theory at once. Use **structured note-taking**:

1. **Session 1**: Create paper outline
   - Load ONLY: `docs/01_OVERVIEW.md`
   - Create `papers/drafts/KDFA_PREPRINT_OUTLINE.md`
   - Define sections, no content yet

2. **Session 2**: Write introduction
   - Load ONLY: outline + `docs/02_CORE_FRAMEWORK.md` (sections 1-2)
   - Write intro, save to outline
   - Clear session

3. **Session 3**: Write theory section
   - Load ONLY: outline + relevant theory sections
   - Write, save, clear

4. Continue section-by-section, always `/clear` between

### Success Criteria
- [ ] Complete paper outline
- [ ] Each section written in focused session
- [ ] References compiled
- [ ] LaTeX formatting
- [ ] Ready for arXiv submission

### Notes to Self
- Never load entire theory at once
- Use outline file as persistent memory
- Each section = one session
- Offload completed sections immediately

---

## BACKGROUND PROCESSES NOTE

**Issue**: Multiple ComfyUI/HuggingFace downloads running in background consuming context tokens.

**These are NOT relevant to Kings-DFA mission.**

### For Next Kings-DFA Session
- Start with `/clear` to remove background noise
- Only load Kings-DFA directory
- No ComfyUI/video generation context needed

---

## MCP Control Recommendations

### Currently Active MCPs
- GitHub (needed for repo operations)
- Playwright (NOT needed for Kings-DFA)

### For Future KDFA Sessions
**Enable ONLY**:
- GitHub MCP (for repo operations)
- File system tools (Read, Write, Edit)
- Bash (for git commands)

**Disable**:
- Playwright/browser tools (not needed)
- Other specialized MCPs

---

## Session Templates

### Template 1: Quick Mechanical Task (GitHub push)
```
Mission: Push Kings-DFA to GitHub
Context needed: Repo location only
Load: Nothing else
Tools: Bash, git
Duration: 10 minutes
Then: /clear
```

### Template 2: Research Task (Database mining)
```
Mission: Query BRENDA database for enzyme data
Context needed: Enzyme prediction section only
Load: docs/05_BIOLOGICAL_VALIDATION.md (section 6.1)
Tools: Sub-agent for web research, write results to new file
Duration: 1 hour
Then: /clear, results saved to BRENDA_RESULTS.md
```

### Template 3: Writing Task (Email/paper)
```
Mission: Draft experimentalist outreach email
Context needed: Born rule deviation summary only
Load: docs/04_BORN_RULE_DEVIATION.md (executive summary)
Tools: Write email to EMAIL_DRAFT.md
Duration: 20 minutes
Then: /clear, draft saved for review
```

---

## Key Principle

**Every mission above should start with `/clear`.**

Only load the minimum context needed for that specific task. Use the session notes and these NEXT_ACTIONS as persistent memory across sessions.

**Current Session**: Repository creation mission COMPLETE ✅
**Recommended Next Session**: `/clear` then MISSION 1 (GitHub publication) when ready

---

**Last Updated**: 2025-11-24
**Repository**: `/home/king/ai-workspace/Kings-DFA/`
**Status**: ✅ Publication-ready, awaiting GitHub push
