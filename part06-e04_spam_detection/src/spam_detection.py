#!/usr/bin/env python3
import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics


def read_emails_from_arch(arch_path: str):
    with gzip.open(arch_path, "rt") as f:
        return f.readlines()


def get_items_fraction(items, fraction: float):
    cnt = int(len(items) * fraction)
    return items[:cnt]


def spam_detection(random_state=0, fraction=1.0):

    # Read all emails.
    hams = read_emails_from_arch("src/ham.txt.gz")
    spams = read_emails_from_arch("src/spam.txt.gz")

    # Get the specified fraction of the emails.
    hams = get_items_fraction(hams, fraction)
    spams = get_items_fraction(spams, fraction)

    # Create feature matrix X.
    corpus = hams + spams
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)

    # Create target labels y.
    ham_labels = np.zeros(len(hams))
    spam_labels = np.ones(len(spams))
    y = np.concatenate([ham_labels, spam_labels])

    # Split data to training/testing parts.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.75, random_state=random_state
    )

    # Train model.
    model = MultinomialNB().fit(X_train, y_train)
    y_predicted = model.predict(X_test)

    accuracy = metrics.accuracy_score(y_test, y_predicted)
    total = len(y_test)
    misclassified = metrics.zero_one_loss(y_test, y_predicted, normalize=False)

    return accuracy, total, misclassified


def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")


if __name__ == "__main__":
    main()
