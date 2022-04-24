"""
Name: Nicholas Loehrke and Dylan Brodie

Course: CS1430, Section 02, Spring 2022

Assignment: Assignment 04

Purpose:    Your program should work with the two given input files.
            Reads in DNA data from a file and outputs to another file.
            Determines whether or not each piece of DNA is a protein.
Input:      The DNA input data consists of line pairs.  The first line has the
            name of the nucleotide sequence, and the second is the nucleotide
            sequence itself.  Each character in a sequence of nucleotides will
            be A, C, G, T, or a dash character, "-".
            The nucleotides in the input can be either upper or lowercase.

            Your program begins with an introduction and prompts for input and
            output file names.
            * You may assume the user will type the name of an
            existing input file that is in the proper format.
            * You may assume that the input file exists, is readable, and
            contains valid input.  (In other words, you should not re-prompt
            for input or output file names.)
            * You may assume that each sequence's number of nucleotides
            without dashes) will be a multiple of 3, although the nucleotides
            on a line might be in either uppercase or lowercase or a
            combination.
            * Your program reads the input file to process its nucleotide
            sequences and outputs the results into the given output file.

Output:     The nucleotide sequence is output in uppercase, and that the
            nucleotide counts and mass percentages are shown in A, C, G, T order.
            A given codon such as GAT might occur more than once in the same
            sequence.
            Your program should overwrite any existing data in the output file.
Notes:      Thanks to Allison Obourn for the idea for this program.
"""
#########################
# IMPORTS
#########################
import os.path

#########################
# CONSTANTS
#########################
_MASSES = [135.128, 111.103, 151.128, 125.107]
_JUNK_MASS = 100.0
_TENTHS_PRECISION = 10.0
_NUM_NUCLEOTIDES = 4   # number of nucleotides (A,C,G,T)
_CODON_LENGTH = 3   # number of nucleotides per codon
_MINIMUM_LENGTH = 5   # shortest length for valid protein
_CG_PERCENTAGE = 30   # min % C/G for a valid protein


def main():
    """
    Reads in DNA data from a file and outputs to another file
    and decides whether or not each piece of DNA is a protein.
    :return: None
    """
    print("This program reports information about DNA")      # intro
    print("nucleotide sequences that may encode proteins.")
        
    # prompt for file names
    in_file = input("Enter the Input file name: ")

    if not os.path.exists(in_file):
        print(in_file + " does not exist!")

    else:
        out_file = input("Enter the Output file name: ")
        with open(out_file, "w") as out_file:

            with open(in_file) as in_file:
                lines = in_file.readlines()
                for i in range(0, len(lines), 2):
                    region_name = lines[i]
                    nucleotides = lines[i + 1].upper()
                    counts = get_counts(nucleotides)
                    junk_count = get_dashes(nucleotides)
                    total_mass = get_total_mass(counts, junk_count)
                    codons_list = get_codons(nucleotides)
                    percentages = get_percentages(counts, total_mass)

                    report_results(region_name, nucleotides, counts, total_mass,
                                   percentages, codons_list, out_file)


def get_counts(chain):
    """
    Counts the nucleotides in the given String of characters ACGT
    and returns a list containing {Acount, Ccount, Gcount, Tcount}.
    :param: chain
    :type chain: string
    :return: list of counts of each nucleotide in ACGT,
    {Acount, Ccount, Gcount, Tcount}
    :rtype: list of integers
    """
    chain = chain.upper()
    counts = [0, 0, 0, 0]
    for i in range(len(chain)):
        if chain[i] == 'A':
            counts[0] += 1
        elif chain[i] == 'C':
            counts[1] += 1
        elif chain[i] == 'G':
            counts[2] += 1
        elif chain[i] == 'T':
            counts[3] += 1
    return counts


def get_total_mass(counts, junk_count):
    """
    Computes/returns the total mass of the given sequence of nucleotides,
    treating each "-" as a junk section with 100.0 mass.
    :param counts: list of counts of each nucleotide in ACGT,
    {Acount, Ccount, Gcount, Tcount}
    :type counts: list of integers
    :param junk_count: number of dashes in the nucleotide sequence
    :type junk_count: integer
    :return: total mass of the given nucleotide sequence
    :rtype: float
    """
    total_mass = junk_count * _JUNK_MASS
    for i in range(0, len(counts)):
        total_mass += counts[i] * _MASSES[i]
    return total_mass


def get_percentages(counts, total_mass):
    """
    Looks at {Acount, Ccount, Gcount, Tcount} in given list counts and
    uses them to compute and return a list of mass percentages
    {A%, C%, G%, T%} rounded to nearest 0.1 based on the molecular
    weight of A, C, G, and T as defined in the spec.
    :param counts:list of counts of each nucleotide in ACGT,
    {Acount, Ccount, Gcount, Tcount}
    :type counts list of integers
    :param total_mass:  total mass of the given nucleotide sequence
    :type total_mass: float
    :return: a list of mass percentages {A%, C%, G%, T%}
    :rtype: list of floats
    """
    mass_percent = [0, 0, 0, 0]
    mass_percent[0] = round1(_MASSES[0] * counts[0] * 100.0 / total_mass)
    mass_percent[1] = round1(_MASSES[1] * counts[1] * 100.0 / total_mass)
    mass_percent[2] = round1(_MASSES[2] * counts[2] * 100.0 / total_mass)
    mass_percent[3] = round1(_MASSES[3] * counts[3] * 100.0 / total_mass)
    return mass_percent


def get_codons(sequence):
    """
    Breaks apart the given String into codons of 3 nucleotides each.
    Precondition: sequence consists of only ACGT and its length is
    a multiple of 3.
    :param sequence: The nucleotide sequence without any junk charcters
    :type sequence: a string
    :return: list of codons consisting of characters ACGT and its length is
    a multiple of 3.
    :rtype: list of strings
    """
    sequence = sequence.strip()
    sequence = sequence.upper()
    sequence = sequence.replace("-", "")
    codons = [sequence[i:i + _CODON_LENGTH]
              for i in range(0, len(sequence), _CODON_LENGTH)]
    return codons


def report_results(name, sequence, counts, total_mass, percentages, codons,
                   out_file):
    """
    Produces an output file of all computations and whether
    it is a protein. 
    :param name: The name line read in before the nucleotide
    :type name: string
    :param sequence: The nucleotide sequence with junk characters
    :type sequence: string
    :param counts: counts of the nucleotides in list  [A, C, G, T]
    :type counts: list of integers
    :param total_mass: total mass of the given nucleotide sequence
    :type total_mass: float
    :param percentages: a list of mass percentages
    {A%, C%, G%, T%} rounded to nearest 0.1 based on the molecular
    weight of A, C, G, and T
    :type percentages: list of floats
    :param codons: a list of codons
    :type codons: list of strings
    :param out_file: a file variable representing the output file to be created
    :type out_file: output file name with extension
    :return: None
    """
    #out_file.write("Region Name: " + name)
    codons_list = get_codons(sequence)
    protein = is_protein(codons_list, percentages)
    name = name.strip()
    sequence = sequence.strip()
    out_file.write(f'Region Name: {name}\n')
    out_file.write(f'Nucleotides: {sequence}\n')
    out_file.write(f'Nuc. Counts: {counts}\n')
    out_file.write(f'Total Mass%: {percentages} of '
                   f'{round1(total_mass)}\n')
    out_file.write(f'Codons List: {codons}\n')
    is_true = "YES" if protein else "NO"
    out_file.write(f'Is Protein?: {is_true}\n\n')

    # Fill in the rest of the out_file.write() statements
    

def is_protein(codons, percentages):
    """
    Returns a True if the given sequence of codons encodes a protein,
    based on its length, C/G mass percentage, start and stop codons.
    Returns a False otherwise.
    :param codons: a list of codons
    :type codons: list of strings
    :param percentages: a list of mass percentages
    {A%, C%, G%, T%} rounded to nearest 0.1 based on the molecular
    weight of A, C, G, and T
    :type percentages: list of floats
    :return: True if a protein, False otherwise
    :rtype: Boolean
    """
    if codons[0] == "ATG":
        last = codons[-1]
        if last in ["TAA", "TAG", "TGA"]:
            if len(codons) >= _MINIMUM_LENGTH:
                if percentages[1] + percentages[2] >= _CG_PERCENTAGE:
                    return True
    return False


def round1(value):
    """
    Rounds the given real number to one digit past the decimal point.
    :param value: value to round to one digit of precision
    :type value: float
    :return: value rounded to one digit of precision
    :rtype: float
    """
    return round(value * _TENTHS_PRECISION) / _TENTHS_PRECISION


def nuc_index(nucleotide):
    """
    Converts a nucleotide character into an array index: 
    A0,C1,G2,T3, else -1
    :param nucleotide: a letter
    :type nucleotide: string
    :return: nucleotide index in [A,C,G,T], -1 if not found
    :rtype: integer
    """
    nucleotide = nucleotide.upper()
    index = ["A", "B", "C", "D"]
    return index.find(nucleotide)


def get_dashes(nucleotide):
    return nucleotide.count('-')


if __name__ == '__main__':
    main()
