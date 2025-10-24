# Nonthanut (KK) Petchpichai

import sys

def normalize_line(line):
    """Remove leading/trailing spaces and collapse internal whitespace."""
    return " ".join(line.strip().split())

def compare_txt_files(file1, file2):
    with open(file1, 'r', encoding='utf-8', errors='ignore') as f1, \
         open(file2, 'r', encoding='utf-8', errors='ignore') as f2:
        # Normalize and filter out blank lines
        lines1 = [normalize_line(l) for l in f1 if l.strip()]
        lines2 = [normalize_line(l) for l in f2 if l.strip()]

    if lines1 == lines2:
        print(f"✅ The files '{file1}' and '{file2}' are identical (ignoring whitespace).")
    else:
        print(f"❌ The files '{file1}' and '{file2}' are NOT identical.")
        # Find the first line that differs
        min_len = min(len(lines1), len(lines2))
        for i in range(min_len):
            if lines1[i] != lines2[i]:
                print(f"Difference found at line {i+1}:")
                print(f"  {file1}: {lines1[i]}")
                print(f"  {file2}: {lines2[i]}")
                break
        if len(lines1) != len(lines2):
            print(f"Files have different lengths ({len(lines1)} vs {len(lines2)} lines).")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_txt_files.py <file1> <file2>")
        sys.exit(1)
    

    compare_txt_files(sys.argv[1], sys.argv[2])
