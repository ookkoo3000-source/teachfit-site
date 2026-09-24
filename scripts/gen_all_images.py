import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import concise_data, gen_image
ROOT = gen_image.ROOT
NAMES = {"gunsan-jungdeung-suhak-gwaoe": "군산 중학생", "gunsan-chodeung-suhak-gwaoe": "군산 초등학생"}
for slug, d in concise_data.D.items():
    out = os.path.join(ROOT, "blog", "img", slug + ".webp")
    if os.path.exists(out):
        continue
    name = NAMES.get(slug, d["who"])
    for attempt in range(3):
        try:
            gen_image.generate(name, slug)
            break
        except Exception as e:
            print("retry", slug, str(e)[:120]); time.sleep(8)
    time.sleep(2)
print("ALL DONE")
