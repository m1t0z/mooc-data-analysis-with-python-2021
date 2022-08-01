#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet = "abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url = "https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename = "src/kotus-sanalista_v1.xml"
    load_from_net = False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines = []
            for line in data:
                lines.append(line.decode("utf-8"))
        doc = "".join(lines)
    else:
        with open(filename, "rb") as data:
            doc = data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath("/kotus-sanalista/st/s")
    return list(map(lambda s: s.text, s_elements))


def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines = map(lambda s: s.rstrip(), data.readlines())
    return lines


def get_features(a: np.ndarray) -> np.ndarray:
    res = np.empty((len(a), len(alphabet)), dtype=int)
    for i, w in enumerate(a):
        c = Counter(w)
        for j, l in enumerate(alphabet):
            res[i, j] = c[l]
    return res


def contains_valid_chars(s: str) -> bool:
    s_set = set(s)
    return s_set.issubset(alphabet_set)


def get_features_and_labels():
    # Load Finnish/English words.
    words_f = load_finnish()
    words_e = load_english()

    # Cleanup Finish words.
    words_f = list(filter(contains_valid_chars, map(str.lower, words_f)))

    # Cleanup English words.
    words_e = list(
        filter(
            contains_valid_chars,
            map(str.lower, filter(lambda w: w[0].islower(), words_e)),
        )
    )

    # Create feature matrix.
    features = get_features(np.array(words_f + words_e))

    # Create target vector.
    labels_f = np.zeros(len(words_f))
    labels_e = np.ones(len(words_e))
    targets = np.concatenate([labels_f, labels_e])

    return (features, targets)


def word_classification():
    X, y = get_features_and_labels()
    model = MultinomialNB()
    return cross_val_score(
        model, X, y, cv=model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    )


def main():
    print("Accuracy scores are:", word_classification())


if __name__ == "__main__":
    main()
