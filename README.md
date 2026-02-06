# Topic Extraction Tool

A Streamlit application that extracts key topics from long text documents using OpenAI's Language Models (LLMs).

## Features

- 📝 **Long Text Processing**: Handle large documents efficiently
- 🤖 **LLM-Powered**: Uses OpenAI's GPT models for intelligent topic extraction
- ⚙️ **Configurable**: Adjust number of topics, model selection, temperature, and more
- 📊 **Detailed Results**: Get topics with descriptions, confidence scores, and key phrases
- 💾 **Export Options**: Download results as JSON or CSV
- 📈 **Summary Statistics**: View average confidence, max confidence, and more

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bhagyashreeb12/topic_extraction.git
cd topic_extraction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API Key:
   - Get your API key from [OpenAI Platform](https://platform.openai.com/account/api-keys)
   - Copy `.env.example` to `.env` and add your key
   - Or provide it directly in the app sidebar

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### How to Use:

1. **Enter API Key**: Paste your OpenAI API key in the sidebar
2. **Configure Settings**:
   - Select your preferred LLM model
   - Choose number of topics to extract (1-10)
   - Adjust temperature for creativity level
3. **Paste Text**: Insert the long text you want to analyze
4. **Extract Topics**: Click the "Extract Topics" button
5. **View Results**: Explore extracted topics with confidence scores
6. **Download**: Export results as JSON or CSV

## Configuration Options

- **Model Selection**: Choose between gpt-3.5-turbo, gpt-4, or gpt-4-turbo-preview
- **Number of Topics**: Extract between 1-10 main topics
- **Temperature**: Control randomness (0.0 = deterministic, 1.0 = creative)
- **Max Tokens**: Limit response length (100-2000)

## Output Format

Each extracted topic includes:
- **Topic Name**: Concise topic title (1-3 words)
- **Description**: Brief explanation of the topic
- **Confidence Score**: Relevance score from 0.0 to 1.0
- **Key Phrases**: Important phrases related to the topic

## Requirements

- Python 3.8+
- OpenAI API key (with active credits)
- Internet connection

## File Structure

```
topic_extraction/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables
└── README.md          # This file
```

## License

MIT License

## Support

For issues or questions, please open an issue on the GitHub repository.
```

## How to Use:

1. **Push these files to your repository** using the code provided above
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Get an OpenAI API key** from [platform.openai.com](https://platform.openai.com/account/api-keys)

4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

5. **Use the app**:
   - Enter your API key in the sidebar
   - Configure your preferences (model, number of topics, temperature)
   - Paste your long text
   - Click "Extract Topics"
   - Download results as JSON or CSV

## Key Features:

✅ **Multi-model support** (GPT-3.5, GPT-4, GPT-4-turbo)
✅ **Configurable parameters** (temperature, tokens, topic count)
✅ **Confidence scoring** for each topic
✅ **Key phrases extraction**
✅ **Export functionality** (JSON & CSV)
✅ **Text statistics** (word/character count)
✅ **Beautiful UI** with tabs and expandable sections
✅ **Error handling** and validation
