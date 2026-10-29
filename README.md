# On a Primorial-Based Sequence and Its Prime-Generating Properties

This repository contains the experimental script used to perform the computational evaluation described in the research note "*On a Primorial-Based Sequence and Its Primality Properties up to n = 1000*" [doi:10.5281/zenodo.23584249](https://doi.org/10.5281/zenodo.23584249).

The implementation is designed for deterministic exploration in number theory, leveraging high-precision arithmetic to handle large-scale primorial growth, gap analysis, and persistent local database storage.

## Requirements

- Python 3
- `gmpy2` (Multiple-precision arithmetic)
- `sympy` (Prime factorization)
- `sqlite3` (Included with Python standard library)

Install dependencies with:

```bash
pip install gmpy2==2.2.2 sympy==1.13.1
```

## Script Overview

### `research_primorials.py`

Performs the sequential generation of primorial numbers ($P_n = p_n\#$), locates the first and second consecutive primes ($q_1$ and $q_2$), computes the displacement $r_n = q_2 - P_n$, verifies its primality deterministically, factorizes the resulting term if composite, and exports everything into a local SQLite database (`primorial_research.db`) in real time.

#### Key Features
- **Incremental Resuming:** Automatically queries the database for the last computed index $n$ and resumes execution seamlessly without recalculating previous terms.
- **Real-Time Persistence:** Performs an immediate database `commit` on each iteration, ensuring data safety against power outages or interruptions and enabling live inspection.
- **Optimized Performance:** Filters primality with `gmpy2` before invoking factorization to handle thousands of digits efficiently.

#### Usage

Run the script directly using Python:

```bash
python research_primorials.py
```

> [!NOTE]
> **Precomputed Results Notice:** Running the script to generate results for the range **n = 1 to 1000** takes approximately **5 hours** of compute time on consumer hardware and populates the SQLite database (`primorial_research.db`). 
> 
> If you prefer to inspect or analyze the data directly without re-running the full computation, the precomputed database is available for download on Zenodo:
> [Download Precomputed Database on Zenodo](https://doi.org/10.5281/zenodo.23583908)

#### Parameters

- `target_max_n`: Sets the upper bound target for the primorial index $n$ (default in main is `1000`, scalable).

#### Database Schema (`primorials` table)

| Column | Type | Description |
| :--- | :--- | :--- |
| `n` | INTEGER | Index of the primorial (Primary Key) |
| `p_n` | TEXT | The $n$-th prime number ($p_n$) |
| `primorial` | TEXT | The primorial value $p_n\#$ |
| `q1` | TEXT | The first prime greater than $p_n\#$ |
| `q2` | TEXT | The second prime greater than $p_n\#$ |
| `r` | TEXT | The displacement $r = q_2 - p_n\#$ |
| `is_r_prime` | INTEGER | Indicator flag (1 if $r$ is prime, 0 if composite) |
| `factor_r` | TEXT | Prime factorization string of $r$ |

## Citation

If you use this code or data in your research, please cite:

Juan Camilo Hernández-Torres (2026). “On a Primorial-Based Sequence and Its Prime-Generating Properties up to n = 1000”. Zenodo. [doi:10.5281/zenodo.23583908](https://doi.org/10.5281/zenodo.23583908).