"""
Show the number of unique tweet authors in the data
"""
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help='path to input file')
    parser.add_argument('-o', '--output', type=str, help='path to output file')
    args = parser.parse_args()
    print('processing file', args.input)
    print('output', args.output)
    authors = set()
    with open(args.input, 'r') as fi:
        col = next(fi)
        for line in fi:
            authors.add(line.strip().split(',')[0])
    print('unique authors', len(authors))
    print(list(authors)[:10])


def take_avg(a, b):
    return (a + b) / 2

main()

# if __name__=='__main__':
#     main()