
# 🎬 Movie Information Extractor

A simple AI-powered web application that extracts structured movie information from a text paragraph using **LangChain**, **Groq**, **Pydantic**, and **Streamlit**.

## 📌 About the Project

The Movie Information Extractor takes a paragraph containing movie details and extracts the information into a structured format using a large language model.

It uses Pydantic to define the movie data schema and validate the model's output.

## ✨ Features

- Extract movie titles
- Identify release years
- Extract movie genres
- Identify directors
- Extract cast information
- Retrieve movie ratings when mentioned
- Generate movie summaries
- Display extracted information through a Streamlit web interface
- View the extracted data as structured JSON

## 🛠️ Technologies Used

- **Python** – Programming language
- **Streamlit** – Web interface
- **LangChain** – LLM integration and prompt management
- **Groq** – Hosted language model inference
- **Pydantic** – Structured data validation
- **python-dotenv** – Environment variable management

## 📂 Project Structure

```text
movie-information-extractor/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/movie-information-extractor.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Navigate to the project directory

```bash
cd movie-information-extractor
```

### 3. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure your Groq API key

Create a `.env` file in the project root directory and add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from the [Groq Console](https://console.groq.com/keys).

**Important:** Never upload your `.env` file or expose your API key publicly.

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

http://localhost:8501

## 🚀 How to Use

1. Open the Movie Information Extractor application.
2. Enter a paragraph containing movie information.
3. Click **Extract Movie Information**.
4. View the extracted movie details.
5. Expand the structured JSON section to inspect the output.

## 📝 Example Input

> Inception is a science fiction film released in 2010, directed by Christopher Nolan. It stars Leonardo DiCaprio, Joseph Gordon-Levitt, and Tom Hardy. The story follows a skilled thief who enters people's dreams to steal secrets. The film received an IMDb rating of approximately 8.8 out of 10.

## 📊 Information Extracted

The application extracts the following fields:

| Field | Description |
|---|---|
| Title | Name of the movie |
| Release Year | Year of release |
| Genre | Movie genres |
| Director | Director's name |
| Cast | Actors in the movie |
| Rating | Movie rating, when provided |
| Summary | Brief movie description |

The extracted values depend on the information in the input paragraph and the model's response.

## 🧠 How It Works

1. The user enters a movie-related paragraph.
2. LangChain formats the prompt with the required output instructions.
3. The Groq-hosted language model processes the paragraph.
4. PydanticOutputParser parses the response into the `Movie` Pydantic model.
5. Streamlit displays the extracted information.

## 🔐 Environment Variables

The application requires a Groq API key to access the model.

Keep credentials in `.env` and ensure that `.env` is listed in `.gitignore`.

This project is available for educational and personal learning purposes. Add a license file if you intend to distribute it under specific reuse terms.
