# On a Primorial-Based Sequence and Its Prime-Generating Properties

This repository contains the experimental script used to perform the computational evaluation described in the research note "*On a Primorial-Based Sequence and Its Prime-Generating Properties up to n = 1000*" [doi:10.5281/zenodo.23584250](https://doi.org/10.5281/zenodo.23584250).

The implementation is designed for deterministic exploration in number theory, leveraging high-precision arithmetic to handle large-scale primorial growth and gap analysis.

## Requirements

* Python 3
* `gmpy2` (Multiple-precision arithmetic)
* `sympy` (Prime factorization)

Install dependencies with:

pip install gmpy2 sympy

## Script Overview

### `research_primorials.py`

Performs the sequential generation of primorial numbers (P_n = p_n#), locates the subsequent consecutive primes (q_1 and q_2), computes the displacement r_n = q_2 - P_n, factorizes the resulting term, and exports a formatted log.

#### Usage

Run the script directly using Python:

python research_primorials.py

#### Parameters

* `max_n`: Sets the upper bound for the primorial index n (default is `15`, scalable up to `1000`).
* `output_file`: Defines the destination text file for the generated sequence data (default is `results.txt`).

#### Output Format

Example row format:
n =  6 | p_n = 13     | p_n# = 30030                    | q = 30059                   | r = 29               | Fact(r) = 29

## Citation

If you use this code or data in your research, please cite:

Juan Camilo Hernández-Torres (2026). “On a Primorial-Based Sequence and Its Prime-Generating Properties up to n = 1000”. Zenodo. [doi:10.5281/zenodo.23583908](https://doi.org/10.5281/zenodo.23583908).
