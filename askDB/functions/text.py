def truncate(text: str, length=300) -> str:
    return text if len(text) < length else text[:length]
