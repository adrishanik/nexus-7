# Nexus-7: Autonomous Humanoid Edge-AI Robotic Assistant

[![View PCB on KiCanvas](https://hack.club/pcb-badge)](https://kicanvas.org/?repo=https://github.com/adrishanik/nexus-7/tree/main/pcb)

![Tier](https://img.shields.io/badge/Stardance%20Tier-X--Tier%20($578)-purple.svg)
![Compute](https://img.shields.io/badge/SBC-Orange%20Pi%205%20Plus%20(16GB)-blue.svg)
![Actuators](https://img.shields.io/badge/Servos-10x%20ST3215%20Serial%20Bus-orange.svg)
![Edge AI](https://img.shields.io/badge/Edge%20AI-Offline%20TinyLlama%20+%20Whisper-green.svg)
![Vision](https://img.shields.io/badge/Vision-Dual%20IMX219%20Stereo%20Depth-red.svg)



Project Status: PRE-PROTOTYPE — PHYSICAL ROBOT NOT YET BUILT

Nexus-7 is a proposed open-source robotics project focused on building an autonomous robotic assistant powered by local/edge AI.

The architecture, hardware plan, software prototypes, configuration and bill of materials have been prepared. However, the physical Nexus-7 prototype has not yet been built.

The next step is to obtain the hardware required to turn this design into a working prototype.

## 🚀 Sponsorship Opportunity 

I am currently looking for hardware sponsors, component sponsors and project funding to build the first Nexus-7 prototype.

Funding target 

Planned hardware budget: approximately $577 USD

The funding will be used for the components required to build and test the prototype, including:

Edge-AI computing hardware High-torque bus servos Tracked chassis Stereo cameras Microphone/audio hardware Display Motor-control electronics Battery and power components Sensors Mechanical and 3D-printing materials Wiring and supporting components 

The complete planned bill of materials is available in BOM.csv.

## 💡 Sponsors can support 

A sponsor does not necessarily need to fund the entire project.

Support can be provided through:

Individual component sponsorship Multiple-component sponsorship Partial hardware funding Full prototype funding Technical sponsorship Development/project support 

Every sponsored component can help move the project from the design stage toward a physical prototype.

## 🤖 What Is Nexus-7? 

Nexus-7 is designed as a compact robotic platform combining:

Edge/local AI Computer vision Speech recognition Text-to-speech Robotic motion Servo-controlled mechanisms Environmental sensing Local processing Human-robot interaction 

The long-term goal is to create a robot that can process important AI functions locally rather than depending entirely on cloud services.

The project is intended to explore the combination of:

Robotics + Edge AI + Computer Vision + Speech + Embedded Systems

## ⚠️ Important Project Status 

Nexus-7 is currently a design and software-prototype project.

The physical robot has not been constructed yet.

Component / Feature Status Overall robot concept ✅ Designed System architecture ✅ Designed Hardware BOM ✅ Prepared Software architecture ✅ Prepared Configuration ✅ Prepared Servo-control prototype 🟡 Prototype Local AI software prototype 🟡 Prototype Robot orchestration 🟡 Prototype Motor hardware integration 🔵 Planned Physical chassis 🔴 Not built Physical servo system 🔴 Not built Cameras 🔴 Not acquired Audio hardware 🔴 Not acquired Physical AI testing 🔴 Not started Complete robot 🔴 Not built First prototype demonstration 🔴 Requires funding 

Planned features are not represented as completed hardware capabilities.

## 🧠 Proposed System Architecture 

The planned system will follow an architecture similar to:

┌─────────────────────┐ │ Microphones │ └──────────┬──────────┘ │ ▼ ┌─────────────────────┐ │ Speech Recognition │ └──────────┬──────────┘ │ ▼ ┌─────────────────────┐ │ Local / Edge │ │ AI │ └──────────┬──────────┘ │ ┌──────────┼──────────┐ ▼ ▼ ▼ ┌───────┐ ┌───────┐ ┌────────┐ │ TTS │ │Display│ │ Motion │ └───────┘ └───────┘ └────────┘ ▲ │ ┌──────────┴──────────┐ │ Cameras / Sensors │ └─────────────────────┘ 

This architecture will be validated and modified during physical prototype development.

## 🖥️ Planned Computing Platform 

The current hardware plan uses an Orange Pi 5 Plus with 16 GB RAM as the main computing platform.

The intended role of the computer is to handle:

Robot software Local AI inference Computer vision Speech processing Sensor processing Robot-control coordination 

Actual performance and AI acceleration will be measured after the physical hardware is acquired.

## ⚙️ Planned Hardware 

The current BOM contains the major components required for the first prototype.

Hardware Planned Purpose Status Orange Pi 5 Plus 16 GB Main edge-computing platform Seeking ST3215 bus servos Robotic movement/mechanisms Seeking Tracked chassis Robot mobility Seeking Stereo cameras Vision/depth perception Seeking Microphone/audio system Voice input Seeking Display Human-robot interaction Seeking Motor-control hardware Chassis movement Seeking Battery/power hardware Portable operation Seeking Sensors Environment and robot state Seeking Mechanical materials Physical construction Seeking 

See BOM.csv for the detailed planned bill of materials.

## 💰 Prototype Funding Plan 

The project is planned in several stages so that sponsorship can support the project progressively.

Phase 1 — Core Hardware 

Build the fundamental computing and movement platform.

Target:

Main computer Servo system Chassis Motor-control hardware Power system Essential mechanical components Phase 2 — Perception 

Add:

Stereo cameras Microphones IMU and other sensors Phase 3 — Interaction 

Add:

Display Audio output Additional interaction hardware Phase 4 — AI and Software Integration 

Integrate:

Local AI Speech recognition Text-to-speech Vision Sensor processing Robot control Phase 5 — Testing 

Measure:

AI response latency Speech recognition performance Servo positioning Motor response Camera performance Battery runtime System temperature Safety-system response Phase 6 — Public Demonstration 

After the prototype is working:

Publish build documentation Publish test results Create demonstration videos Document lessons learned Improve the open-source design 📊 Funding Status 

Prototype hardware target: ~$577 USD

Currently funded: $0

Remaining target: ~$577

Funding figures will be updated as components are sponsored or purchased.

Sponsored Components Component Sponsor Status Orange Pi 5 Plus — Seeking sponsor ST3215 servos — Seeking sponsor Chassis — Seeking sponsor Cameras — Seeking sponsor Audio hardware — Seeking sponsor Display — Seeking sponsor Power hardware — Seeking sponsor Sensors — Seeking sponsor 🤝 Why Sponsor Nexus-7? 

Nexus-7 is being developed as an open-source student robotics project.

The project aims to document the complete development process, from:

Hardware selection → Mechanical design → Electronics → Embedded software → Edge AI → System integration → Testing

A hardware sponsor can help transform a detailed engineering plan into a physical prototype.

The project will be publicly documented so that other students, makers and robotics enthusiasts can learn from the development process.

## 🎁 Sponsor Recognition 

Depending on the type and size of sponsorship, sponsor recognition can include:

Sponsor acknowledgement in this repository Sponsor acknowledgement in project documentation Sponsor/product attribution where appropriate Development updates Prototype demonstration videos after hardware is available Links to the sponsor's official website or product page Mention in project presentations where appropriate 

Specific sponsor benefits will be agreed upon with each sponsor before sponsorship is accepted.

## 🧩 Component Sponsorship 

A sponsor does not need to provide the entire $577 budget.

For example, a company could sponsor:

One component ↓ One subsystem ↓ Multiple components ↓ Complete prototype 

This allows companies and hardware manufacturers to support the part of the project that best matches their products or interests.

## 🛠️ Repository Contents nexus-7/ │ ├── README.md ├── BOM.csv ├── LICENSE ├── config.json ├── requirements.txt │ ├── hardware/ │ └── ... │ └── scripts/ ├── main_robot.py ├── servo_controller.py ├── motor_driver.py ├── llm_engine.py └── face_display.py 

The repository will expand as the physical prototype is developed.

## 💻 Software Prototype 

The repository contains early software prototypes for the planned robot architecture.

Current software work includes prototypes for:

Robot orchestration Servo communication Motor-control structure Local AI communication Display-state management Configuration 

Some modules currently contain simulation, placeholder or hardware-independent functionality because the physical prototype has not yet been built.

Physical hardware validation will be added after the required components are obtained.

## 🧪 Prototype Success Criteria 

The first physical prototype will be evaluated using measurable tests rather than only visual demonstrations.

Planned measurements include:

Servo positioning accuracy Motor response AI response latency Speech recognition latency Text-to-speech latency Camera/depth performance Battery runtime System temperature Power consumption Emergency-stop response Overall system stability 

Measured results will be added to the repository as development progresses.

🗺️ Development Roadmap [1] System Architecture │ ▼ [2] Hardware BOM │ ▼ [3] Sponsorship / Funding │ ▼ [4] Acquire Components │ ▼ [5] Mechanical Assembly │ ▼ [6] Electronics Integration │ ▼ [7] Software Bring-Up │ ▼ [8] Edge-AI Integration │ ▼ [9] Testing & Optimization │ ▼ [10] First Nexus-7 Prototype │ ▼ [11] Public Demonstration 🔬 Open-Source Development 

The goal is to document the project openly.

As development progresses, the repository will contain:

Source code Configuration Hardware documentation CAD/design files where appropriate Testing results Development notes Build documentation Project updates 

The project is intended to make the development process useful to other students and makers.

## ⚠️ Safety 

Nexus-7 will involve:

Motors Servos Batteries Power electronics Moving mechanical parts 

Physical construction and testing will follow appropriate manufacturer safety instructions.

Battery, high-current electrical work and mechanical testing will be performed with appropriate adult or qualified supervision.

Safety systems, including an emergency-stop mechanism, will be considered part of the physical prototype design.

## 📦 Bill of Materials 

The complete planned component list is available here:

BOM.csv

The BOM represents the planned prototype requirement, not hardware that has already been purchased or assembled.

Prices may change depending on supplier, shipping and availability.

## 📈 What Happens After Sponsorship? 

After receiving the required hardware, the development process will be documented in stages:

1. Component verification 

Verify that all sponsored components are compatible.

2. Hardware assembly 

Build the first physical platform.

3. Software bring-up 

Test each subsystem individually.

4. AI integration 

Connect local AI with the physical robot.

5. Testing 

Measure performance and identify problems.

6. Documentation 

Publish results and lessons learned.

7. Demonstration 

Create a working prototype demonstration.

The objective is to make the development process transparent rather than simply presenting a final result.

## 🌟 Long-Term Vision 

The long-term vision is to develop Nexus-7 into a more capable open-source robotics platform combining:

Edge AI + Robotics + Computer Vision + Speech + Embedded Systems

Future versions may explore:

Better perception More capable local AI Improved mobility More advanced manipulation Better human-robot interaction Additional sensors Improved power efficiency More autonomous behavior 

These are future goals and are not claimed as currently implemented capabilities.

## 📬 Sponsorship 

If you are a hardware manufacturer, robotics company, technology company, maker organization or individual interested in supporting Nexus-7, sponsorship can be provided through:

Hardware/components Partial hardware funding Full prototype funding Technical support Development support 

The current hardware target is approximately $577 USD.

For sponsorship discussions, please contact me through the contact method listed on my GitHub profile.

## 📜 License 

The software in this repository is released under the MIT License.

See LICENSE for the complete license text.

Hardware and CAD licensing will be documented separately where applicable.

## ⭐ Support the Project 

Nexus-7 is currently at the stage where the design exists, but the physical prototype still needs to be built.

If you are interested in helping turn the design into a real robot, hardware sponsorship or project funding can directly support the next stage of development.

From a design on GitHub → to a working physical robot.

Project Status 

Current stage: Pre-prototype
Physical robot: Not built
Hardware funding: Seeking
Planned hardware budget: ~$577 USD
Project type: Open-source student robotics / Edge AI
Repository: Nexus-7





