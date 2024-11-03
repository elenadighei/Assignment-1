def find_gc_content(dna):
    g_count = dna.count('G')
    c_count = dna.count('C')
    total_length = len(dna)
    gc_content = (g_count + c_count) / total_length * 100
    return gc_content

def parse_fasta(fasta_strings):
    fasta_data = {}
    current_id = ""
    current_sequence = ""

    for line in fasta_strings:
        line = line.strip()
        if line.startswith(">"):
            if current_id: 
                fasta_data[current_id] = current_sequence
            current_id = line[1:]  
            current_sequence = ""
        else:
            current_sequence += line  

    if current_id:  
        fasta_data[current_id] = current_sequence

    return fasta_data

def find_highest_gc_content(fasta_strings):
    fasta_data = parse_fasta(fasta_strings)
    max_gc_content = 0
    max_id = ""

    for dna_id, dna_sequence in fasta_data.items():
        gc_content = find_gc_content(dna_sequence)
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_id = dna_id

    return max_id, max_gc_content


if __name__ == "__main__":
    fasta_file_path = '/home/elenadg04/PoC2/rosalind_gc (2).txt'
    with open(fasta_file_path, 'r') as f:
        fasta_strings = f.readlines()

    

result_id, result_gc_content = find_highest_gc_content(fasta_strings)
print(f"{result_id}\n{result_gc_content:.6f}")
