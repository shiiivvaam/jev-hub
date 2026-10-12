# Email and messages: community builds with Jev

7 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/email-and-messages).

## [Jevmail: open-source Gmail triage](https://github.com/fazlerocks/jevmail)
By [Syed Fazle Rahman](https://github.com/fazlerocks), 2026-09-19

Sorts a Gmail inbox into Needs reply, Updates, Promos, Sales and Spam, read-only and running locally.

How Jev is used: Jev classifies each message and gives an urgency score; the author reports 1,000 emails in about a minute for around three cents.

## [Mail for Omarchy](https://github.com/petrzpav/omarchy-mail)
By [Pavel Petržela](https://github.com/petrzpav), 2026-09-29

A terminal Gmail client that files your inbox and checks your replies before you send them.

How Jev is used: Jev files messages into Gmail labels only when confident and leaves personal or unclear mail in the inbox; it also reviews drafts.

## [Gmail filters in plain English](https://github.com/ziyacivan/jev-mail-filter)
By [Yusuf Ziya Cıvan](https://github.com/ziyacivan), 2026-09-27

Gmail filters written as sentences, plus a morning digest and follow-up reminders.

How Jev is used: Jev reads every new email and labels, stars, archives or flags it as phishing according to your sentence rules. One Apps Script file, no server.

## [In-Basket Triage for patient messages](https://github.com/Stephonomon/inbasket-triage)
By [Stephon Proctor](https://github.com/Stephonomon), 2026-09-23

A synthetic demo that sorts patient-portal messages for a clinic.

How Jev is used: Jev reads each message once and answers 26 questions (urgency, category, owner, flags, which prompt snippets the reply drafter needs); code routes it and an LLM drafts the reply.

## [Jev-Mail: always-on Gmail classification](https://github.com/vynnlee/jev-mail)
By [Seongbeen Lee](https://github.com/vynnlee), 2026-09-20

Gmail classification that runs continuously on Google Apps Script.

How Jev is used: Jev classifies new mail around the clock; setup is managed from a command line and uses your own Google Cloud project.

## [Jev Triage: message triage in Go](https://github.com/boldbug1/jev-triage)
By [Boldbug](https://github.com/boldbug1), 2026-09-20

A command-line tool that sorts messages by type and urgency and writes an HTML report.

How Jev is used: Jev answers three questions per message (kind, urgency, frustration); low-confidence messages go to a separate review list.

## [Jev Mail Classifier](https://github.com/parth-kp/jev-mail-classifier)
By [Parth Kishorbhai Patel](https://github.com/parth-kp), 2026-09-19

Tags, moves, flags and notifies on incoming mail, all driven by a config file.

How Jev is used: Jev classifies each message and the config decides what happens to each class.

