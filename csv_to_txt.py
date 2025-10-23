import csv
import sys

def csv_to_txt(input_csv, output_txt):
    with open(input_csv, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    # Find where the actual table header starts
    start_index = next(i for i, line in enumerate(lines) if line.startswith('"Captured Picture"'))
    
    # Read only the table portion as a CSV
    data_lines = lines[start_index:]
    reader = csv.DictReader(data_lines)
    
    with open(output_txt, 'w', encoding='utf-8') as out:
        for row in reader:
            person_id = row['Last Name'].strip()
            time_str = row['Time'].strip()
            
            # Split date and time
            date, t = time_str.split(' ')
            date = date.replace('-', '')  # 2025-10-06 → 20251006
            
            # Write formatted line: ID + date + time
            out.write(f"{person_id:<12}{date} {t[:5]}\n")

    print(f"✅ Converted {input_csv} → {output_txt}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python csv_to_txt.py <input_csv> <output_txt>")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_txt = sys.argv[2]
    csv_to_txt(input_csv, output_txt)