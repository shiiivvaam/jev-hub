# Voice control: community builds with Jev

9 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/voice-control).

## [Voice-controlled computer use for the Mac](https://x.com/instantricecook/status/2100814590300889426)
By [Andy Gao](https://x.com/instantricecook), 2026-09-18

Dictate a command and the Mac starts acting on it before the sentence is finished.

How Jev is used: Jev reads the transcript as it streams in and picks the next on-screen action, fast enough that the app opens mid-sentence.

## [On-device voice pipeline with Jev picking the models](https://x.com/desertantlabs/status/2102423007494889785)
By [Desert Ant Labs](https://x.com/desertantlabs), 2026-09-22

A demo that turns voice memos into to-do lists and meetings into redacted transcripts.

How Jev is used: Models for language detection, transcription and removing personal data run on the device, and Jev makes about 20 decisions in one call to choose which to run.

## [Tool calling that starts before you finish speaking](https://x.com/BhosalePratim/status/2100986774742765991)
By [Pratim Bhosale](https://x.com/BhosalePratim), 2026-09-18

An experiment replacing the language model's tool-choice step with Jev.

How Jev is used: Jev picks the tool instead of an LLM, which the author found lets the agent act before the user finishes the sentence.

## [Controlling Figma by voice](https://x.com/mikegee/status/2100845388655960112)
By [mikegee](https://x.com/mikegee), 2026-09-18

Spoken commands drive Figma directly.

How Jev is used: Jev maps each spoken command to a Figma action. The author reports a total cost of one cent from first line of code to the recorded demo.

## [Jev Voice: talk to your Mac](https://github.com/kevinbadi/jev-voice)
By [Kev Builds](https://github.com/kevinbadi), 2026-09-18

Speak and the Mac opens apps, types, searches, scrolls and presses keys.

How Jev is used: Speech is transcribed locally; one Jev call of about 250 ms turns the transcript into a typed action and its arguments.

## [An always-on voice assistant with no wake word](https://x.com/_MaxBlade/status/2100967959879471519)
By [Max Blade](https://x.com/_MaxBlade), 2026-09-18

A computer assistant that listens all the time and decides when you are talking to it.

How Jev is used: Jev uses probabilities to tell a command from idle talk, which the author says makes an ambient assistant possible.

## [talkr: a speech coach built on Jev](https://x.com/0xaniol/status/2101076982373191927)
By [aniol](https://x.com/0xaniol), 2026-09-18

A speaking-practice app.

How Jev is used: It gives you a topic and you talk for 30 seconds, then Jev analyses pauses, filler words, repetition, confidence and clarity and gives a score and feedback.

## [A voice computer assistant with a Swift accessibility app](https://x.com/marckohlbrugge/status/2100930430690050336)
By [Marc Köhlbrugge](https://x.com/marckohlbrugge), 2026-09-18

An early computer assistant that acts on what you say.

How Jev is used: Local Whisper transcribes, Jev classifies the action, and a small Swift app supplies the screen's accessibility tree. The author says it would be fully private if Jev ran locally.

## [voice-browser: it acts before you finish the sentence](https://github.com/moritzkremb/jev-voice-browser)
By [Moritz Kremb](https://github.com/moritzkremb), 2026-09-17

Controls a real browser by voice, word by word.

How Jev is used: On every partial transcript, Jev answers a dozen questions (intent, target, is the command complete, is it destructive) in about 300 ms, and code decides whether to act, wait or ask.

