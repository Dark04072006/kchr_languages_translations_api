# KCHR Languages Translations API

Welcome to the KCHR Languages Translations API! This project serves as an API dictionary for Russian to Caucasian expressions. Currently, it supports the Circassian and Karachay languages. The API provides a single endpoint for translations.

## Getting Started

To get started with the API, follow the instructions below.

### Prerequisites

Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Dark04072006/kchr_languages_translations_api.git
   ```

2. Navigate to the project directory:
   ```bash
   cd kchr_languages_translations_api
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

Before running the API, make sure to set the required environment variables in `start.sh`:

```bash
export DB_URL=REQUIRED
export SECRET_KEY=REQUIRED
```

## Usage

Run the API server using the `start.sh` script:
```bash
cd src && bash scripts/start.sh
```

The API will be accessible at `http://localhost:8000`.

## Endpoint

### `translations/`

This endpoint accepts the following query parameters:

- `word`: The word to search for translations.
- `variation`: The translation variation, e.g., `ru-cs` (Russian to Circassian), `ru-kr` (Russian to Karachay), `kr-ru` (Karachay to Russian), `cs-ru` (Circassian to Russian).
- `offset`: Offset for retrieving data from the database.
- `limit`: Limit for the number of results to retrieve (the difference between `offset` and `limit` should not exceed 20).

**Example Request:**
```http
GET /translations/?word=example&variation=ru-cs&offset=0&limit=10
```

**Example Response:**
```json
{
  "translations": [
    {
      "word": "example",
      "translation": "пример",
      "language": "ru-cs"
    },
    // More translations...
  ]
}
```