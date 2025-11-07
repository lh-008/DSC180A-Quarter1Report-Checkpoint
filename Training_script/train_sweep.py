#!/usr/bin/env python
import os
import sys
import subprocess
import wandb

os.environ["WANDB_ENTITY"] = "lemn-lab"
os.environ["WANDB_MODE"] = "online"

def main():
    if wandb.run is None:
        wandb.init(entity="lemn-lab", project="climb-perplexity-sweep")
    
    print(f"Running sweep for wandb run: {wandb.run.name}")
    print(f"Entity: {wandb.run.entity}, Project: {wandb.run.project}")
    
    sweep_config = dict(wandb.config)
    
    hydra_overrides = []
    
    for key, value in sweep_config.items():
        if key.startswith('_'):
            continue

        if isinstance(value, dict):
            for subkey, subvalue in value.items():
                hydra_overrides.append(f"{key}.{subkey}={subvalue}")
        else:
            hydra_overrides.append(f"{key}={value}")
    
    hydra_overrides.append(f"experiment.name={wandb.run.name}")
    cmd = [sys.executable, "train.py"] + hydra_overrides
    
    print(f"\n{'='*60}")
    print("Running training with the following Hydra overrides:")
    print(f"{'='*60}")
    for override in hydra_overrides:
        print(f"  {override}")
    print(f"{'='*60}\n")
    
    result = subprocess.run(cmd, env=os.environ.copy())
    
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
