from bs4 import BeautifulSoup

html = open("Problems - Codeforces.html").read()
soup = BeautifulSoup(html, "html.parser")


samples = soup.select(".sample-test")

for i, s in enumerate(samples):
    open(f"in{i+1}.txt","w").write(
        s.select_one(".input pre").get_text("\n",strip=True)
    )
    open(f"out{i+1}.txt","w").write(
        s.select_one(".output pre").get_text("\n",strip=True)
    )

