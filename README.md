# Query Generator

A modular Python system for generating formatted search queries from text input. Supports multiple search engines and advanced NLP features.

## Features

- Advanced text preprocessing with NLTK and SpaCy support
- Named entity recognition
- Customizable query formatting for different search engines
- Field-specific search parameters
- Extensible architecture

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from query_generator import QueryGenerator

# Initialize with SpaCy support
generator = QueryGenerator(use_spacy=True)

# Generate a basic query
input_text = "AI technologies in healthcare and robotics"
query = generator.generate_query(input_text, search_engine='patents')

# Generate a query with field parameters
fields = {
    'year': '2020..2025',
    'type': 'patent'
}
query = generator.generate_query(input_text, search_engine='patents', fields=fields)
```

## Advanced Usage

See the documentation for advanced features and customization options.

## Testing

Run tests using pytest:

```bash
pytest tests/
```

## License

MIT License