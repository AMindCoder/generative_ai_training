Here’s a tailored **instruction prompt** to generate a GitHub-centric course structure for Modules 1 & 2, emphasizing Codespaces, Python/Colab labs, and a 50-50 theory-practice split. Adjust as needed:

---

### **Instruction Prompt for LLM**  
```markdown 
Act as an expert course designer for Generative AI. Design the structure for **Module 1: Introduction to Generative AI & Tools** and **Module 2: Mastering Prompt Engineering**, with the following requirements:  

1. **Format**:  
   - Organize content as a **GitHub repository** with clear folder structure and GitHub Pages-ready markdown.  
   - Use GitHub Codespaces for **pre-configured, browser-based labs** (Python/Jupyter).  
   - Include a mix of theory (50%) and hands-on labs (50%) with Colab/Python notebooks.  

2. **Module 1: Introduction to Generative AI & Tools**  
   - **Theory**:  
     - What is Generative AI? Key concepts (e.g., LLMs, diffusion models).  
     - Ethical considerations and real-world use cases.  
     - Tools overview: OpenAI API, Hugging Face, PyTorch.  
   - **Labs**:  
     - Lab 1: Set up a Codespace environment with Python/LLM libraries.  
     - Lab 2: Use OpenAI API to generate text/code in a Colab notebook.  
     - Lab 3: Explore Hugging Face models with `transformers` library.  

3. **Module 2: Mastering Prompt Engineering**  
   - **Theory**:  
     - Prompting fundamentals: zero-shot, few-shot, chain-of-thought.  
     - Domain-specific prompting (code, creative writing).  
     - Tools: LangChain, PromptFlow, OpenAI playground.  
   - **Labs**:  
     - Lab 1: Build a Q&A bot with iterative prompt refinement (OpenAI API).  
     - Lab 2: Create a code generator using few-shot examples.  
     - Lab 3: Chain prompts with LangChain for multi-step tasks.  

4. **GitHub Structure**:  
   - Repository must include:  
     - `/module1` and `/module2` folders with:  
       - `theory.md` (theory summaries, diagrams, links).  
       - `/labs` with Python notebooks (`.ipynb`) and Codespaces configs.  
     - `README.md` with course overview, setup instructions, and prerequisites.  
     - `requirements.txt` for Python dependencies.  
     - GitHub Pages branch for rendering theory as a website.  

5. **Additional Requirements**:  
   - Every lab must include a **Codespaces configuration** for one-click setup.  
   - Use Colab notebooks for GPU access and Codespaces for browser-based IDE.  
   - Add **quizzes** (theory) and **project prompts** (labs) to each module.  
```

---

### **Sample Output Structure (LLM Response)**  
The LLM should generate a GitHub-like structure, such as:  
```markdown 
# Generative AI Course (Modules 1 & 2)  
🚀 **Live Demo**: [GitHub Pages Site](https://your-username.github.io/gen-ai-course)  

## Module 1: Introduction to Generative AI & Tools  
### Theory ([theory.md](/module1/theory.md))  
- Key concepts: LLMs, diffusion models, ethics.  
- Tools: OpenAI API, Hugging Face, PyTorch.  

### Labs  
1. **Lab 1**: [Setup Codespace](/module1/labs/lab1_codespace_setup.ipynb)  
   - Launch a pre-configured Codespace with LLM libraries.  
2. **Lab 2**: [First OpenAI API Call](/module1/labs/lab2_openai_textgen.ipynb)  
   - Generate text using `gpt-3.5-turbo` in Colab.  
3. **Lab 3**: [Hugging Face Playground](/module1/labs/lab3_huggingface_transformers.ipynb)  
   - Run a GPT-2 model for text completion.  

## Module 2: Mastering Prompt Engineering  
### Theory ([theory.md](/module2/theory.md))  
- Prompt engineering techniques (zero-shot, chain-of-thought).  
- Domain-specific examples (code, creative writing).  

### Labs  
1. **Lab 1**: [Q&A Chatbot](/module2/labs/lab1_qa_chatbot.ipynb)  
   - Refine prompts iteratively for accuracy.  
2. **Lab 2**: [Code Generator](/module2/labs/lab2_code_generation.ipynb)  
   - Generate Python functions with few-shot prompts.  
3. **Lab 3**: [LangChain Workflow](/module2/labs/lab3_langchain_prompt_chaining.ipynb)  
   - Chain prompts to automate a multi-step task.  

## Setup  
1. Clone this repo and launch in [GitHub Codespaces](https://codespaces.new/your-repo).  
2. For GPU support, open labs in **Google Colab** (links provided).  
``` 

--- 

### **Why This Works**  
- **GitHub-Centric**: Appeals to coders familiar with repositories and collaborative workflows.  
- **Immediate Hands-On**: Codespaces/Colab removes setup friction.  
- **Balanced Learning**: 50% theory (markdown) + 50% labs (notebooks).  
- **Industry Relevance**: Focus on tools like OpenAI, Hugging Face, and LangChain.  

Adjust the prompt to add/remove tools or labs based on your audience!