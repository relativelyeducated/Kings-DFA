# LaTeX Math Formatting Guide for Kings-DFA

**How to write beautiful mathematical equations in Markdown**

---

## Quick Reference

### Inline Math (in text)
Use single dollar signs: `$\kappa = 0.35$` → $\kappa = 0.35$

### Display Math (centered, separate line)
Use double dollar signs:
```
$$\kappa = \frac{T}{T + |U|}$$
```

---

## Common KDFA Equations (Copy-Paste Ready)

### 1. The Coupling Constant
```latex
$$\kappa = \frac{R}{S + R} = \frac{T}{T + |U|}$$
```
$$\kappa = \frac{R}{S + R} = \frac{T}{T + |U|}$$

### 2. Virial Theorem
```latex
$$2T + U = 0 \quad \Rightarrow \quad \kappa = \frac{1}{3} = 0.333$$
```
$$2T + U = 0 \quad \Rightarrow \quad \kappa = \frac{1}{3} = 0.333$$

### 3. Optimal Stern-Gerlach Gradient
```latex
$$\left(\frac{\partial B_z}{\partial z}\right)_{\text{optimal}} = \frac{m v^2}{2L \mu_B} = 0.491 \text{ T/m}$$
```
$$\left(\frac{\partial B_z}{\partial z}\right)_{\text{optimal}} = \frac{m v^2}{2L \mu_B} = 0.491 \text{ T/m}$$

### 4. Born Rule Modification
```latex
$$P_{\text{KDFA}}(\text{state}) = |\psi|^2 \times \left(1 + \alpha \frac{C}{H}\right)$$
```
$$P_{\text{KDFA}}(\text{state}) = |\psi|^2 \times \left(1 + \alpha \frac{C}{H}\right)$$

Where:
```latex
$$\alpha = 0.35, \quad C = \text{R-axis coherence}, \quad H = \text{S-axis entropy}$$
```

### 5. The 456 Harmonic
```latex
$$456 = \frac{4}{3} \times 0.342 \times 1000 = \gamma_{\text{adiabatic}} \times \kappa_{\text{cosmological}} \times N$$
```
$$456 = \frac{4}{3} \times 0.342 \times 1000 = \gamma_{\text{adiabatic}} \times \kappa_{\text{cosmological}} \times N$$

### 6. Cosmological Constant
```latex
$$\kappa_{\text{cosmological}} = \sqrt[3]{\Omega_\Lambda} = \sqrt[3]{0.04} = 0.342$$
```
$$\kappa_{\text{cosmological}} = \sqrt[3]{\Omega_\Lambda} = \sqrt[3]{0.04} = 0.342$$

### 7. Force-Momentum Dialectic
```latex
$$F = \frac{dp}{dt} \quad \Rightarrow \quad S\text{-axis} = \frac{d(R\text{-axis})}{dt}$$
```
$$F = \frac{dp}{dt} \quad \Rightarrow \quad S\text{-axis} = \frac{d(R\text{-axis})}{dt}$$

### 8. Relational Forcing (Stern-Gerlach)
```latex
$$R = \mu_B \left|\frac{\partial B_z}{\partial z}\right|$$
```
$$R = \mu_B \left|\frac{\partial B_z}{\partial z}\right|$$

### 9. Structural Binding (Stern-Gerlach)
```latex
$$S = \frac{mv^2}{2L}$$
```
$$S = \frac{mv^2}{2L}$$

### 10. Condition for Optimal Measurement
```latex
$$R = S \quad \Rightarrow \quad \kappa = 0.50 \quad \text{(hydrostatic equilibrium)}$$
```
$$R = S \quad \Rightarrow \quad \kappa = 0.50 \quad \text{(hydrostatic equilibrium)}$$

---

## Greek Letters

| Symbol | LaTeX | Example |
|--------|-------|---------|
| κ (kappa) | `\kappa` | $\kappa = 0.35$ |
| α (alpha) | `\alpha` | $\alpha = 0.35$ |
| β (beta) | `\beta` | $\beta = \sqrt{1-p}$ |
| γ (gamma) | `\gamma` | $\gamma = 4/3$ |
| μ (mu) | `\mu` | $\mu_B$ |
| Ω (Omega) | `\Omega` | $\Omega_\Lambda$ |
| ψ (psi) | `\psi` | $|\psi\rangle$ |
| Λ (Lambda) | `\Lambda` | $\Lambda$ |

---

## Special Symbols

| Symbol | LaTeX | Example |
|--------|-------|---------|
| Partial derivative | `\partial` | $\frac{\partial B}{\partial z}$ |
| Infinity | `\infty` | $\lim_{x \to \infty}$ |
| Plus-minus | `\pm` | $0.35 \pm 0.05$ |
| Approximately | `\approx` | $\kappa \approx 0.35$ |
| Much less than | `\ll` | $\kappa \ll 1$ |
| Much greater than | `\gg` | $R \gg S$ |
| Right arrow | `\Rightarrow` or `\rightarrow` | $A \Rightarrow B$ |
| Proportional to | `\propto` | $F \propto r^{-2}$ |

---

## Fractions

**Simple:** `\frac{numerator}{denominator}`
```latex
$$\kappa = \frac{T}{T + |U|}$$
```

**Continued fraction:**
```latex
$$\kappa = \frac{1}{1 + \frac{|U|}{T}}$$
```

---

## Subscripts and Superscripts

**Subscript:** `x_i` → $x_i$
**Superscript:** `x^2` → $x^2$
**Both:** `x_i^2` → $x_i^2$

**Multiple characters (use braces):**
```latex
$\mu_B$ vs $\mu_{Bohr}$
$E_k$ vs $E_{kinetic}$
```

---

## Brackets and Parentheses

**Auto-sizing:** Use `\left` and `\right`
```latex
$$\left(\frac{\partial B}{\partial z}\right)_{\text{optimal}}$$
```

**Types:**
- `( )` - Regular parentheses
- `[ ]` - Square brackets
- `\{ \}` - Curly braces (need backslash!)
- `\langle \rangle` - Angle brackets: $\langle\psi|$
- `| |` - Absolute value/determinant

---

## Matrices and Systems

**Matrix:**
```latex
$$\rho = \begin{pmatrix}
\rho_{11} & \rho_{12} \\
\rho_{21} & \rho_{22}
\end{pmatrix}$$
```

**System of equations:**
```latex
$$\begin{cases}
2T + U = 0 \\
\kappa = \frac{T}{T + |U|}
\end{cases}$$
```

---

## Text in Math Mode

Use `\text{...}` for words:
```latex
$$\kappa_{\text{optimal}} = 0.50 \quad \text{(not } \kappa_{optimal} \text{)}$$
```

---

## Common Functions

| Function | LaTeX | Renders As |
|----------|-------|------------|
| Square root | `\sqrt{x}` | $\sqrt{x}$ |
| Nth root | `\sqrt[3]{x}` | $\sqrt[3]{x}$ |
| Exponential | `e^{x}` or `\exp(x)` | $e^{x}$ or $\exp(x)$ |
| Logarithm | `\log(x)` or `\ln(x)` | $\log(x)$ or $\ln(x)$ |
| Sine/Cosine | `\sin(x)` | $\sin(x)$ |
| Summation | `\sum_{i=1}^{n} x_i` | $\sum_{i=1}^{n} x_i$ |
| Integral | `\int_0^\infty f(x) dx` | $\int_0^\infty f(x) dx$ |

---

## Quantum Notation

**Ket:** `|state\rangle` → $|state\rangle$
**Bra:** `\langle state|` → $\langle state|$
**Braket:** `\langle \psi|\phi\rangle` → $\langle \psi|\phi\rangle$

**Spin states:**
```latex
$$|\psi\rangle = \alpha|\uparrow\rangle + \beta|\downarrow\rangle$$
```

Or use arrows directly: `\uparrow` and `\downarrow`

---

## Alignment (Multi-line Equations)

Use `\begin{align}` for aligned equations:
```latex
\begin{align}
\kappa &= \frac{R}{S+R} \\
&= \frac{T}{T+|U|} \\
&= \frac{1}{3} \quad \text{(virial)}
\end{align}
```

---

## Before/After Examples

### Before (Plain Text):
```
kappa = T/(T+|U|) = 1/3 = 0.333
```

### After (LaTeX):
```latex
$$\kappa = \frac{T}{T+|U|} = \frac{1}{3} = 0.333$$
```

### Before:
```
(dB/dz)_optimal = (m*v^2)/(2*L*mu_B)
```

### After:
```latex
$$\left(\frac{\partial B_z}{\partial z}\right)_{\text{optimal}} = \frac{m v^2}{2L \mu_B}$$
```

---

## Inline vs Display

**Inline** (in sentences): Use single `$...$`
> The coupling constant $\kappa = 0.35$ determines the regime.

**Display** (standalone): Use double `$$...$$`
$$\kappa = \frac{T}{T+|U|} = 0.35$$

---

## Common Mistakes

❌ **Wrong:** `kappa = T/(T+|U|)`
✅ **Right:** `$\kappa = \frac{T}{T+|U|}$`

❌ **Wrong:** `{x}` (renders braces)
✅ **Right:** `\{x\}` (LaTeX braces)

❌ **Wrong:** `sqrt(x)`
✅ **Right:** `\sqrt{x}`

❌ **Wrong:** `|dB/dz|`
✅ **Right:** `\left|\frac{\partial B}{\partial z}\right|`

---

## Conversion Checklist

When converting documents, replace:

- [ ] `kappa` → `\kappa`
- [ ] `alpha` → `\alpha`
- [ ] `/` (division) → `\frac{num}{den}`
- [ ] `^` (exponent) → keep but use `{}` for multi-char
- [ ] `sqrt()` → `\sqrt{}`
- [ ] `|x|` → `|x|` (this one's fine)
- [ ] Plain text "optimal" → `\text{optimal}`
- [ ] `(dX/dx)` → `\left(\frac{dX}{dx}\right)`

---

## GitHub Markdown Support

GitHub supports LaTeX via:
- **Inline:** `$...$`
- **Display:** `$$...$$`

**Works in:**
- README.md
- All .md files
- Issue comments
- Pull request comments

**Note:** May take a moment to render on first load.

---

## Examples from Kings-DFA

### Example 1: Core Definition
```markdown
The universal coupling constant is defined as:

$$\kappa = \frac{R}{S + R} = \frac{T}{T + |U|}$$

where $T$ is kinetic energy and $U$ is potential energy.
```

### Example 2: Deviation Calculation
```markdown
The Born rule deviation at critical coupling:

$$\Delta = \frac{P_{\text{KDFA}} - P_{\text{Born}}}{P_{\text{Born}}} = \frac{0.7498 - 0.6000}{0.6000} = 0.2497 = 24.97\%$$
```

### Example 3: Gradient Formula
```markdown
For an electron beam with velocity $v$ and interaction length $L$:

$$\left(\frac{\partial B_z}{\partial z}\right)_{\text{optimal}} = \frac{m_e v^2}{2L \mu_B}$$

With standard values ($m_e = 9.109 \times 10^{-31}$ kg, $v = 1000$ m/s, $L = 0.1$ m), we obtain:

$$\left(\frac{\partial B_z}{\partial z}\right)_{\text{optimal}} \approx 0.491 \text{ T/m}$$
```

---

## Quick Tips

1. **Preview as you write** - Use a Markdown previewer
2. **Start simple** - Convert basic equations first
3. **Copy templates** - Reuse equation structures
4. **Test on GitHub** - Push and check rendering
5. **Use `\text{...}`** - For any English words in equations
6. **Spaces matter** - `$x = 5$` not `$x=5$` for readability

---

## Tools

**Online LaTeX Editors:**
- [LaTeX Equation Editor](https://www.codecogs.com/latex/eqneditor.php)
- [Overleaf](https://www.overleaf.com/)

**Cheat Sheets:**
- [Overleaf LaTeX Symbols](https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols)

---

**Ready to make the math beautiful!** 🎨📐
