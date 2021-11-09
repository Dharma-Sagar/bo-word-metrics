from difflib import SequenceMatcher
import keyness
from pathlib import Path

a = 'abc def ghijkl'
b = 'abd eog hijkl'
sm = SequenceMatcher(None, a, b)
matches = list(sm.get_matching_blocks())
strings = [a[m.a:m.size] for m in matches]


text1 = Path('output/laglen_commentaries/wangchuk.txt').read_text().split()
text2 = Path('output/laglen_commentaries/thragu.txt').read_text().split()
k = keyness.log_likelihood([text1], [text2])

print('')
