import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def read_csv(name):
    with (ROOT / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

obs = read_csv("OBSERVATION_MATRIX.csv")
recheck = read_csv("CURRENT_RECHECK.csv")
cross_t001 = read_csv("CROSSWALK_INDEX_T001.csv")
cross_t027 = read_csv("CROSSWALK_INDEX_T027.csv")
results = json.loads((ROOT / "RESULTS.json").read_text(encoding="utf-8"))

ranks = [int(r["observed_rank"]) for r in obs]
names = [r["person"] for r in obs]

assert ranks == list(range(1, 11)), ranks
assert len(names) == len(set(names)) == 10
assert len(recheck) == 10
assert [x["person"] for x in results["observedRanking"]] == names
assert [int(x["rank"]) for x in results["observedRanking"]] == ranks
assert sum(1 for r in cross_t001 if r["in_index_t001"] == "да") == 1
assert sum(1 for r in cross_t027 if r["in_chatgpt_july_snapshot"] == "да") == 1
assert results["overlapWithIndexT001"]["count"] == 1
assert results["overlapWithChatGPTJulySnapshot"]["count"] == 1
assert results["isOfficialYandexRanking"] is False
assert results["isCurrentAliceRanking"] is False

print("PASS: historical Alice snapshot is internally consistent")
