# In 2022, when LLM models started to gain popularity,
# there were many companies that offered API access to their models.
# Some of the notable companies included OpenAI, Google, Microsoft, and Anthropic.

# But each of these companies had different ways of structuring their API calls,
# different authentication methods, and different response formats.

# Therefore, they wanted build a framework that would allow them to easily switch between different LLM providers
# without having to rewrite their entire codebase each time they wanted to use a different model. 

# so they created LangChain, a framework that abstracts away the differences between different LLM providers

#_______________________________________________________________

# now for to simplfy the process of working with LLMs,
# they introductued chains (a sequence of calls to LLMs and other utilities),

# which basically allows us to chain together multiple calls to LLMs and other utilities
# in a single pipeline, making it easier to build complex applications.1

# for example, we can create a chain that takes a user input,
# processes it using an LLM, and then stores the result in a database,
# all in a single function call.

# but what happened is that, the AI engineers started to realize that
# the ended up writting a lot of such chains.

# The problem with this approach is that,
# while chains are great for simplifying the process of working with LLMs,
# they can become difficult to manage and maintain as the number of chains grows. (The codebase can become cluttered with many different chains, making it hard to find and update specific functionality.)
# also the learning curve for new developers can be steep, as they need to understand the intricacies of each chain in order to effectively use and modify them.

# https://www.langchain.com/

# To address these issues, LangChain introduced Runnables,
# which are a more modular and reusable way to build applications with LLMs.
# Unit of Work: Runnables are designed to encapsulate a single unit of work,
# making it easier to understand and manage individual components of an application.

# common interface: Runnables provide a common interface for different types of components, like invoke(),batch(), stream(), etc.
# This makes it easier to switch between different implementations and integrate new components into an application.
# in layman terms, Runnables are like building blocks that can be easily combined and reused to create complex applications with LLMs,
# without the need to create and manage many different chains.

# _______________________________________________

# Runnavles are of 2 types:
# Task Specific Runnables: These are designed to perform a specific task,
# such as text generation, summarization, or translation. It provides specialized functionality for a particular use case.
# These Runnables are optimized for their specific task and may include additional features or parameters to enhance their performance.
# Examples include LLMs, PromptTemplates, and TextSplitters.

# Runnable Primitives: These are more general-purpose components that can be used to build a variety of applications. Fundamental building blocks that can be composed together to create more complex Runnables.
# it provides basic functionality that can be extended or combined with other Runnables to create more specialized behavior.
# Examples include Chains, Maps, and Reduces.


# 1. RunnaleSequence: This Runnable allows you to chain together multiple Runnables in a sequence.
# It takes a list of Runnables as input and executes them one after the other, passing the output of one Runnable as the input to the next.
# This is useful for creating complex workflows that involve multiple steps, such as data preprocessing, model inference, and post-processing.

# R1 -> R2 -> R3 -> ... -> Rn