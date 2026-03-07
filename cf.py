from bs4 import BeautifulSoup
import re
from collections import defaultdict

html = open("Problems - Codeforces.html", encoding="utf8").read()
soup = BeautifulSoup(html, "html.parser")

problems = soup.select(".problemindexholder")
smooth = True

for prob in problems:
    idx = prob.get("problemindex")

    if not idx:
        print("ERROR: problem without index")
        continue

    sample = prob.select_one(".sample-test")
    if not sample:
        print(f"ERROR: problem {idx} has no sample tests")
        continue

    # ---------- INPUT ----------
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

    full_input = "\n".join(sum([inputs[i] for i in sorted(inputs)], []))



    # ---------- OUTPUT ----------
    out_pre = sample.select_one(".output pre")
    if not out_pre:
        print(f"ERROR: problem {idx} missing output sample")
        continue

    output = out_pre.get_text("\n", strip=True)



    # ---------- WRITE FILES ----------
    try:
        with open(f"in{idx}.txt", "w") as f:
            f.write(full_input + "\n")

        with open(f"out{idx}.txt", "w") as f:
            f.write(output + "\n")
    except Exception as e:
        smooth = False
        print(f"ERROR: writing files for problem {idx}: {e}")

if smooth:
    print("Ready to go")