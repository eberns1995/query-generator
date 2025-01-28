from typing import List, Dict, Optional
from .preprocessor import TextPreprocessor
from .formatters import QueryFormatter

class QueryGenerator:
    """Main class for generating search queries from input text."""

    def __init__(self, 
                 use_spacy: bool = False,
                 language: str = 'en',
                 custom_stop_words: Optional[List[str]] = None):
        self.preprocessor = TextPreprocessor(use_spacy=use_spacy, language=language)
        self.custom_stop_words = set(custom_stop_words or [])

    def generate_query(self,
                      input_text: str,
                      search_engine: str = 'google',
                      fields: Dict[str, str] = None,
                      min_term_length: int = 2) -> str:
        """Generate a formatted search query from input text."""
        # Preprocess text
        processed_text = self.preprocessor.preprocess(input_text)
        
        # Extract terms and entities
        terms = [term for term in processed_text.split()
                if len(term) >= min_term_length
                and term not in self.custom_stop_words]
        
        entities = self.preprocessor.extract_entities(input_text)
        
        # Combine terms and entities
        all_terms = list(set(terms + entities))
        
        # Format query
        return QueryFormatter.format_query(
            terms=all_terms,
            search_engine=search_engine,
            fields=fields
        )