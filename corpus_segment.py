from pathlib import Path
import re

from botok import WordTokenizer, Config
import yaml


def set_tok():
    c = Config(dialect_name='general', base_path=Path('output/tok_data'))
    return WordTokenizer(config=c)


def tokenize(tok, string):
    lemmatization_exceptions = ['བཅས་', 'མཁས་']
    tokens = tok.tokenize(string)
    words = []
    for t in tokens:
        if t.chunk_type == 'TEXT':
            if not t.lemma:
                text = t.text
            else:
                if t.pos == 'PART':
                    if t.affix:
                        text = '-' + t.text
                    else:
                        text = t.text
                else:
                    # Hack because of botok limitation:
                    if t.text_cleaned not in lemmatization_exceptions and t.affixation and 'aa' in t.affixation and t.affixation['aa']:
                        text = t.lemma
                    else:
                        text = t.text
            text = text.strip().replace('༌', '་')
            if not text.endswith('་'):
                text += '་'

            if t.pos == 'NON_WORD':
                text += '#'
            words.append(text)

        else:
            t = t.text.strip().replace(' ', '_')
            words.append(t)

    tokenized = ' '.join(words)

    # do replacements
    repl_path = Path('output/tok_data') / 'general' / 'adjustments' / 'rules' / 'replacements.txt'
    for line in repl_path.read_text().split('\n'):
        orig, repl = line.split('—')
        tokenized = tokenized.replace(orig, repl)

    return tokenized


def tok_corpus(in_path, out_path):
    if not out_path.is_dir():
        out_path.mkdir()
    tok = set_tok()
    for f in in_path.glob('*'):
        print(f)
        dump = f.read_text()
        out = tokenize(tok, dump)
        out_file = out_path / f.name
        out_file.write_text(out)


if __name__ == '__main__':
    in_path = Path('input/laglen_commentaries')
    out_path = Path('output/laglen_commentaries')
    tok_corpus(in_path, out_path)

