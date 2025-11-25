# Retrival Augmented Generation (RAG) notes

## What is RAG?

LLM are giant transformers trained on massive datasets to generate human-like text. However, they have limitations in terms of knowledge cutoff dates and may not have access to the most up-to-date or specific information.

LLM store knowledge in their parameters, which makes it difficult to update or expand their knowledge without retraining the entire model. This is where RAG comes in. 

1. But LLM cant answer every question accurately, especially if the information is not present in their training data. RAG addresses this limitation by combining LLM with an external knowledge base or document store.

2. If LLM was last trained in 2021, it may not know about events or developments that occurred after that date. RAG allows the model to access external documents, which can be updated independently of the LLM. This way, the model can provide more accurate and up-to-date information.
(This may not be tru for perplexity or chatgpt which have access to live web data but other open source models do not have this capability)

3. Hallucination is a common problem with LLM where they generate plausible-sounding but incorrect or nonsensical answers. By grounding the model's responses in external documents, RAG can help reduce hallucination and improve the reliability of the generated text.


We can break all these disadvantages by 

### FINETUNING

Finetuning is the process of taking a pre-trained LLM and training it further on a domain-specific dataset or task. This allows the model to adapt to new information and improve its performance on specific tasks.

There are two main approaches to finetuning:

## Supervised Fine-Tuning (SFT)
In SFT, the model is trained on a labeled dataset where each input has a corresponding correct output. The model learns to map inputs to outputs by minimizing the difference between its predictions and the true labels. This approach is effective for tasks where high-quality labeled data is available.
eg: training a model to answer questions based on a set of documents where the correct answers are known.

## Continued Pre-Training (CPT)
In CPT, the model is further pre-trained on a large corpus of unlabeled text that is relevant to the target domain. This helps the model learn domain-specific language patterns and knowledge, which can improve its performance on downstream tasks. CPT is particularly useful when labeled data is scarce or unavailable.
eg: continuing to pre-train a general LLM on a corpus of medical literature to improve its understanding of medical terminology and concepts.


## How finetuing takes place

### Data Collection
The first step in finetuning is to collect a dataset that is relevant to the target domain or task. This dataset can be sourced from various places, such as public datasets, web scraping, or proprietary data.

### Choose a method
FUll parameter finetuning: updating all the parameters of the model during training. This approach can lead to better performance but requires more computational resources and may risk overfitting, especially with small datasets.

LoRA (Low-Rank Adaptation): a more efficient method that adds a small number of trainable parameters to the model while keeping the original parameters frozen. This approach reduces the computational cost and memory requirements, making it suitable for finetuning large models on limited hardware.

QLoRA: combines quantization and LoRA techniques to further reduce the model size and computational requirements during finetuning. This method is particularly useful for deploying finetuned models on resource-constrained devices.

### Train for a few epochs
Once the dataset is prepared and the finetuning method is chosen, the model is trained for a few epochs(meaning complete passes through the entire dataset). The training process involves feeding the model with the input data and updating its parameters based on the loss function, which measures the difference between the model's predictions and the true labels (for SFT) or the likelihood of the text (for CPT).

### Evaluation & Safety Testing
After finetuning, the model is evaluated on a validation dataset to assess its performance. This step helps identify any issues such as overfitting or degradation in performance on general tasks. Additionally, safety testing is conducted to ensure that the finetuned model does not produce harmful or biased outputs.


So all these above methods help in updating the knowledge of LLMs and making them more reliable and accurate for specific tasks or domains.

But the probelm with finetuning is that 

### 1. Computationally Expensive
Finetuning large LLMs requires significant computational resources, including powerful GPUs or TPUs,which can be costly and may not be accessible to everyone.

### 2. Strong Domain Expertise Required
Creating a high-quality finetuning dataset often requires domain expertise to ensure that the data is relevant
and accurately labeled. This can be a barrier for individuals or organizations without access to such expertise.

### 3. Risk of Overfitting
If the finetuning dataset is small or not diverse enough, there is a risk that the model may overfit to the training data, leading to poor generalization on unseen inputs.

__________________________________________


# In Context Learning (ICL) notes

## What is ICL?

In-Context Learning (ICL) is a technique used in large language models (LLMs) that allows them to learn and adapt to new tasks or information without the need for explicit fine-tuning or parameter updates. Instead of modifying the model's weights, ICL leverages the model's ability to understand and generate text based on the context provided in the input prompt.

eg:
  LAbel the name and entities in the following sentence:
    
    *"Barack Obama was born in Hawaii."*
  The entities are:
    1. Barack Obama - Person
    2. Hawaii - Location
    
In this example, the model is given a prompt that includes instructions and an example of the task (labeling entities in a sentence). The model uses this context to generate the desired output without any changes to its underlying parameters.

LLM is an *emergent property of large language models*, meaning that it arises naturally as a result of the model's size and training data, rather than being explicitly programmed into the model. As LLMs become larger and are trained on more diverse datasets, their ability to perform ICL improves significantly.

But it is not effective for all tasks. ICL works best for tasks that are similar to those seen during the model's pre-training phase. For tasks that are significantly different or require specialized knowledge, ICL may not perform as well as fine-tuning.

# Now we come to RAG

RAG combines the strengths of both LLM and ICL by allowing the model to access external documents or knowledge bases during the generation process. This is typically done through a two-step process:
  
## 1. Retrieval:
  When a user inputs a query or prompt, the RAG system first retrieves relevant documents or information from an external knowledge base or document store. This retrieval step is often performed using techniques such as dense vector search or traditional keyword-based search.
## 2. Generation:
  The retrieved documents are then provided as additional context to the LLM, which uses this information to generate a more accurate and informed response to the user's query. The model effectively "reads" the retrieved documents and incorporates their content into its generated output.
  
Refer RAG.md for more details on RAG architecture and implementation.