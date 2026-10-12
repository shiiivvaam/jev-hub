# Jev for agent and browser decisions

Yes, for the choice steps. Agents spend much of their time picking the next action from a known list. Jev can make that pick in tens to hundreds of milliseconds while a language model handles planning and writing. Reported browser-agent runs cost fractions of a cent per task.

**Fit:** Partial fit

**Good when**
- Your agent repeatedly chooses from a known set of actions or elements.
- Latency matters: games, browsers, real-time systems.
- You already use a language model for planning and want to cut its calls.

**Avoid when**
- The step requires writing, coding or multi-step reasoning. Jev can't plan.
- The set of possible actions isn't known in advance.

## Example request

Send this to `POST https://api.typesafe.ai/v1/systemone` with your own TypeSafe API key (`Authorization: Bearer <your key>`). The body is in [`agent-decisions.json`](./agent-decisions.json):

```json
{
  "model": "jev-latest",
  "state": "Goal: Book the cheapest nonstop SFO→JFK on Oct 12.\nPage: Search results. Visible elements: [1] Sort by price, [2] Nonstop filter, [3] First result $412 (1 stop), [4] Next page",
  "questions": {
    "next_action": {
      "type": "choice",
      "instructions": "Which element should the agent click next to make progress on the goal?",
      "criteria": {
        "1": "Sort by price",
        "2": "Nonstop filter",
        "3": "First result",
        "4": "Next page"
      }
    },
    "goal_done": {
      "type": "noul",
      "instructions": "Has the goal been fully completed on this page?"
    }
  }
}
```

## How to wire it in
1. Let your planner (a text model) decide the goal and sub-goal.
2. At each step, send the goal plus the list of visible elements to Jev as a Choice.
3. Fall back to the text model when confidence is low or no option fits.

## Common mistakes
- Large pages mean large state. Send the element list, not the raw HTML.
- Watch the 32k-token limit on state plus the longest question.

Full write-up, with the cost for your own volume: https://jevhub.io/use-cases/agent-decisions
