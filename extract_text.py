import json
from collections import defaultdict
from pathlib import Path

input_file = "gutenberg-poetry-v001.ndjson"
output_path = Path("data.txt")

poem_lines = defaultdict(list)

# Group by poem (gid)
with open(input_file, "r", encoding="utf-8") as file:
    for line in file:
        try:
            data = json.loads(line)
            gid = data.get("gid")
            text = data.get("s")
            if gid and text:
                poem_lines[gid].append(text.strip())
        except json.JSONDecodeError:
            continue

# Format poems
poems = ["\n".join(lines) for lines in poem_lines.values()]
content = "\n\n".join(poems)

# ✅ Write using pathlib (bypasses open()/write())
output_path.write_text(content, encoding="utf-8")

print(f"✅ data.txt created with {len(poems)} poems")
