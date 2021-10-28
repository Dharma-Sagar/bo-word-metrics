# bo-word-metrics
word metrics for Tibetan texts

## syntax for corpus segmentation
- additions: `+` at the end of words
- removals: `/` at the end of words
- span: to add/remove more than one word, add `(` at the beginning of the span

joining affixed particles:

ex: to join `རྣམ་པ -ར་ དག་པ་` in a single word, simply do `(རྣམ་པ་ -ར་ དག་པ་+`. the script will turn it into `རྣམ་པར་དག་པ་`.
