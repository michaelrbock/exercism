DNA_TO_RNA = {
  'G': 'C',
  'C': 'G',
  'T': 'A',
  'A': 'U'
}


def to_rna(dna_strand):
  rna = []
  for nuc in dna_strand:
    rna.append(DNA_TO_RNA[nuc])
  return ''.join(rna)
