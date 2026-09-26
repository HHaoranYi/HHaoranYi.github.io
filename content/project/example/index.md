---
title: AI Model Deployment and Performance Acceleration on ARM-based System
summary: Streamlined a pre-trained model for efficient deployment on Raspberry Pi development boards. Enhanced multi-core performance to accelerate model inference, leveraging the capabilities of the Raspberry Pi’s hardware for efficient AI computation.
# tags:
#   - Deep Learning
date: '2023-04-01'

# Optional external URL for project (replaces project detail page).
external_link: ''

# Slides (optional).
slides: ''
---

## Overview

Streamlined a pre-trained deep learning model for efficient deployment on ARM-based embedded development boards (Raspberry Pi). Enhanced multi-core workload distribution to accelerate model inference, leveraging the hardware capabilities for low-power edge AI computation.

## Motivation

Deploying modern deep neural networks directly on resource-constrained edge platforms presents significant memory and latency challenges. This project aimed to explore practical optimizations for running real-time inference without dedicated neural accelerators.

## My Contribution & Implementation

- Profiling inference latency bottlenecks across multi-core ARM CPU architectures.
- Implementing thread-level parallelism and lightweight runtime tuning on Linux/Raspberry Pi.
- Evaluating latency, throughput, and power efficiency under varying workloads.

