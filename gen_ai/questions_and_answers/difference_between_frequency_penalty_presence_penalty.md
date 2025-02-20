In language models, **frequency penalty** and **presence penalty** are parameters designed to influence the diversity and repetitiveness of generated text. Adjusting these penalties helps control the model's tendency to repeat words or phrases, thereby enhancing the creativity and variability of the output.

**Frequency Penalty:**

The frequency penalty discourages the model from repeating tokens based on their frequency in the generated text. It reduces the likelihood of a token being selected again proportionally to the number of times it has already appeared. This mechanism ensures that words used frequently are less likely to be repeated, promoting a varied vocabulary.

*Example:*

- *Without Frequency Penalty:* "The cat sat on the mat. The cat is happy."

- *With Frequency Penalty:* "The feline sat on the mat. It is happy."

In the second example, the repetition of "the cat" is reduced, and alternative expressions are used.

**Presence Penalty:**

The presence penalty reduces the likelihood of a token being selected again if it has already appeared in the generated text, regardless of how many times. This encourages the model to introduce new concepts or topics, enhancing the overall diversity of the content.

*Example:*

- *Without Presence Penalty:* "She loves to paint. Painting is her passion."

- *With Presence Penalty:* "She loves to paint. Art is her passion."

Here, the model replaces "Painting" with "Art" to avoid repetition, introducing a broader concept.

**Key Differences:**

- **Scope of Penalty:**
  - *Frequency Penalty:* Applies a cumulative penalty based on the number of times a token has been used.
  - *Presence Penalty:* Applies a one-time penalty if a token has appeared at least once.

- **Impact on Text Generation:**
  - *Frequency Penalty:* Controls overall word frequency, reducing repeated usage and promoting varied word choice.
  - *Presence Penalty:* Discourages immediate repetition, encouraging the introduction of new words or topics.

By fine-tuning these parameters, you can balance coherence and diversity in the model's output, tailoring the text generation to specific needs.

For a visual explanation, you might find this video helpful:

[What are LLM Presence and Frequency Penalties?](https://www.youtube.com/watch?v=J66CRz6s734) 