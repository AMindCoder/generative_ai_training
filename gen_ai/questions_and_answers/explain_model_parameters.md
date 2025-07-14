# Parameters of the AI Model

## 1. Temperature

The "Temperature" setting in an AI model is like adjusting the creativity dial. Imagine you have a magic storybook that can write stories on its own. If you turn the temperature down, the book plays it safe, sticking to common tales it knows well. But if you crank up the temperature, the book gets bolder, coming up with wild and unexpected twists. So, the temperature controls how predictable or surprising the stories (or answers) from the AI will be. Lower temperatures lead to more familiar paths, while higher temperatures open the door to the world of imagination and novelty.

### Example Comparison

**Prompt:** Write a story about a space adventure where the main character discovers a new planet.

| Temperature Setting | Output |
|-------------------|--------|
| **Lower Temperature (e.g., 0.3)** | The story begins with Captain Alex, a seasoned astronaut, navigating his spaceship through the vast expanse of space. After months of journeying, Alex and his crew discover a new planet. It's similar to Earth, with vast oceans and green forests. They land and explore, finding the planet uninhabited but perfect for human life. The story ends with Alex reporting their discovery back to Earth, hailed as a hero for finding a new home for humanity. |
| **Higher Temperature (e.g., 0.9)** | In the midst of a galaxy-spanning space odyssey, Captain Alex encounters a sentient planet named Zorgon. Unlike anything known to humanity, Zorgon communicates through cosmic melodies and has the ability to shift its terrain. Fascinated, Alex befriends Zorgon, learning of its centuries-long loneliness and dreams of exploring the universe. Together, they embark on a quest to find Zorgon's lost planet siblings, weaving through wormholes and battling space pirates. The adventure leaves Alex with a profound sense of the universe's wonders and mysteries. |

### Conclusion

At a lower temperature, the AI produces a story that feels more traditional and straightforward, sticking to well-trodden paths of space exploration and discovery. It's coherent and closely aligns with what we might expect from a space adventure narrative.

At a higher temperature, the story becomes far more imaginative and less predictable. The AI introduces unique concepts, like a sentient planet, and weaves a tale that combines friendship, adventure, and cosmic mysteries. This output is more creative and deviates significantly from standard space adventure themes.

This comparison illustrates how the temperature setting can dramatically affect the creativity and unpredictability of AI-generated content, allowing users to tailor the output according to their desired level of novelty or conventionality.

### Mathematical Intuition behind the Temperature Setting

**Probability Distribution:** When generating text, the model predicts the next word by assigning probabilities to all possible words in its vocabulary. These probabilities form a distribution, indicating how likely each word is to follow the given text.

**Softmax Function:** The model uses a mathematical function called "softmax" to convert the raw output scores (logits) for each word into probabilities. The softmax function ensures that the sum of probabilities for all words equals 1, making it a proper probability distribution.

**Influence of Temperature:**
- **At Temperature = 1:** The probabilities calculated by the softmax function are used as they are. This is the default setting, providing a balance between predictability and creativity.
- **At Lower Temperature (<1):** The softmax function is adjusted to make the distribution "sharper," increasing the probability of the most likely words and decreasing it for less likely ones. This makes the model's output more deterministic and less diverse.
- **At Higher Temperature (>1):** The softmax function is adjusted to make the distribution "flatter," which means reducing the difference in probability between the most likely words and the others. This results in more creative and diverse outputs, as less probable words are more likely to be chosen.

**Entropy:** The concept of entropy, in the context of information theory, measures the unpredictability or randomness of a distribution. Lowering the temperature reduces entropy (making the output more predictable), while raising the temperature increases entropy (making the output more varied and less predictable).

**Exploration vs. Exploitation:** Temperature acts as a dial between exploitation (choosing the most likely or safe words) and exploration (sampling less likely words for more creative or varied outputs). Lower temperatures favor exploitation, and higher temperatures favor exploration.

---

## 2. Max Tokens

"Max Tokens" in an AI model is like setting a limit on how much the model can say or write in one go. Imagine you're telling a story but you're only allowed to use a certain number of words; that's what Max Tokens does—it sets the maximum number of words or characters the AI is allowed to use for its response. If you set a low number, the AI gives you a short answer. If you set a high number, it can tell a longer story or provide a more detailed explanation. It's like setting the boundaries for how long or short you want the AI's messages to be.

### Example Comparison

**Prompt:** Describe a day in the life of someone living in a futuristic city.

| Max Tokens Setting | Output |
|-------------------|--------|
| **Lower Max Tokens (e.g., 50 Tokens)** | In the city of Tomorrowland, residents start their day with sunrise simulations. Automated systems prepare breakfast, while personal drones deliver the morning news. People commute via hyperloops, reaching their destinations in minutes. |
| **Higher Max Tokens (e.g., 200 Tokens)** | In the sprawling metropolis of Futureville, the day begins with the gentle glow of artificial sunrise, courtesy of the city's environmental control dome. Residents wake to the aroma of breakfast, meticulously prepared by their kitchen robots, tailored to their dietary preferences. News and updates are seamlessly projected onto walls, thanks to the advanced AR (Augmented Reality) infrastructure. Commuting is a breeze in this city; hyperloops and anti-gravity pods make traffic jams a thing of the past. Workplaces are dynamic environments that adapt to individual needs, promoting creativity and efficiency. Lunch is often a community affair, with food synthesized from organic compounds, offering unparalleled taste and nutrition. After work, leisure can take many forms, from virtual reality expeditions to exotic, digitally created landscapes, to social gatherings in parks that float above the city, maintained by drones. The day winds down with holographic entertainment shows, before the environmental control dims the lights, mimicking the setting sun, encouraging residents to unwind and prepare for rest. |

### Conclusion

The lower Max Tokens output provides a concise snapshot, highlighting key futuristic concepts like sunrise simulations, automated breakfast preparation, and hyperloop commutes. It gives a quick glimpse into the futuristic city life but leaves many details to the imagination.

The higher Max Tokens output, on the other hand, dives deep into the daily life, painting a vivid picture of the city and its inhabitants. It explores various aspects of living in a futuristic city, from waking up to personalized breakfasts, innovative commuting methods, to leisure activities in the evening. The detailed description allows readers to immerse themselves in the city's atmosphere, offering a comprehensive view of the futuristic lifestyle.

This example showcases how the Max Tokens setting can drastically change the depth and breadth of the AI's output, from a brief overview to a detailed narrative.

### Mathematical Intuition behind the Max Token Setting

**Tokenization:** First, both the input (prompt) and any generated text are broken down into tokens, which could be words, parts of words, punctuation, or special characters. This is crucial because "Max Tokens" refers to the total count of these tokens.

**Probability Distribution Over Tokens:** At each step of the generation, the model predicts the next token by creating a probability distribution over the entire vocabulary. This distribution represents the model's beliefs about which token is most likely to come next, based on the sequence of tokens it has seen so far (including the initial prompt and any tokens it has generated up to that point).

**Cumulative Token Counting:** As the model generates text, it keeps a running total of the number of tokens generated. This count includes both the tokens in the prompt and the tokens that the model has added.

**Mathematical Representation:**
- Let **N** be the "Max Tokens" limit.
- Let **np** represent the number of tokens in the prompt.
- Let **ng** represent the number of tokens generated by the model.
- The process continues (ng increases) as long as **np + ng < N**

**Decision Making at Each Step:** Mathematically, at each step where the model decides what token to generate next, it evaluates whether adding another token would exceed the "Max Tokens" limit. If generating another token would cause **np + ng** to exceed **N**, the model stops generating further tokens.

**Effect on Output:** The "Max Tokens" limit thus directly influences the length and detail of the model's output. It ensures that the model's response does not exceed a predefined total number of tokens, balancing between the depth of content and computational constraints.

---

## 3. Top P (Nucleus Sampling)

"Top P" is like a filter for an AI's creativity when it's making up a story or answering a question. Imagine if you had a magic bag full of ideas, but not all of them are good. "Top P" helps by only letting the AI pick from the best ideas in the bag, making sure the story stays interesting and makes sense. The "P" stands for probability, and by setting "Top P," you decide how big or small the pool of good ideas should be. If you set it wide, the AI might surprise you with unexpected twists; set it narrow, and the AI will stick to what it knows best.

### Example Comparison

**Prompt:** Generate an idea for a novel.

| Top P Setting | Output |
|---------------|--------|
| **Lower Top P (e.g., 0.5)** | The novel centers around a young detective living in London who stumbles upon a mysterious case that has baffled the police for decades. As she delves deeper into the mystery, she uncovers secrets that could change her life forever. The story combines elements of mystery, suspense, and a touch of romance as the detective navigates through the dark underbelly of London. |
| **Higher Top P (e.g., 0.9)** | In a world where people's dreams are interconnected, a librarian discovers she can manipulate the dreamscape to solve mysteries in the waking world. She teams up with an unlikely group of dreamers: a retired circus performer, a disillusioned scientist, and a child with the power to dream the future. Together, they unravel a conspiracy that threatens the very fabric of reality, moving between dreams and waking life to save their interconnected world. |

### Conclusion

The lower Top P output gives us a solid and familiar detective story set in London, sticking closely to well-trodden narrative paths of mystery and suspense. It's a safe, reliable idea that fits comfortably within the genre's expectations.

The higher Top P output, however, ventures into much more unique territory, blending genres and introducing novel concepts like interconnected dreams and a diverse cast with special abilities. This idea is less predictable and more imaginative, showcasing how adjusting "Top P" can significantly alter the novelty and creativity of the AI's output.

This example demonstrates how "Top P" acts as a creative dial for AI, controlling the balance between sticking to the probable and exploring the imaginative, thereby affecting the originality and diversity of the generated content.

### Mathematical Intuition behind the Top P Setting

**Probability Distribution of Tokens:** When generating the next token in a sequence, the model first calculates a probability distribution over its entire vocabulary. This distribution reflects the likelihood of each token being the appropriate next choice given the context provided by the preceding text.

**Sorting and Cumulative Sum:** The tokens are then sorted by their probability in descending order. The cumulative sum of these probabilities is computed, starting from the most probable token to the least.

**Selecting the Nucleus:** The "Top P" threshold is applied to this cumulative distribution. The "nucleus" consists of the smallest set of tokens at the top of this sorted list whose cumulative probability exceeds the "Top P" value. For instance, if "Top P" is set to 0.9 (or 90%), the model identifies the smallest set of most likely tokens whose combined probability is just over 90%.

**Sampling from the Nucleus:** Instead of considering the entire vocabulary for the next token, the model now only samples from this selected nucleus. This ensures that the generated token is among the more probable options but allows for some variability based on the cumulative probability threshold set by "Top P".

Mathematically, if we denote the sorted probabilities as **p₁, p₂, ...., pₙ** (where p₁ is the highest), and the "Top P" threshold as **P**, then we find the smallest **K** such that:

**∑ᵢ₌₁ᴷ pᵢ ≥ P**

Here **k** represents the number of top tokens selected to form the nucleus, from which the next token is sampled.

**Impact of Top P on Text Generation:**
- **Lower Top P:** A smaller nucleus is formed, making text generation more conservative and predictable since it relies on the most likely tokens.
- **Higher Top P:** A larger set of tokens can qualify into the nucleus, introducing more diversity and creativity into the generated text.

"Top P" thus provides a flexible mechanism for controlling the randomness and unpredictability of text generation, enabling a balance between coherency and inventiveness in the model's output.

---

## 4. Top K (Top-k Sampling)

"Top K" (Top-k Sampling) is like setting up a talent show where only the best performers are allowed to compete. Imagine you have a huge group of words that all want to be the next word in a sentence the AI is writing. "Top K" decides how many of these words—let's say the top 50 or 100—get a chance to be chosen. The AI then picks from this smaller, more talented group, making sure the sentence stays interesting but also makes sense. This way, "Top K" helps keep the AI's writing sharp and on track by limiting its choices to the best contenders.

### Example Comparison

**Prompt:** Write an ending for a story where explorers find a mysterious ancient artifact in an old temple.

| Top K Setting | Output |
|---------------|--------|
| **Lower Top K (e.g., 5)** | As the explorers lifted the artifact, the temple began to shake. Realizing the danger, they rushed out just as the temple collapsed behind them. Safely outside, they marveled at the artifact in the sunlight, knowing they had discovered something incredible. The artifact was later studied by historians, revealing secrets about the ancient civilization that built the temple. |
| **Higher Top K (e.g., 50)** | As soon as the artifact was disturbed, a holographic map appeared in the air, pointing to hidden locations across the globe. The explorers realized they hadn't just found a relic; they had uncovered a global treasure hunt set by an ancient civilization. Embarking on this new adventure, they followed the map to various temples, each revealing a piece of advanced technology. Together, these pieces unlocked a renewable energy source, leading to a new era of prosperity. |

### Conclusion

The lower Top K output gives us a straightforward adventure story climax, where the physical danger of the collapsing temple adds drama, followed by a traditional discovery that enriches historical understanding. It's a satisfying but expected conclusion.

The higher Top K output, however, introduces unexpected elements like a holographic map and a global treasure hunt leading to a revolutionary discovery. This ending not only adds layers to the adventure but also ties the story to a larger, more impactful conclusion.

This demonstrates how "Top K" can significantly affect the creativity and uniqueness of the AI's output. Lower settings stick closer to likely scenarios, while higher settings allow the AI to explore a broader and more imaginative range of possibilities, leading to more original and sometimes surprising outcomes.

### Mathematical Intuition behind the Top K Setting

**1. Probability Distribution:** After processing the input (e.g., the start of a sentence), the model predicts the next token by assigning a probability to every possible token in its vocabulary. These probabilities indicate how likely each token is to be the correct next piece in the sequence.

**2. Top K Filtering:** The model then sorts these tokens by their probability, from highest to lowest, and selects the top K tokens. The value of **K** is the parameter you set; it determines how many of the most likely tokens are considered for the next step. All other tokens, even if they have some probability, are ignored for this particular decision.

**3. Normalized Distribution:** The probabilities of these top K tokens are then normalized so that they sum up to 1. This step is crucial because it adjusts the probabilities to form a new, smaller probability distribution limited to just these **K** tokens.

**4. Random Selection:** Finally, the model randomly selects the next token from this filtered, normalized distribution. Because the selection is limited to the top K tokens, the output is more predictable than sampling from the entire distribution but allows for some variation and creativity.

Mathematically, suppose the original probability distribution over the vocabulary is **P = {p₁, p₂, ..., pᵥ}**, where **V** is the size of the vocabulary, and **pᵢ** is the probability of the i-th token. "Top K" sampling involves the following steps:

- Sort **P** in descending order of **pᵢ**.
- Select the subset **Pₖ = {p₁, p₂, ..., pₖ}**, which includes only the top k probabilities.
- Normalize **Pₖ** so that the sum of probabilities in **Pₖ** equals 1.
- Randomly select the next token from **Pₖ** according to the normalized probabilities.

By focusing on the most probable tokens, "Top K" sampling effectively balances between the randomness of generation and the likelihood of the tokens, steering the model towards generating coherent yet diverse and interesting text. This approach helps manage the trade-off between creativity (by allowing for a range of possibilities) and coherence (by not straying too far into implausible territory).

---

## 5. Frequency Penalty

"Frequency Penalty" is like telling a storyteller to avoid repeating the same phrases too often in a tale. When an AI writes a story or explanation, this setting nudges it to use a variety of words and ideas instead of sticking to the ones it already mentioned. Think of it as encouraging the AI to expand its vocabulary and introduce new concepts as it goes along, making the story or explanation more interesting and less repetitive. It's a way to keep the conversation fresh and engaging.

### Example Comparison

**Prompt:** Describe a futuristic city with advanced technology and unique features.

| Frequency Penalty Setting | Output |
|---------------------------|--------|
| **Lower Frequency Penalty (e.g., 0)** | The futuristic city is filled with towering skyscrapers, each skyscraper taller than the last. The streets are clean and efficient, with cars that drive themselves. People use devices that are advanced, making life easier and more efficient. The city's energy comes from renewable sources, powering everything from homes to skyscrapers. Skyscrapers dominate the skyline, showcasing the city's architectural advancements. |
| **Higher Frequency Penalty (e.g., 1)** | In this visionary metropolis, colossal eco-structures blend seamlessly with verdant hanging gardens, purifying the air. Hovering vehicles zip through skyways, orchestrated by an AI traffic grid to ensure swift, serene commutes. Citizens interact with holographic interfaces, accessing vast digital realms with a simple gesture. Renewable energy fuels the city, from solar arrays that glisten at dawn to bio-reactive algae farms illuminating the night. Architectural wonders, from levitating platforms to water-recycling towers, epitomize this haven of sustainability and innovation. |

### Conclusion

The lower Frequency Penalty output tends to repeat certain terms, like "skyscrapers" and "efficient," which can make the description feel a bit redundant. It provides a clear picture, but it lacks variety in its language and concepts.

The higher Frequency Penalty output, however, introduces a wider range of ideas and vocabulary, from "eco-structures" and "holographic interfaces" to "bio-reactive algae farms." This not only makes the description more engaging and vivid but also paints a richer, more diverse picture of the futuristic city.

This comparison shows how adjusting the "Frequency Penalty" can significantly impact the AI's creativity and the richness of its output, encouraging it to explore a broader lexicon and present a more detailed and imaginative vision.

### Mathematical Intuition behind the Frequency Penalty Setting

**1. Objective of Frequency Penalty:** The frequency penalty is designed to decrease the likelihood of repeating the same token or similar tokens too often in the generated text. This parameter helps in diversifying the content and preventing redundancy, which can be crucial in generating more natural and engaging text.

**2. Application of Frequency Penalty:** As the model generates each new token, it adjusts the probabilities of subsequent tokens based on their previous occurrences in the text. The more frequently a token has appeared, the greater the reduction in its probability of being selected again.

**3. Calculation of Penalty:** The penalty applied to each token is proportional to its occurrence count in the generated text so far. The penalty value, typically a negative multiplier (denoted as **-α**), is applied to the log probability of each token. If a token has appeared **n** times, its adjusted log probability becomes:

**adjusted log probability = original log probability − (α × n)**

*NOTE: The formula provided above is a general formula and different LLMs may use slightly different variations*

**4. Effect on Sampling:** After applying the frequency penalty, the probabilities of all tokens are recalculated (exponentiating the adjusted log probabilities) to form a new distribution from which the next token is sampled. This penalization ensures that tokens which have already appeared multiple times are less likely to be chosen again, promoting variety in the output.

**Mathematical Steps:**
- **Track Token Occurrences:** Maintain a count of occurrences for each token that appears in the output as the generation proceeds.
- **Adjust Probabilities:** For each token, calculate the frequency penalty based on its count. Adjust the log probability by subtracting **α × n** from the log probability of the token.
- **Normalize Probabilities:** Convert the adjusted log probabilities back to a standard probability distribution by taking the exponential of each adjusted log probability.
- **Sampling:** Select the next token from this adjusted distribution, which now reflects reduced probabilities for tokens that have appeared frequently.

By implementing a frequency penalty, the model not only enhances the creativity and readability of the generated text but also avoids repetitiveness that can detract from user engagement. This setting is particularly useful in scenarios where the diversity of expression is valued, such as in creative writing, content generation, and conversational AI systems.