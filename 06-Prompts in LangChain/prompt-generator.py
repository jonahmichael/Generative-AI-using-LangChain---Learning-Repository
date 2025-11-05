from langchain_core.prompts import PromptTemplate # CORRECTED IMPORT for PromptTemplate as we are using langchain_core  

template = PromptTemplate(
  template="Explain the research paper titled '{paper_name}' in a {explanation_style} style with a {explanation_length} length.",
  input_variables=["paper_name", "explanation_style", "explanation_length"]   #these are the variables used in the template
  # REMOVE THIS LINE: variable_templates=True
)

template.save('template.json')