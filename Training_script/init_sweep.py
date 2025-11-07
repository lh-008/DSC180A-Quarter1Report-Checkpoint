# init_sweep.py
import wandb
import yaml

with open('perplexity_sweep.yaml', 'r') as f:
    sweep_config = yaml.safe_load(f)

sweep_id = wandb.sweep(
    sweep_config, 
    project="climb-perplexity-sweep",
    entity="lemn-lab"
)

print(f"\nSweep ID: {sweep_id}")
print(f"https://wandb.ai/lemn-lab/climb-perplexity-sweep/sweeps/{sweep_id}")
