from difflib import SequenceMatcher
import keyness
from pathlib import Path

a = 'abc def ghijkl'
b = 'abd eog hijkl'
sm = SequenceMatcher(None, a, b)
matches = list(sm.get_matching_blocks())
strings = [a[m.a:m.a+m.size] for m in matches]


text1 = Path('../../create-level-packs/output/laglen_commentaries/wangchuk.txt').read_text().split()
text2 = Path('../../create-level-packs/output/laglen_commentaries/thragu.txt').read_text().split()
sm = SequenceMatcher(None, ' '.join(text1), ' '.join(text2))
matches = list(sm.get_matching_blocks())
matches = [a[m.a:m.a+m.size] for m in matches]
k = keyness.log_likelihood([text1], [text2])

print('')
