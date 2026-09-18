# Ultraviolet flavor information in T-violating neutrino oscillations

Reproducibility repository for:

**P. Kar, B. S. Koranga, and V. Nautiyal, “Ultraviolet flavor information in T-violating neutrino oscillations: seesaw matching, sterile mixing, and Planck-suppressed corrections.”**

This repository contains the JPhys G submission materials, figure-generation code, benchmark data, and a transparent reference implementation of the neutrino-oscillation calculations described in the manuscript.

## Contents

- `figs/` — manuscript figures and generated reproductions.
- `scripts/` — deterministic figure-generation scripts.
- `data/` — machine-readable benchmark/plot data.
- `src/` — compact neutrino-oscillation utilities.
- `requirements.txt` — Python dependencies.
- `.github/workflows/reproduce.yml` — GitHub Actions workflow that regenerates the figures.

## Reproduction

Python 3.10+ is recommended.

```bash
pip install -r requirements.txt
python scripts/reproduce_all.py
```

The generated figures are written to `figs/generated/`.

A GitHub Actions workflow also regenerates the figures automatically on pushes to `main` and can be run manually from the Actions tab.

The plotting scripts are deliberately deterministic. The current repository reconstructs the published figure panels from the benchmark values and curves documented in the manuscript. It does **not** claim bit-for-bit identity with an unreleased original numerical implementation; where the manuscript gives only a plotted curve or benchmark range rather than the underlying raw array, the repository stores the corresponding reconstruction explicitly in `data/`.

## Numerical model

`src/neutrino_uv.py` contains:

- PMNS and 3+1 mixing-matrix construction;
- Type-I seesaw/Casas–Ibarra reconstruction;
- Weinberg-operator flavor basis;
- matter Hamiltonian construction;
- exact matrix-exponential propagation;
- first-order perturbative propagation;
- T and CP asymmetry evaluation.

The implementation follows the conventions and equations in the manuscript and is intended as a transparent reference implementation rather than a replacement for a full GLoBES likelihood analysis.

## Manuscript benchmark

The main benchmark uses:

- `M_R = (0.1, 0.3, 1) × 10^13 GeV`;
- normal ordering;
- NuFIT 6.0 best-fit low-energy inputs;
- `L = 1300 km`;
- `E = 2.5 GeV`;
- sterile benchmark `(theta14, theta24, theta34) = (0.15, 0.10, 0.05)`;
- `epsilon = 1`;
- adaptive-RK accuracy target `1e-11` in the manuscript calculation.

## Citation

Please cite the associated manuscript when using these materials. A persistent repository DOI should be added after the GitHub repository is connected to Zenodo.
