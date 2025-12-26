import os
import json


def load_config():
    cfg = {
        "TIMEOUT_PROB": float(os.getenv("TIMEOUT_PROB", 0.1)),
        "EXCEPTION_PROB": float(os.getenv("EXCEPTION_PROB", 0.2)),
        "SLOWDOWN_PROB": float(os.getenv("SLOWDOWN_PROB", 0.3)),
        "SLOWDOWN_SECONDS": float(os.getenv("SLOWDOWN_SECONDS", 1.5)),
        "SEED": int(os.getenv("SEED", 123)),
    }

    if os.path.exists("config.json"):
        try:
            with open("config.json", "r") as f:
                file_cfg = json.load(f)
                cfg.update({
                    "TIMEOUT_PROB": file_cfg.get("timeout_prob", cfg["TIMEOUT_PROB"]),
                    "EXCEPTION_PROB": file_cfg.get("exception_prob", cfg["EXCEPTION_PROB"]),
                    "SLOWDOWN_PROB": file_cfg.get("slowdown_prob", cfg["SLOWDOWN_PROB"]),
                    "SLOWDOWN_SECONDS": file_cfg.get("slowdown_seconds", cfg["SLOWDOWN_SECONDS"]),
                    "SEED": file_cfg.get("seed", cfg["SEED"]),
                })
        except Exception:
            pass

    return cfg
