![License](https://img.shields.io/github/license/hanzili/QMaze?style=for-the-badge) ![Repo Size](https://img.shields.io/github/languages/code-size/hanzili/QMaze?style=for-the-badge) ![TOP_LANGUAGE](https://img.shields.io/github/languages/top/hanzili/QMaze?style=for-the-badge) ![FORKS](https://img.shields.io/github/forks/hanzili/QMaze?style=for-the-badge&social) ![Stars](https://img.shields.io/github/stars/hanzili/QMaze?style=for-the-badge)

**WOMANIUM HACKATHON 2022**

# :space_invader: Quantum Maze

- [Team Introduction](#team-introduction)
- [Game Summary](#game-summary)
  - [Mission](#mission)
  - [Story](#story)
  - [How To Play](#how-to-play)
- [How to Install](#how-to-install)
- [Challenges Faced](#challenges-faced)
- [Software & Tools Used](#software--tools-used)
- [Future Plans](#future-plans)
- [License](#license)
- [References](#references)

# Team Introduction
**Team Name:** Quantum Maniacs

**Challenge Name:** Humans vs Quantum Computers (IBM)

**Pitch Presenter:** Hanzi Li

****Member Names:****

------------

**Abdullah Kazi**

Discord ID: **K🐺#8200**

GitHub ID: **AbdullahKazi500**

eMail: [_kazi.abdullah.temea66@gmail.com_](mailto:kazi.abdullah.temea66@gmail.com)

------------

**Afrah Aamer**

Discord ID: alastine#5191

GitHub ID: AfrahAamer

eMail: [_afrahaamer@gmail.com_](mailto:afrahaamer@gmail.com)
 
------------


**Hanzi Li**


Discord ID: hanzili#4885


GitHub ID: hanzili


eMail: [_hanzili0217@gmail.com_](mailto:hanzili0217@gmail.com)

------------

**Raymundo Vazquez**


Discord ID: Raymundo21#2210


GitHub ID: Raymundv


eMail: [_gusvazra@student.gu.se_](mailto:gusvazra@student.gu.se)

------------

**Shanice St John**


Discord ID: Shan#4498


GitHub ID: GitHub ID: Shanicesj 


eMail: [_thebutterflymaze@gmail.com_](mailto:thebutterflymaze@gmail.com)

------------

**Sri Sowmya Tirukkovalluri**


Discord ID: srisowmya_tirukkovalluri#1409


GitHub ID: Sowmyat1


eMail: [_tsrisowmya@gmail.com_  ](mailto:tsrisowmya@gmail.com)

------------

# Game Summary


## Mission

We have developed a Quantum Game “ Quantum Maze” using IBM Qiskit and Godot. Our Aim is to introduce the players to the world of Quantum Computation. Quantum Maze helps the players to learn about Qubits, Quantum gates, Quantum Circuits, and Noise.


## Story 

In the Quantum world, your worst enemy is Noise. When the qubits interact with the noise it results in an uncontrollable change in the quantum states and causes a loss of information stored by the quantum computer. Your mission is to help the qubit to achieve a given target state by passing through a certain set of quantum gates and also avoiding the noise balls which are scattered around the maze.

> Survival Tip: Be careful of noise balls, they are very powerful and can kill your quantum state with just one touch!


## How To Play

1. **Move the ball through the blocks. Each block represents a quantum gate.**
2. **Use the keypad to move through the maze.**
3. **You must avoid the noise objects, otherwise, you’ll lose the game.**
4. [Watch the Gameplay/Walthrough](https://drive.google.com/file/d/1_oKQ7oStvsb5tgTWm-Rmj3Z_zAYdiITj/view)


# How to Install
Python environment is already setted up from [godot-python](https://github.com/touilleMan/godot-python)
and [Qiskit library](https://github.com/Qiskit) is already installed for windows-64
Install qiskit：
1. ```cd addons/pythonscript/(choose_operating_system)```
2. For windows:
    ```
    python.exe -m ensurepip
    python.exe -m pip install qiskit
    ```
    For MAC:
    ```
    cd ox-64/bin
    python3 -m ensurepip
    python3 -m pip install qiskit
    ```

# Challenges Faced

Characterizing the player and conceptualizing the quantum world in a way that is easily interpretable.

- We found that there were many qiskit packages such as the_qiskit.visualization d_oesn't work on Godot. So we only had access to limited qiskit resources.
- Since there are no quantum games which were developed using Godot. We ran into a


# Software & Tools Used  


- Qiskit
- Godot
- Python


# Future Plans

1. Add more levels to introduce more quantum gates and different types of noise obstacles to the game.
2. Introduce more quantum computing concepts eg. Entanglement, Quantum Tunneling, etc.
3. Introduce more graphics and animations in the Game
4. Introduce multiple qubits to the game
5. Introduce error correcting codes to the game which can help the player restore the state of qubit after they come in contact with the noise balls
6. Introduce engaging characters for the game storyline. Represent them as Qubits, state 0 being a bad person, and state 1 a good character. Through life experiences(quantum gates), the character chooses and affects its inner state, and then after a measurement (situation) decides to be either bad or good
7. Introduce engaging characters for the game storyline
8. Represent them as Qubits, state 0 being a bad person, and state 1 a good character. Through life experiences(quantum gates), the character chooses and affects its inner state, and then after a measurement (situation) decides to be either bad or good


# License

<a href="https://choosealicense.com/licenses/mit/"><img src="https://raw.githubusercontent.com/johnturner4004/readme-generator/master/src/components/assets/images/mit.svg" height=40 />MIT License</a>

# References

[_https://builtin.com/hardware/quantum-computer-games_](https://builtin.com/hardware/quantum-computer-games)

[_https://www.wilsoncenter.org/blog-post/games-round-quantum-computing_](https://www.wilsoncenter.org/blog-post/games-round-quantum-computing)

[_https://www.researchgate.net/publication/361022971_Defining_Quantum_Games_](https://www.researchgate.net/publication/361022971_Defining_Quantum_Games)

[_https://decodoku.medium.com/why-we-need-to-make-quantum-games-6f8c7bc4ace7_](https://decodoku.medium.com/why-we-need-to-make-quantum-games-6f8c7bc4ace7)

[_https://uwaterloo.ca/news/news/new-quantum-cats-game-launches-better-understanding-quantum_](https://uwaterloo.ca/news/news/new-quantum-cats-game-launches-better-understanding-quantum)

[_https://decodoku.medium.com/quantum-battleships-the-first-multiplayer-game-for-a-quantum-computer-e4d600ccb3f3_](https://decodoku.medium.com/quantum-battleships-the-first-multiplayer-game-for-a-quantum-computer-e4d600ccb3f3)
