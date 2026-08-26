# Multimodal RAG

A Python-based foundation for a **Multimodal Retrieval-Augmented Generation (RAG)** application. The project is intended to ingest knowledge from multiple content types—such as text documents, images, and tabular data—store searchable representations of that content, retrieve the most relevant context for a question, and use it to produce grounded answers.

## Project goals

- Ingest and process multimodal source material.
- Create embeddings and store them in a vector database.
- Retrieve relevant context for a user query.
- Provide that context to a language model to generate source-grounded answers.
- Keep configuration and credentials outside version control.

## Planned workflow

```text
Source files → extraction/chunking → embeddings → vector store
                                                ↓
User question → query embedding → relevant context → LLM answer
```

## Requirements

- [Python 3.12](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/), used for Python installation and virtual-environment management
- Git (recommended)

The project uses a local virtual environment named `env`. It is excluded from Git, along with the local `.env` configuration file.

## Set up the development environment

From the project root in Windows Command Prompt (`cmd`), first list the Python versions managed or available through `uv`:

```cmd
uv python list
```

Create the project virtual environment with Python 3.12:

```cmd
uv venv env --python 3.12
```

This creates the environment in the `env` directory. To activate it in Windows Command Prompt:

```cmd
env\Scripts\activate.bat
```

After activation, confirm that the environment uses Python 3.12:

```cmd
python --version
```

To leave the environment when you are done:

```cmd
deactivate
```

> Command Prompt does not require PowerShell execution-policy configuration to activate the environment.

## Install dependencies

There is no dependency manifest in the repository yet. Once a `pyproject.toml` is added, install or synchronize the project dependencies with:

```cmd
uv sync
```

For a one-off package installation during development, use:

```cmd
uv pip install <package-name>
```

## Configuration

Create a local `.env` file for API keys, model settings, vector-database connection details, and other machine-specific configuration. Never commit real secrets. Example placeholders:

```env
# LLM_API_KEY=your_api_key
# VECTOR_DB_URL=your_vector_database_url
# EMBEDDING_MODEL=your_embedding_model
```

## Repository layout

```text
.
├── env/           # Local Python 3.12 virtual environment (not committed)
├── .env           # Local configuration and secrets (not committed)
├── .gitignore     # Excludes env/ and .env
└── README.md      # Project documentation
```

## Next steps

1. Add a `pyproject.toml` file and declare project dependencies.
2. Add modules for document ingestion, multimodal processing, embeddings, retrieval, and answer generation.
3. Choose and configure a vector database and language-model provider through `.env`.
4. Add tests and a command-line or web interface for querying the RAG pipeline.
