## RAG : Basics to Advance Training 

This training consits of multiple modules. Each module is divided into two parts: 

1. Concepts
2. Practical : Jupyter Notebook

Module 1, Module 2 and Module 5 will be of **2 hours** duration each.
Module 3 and Module 4 will be of **4 hours** duration each.

### Module 1: Introduction to RAG (2 Hrs)

#### Concepts

* What is RAG?
* Use cases of RAG
* Architecture of RAG application
* Types of RAG
* RAG Evaluation Frameworks

#### Practical

* Create a QnA application using basic (text) RAG


### Module 2: Embedding Model & Vector DB (2 Hrs)

#### Concepts

* What is tokenization?
* What is Embedding model?
* Architecture of Embedding model
* Internals of Vector DB

#### Practical

* Create an application to Store Annual Reports of a company in Vector DB and retrieve financial information


### Module 3: Strategies for Indexing data (4 Hrs)

#### Concepts

* Chunking Strategies (Fixed, Hierarchical, Semantic, Agentic)
* How to choose an Embedding Model

#### Practical

* Scenario 1 : Companies conduct investor meetings for providing latest updates to investors. These meetings are shared in the form of transcripts for reference. Normally conversation from single speaker can span over multiple pages. We will implement a data parsing strategy to handle multi page conversation so that we can get search results for our queries. 
* Scenario 2 : Companies publish annual report which are between 100-200 pages and these annual reports contain lot of textual and tabular data. We will implement an indexing strategy to handle tabular data along with textual data. (Use llamaparse for parsing the data and store in vector DB with Sales force Annual Report)
* Scenario 3 : Implementation of chunking strategy for documents with images (charts, graphs, tables, etc).  (Use langchain based summary of tabluar data strategy)
* Scenario 4 : Indian Companies publish annual report which are 300-500 pages. And these annual reports contain lot of textual data, tabular data and some images (presumably charts, graphs, tables, etc). We will implement an indexing strategy to query tabular data and images along with textual data.

### Module 4: Strategies for Data Retrieval (4 Hrs)

#### Concepts

* Hybrid Search
* Embedding Models for Query embeddings
* Multi-query
* How to choose Re-ranking strategies

#### Practical

* Scenario 1 : We want to retrieve the value of Debt to Equity ratio which is not mentioned in the Annual Report as a direct field rather it is mentioned as debt in separate section and equity in separate section in the Annual Report. We will implement the retrieval system which will help us to get the value of Debt to Equity ratio. (Use Multi Query)
* Scenario 2 : We want to extract key financial information from the Annual Report e.g revenue, profit, loss, etc. We will implement the retrieval system which will help us to get the value of revenue, profit, loss, etc. (Use Hybrid Search)
* Scenario 3 : Despite having hybrid search, we are not able to retrieve semantically correct data from vector DB. We will implement the another retrieval system which will help us to get the value of some of the key financial metric like capital spend, future expense, entity ownsership cost etc which are not strongly highlighted in the report. (Use Re-ranking)


### Module 5 : Multimodal RAG (2 hrs)

#### Concepts

* What is Multimodal RAG?
* Use cases of Multimodal RAG
* Architecture of Multimodal RAG application


#### Practical

* Create a QnA application using Multimodal RAG





Module 1 and 2 : 20K Each ( 4 hrs)

Module 3 : 50K (Including code with real use case implementation) : 4 hrs

Module 4 : 50K (Including code with real use case implementation) : 4 hrs

Module 5 : 30K ( 2 hrs)

Total : 170K ( 14 hrs)




