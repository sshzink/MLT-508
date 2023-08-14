# Translator Flask API Documentation

## Translate a Word

You can use the API to translate a word from the source language to the target language.

- **Endpoint**: `/translate`
- **Method**: POST

### Request Format

To translate a word, send a POST request to the `/translate` endpoint with the following JSON data in the request body:

```json
{
  "word": "dog",
  "source_language": "en",
  "target_language": "fr"
}
```
If the translation is found, the API will respond with a JSON object containing the translation and the part of speech:

```json
{
  "translation": "chien",
  "pos": "NOUN"
}
```
If the translation is not found, the API will respond with an error message:
```json
{
  "message": "Translation not found"
}

```
## Example Usage

### Using the UI

You can interact with the API using a web browser. Open the provided HTML form and follow these steps:

1. Enter the word you want to translate in the "Word" field.
2. Select the source language from the dropdown menu.
3. Select the target language from the dropdown menu.
4. Click the "Translate" button.
5. The translation result will be displayed on the page.

### Using cURL

You can also interact with the API programmatically using the cURL command-line tool:

```bash
curl -X POST "http://localhost:5001/translate" -H "Content-Type: application/json" -d '{
  "word": "word_to_translate",
  "source_language": "source_language_code",
  "target_language": "target_language_code"
}'
```
Replace word_to_translate, source_language_code, and target_language_code with your desired values.