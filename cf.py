from bs4 import BeautifulSoup
import re
from collections import defaultdict
import os

def load_config(path="config.txt"):
    config = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            k, v = line.split("=", 1)

            if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
                v = v[1:-1]
            config[k.strip()] = v.strip()
    return config

script_dir = os.path.dirname(os.path.abspath(__file__))
cfg = load_config(os.path.join(script_dir, "config.txt"))

html_path = cfg.get("HTML_PATH", "Problems - Codeforces.html")
template_path = cfg.get("TEMPLATE_PATH", "template.cpp")
output_dir = cfg.get("OUTPUT_DIR", ".")
mode = cfg.get("MODE")

if mode == "MULTIFILE":
    print("Mode: MULTIFILE")
else:
    print("Mode: SINGLEFILE")
print("Generating test cases.")

html = open(html_path, encoding="utf8").read()
soup = BeautifulSoup(html, "html.parser")

problems = soup.select(".problemindexholder")
smooth = True
template = open(template_path).read()

inputspath = "ins_outs"

os.makedirs(inputspath, exist_ok=True)

for prob in problems:
    idx = prob.get("problemindex")

    if not idx:
        print("ERROR: problem without index")
        continue

    if mode == "MULTIFILE":
        open(os.path.join(output_dir, f"{idx}.cpp"), "w").write(template)

    sample = prob.select_one(".sample-test")
    if not sample:
        print(f"ERROR: problem {idx} has no sample tests")
        continue

    inputs = defaultdict(list)

    for line in sample.select(".input .test-example-line"):
        text = line.get_text(strip=True)

        case = None
        for c in line["class"]:
            m = re.match(r"test-example-line-(\d+)", c)
            if m:
                case = int(m.group(1))

        if case is None:
            print(f"ERROR: problem {idx} malformed input line")
            continue

        inputs[case].append(text)

    if not inputs:
        print(f"ERROR: problem {idx} input parsing failed")
        continue

    full_input = "\n".join(
        line for i in sorted(inputs) for line in inputs[i]
    )

    out_pre = sample.select_one(".output pre")
    if not out_pre:
        print(f"ERROR: problem {idx} missing output sample")
        continue

    output = out_pre.get_text("\n", strip=True)

    try:
        with open(os.path.join(inputspath, f"in{idx}.txt"), "w") as f:
            f.write(full_input + "\n")

        with open(os.path.join(inputspath, f"out{idx}.txt"), "w") as f:
            f.write(output + "\n")

    except Exception as e:
        smooth = False
        print(f"ERROR: writing files for problem {idx}: {e}")

if smooth:
    print("Ready to go")