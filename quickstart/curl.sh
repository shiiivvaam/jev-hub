#!/usr/bin/env bash
# Needs your own TypeSafe API key: export TYPESAFE_API_KEY=...
curl -s https://api.typesafe.ai/v1/systemone \
  -H "Authorization: Bearer $TYPESAFE_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
