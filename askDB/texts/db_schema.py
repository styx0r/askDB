explanation: str = f"""
    For a database schema to be effectively interpreted and utilized by Language Learning Models (LLMs) like GPT-4, it's essential to present the schema in a clear, structured, and detailed format. Here are key aspects to consider for an LLM-friendly database schema format:

    1. **Use Plain Language Descriptions**: Describe each table and its purpose in simple, clear language. Avoid overly technical jargon unless necessary.
    2. **Detail Table Structures**: Clearly outline the structure of each table, including:
        - Table Name
        - Column Names
        - Data Types for each column (e.g., integer, varchar, date)
        - Any default values or constraints (e.g., primary keys, foreign keys, not null constraints)
    3. **Explain Relationships**: If there are relationships between tables (like foreign keys or many-to-many relationships), describe these clearly. Diagrams are helpful but should be accompanied by text explanations for LLMs.
    4. **Use Standard Formatting**: Present the schema in a commonly used format, such as SQL DDL (Data Definition Language) commands, tabular formats, or structured text.
    5. **Include Examples**: Provide examples of how data is stored or how tables are related. This can help in understanding the practical application of the schema.
    6. **Document Procedures and Functions**: If your schema includes stored procedures, functions, or triggers, describe their purpose and how they interact with the tables.
    7. **Version Information**: If relevant, include information about the specific database system and version the schema is designed for.
    8. **Contextual Information**: Provide any necessary context that might not be immediately obvious, such as the overall purpose of the database or specific business rules that impact the schema design.
    """
