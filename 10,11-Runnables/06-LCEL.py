'''
6. LCEL (Lang Chain experession language)

LCEL (LangChain Expression Language) is a powerful feature in LangChain that allows users to define complex workflows and operations using a concise and expressive syntax. LCEL enables the composition of Runnables, data transformations, and control flow constructs in a way that is both readable and maintainable.

eg: You want to create a workflow that generates a story based on a given prompt, summarizes it, and then translates the summary into another language.

report_generator = RunnableSequence([ prompt, model, parser ])   # Chaining prompt, model, and parser together


we write,

 report_generator = prompt|model|parser 



'''