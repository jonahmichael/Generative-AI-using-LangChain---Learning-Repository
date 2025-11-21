'''
Semantic Meaning Text Splitter 

This example demonstrates how to use a semantic meaning-based text splitter to divide a large text into smaller chunks based on the underlying meaning and context of the content. This method is particularly useful for documents where preserving the semantic integrity of the text is crucial, such as articles, essays, or any content where meaning is derived from context.

WHy this is important?
By using a semantic meaning-based splitter, we can ensure that the resulting chunks maintain their intended meaning and context, which is essential for tasks such as natural language processing, information retrieval, and machine learning applications.

How does this work?
The semantic meaning-based text splitter analyzes the content of the text to identify logical breakpoints that preserve

They use a sliding window approach to create overlapping chunks of text. This means that each chunk will share some content with the previous and next chunks, ensuring that important context is not lost during the splitting process. the semantic integrity of the text. This is particularly useful for longer texts where context is key to understanding.

BASed on mathematical concepts, standatd deviation, mean, median etc.

This is still in experimental phase and may not be available in all versions of the library and also not very accurate.
'''


from langchain_experimental.text_splitters import SemanticChunker
from langchain_google_genai import GoogleGenAI
from dotenv import load_dotenv

load_dotenv()

text="""
Cricket is a bat-and-ball game played between two teams of eleven players on a field at the center of which is a 22-yard (20.12 m) pitch with a wicket at each end, each comprising two bails balanced on three stumps. The batting side scores runs by striking the ball bowled at the wicket with the bat, while the bowling and fielding side tries to prevent this and dismiss each player (so they are "out"). Means of dismissal include being bowled, when the ball hits the stumps and dislodges the bails, and by the fielding side catching the ball after it is hit by the bat but before it hits the ground. When ten players have been dismissed, the innings ends and the teams swap roles. The game is adjudicated by two umpires, aided by a third umpire and match referee in international matches. They communicate with two off-field scorers who record the match's statistical information.

Bharatanatyam, is a major form of Indian classical dance that originated in Tamil Nadu. It is one of the oldest classical dance traditions in India and is known for its fixed upper torso, bent legs, and intricate footwork combined with expressive hand gestures (mudras) and facial expressions. Bharatanatyam is traditionally. It is performed by a solo dancer, who narrates a story through dance, often depicting themes from Hindu mythology and spiritual ideas. The dance form is characterized by its grace, purity, tenderness, and sculpturesque poses. It is usually performed to Carnatic music and involves a combination of rhythmic movements (nritta), expressive gestures (abhinaya), and storytelling (natya). Bharatanatyam has a rich history and has evolved over centuries, maintaining its traditional roots while also adapting to contemporary themes and styles.
"""


text-splitter = SemanticChunker(
    llm=GoogleGenAI(model_name="gemini-1.5-flash",breakpoint_threshold_type="standard_deviation", breakpoint_threshold=1.0),
    chunk_size=300
)
result=text-splitter.split_text(text)
print(result)
print(f"Total Chunks: {len(result)}")
