# Background: Why LangChain Was Created

In 2022, when LLM models started to gain popularity, many companies began offering API access to their models.  
Some notable companies included **OpenAI, Google, Microsoft, and Anthropic**.

However, each company had:

- different API structures  
- different authentication methods  
- different response formats  

Because of these inconsistencies, developers needed a framework that would allow them to switch between different LLM providers **without rewriting their entire codebase**.

This led to the creation of **LangChain**, a framework that abstracts away the differences between LLM providers.

---

# Introduction of Chains

To simplify working with LLMs, LangChain introduced **chains**, which are sequences of calls to LLMs and other utilities.

Chains allow developers to:

- combine multiple steps in a single pipeline  
- build complex applications more easily  

**Example:**  
A chain can take user input → process it with an LLM → store the result in a database, all in one function call.

---

# The Problem With Too Many Chains

As AI engineers continued building more chains, they realized:

- the number of chains became difficult to manage  
- the codebase grew cluttered  
- updating specific functionality became harder  
- new developers faced a steep learning curve, since they had to understand many individual chains

---

# Solution: Runnables

To address these issues, LangChain introduced **Runnables** — a more modular and reusable approach.

### Key ideas behind Runnables:

- **Unit of Work:** Each Runnable encapsulates a single task  
- **Common Interface:** Methods like `invoke()`, `batch()`, and `stream()` work across all Runnables  
- **Modularity:** Runnables act like building blocks that can be easily combined to form complex applications  
- **Less need for manually managing many chains**

---

# Types of Runnables

There are **two main types**:

## 1. Task-Specific Runnables
Designed for specific tasks like:

- text generation  
- summarization  
- translation  

Examples include:

- LLMs  
- PromptTemplates  
- TextSplitters  

These are optimized for their individual tasks.

---

## 2. Runnable Primitives
General-purpose building blocks used to compose more complex logic.  
They provide basic functionality and can be extended or combined.

Examples include:

- Chains  
- Maps  
- Reduces  

---

# RunnableSequence

`RunnableSequence` allows chaining multiple Runnables in order.

It takes a list of Runnables and executes them one by one:

