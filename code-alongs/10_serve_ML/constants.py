from pathlib import Path

MODEL_PATH =Path(__file__).parent / "models" 
DATA_PATH =Path(__file__).parents[2] / "data"

print(MODEL_PATH)
print(DATA_PATH)