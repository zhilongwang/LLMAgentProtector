import json
import glob 


good_separators = []
files = glob.glob('results/round_statistic_*')
for file_path in files:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)  

        for sample in data:

            if int(sample["attack_success_rate"].split('.')[0]) / 100 <= 0.2:
                good_separators.append(sample["separator"])

print(good_separators)
print(len(good_separators))