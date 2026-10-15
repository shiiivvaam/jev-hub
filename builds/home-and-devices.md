# Home and devices: community builds with Jev

7 projects, each credited to its author and linked to the original. Jev Hub has not tested them: read the source before relying on one. Browse them all with filters on [jevhub.io/builds](https://jevhub.io/builds/topic/home-and-devices).

## [Jev as Policy: MuJoCo robot control studio](https://github.com/YuanKJing/Jev-as-Policy)
By [Junqi(Junairi) Jing](https://github.com/YuanKJing), 2026-09-21

A reproduction of a public control structure where Jev acts as a robot's policy.

How Jev is used: Text state becomes a Jev intent, then motor choices, then inverse kinematics in MuJoCo, with recording and a studio-style web panel. The demo task is to grasp an orange.

## [EmbodiedJev: a robot decision workbench](https://github.com/FBddcz/embodied-jev)
By [a bo](https://github.com/FBddcz), 2026-09-20

A MuJoCo workbench for trying decision models on three simulated robot tasks.

How Jev is used: It compares local small models with Jev and other model APIs on observe, decide, execute and feedback loops, and shows speed and cost. The page is mostly in Chinese.

## [Dasheng: read English aloud and see which words you got wrong](https://github.com/wquguru/dasheng)
By [WquGuru](https://github.com/wquguru), 2026-09-20

A practice tool that listens to you read an English passage and marks mispronounced words as you go.

How Jev is used: A streaming speech model listens and Jev judges each word, so wrong words turn red in real time and a total score appears at the end. The page is mostly in Chinese.

## [RoboJEV: two-stage Jev control of a Franka robot arm](https://github.com/lykycy123/RoboJEV)
By [Yuke Liu](https://github.com/lykycy123), 2026-09-20

A small robotics lab that controls a simulated Franka Panda arm.

How Jev is used: Jev receives structured simulator state rather than images, picks an intent, then picks directions, and code does the motion maths.

## [A Mac app that files your downloads by rule](https://x.com/marcelpociot/status/2100906882365788167)
By [Marcel Pociot 🧪](https://x.com/marcelpociot), 2026-09-18

A macOS app that watches the Downloads folder and applies customisable rules.

How Jev is used: Jev decides whether a file is an invoice, for example, and the app moves it and renames it, with no other model calls.

## [A two-arm robot controlled with Jev](https://x.com/Raptor_zip/status/2101091398447505567)
By [ラプター | 高専 ロボコン ビジコン](https://x.com/Raptor_zip), 2026-09-18

A robotics write-up in Japanese where Jev handles one layer of a three-layer control system.

How Jev is used: Jev takes the decision layer while code handles inverse kinematics and physics. The author reports 500 ms responses and about 0.5 yen per trial.

## [Jev for Home Assistant](https://github.com/AboveColin/HA-Jev)
By [Colin de Vries](https://github.com/AboveColin), 2026-09-17

Ask your house a question and get a number back you can automate on.

How Jev is used: Questions become sensors (a probability, a choice or a score), with actions for automations and a conversation agent.

