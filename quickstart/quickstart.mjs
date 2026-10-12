// Sends request.json to Jev and prints the answer. Node 18+, no dependencies.
// Needs your own TypeSafe API key: export TYPESAFE_API_KEY=...
import { readFileSync } from "node:fs"

const body = readFileSync(new URL("./request.json", import.meta.url), "utf8")
const res = await fetch("https://api.typesafe.ai/v1/systemone", {
  method: "POST",
  headers: { Authorization: `Bearer ${process.env.TYPESAFE_API_KEY}`, "Content-Type": "application/json" },
  body,
})
console.log(JSON.stringify(await res.json(), null, 2))
