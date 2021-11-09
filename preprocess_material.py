from pathlib import Path
from tibetan_sort.tibetan_sort import TibetanSort


bo_sort = TibetanSort()


def extract_vocab(sent_path, vocab_path):
    sents = sent_path.read_text().split()
    sents = [s.strip() for s in sents]
    vocab = vocab_path.read_text().split()
    vocab = [v.strip() for v in vocab]
    total = list(set(sents + vocab))
    total = bo_sort.sort_list(total)
    return '\n'.join(total)


if __name__ == '__main__':
    a0 = 'input/esukhia/A0'
    a1_easy = 'input/esukhia/A1/A1-easy'
    in_path = Path(a1_easy)
    out_path = Path('output') / in_path.parts[-1]
    if not out_path.is_dir():
        out_path.mkdir()
    for f in in_path.glob('*_sentences.txt'):
        v = f.parent / (f.stem.split('_')[0] + '_vocab.txt')
        t = out_path / (f.stem.split('_')[0] + '_vocab-total.txt')
        total = extract_vocab(f, v)
        t.write_text(total)

    total_vocab = []
    for f in in_path.glob('*_vocab-total.txt'):
        total_vocab.extend(f.read_text().split())
    total_vocab = [t.strip() for t in total_vocab]
    total_vocab = bo_sort.sort_list(list(set(total_vocab)))
    t = out_path / f'total-vocab_{in_path.parts[-1]}.txt'
    t.write_text('\n'.join(total_vocab))

    total_sentences = []
    for f in in_path.glob('*_sentences.txt'):
        total_sentences.extend(f.read_text().split('\n'))
    total_sentences = [t.strip() for t in total_sentences]
    total_sentences = bo_sort.sort_list(list(set(total_sentences)))
    t = out_path / f'total-sentences_{in_path.parts[-1]}.txt'
    t.write_text('\n'.join(total_sentences))
