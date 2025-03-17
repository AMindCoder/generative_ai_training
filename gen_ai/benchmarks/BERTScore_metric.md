BERTScore is an evaluation metric that measures the semantic similarity between a candidate (e.g., a machine-generated summary or translation) and one or more reference texts by using contextual embeddings from BERT (or similar transformer models). Instead of counting exact word matches like BLEU or ROUGE, BERTScore computes cosine similarity between embeddings, making it more robust to synonyms, paraphrasing, and varied word order.

Below is an overview and some real-world examples to illustrate BERTScore from basics:

---

### How BERTScore Works

1. **Contextual Embeddings:**  
   BERTScore first converts each token in both the candidate and reference texts into high-dimensional vectors using a pre-trained BERT model. These embeddings capture not only the word meaning but also its context.  
   *For example, the word “bank” will have different embeddings in “river bank” versus “financial bank.”*  
   citeturn1academia10

2. **Cosine Similarity & Greedy Matching:**  
   Once you have the embeddings, BERTScore computes the cosine similarity between every token in the candidate and every token in the reference text.  
   - **Precision:** For each token in the candidate, find the most similar token in the reference and average these maximum scores.  
   - **Recall:** For each token in the reference, find the most similar token in the candidate and average these scores.  
   - **F1 Score:** The harmonic mean of precision and recall gives the final BERTScore.  
   Mathematically, for candidate tokens \(\hat{x}\) and reference tokens \(x\):
   \[
   P_{BERT} = \frac{1}{|\hat{x}|}\sum_{\hat{x}_j \in \hat{x}} \max_{x_i \in x} \; \cos(\mathbf{x_i}, \mathbf{\hat{x}_j})
   \]
   \[
   R_{BERT} = \frac{1}{|x|}\sum_{x_i \in x} \max_{\hat{x}_j \in \hat{x}} \; \cos(\mathbf{x_i}, \mathbf{\hat{x}_j})
   \]
   \[
   F_{BERT} = 2 \times \frac{P_{BERT} \times R_{BERT}}{P_{BERT} + R_{BERT}}
   \]
   citeturn1search2

3. **Semantic Robustness:**  
   Because it uses embeddings, BERTScore recognizes semantic equivalence. For instance, if the candidate text says “The feline rested on the mat” and the reference says “The cat sat on the mat,” BERTScore will likely assign high similarity even though the surface forms differ.

---

### Real-World Examples

1. **Machine Translation:**  
   - **Example 1:**  
     - **Reference:** “The cat sat on the mat.”  
     - **Candidate:** “A feline rested on the mat.”  
     
     Even though the words differ (“cat” vs. “feline”, “sat” vs. “rested”), BERTScore recognizes the similar meanings and assigns high precision and recall, yielding a high F1 score.
     
   - **Example 2:**  
     - **Reference:** “The cat sat on the mat.”  
     - **Candidate:** “The dog ran across the park.”  
     
     Here, the semantic overlap is low, so BERTScore produces a lower score, reflecting the dissimilarity.
     
2. **Text Summarization:**  
   - **Example:**  
     - **Reference Summary:** “Economic recovery is underway with steady growth and decreasing unemployment.”  
     - **Candidate Summary:** “The economy is recovering, with rising growth rates and lower joblessness.”  
     
     BERTScore evaluates the semantic content, capturing that both summaries convey the same underlying message about recovery and improved employment, despite different wording.

---

### Simple Python Code Example

Here’s how you might compute BERTScore using the [bert-score](https://github.com/Tiiiger/bert_score) package:

```python
from bert_score import score

# Define candidate and reference texts
candidates = ["A feline rested on the mat."]
references = ["The cat sat on the mat."]

# Compute BERTScore (using default model, e.g., roberta-large)
P, R, F1 = score(candidates, references, lang="en", verbose=True)

# Average scores for single-sentence examples
print(f"Precision: {P.mean().item():.4f}")
print(f"Recall:    {R.mean().item():.4f}")
print(f"F1 Score:  {F1.mean().item():.4f}")
```

In this example, even though “feline” and “cat” aren’t identical words, BERTScore will likely yield a high F1 score (close to 1) due to their semantic similarity.  
citeturn1search3

---

### Summary

- **BERTScore** uses contextual embeddings from models like BERT to evaluate text similarity at a semantic level.
- It computes token-level cosine similarity and aggregates these using precision, recall, and F1 scores.
- Real-world applications include machine translation, text summarization, and paraphrase detection—especially useful when different words can convey the same meaning.
- Its advantages include robustness to paraphrasing and context sensitivity, though it can be computationally heavier than traditional metrics.