# Voice control: community builds with Jev

9 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/voice-control).

## [Voice-controlled computer use for the Mac](https://x.com/instantricecook/status/2100814590300889426)
By [Andy Gao](https://x.com/instantricecook), 2026-09-18

Dictate a command and the Mac starts acting on it before the sentence is finished.

How Jev is used: Jev reads the transcript as it streams in and picks the next on-screen action, fast enough that the app opens mid-sentence.

## [partway: voice control that acts mid-sentence](https://github.com/tostechbr/partway)
By [Tiago Oliveira](https://github.com/tostechbr), 2026-09-23

A macOS voice-control app that starts acting partway through what you say.

How Jev is used: Jev is asked about every word as you speak and answers in about 200 ms, so the app acts early and waits only when it must.

## [Jev VAD: turn detection for voice agents](https://github.com/AgoraIO-Community/convoai-jev-vad)
By [Agora Community](https://github.com/AgoraIO-Community), 2026-09-23

Client-side turn detection for Agora's Conversational AI.

How Jev is used: A simple sound gate opens the turn; Jev then decides from the live transcript whether the user is done, talking to the agent at all, or really interrupting.

## [Tool calling that starts before you finish speaking](https://x.com/BhosalePratim/status/2100986774742765991)
By [Pratim Bhosale](https://x.com/BhosalePratim), 2026-09-18

An experiment replacing the language model's tool-choice step with Jev.

How Jev is used: Jev picks the tool instead of an LLM, which the author found lets the agent act before the user finishes the sentence.

## [Controlling Figma by voice](https://x.com/mikegee/status/2100845388655960112)
By [mikegee](https://x.com/mikegee), 2026-09-18

Spoken commands drive Figma directly.

How Jev is used: Jev maps each spoken command to a Figma action. The author reports a total cost of one cent from first line of code to the recorded demo.

## [Voice-controlled browser agent](https://x.com/yatharth170699/status/2100986863788159191)
By [Yatharth Verma](https://x.com/yatharth170699), 2026-09-18

Tell it what to do and it navigates the browser for you.

How Jev is used: Jev turns each spoken instruction into the next browser action.

## [Jev Voice: talk to your Mac](https://github.com/kevinbadi/jev-voice)
By [Kev Builds](https://github.com/kevinbadi), 2026-09-18

Speak and the Mac opens apps, types, searches, scrolls and presses keys.

How Jev is used: Speech is transcribed locally; one Jev call of about 250 ms turns the transcript into a typed action and its arguments.

## [Jev Voice: a menu-bar app for the Mac](https://github.com/chris-wozniczek/jev-voice-control)
By [chris-wozniczek](https://github.com/chris-wozniczek), 2026-09-18

Hold a key, speak a command, and the Mac carries it out.

How Jev is used: Speech becomes text, Jev returns a typed decision with probabilities, and the app performs the matching macOS action.

## [voice-browser: it acts before you finish the sentence](https://github.com/moritzkremb/jev-voice-browser)
By [Moritz Kremb](https://github.com/moritzkremb), 2026-09-17

Controls a real browser by voice, word by word.

How Jev is used: On every partial transcript, Jev answers a dozen questions (intent, target, is the command complete, is it destructive) in about 300 ms, and code decides whether to act, wait or ask.

