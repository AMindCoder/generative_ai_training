The BLEU (Bilingual Evaluation Understudy) score is a widely used metric for evaluating the quality of machine-generated translations by comparing them to one or more human reference translations. It assesses how closely the machine translation matches the reference translations based on overlapping n-grams (contiguous sequences of words). ([Understanding BLEU and ROUGE score for NLP evaluation - Medium](https://medium.com/%40sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb?utm_source=chatgpt.com))

---

### 🔍 How BLEU Works

1. **Modified n-gram Precision**:
   - BLEU calculates the precision of n-grams (typically up to 4-grams) in the candidate translation that match the reference translations.
   - To prevent inflated scores from repeated words, BLEU uses "clipped" counts, where the count of each n-gram in the candidate is limited to the maximum count in any reference. ([Understanding the BLEU Score for Translation Model Evaluation](https://deconvoluteai.com/blog/bleu-score?utm_source=chatgpt.com))

2. **Brevity Penalty (BP)**:
   - To discourage overly short translations that might have high precision, BLEU applies a brevity penalty.
   - If the candidate translation is shorter than the reference, the score is penalized exponentially based on the length difference. ([Understanding the BLEU Score for Translation Model Evaluation](https://deconvoluteai.com/blog/bleu-score?utm_source=chatgpt.com))

3. **Final BLEU Score**:
   - The BLEU score is computed as: ([Calculate BLEU score in Python - Stack Overflow](https://stackoverflow.com/questions/32395880/calculate-bleu-score-in-python?utm_source=chatgpt.com))
     \[ \text{BLEU} = \text{BP} \times \exp\left( \sum_{n=1}^{N} w_n \log p_n \right) \]
     where \( p_n \) is the modified precision for n-grams of size \( n \), and \( w_n \) are the weights (typically equal) assigned to each n-gram level.

---

### 📘 Example

**Reference Translations**:
- R1: "The cat is on the mat."
- R2: "There is a cat on the mat." ([Two minutes NLP — Learn the BLEU metric by examples - Medium](https://medium.com/nlplanet/two-minutes-nlp-learn-the-bleu-metric-by-examples-df015ca73a86?utm_source=chatgpt.com))

**Candidate Translation**:
- C1: "The cat the cat the cat." ([BLEU](https://en.wikipedia.org/wiki/BLEU?utm_source=chatgpt.com))

**Unigram Precision**:
- Words in C1: "The", "cat", repeated.
- Clipped counts: "The" appears twice in references; "cat" appears once. So, maximum matches = 2 ("The") + 1 ("cat") = 3.
- Total words in C1 = 6.
- Unigram precision = 3/6 = 0.5. ([Two minutes NLP — Learn the BLEU metric by examples - Medium](https://medium.com/nlplanet/two-minutes-nlp-learn-the-bleu-metric-by-examples-df015ca73a86?utm_source=chatgpt.com), [BLEU Score for Evaluating Neural Machine Translation – Python](https://www.geeksforgeeks.org/nlp-bleu-score-for-evaluating-neural-machine-translation-python/?utm_source=chatgpt.com), [BLEU](https://en.wikipedia.org/wiki/BLEU?utm_source=chatgpt.com))

**Brevity Penalty**:
- Length of C1 = 6; average reference length = 6.
- Since lengths are equal, BP = 1. ([Two minutes NLP — Learn the BLEU metric by examples - Medium](https://medium.com/nlplanet/two-minutes-nlp-learn-the-bleu-metric-by-examples-df015ca73a86?utm_source=chatgpt.com))

**Final BLEU Score**:
- Assuming only unigram precision is considered, BLEU = 1 × 0.5 = 0.5. ([Understanding the BLEU Score for Translation Model Evaluation](https://deconvoluteai.com/blog/bleu-score?utm_source=chatgpt.com))


---

### ⚠️ Limitations

- **Lack of Recall**: BLEU focuses on precision and doesn't account for recall, potentially overlooking missing but important words.
- **Sensitivity to Exact Matches**: It doesn't handle synonyms or paraphrasing well; different wordings conveying the same meaning may score poorly.
- **Not Ideal for Sentence-Level Evaluation**: BLEU is more reliable at the corpus level; individual sentence scores can be misleading. ([Evaluation of machine translation](https://en.wikipedia.org/wiki/Evaluation_of_machine_translation?utm_source=chatgpt.com))

---

For a visual explanation, you might find this video helpful:

 ([BLEU Score Explained](https://www.youtube.com/watch?v=25kutmqou6o&utm_source=chatgpt.com))

--- 