
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq",
)

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    ('system', """
Extract movie information from the paragraph
{format_instructions}
"""),
    ("human", "{paragraph}")
])

# Streamlit UI
st.title("🎬 Movie Information Extractor")

para = st.text_area("Give your paragraph:")

if st.button("Extract Movie Information"):

    if para:
        final_prompt = prompt.invoke(
            {
                "paragraph": para,
                "format_instructions": parser.get_format_instructions()
            }
        )

        with st.spinner("Extracting movie information..."):
            response = model.invoke(final_prompt)

        movie_data = parser.parse(response.content)

        st.subheader("Extracted Movie Information")
        st.write(movie_data)

    else:
        st.warning("Please enter a paragraph.")