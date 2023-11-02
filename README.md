![License](https://img.shields.io/github/license/hanzili/QMaze?style=for-the-badge) ![Repo Size](https://img.shields.io/github/languages/code-size/hanzili/QMaze?style=for-the-badge) ![TOP_LANGUAGE](https://img.shields.io/github/languages/top/hanzili/QMaze?style=for-the-badge) ![FORKS](https://img.shields.io/github/forks/hanzili/QMaze?style=for-the-badge&social) ![Stars](https://img.shields.io/github/stars/hanzili/QMaze?style=for-the-badge)

# :space_invader: Quantum Maze

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
1. install [godot-python](https://github.com/touilleMan/godot-python) from godot addons
2. install [Qiskit library](https://github.com/Qiskit) using pip


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

