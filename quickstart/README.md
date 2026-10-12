# Quickstart

Send one request to Jev and read the answer. You need your own TypeSafe API key ([TypeSafe's quickstart](https://docs.typesafe.ai/introduction/quickstart) shows how to get one). Jev Hub does not provide keys or run Jev for you.

`request.json` is the email-triage example: one email, three typed questions. Pick any of the other [examples](../examples) and swap it in.

```bash
export TYPESAFE_API_KEY=your-key
bash curl.sh            # curl
python3 quickstart.py   # Python, no dependencies
node quickstart.mjs     # Node 18+, no dependencies
```

Each one sends the same request to `POST https://api.typesafe.ai/v1/systemone` and prints what comes back. See [TypeSafe's API reference](https://docs.typesafe.ai/api) for every field.
