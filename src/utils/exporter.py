import csv
import os
def export_to_csv(ranked_results,output_path="results/match_results.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path,mode='w', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Resume","Job","Score"])
        for resume,matches in ranked_results.items():
            for job,score in matches:
                writer.writerow([resume,job,score])
