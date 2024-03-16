import argparse
from Bio import SeqIO

def split_fasta(fasta_file, window_size, step_size):
    """Split a FASTA file into smaller windows and combine corresponding windows."""
    seq_records = list(SeqIO.parse(fasta_file, "fasta"))
    seq_length = len(seq_records[0].seq)

    for start in range(0, seq_length, step_size):
        end = min(start + window_size, seq_length)
        window_seqs = [seq_record.seq[start:end] for seq_record in seq_records]

        with open(f"{start}_{end}.fasta", "w") as output_file:
            for seq_record, window_seq in zip(seq_records, window_seqs):
                output_file.write(f">{seq_record.id}\n{window_seq}\n")

def main():
    parser = argparse.ArgumentParser(description="Split a FASTA file into smaller windows.")
    parser.add_argument('-i', '--infile', required=True, help="Input FASTA file")
    parser.add_argument('-l', '--window_size', type=int, required=True, help="Size of each window")
    parser.add_argument('-s', '--step_size', type=int, required=True, help="Step size for sliding window")
    
    args = parser.parse_args()

    split_fasta(args.infile, args.window_size, args.step_size)

if __name__ == "__main__":
    main()
