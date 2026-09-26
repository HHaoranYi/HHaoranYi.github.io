---
title: "Analog Compute-in-Memory: Scaling Limits and Architectural Tradeoffs"
summary: "An engineering perspective on the precision, noise margins, ADC power overheads, and design compromises in analog compute-in-memory architectures."
date: 2026-09-26
params:
  kind: "technical"
draft: true
toc: true
math: true
tags:
  - Compute-in-Memory
  - Analog IC
  - AI Hardware
---

## Introduction

Compute-in-Memory (CIM) paradigms promise to bypass the traditional von Neumann memory bottleneck by performing multiply-accumulate (MAC) operations directly inside memory arrays. While analog CIM achieves impressive peak energy efficiency numbers in TOPS/W, scaling to high-precision matrix multiplications reveals fundamental circuit and system tradeoffs.

## The ADC Bottleneck

In analog CIM, row activations drive bitlines, where Kirchoff's current law or charge-sharing performs summation:

$$I_{BL} = \sum_{i} V_{WL,i} \cdot G_{cell,i}$$

However, converting this analog result back into digital values requires Analog-to-Digital Converters (ADCs). The energy and silicon area of ADCs scale exponentially with resolution:

$$\text{Energy}_{\text{ADC}} \propto 2^B$$

where $B$ is the bit precision. For activations and weights exceeding 4-to-8 bits, ADC power often dominates the entire macro dissipation.

## Key Design Takeaways

1. **Precision vs. Noise Margin**: Process, Voltage, and Temperature (PVT) variations severely degrade analog resolution unless aggressive calibration is applied.
2. **Hybrid Approaches**: Digital CIM and mixed-precision architectures offer more predictable SNR and better scalability for modern deep learning models.
