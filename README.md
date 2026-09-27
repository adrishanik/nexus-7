# Nexus-7 ## Autonomous Humanoid Edge-AI Robotic Assistant ![Status](https://img.shields.io/badge/Status-Pre--Prototype-yellow) ![Open Source](https://img.shields.io/badge/Open%20Source-MIT-green) ![Compute](https://img.shields.io/badge/Compute-Orange%20Pi%205%20Plus%2016GB-blue) ![Edge AI](https://img.shields.io/badge/AI-Edge%20%2F%20Local%20AI-purple) ![Funding](https://img.shields.io/badge/Funding-Seeking-orange) --- # ⚠️ Project Status **PRE-PROTOTYPE — THE PHYSICAL ROBOT HAS NOT BEEN BUILT YET** Nexus-7 is a proposed open-source robotics project focused on building an autonomous robotic assistant using local/edge AI, computer vision, speech processing, sensors, and robotic motion. The system architecture, hardware plan, software prototypes, configuration, and bill of materials have been prepared. The physical Nexus-7 robot has **not** been built yet. The next goal is to obtain the required hardware and turn this design into a working physical prototype. --- # 🤝 Sponsorship Opportunity I am currently looking for: - Hardware sponsors - Component sponsors - Partial hardware funding - Full prototype funding - Technical support - Development support ## 💰 Planned Hardware Budget **Approximately $577 USD** The planned budget will be used for components required to build and test the first prototype. The complete planned bill of materials is available in [`BOM.csv`](BOM.csv). --- # 💡 What Can a Sponsor Support? A sponsor does not need to fund the entire project. Support can be provided through: - Individual component sponsorship - Multiple-component sponsorship - Partial hardware funding - Full prototype funding - Technical sponsorship - Development support Even one sponsored component can help move Nexus-7 from the design stage toward a physical prototype. --- # 🤖 What Is Nexus-7? Nexus-7 is a proposed robotic platform combining: - Edge/local AI - Computer vision - Speech recognition - Text-to-speech - Robotic motion - Servo-controlled mechanisms - Environmental sensing - Local processing - Human-robot interaction The long-term goal is to explore how robotics and AI can work together while keeping important AI processing locally on the robot instead of depending entirely on cloud services. ### Core Technologies **Robotics + Edge AI + Computer Vision + Speech + Embedded Systems** --- # 📊 Current Development Status Nexus-7 is currently a **design and software-prototype project**. The physical robot has **not** been constructed. ### Completed - ✅ Robot concept - ✅ System architecture - ✅ Hardware plan - ✅ Bill of materials - ✅ Software architecture - ✅ Configuration - ✅ Initial software prototypes ### In Development - 🟡 Servo-control prototype - 🟡 Local AI software prototype - 🟡 Robot orchestration - 🟡 Motor-control structure ### Waiting for Hardware - 🔴 Physical chassis - 🔴 Physical servo system - 🔴 Cameras - 🔴 Audio hardware - 🔴 Sensors - 🔴 Physical AI testing - 🔴 Complete robot - 🔴 First physical demonstration **Important:** Planned features are not represented as completed hardware capabilities. --- # 🧠 Proposed System Architecture The planned system will work approximately like this: ```text ┌─────────────────┐ │ Microphones │ └────────┬────────┘ │ ▼ ┌─────────────────┐ │ Speech │ │ Recognition │ └────────┬────────┘ │ ▼ ┌─────────────────┐ │ Local / Edge │ │ AI │ └────────┬────────┘ │ ┌──────────────┼──────────────┐ │ │ │ ▼ ▼ ▼ ┌──────────┐ ┌──────────┐ ┌──────────┐ │ TTS │ │ Display │ │ Motion │ └──────────┘ └──────────┘ └──────────┘ ▲ │ ┌──────┴───────┐ │ Cameras │ │ + Sensors │ └──────────────┘ 

This architecture is a proposal and will be validated and modified during physical prototype development.

🖥️ Planned Computing Platform 

The current hardware plan uses an:

Orange Pi 5 Plus — 16 GB RAM

The intended responsibilities include:

Robot software Local AI inference Computer vision Speech processing Sensor processing Robot-control coordination 

Actual performance and AI acceleration will be measured after the physical hardware is acquired.

⚙️ Planned Hardware Computing Orange Pi 5 Plus 16 GB Robotics ST3215 serial bus servos Tracked chassis Motor-control hardware Mechanical components Vision Dual-camera setup Stereo/depth perception Audio Microphone/audio system Speaker/audio output Interaction Display Buttons and controls Environmental sensors Power Battery system Power-management components Supporting electrical components 

All hardware listed above is planned hardware and has not been represented as already purchased or assembled.

💰 Prototype Funding Plan 

The project will be developed in several stages.

Phase 1 — Core Hardware 

Build the basic computing and movement platform.

Planned components:

Main computer Servo system Chassis Motor-control hardware Power system Essential mechanical components Phase 2 — Perception 

Add:

Stereo cameras Microphones IMU Additional sensors Phase 3 — Interaction 

Add:

Display Audio output Additional interaction hardware Phase 4 — AI and Software Integration 

Integrate:

Local AI Speech recognition Text-to-speech Computer vision Sensor processing Robot control Phase 5 — Testing 

Measure:

AI response latency Speech recognition performance Servo positioning Motor response Camera performance Battery runtime System temperature Power consumption Emergency-stop response Overall system stability Phase 6 — Public Demonstration 

After the prototype is working:

Publish build documentation Publish test results Create demonstration videos Document lessons learned Improve the open-source design 📈 Funding Status 

Prototype hardware target: ~$577 USD

Currently funded: $0

Remaining target: ~$577 USD

Funding figures will be updated as components are sponsored or purchased.

Components Seeking Sponsorship Orange Pi 5 Plus ST3215 servos Tracked chassis Stereo cameras Audio hardware Display Power hardware Sensors Mechanical materials 🤝 Why Support Nexus-7? 

Nexus-7 is being developed as an open-source student robotics project.

The project aims to document the development process from:

Hardware Selection ↓ Mechanical Design ↓ Electronics ↓ Embedded Software ↓ Edge AI ↓ System Integration ↓ Testing ↓ Public Demonstration 

Hardware sponsorship can help transform the engineering plan into a physical prototype.

The development process will be publicly documented so that students, makers, and robotics enthusiasts can learn from the project.

🎁 Sponsor Recognition 

Depending on the type of sponsorship, sponsor recognition may include:

Sponsor acknowledgement in this repository Sponsor acknowledgement in project documentation Product attribution where appropriate Development updates Prototype demonstration videos after hardware is available Link to the sponsor's official website or product page Mention in project presentations where appropriate 

Specific sponsor benefits will be agreed upon before sponsorship is accepted.

🧩 Component Sponsorship 

A sponsor does not need to provide the entire project budget.

The project can be supported at different levels:

One Component ↓ One Subsystem ↓ Multiple Components ↓ Complete Prototype 

This allows hardware manufacturers and other supporters to contribute to the part of the project that best matches their products or interests.

📁 Repository Contents nexus-7/ │ ├── README.md ├── BOM.csv ├── LICENSE ├── config.json ├── requirements.txt │ ├── hardware/ │ └── ... │ └── scripts/ ├── main_robot.py ├── servo_controller.py ├── motor_driver.py ├── llm_engine.py └── face_display.py 

The repository will expand as development progresses.

💻 Software Prototype 

The repository contains early software prototypes for the planned robot architecture.

Current software work includes:

Robot orchestration Servo communication Motor-control structure Local AI communication Display-state management Configuration 

Some modules currently contain simulation, placeholder, or hardware-independent functionality because the physical prototype has not yet been built.

Physical hardware validation will be added after the required components are obtained.

🧪 Prototype Success Criteria 

The first physical prototype will be evaluated using measurable tests.

Planned measurements include:

Servo positioning accuracy Motor response AI response latency Speech recognition latency Text-to-speech latency Camera/depth performance Battery runtime System temperature Power consumption Emergency-stop response Overall system stability 

Measured results will be added to the repository as development progresses.

🗺️ Development Roadmap [1] System Architecture ↓ [2] Hardware BOM ↓ [3] Sponsorship / Funding ↓ [4] Acquire Components ↓ [5] Mechanical Assembly ↓ [6] Electronics Integration ↓ [7] Software Bring-Up ↓ [8] Edge-AI Integration ↓ [9] Testing & Optimization ↓ [10] First Nexus-7 Prototype ↓ [11] Public Demonstration 🔬 Open-Source Development 

The goal is to document the project openly.

As development progresses, the repository will contain:

Source code Configuration Hardware documentation CAD/design files where appropriate Testing results Development notes Build documentation Project updates 

The project is intended to make the development process useful to other students and makers.

⚠️ Safety 

Nexus-7 will involve:

Motors Servos Batteries Power electronics Moving mechanical parts 

Physical construction and testing will follow appropriate manufacturer safety instructions.

Battery, high-current electrical work, and mechanical testing should be performed with appropriate adult or qualified supervision.

Safety systems, including an emergency-stop mechanism, will be considered part of the physical prototype design.

📦 Bill of Materials 

The complete planned component list is available here:

BOM.csv

The BOM represents the planned prototype requirement, not hardware that has already been purchased or assembled.

Prices may change depending on supplier, shipping, and availability.

📈 What Happens After Sponsorship? 

After receiving the required hardware, development will be documented in stages.

1. Component Verification 

Verify that all sponsored components are compatible.

2. Hardware Assembly 

Build the first physical platform.

3. Software Bring-Up 

Test each subsystem individually.

4. AI Integration 

Connect local AI with the physical robot.

5. Testing 

Measure performance and identify problems.

6. Documentation 

Publish results and lessons learned.

7. Demonstration 

Create a working prototype demonstration.

The objective is to make the development process transparent rather than simply presenting a final result.

🌟 Long-Term Vision 

The long-term vision is to develop Nexus-7 into a more capable open-source robotics platform combining:

Edge AI + Robotics + Computer Vision + Speech + Embedded Systems

Future versions may explore:

Better perception More capable local AI Improved mobility More advanced manipulation Better human-robot interaction Additional sensors Improved power efficiency More autonomous behavior 

These are future goals and are not claimed as currently implemented capabilities.

📬 Sponsorship 

If you are a hardware manufacturer, robotics company, technology company, maker organization, or individual interested in supporting Nexus-7, sponsorship can be provided through:

Hardware/components Partial hardware funding Full prototype funding Technical support Development support 

The current planned hardware target is approximately $577 USD.

For sponsorship discussions, please use the contact method listed on my GitHub profile.

📜 License 

The software in this repository is released under the MIT License.

See LICENSE for the complete license text.

Hardware and CAD licensing will be documented separately where applicable.

⭐ Support the Project 

Nexus-7 is currently at the stage where the design exists, but the physical prototype still needs to be built.

Hardware sponsorship or project funding can help move the project from the design stage toward a working physical prototype.

Design on GitHub ↓ Hardware Sponsorship ↓ Physical Prototype ↓ Testing ↓ Open-Source Documentation ↓ Working Nexus-7 Robot 📌 Project Summary 

Current stage: Pre-prototype

Physical robot: Not built

Hardware funding: Seeking

Planned hardware budget: ~$577 USD

Project type: Open-source student robotics / Edge AI

Repository: Nexus-7

