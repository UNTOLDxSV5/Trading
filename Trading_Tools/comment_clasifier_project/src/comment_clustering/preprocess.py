import re
import pandas as pd
from src.logs.logger import logger  # Import the logger

def clean_comment(text_comment: str) -> str:
    """
    Clean a single comment string by lowercasing, removing punctuation, and stripping whitespace.

    Parameters
    ----------
    text_comment : str
        The comment string to be cleaned.

    Returns
    -------
    str
        The cleaned comment string.
    """
    if pd.isna(text_comment):
        return ""
    logger.info("Cleaning a comment.")
    text_comment = text_comment.lower()
    text_comment = re.sub(r'[^\w\s]', '', text_comment)
    text_comment = text_comment.strip()
    logger.info("Comment cleaned.")
    return text_comment

def preprocess_comments(df: pd.DataFrame, comment_col: str = 'comment') -> pd.DataFrame:
    """
    Preprocess the comments in a DataFrame by cleaning each comment.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame containing comments to be cleaned.
    comment_col : str, optional (default='comment')
        The name of the column containing the comments.

    Returns
    -------
    pandas.DataFrame
        The DataFrame with an additional 'cleaned_comment' column containing the cleaned comments.
    """
    logger.info("Starting comment preprocessing.")
    df['cleaned_comment'] = df[comment_col].astype(str).apply(clean_comment)
    logger.info("Comment preprocessing completed.")
    return df
