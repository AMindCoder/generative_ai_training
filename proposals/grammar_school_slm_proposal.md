# Proposal: Small Language Model Training for UK Grammar School Education

**Prepared by: Eightgen AI Services Pvt Ltd**  
**Date: May 28, 2025**

## Executive Summary

Eightgen AI Services Pvt Ltd is pleased to present this proposal for the development of a specialized Small Language Model (SLM) designed to enhance educational outcomes for UK grammar school students. Our solution addresses the critical need for AI-powered educational tools tailored to the UK curriculum across Key Stages 1-3, with particular emphasis on the three core subjects essential for grammar school entrance examinations: English, Mathematics, and Verbal Reasoning.

This proposal outlines our comprehensive approach to creating a high-performance, domain-specific language model that will effectively support both educators and students in the grammar school environment. Our team of AI specialists will collaborate to deliver a solution that meets your specific requirements within the proposed timeframe and budget.

## Project Scope

### Target Audience
- Students preparing for UK grammar school entrance examinations
- Grammar school educators seeking AI-assisted teaching tools
- Educational content developers creating preparation materials
- Parents supporting students through the preparation process

### Educational Coverage
- **Key Stages:** KS1, lower KS2, upper KS2, and KS3
- **Primary Focus Subjects:** English, Mathematics, and Verbal Reasoning
- **Secondary Applications:** Supporting general curriculum learning

### Technological Foundation
We propose utilizing state-of-the-art Small Language Models, including:
- SmolLM2
- Phi3/3.5/4 Reasoning Plus
- Llama3 8B
- Gemma 3 4B
- Qwen 3 8B

## Subject-Specific Requirements & Implementation

Note : These are high level break down of requirements. Actual implementation will require more details and analysis.

### 1. English Language Capabilities

**Content Distribution:**
- MCQ-type questions (80%): Comprehension, vocabulary, grammar, punctuation
- Short Answer questions (20%): Creative writing, text analysis, language usage

**Comprehensive Topic Coverage:**
| Topic Area | Key Stage Coverage | Sample Size |
|------------|-------------------|-------------|
| Comprehension | KS1-KS3 | 2,000 |
| Vocabulary | KS1-KS3 | 2,000 |
| Grammar & Punctuation | KS1-KS3 | 2,000 |
| Creative Writing | KS1-KS3 | 2,000 |
| Text Analysis | KS2-KS3 | 2,000 |

**Total English Dataset:** 10,000 curated samples

### 2. Mathematics Capabilities

**Content Distribution:**
- Short Answer questions (80%): Problem-solving, calculations, word problems
- MCQ-type questions (20%): Quick calculations, concept identification

**Comprehensive Topic Coverage:**
| Topic Area | Key Stage Coverage | Sub-topics | Sample Size |
|------------|-------------------|------------|-------------|
| Number & Place Value | KS1-KS3 | 5 | 5,000 |
| Operations | KS1-KS3 | 4 | 5,000 |
| Fractions, Decimals & Percentages | KS1-KS3 | 5 | 5,000 |
| Ratio & Proportion | KS2-KS3 | 4 | 5,000 |
| Algebra | KS2-KS3 | 5 | 5,000 |
| Measurement | KS1-KS3 | 4 | 5,000 |
| Geometry | KS1-KS3 | 5 | 5,000 |
| Statistics | KS1-KS3 | 4 | 5,000 |
| Problem-solving | KS1-KS3 | 5 | 10,000 |

**Total Mathematics Dataset:** 50,000 curated samples

### 3. Verbal Reasoning Capabilities

**Content Distribution:**
- Equal distribution across 21 standard question types
- Each question type subdivided into 4-5 variations

**Question Types Framework:**
| Category | Question Types | Sub-types | Sample Size |
|----------|---------------|-----------|-------------|
| Word-based | 12 types | 4-5 each | 15,000 |
| Logic-based | 5 types | 4-5 each | 7,500 |
| Pattern-based | 4 types | 4-5 each | 7,500 |

**Total Verbal Reasoning Dataset:** 30,000 curated samples with reasoning traces

## Implementation Methodology

### Phase 1: Data Architecture & Framework Development (Week 1)
- Develop multi-dimensional labeling framework
- Map question types to Key Stage levels
- Create difficulty classification system
- Establish quality metrics for dataset evaluation

At the end of phase 1, we will ask you for the following :
- To review the framework and provide feedback. 
- Provide sample questions for those question types/sub types where no sample questions are available.

### Phase 2: Data Generation & Curation (Weeks 2-3)
- Deploy specialized AI systems for content generation:
  - Llama 3/4 for English question sets
  - Deepseek R1 for reasoning questions
  - Qwen 3/Phi 4 for mathematical problem sets
- Implement iterative generation processes to ensure diversity
  - Initial set → expanded set → comprehensive collection
  - Growth pattern: 10 → 100 → 1000 or 10 → 20 → 40 → 80 ...
- Apply strict quality control measures

### Phase 3: Data Validation & Refinement (Week 4)
- Subject matter expert review of generated content
- Alignment verification with UK curriculum standards
- Correction and enhancement of problematic content
- Final labeling and organization of datasets

### Phase 4: Model Training & Optimization (Weeks 5-6)
- Fine-tune selected SLMs using validated datasets
- Implement Weights and Biases integration for performance tracking
- Optimize model parameters for educational applications
- Conduct benchmarking against established standards

## Technical Infrastructure Requirements

Our implementation will require dedicated GPU-based infrastructure for model deployment and training:

- **Development Environment:** High-performance GPU clusters : These will be used for Data curation using open source models like Deepseek R1, Llama 3/4, Qwen 3/Phi 4
- **Training Environment:** High-performance GPU clusters : These will be used for Model training of identified SLMs
- **Monitoring Tools:** Real-time performance tracking and optimization


## Quality Assurance Framework

Our comprehensive QA process ensures the resulting model will meet the highest educational standards:

1. **Educational Alignment Check:** Verification against UK National Curriculum
2. **Accuracy Verification:** Subject matter expert review
3. **User Testing:** Controlled testing for target age groups

## Deliverables

Upon project completion, we will provide:

1. **Trained SLM:** Optimized for grammar school educational applications
2. **Documentation:** Comprehensive technical and usage documentation
3. **Dataset:** Full access to the curated training datasets
4. **Implementation Guide:** Recommendations for educational integration

## Project Timeline

| Phase | Timeline | Key Milestones |
|-------|----------|----------------|
| Framework Development | Week 1 | Labeling system, quality metrics |
| Data Generation | Weeks 2-3 | English, Mathematics, and Verbal Reasoning datasets |
| Validation | Week 4 | Expert-reviewed content, curriculum alignment |
| Model Training | Week 5 | Initial model training, performance assessment |
| Optimization | Week 6 | Final model refinement, documentation, delivery |

**Total Project Duration:** 4-6 weeks
Note: This is a rough estimate and can be adjusted based on the complexity of the project.

## Investment

The comprehensive solution outlined in this proposal requires an investment of:

**Total Project Cost: ₹5 Lac + GST**

This investment covers:
- Data curation and labeling
- Model training and optimization
- Quality assurance processes
- Comprehensive documentation

This investment does not include:
- Infrastructure costs for GPU-based training

Model Training infra cost will be borne by the client.

## Next Steps

To proceed with this project, we propose the following next steps:

1. **Initial Consultation:** Schedule a detailed discussion of requirements
2. **Project Scoping:** Finalize specific deliverables and timeline
3. **Agreement Finalization:** Complete contractual requirements
4. **Project Initiation:** Begin framework development phase

We look forward to the opportunity to collaborate on this transformative educational AI project. Please contact our team at contact@eightgen.ai to schedule an initial consultation or to address any questions regarding this proposal.

---

**Eightgen AI Services pvt ltd**  
https://eightgen.ai
