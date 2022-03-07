from collections import defaultdict
from pprint import pprint


class FastaParser:
    def __init__(self, fasta_file: str):
        self.__parsed_data = defaultdict(list)
        with open(fasta_file, 'r') as file:
            self.__all_seq = tuple(file.read().split('>')[1:])


    def parse(self):
        for block in self.__all_seq:
            info, sequence = block[:-1].split('\n')[:1][0].split(), ''.join(block.split('\n')[1:])

            key_word_index = info.index('member')
            self.__parsed_data[' '.join(info[key_word_index:key_word_index + 2])].append((info[0], sequence))


    @property
    def data(self) -> dict:
        return dict(self.__parsed_data)


if __name__ == '__main__':
    fasta = FastaParser('abcd.fasta')
    fasta.parse()
    pprint(fasta.data, sort_dicts=False)
