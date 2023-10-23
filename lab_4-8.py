# Author: caleb moura

# Prompt user for  6-letter DNA sequence
dna_sequence = input("Enter a 6-letter DNA sequence (a,c,t,g): ")

# Create dictionary to store complementary bases
complementary_bases = {'a': 't', 'c': 'g', 't': 'a', 'g': 'c'}

# Generate complementary DNA sequence
complementary_dna_sequence = ''.join(complementary_bases[base] for base in dna_sequence)

# Printing complementary DNA sequence
print(f'Complementary DNA sequence: {complementary_dna_sequence}')