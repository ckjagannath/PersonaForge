import glob
import json

modern_files = sorted(glob.glob("./data/*_modern.snt.aligned"))
original_files = sorted(glob.glob("./data/*_original.snt.aligned"))

data = []

for mfile, ofile in zip(modern_files, original_files):
    with open(mfile, "r", encoding="utf-8") as fm, open(ofile, "r", encoding="utf-8") as fo:
        modern_lines = fm.readlines()
        original_lines = fo.readlines()
        for m, o in zip(modern_lines, original_lines):
            m = m.strip()
            o = o.strip()
            if m and o:
                data.append({
                    "instruction": "Rewrite the text in Shakespearean style.",
                    "input": m,
                    "output": o
                })

with open("shakespeare.jsonl", "w", encoding="utf-8") as f:
    for item in data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"Saved {len(data)} data samples to shakespeare.jsonl")
