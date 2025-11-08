# DSC180A-Quarter1Report-Checkpoint
_______

<br>

## Project Information
**Name:** Longhao Lin  
**Mentor:** Alex Warstadt  
**Section:** A10 - Baby Language Models

---

## Overview
This repository contains replication work for DSC180A (Weeks 1-6), focusing on reproducing papers from the BabyLM Challenge. The primary goals were:
1. Replicating the GPT-BERT model from the 2024 BabyLM Challenge
2. Conducting hyperparameter sweeps using Weights & Biases for the CLIMB curriculum learning approach

---

## Repository Structure
```
├── Training_script/          # Training configuration files (.yaml)
├── Evaluation_Result_GPT-BERT/  # Model evaluation results (.txt)
├── GPT-BERT/                 # GPT-BERT implementation and eval_results
├── SweepReport/              # Hyperparameter sweep analysis (PDF)
└── CLIMB-CurriculumLearning/ # Curriculum learning experiments
```

---

## Project Components

### 1. GPT-BERT Replication
The first paper assigned for replication was **GPT-BERT** from the 2024 BabyLM Challenge. 
- **Training scripts:** `/Training_script/`
- **Evaluation results:** `/Evaluation_Result_GPT-BERT/` or `/GPT-BERT/eval_results/`

### 2. CLIMB Hyperparameter Sweep
Hyperparameter sweep using weights & biases for the CLIMB (Curriculum Learning) paper.
- **Training scripts:** `/Training_script/`
- **Analysis report:** `/SweepReport/` (PDF format)

---

## Notes
Since this project focuses on replication and learning from existing submissions, most code in this repository comes from the original repo. 

---

## References and Credits
This repository contains code from the following repo:

- **GPT-BERT:** [Official implementation of "GPT or BERT: why not both?"](https://github.com/ltgoslo/gpt-bert)
- **CLIMB:** [Curriculum Learning for Baby Language Models](https://huggingface.co/ltg/gpt-bert-babylm-base)

This repo mainly used resource from above repo for replication and learning purpose.
