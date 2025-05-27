import re
import pandas as pd

def clean_comment(text_comment: str) -> str:
    if pd.isna(text_comment):
        return ""
    text_comment = text_comment.lower()
    text_comment = re.sub(r'[^\w\s]', '', text_comment)
    text_comment = text_comment.strip()
    return text_comment

def preprocess_comments(df: pd.DataFrame, comment_col: str = 'comment') -> pd.DataFrame:
    df['cleaned_comment'] = df[comment_col].astype(str).apply(clean_comment)
    return df
