<div align = "center">
<h1 align = "center">
Sonic AI with Genetic Algorithm
  </h1>
  </div>
  
  <p align = "center">
A Genetic algorithm that revolves around the game Sonic The Hedgehog. This algorithm is used to create and learn how to play the game.
The algorithm was created by me with help from a friend (If interested about his projects here is his github: https://github.com/simplicity-load).
</p>  
<br>
<br>

<h2 align = "center">
Development
  </h2>

<div align = "center">
  <p>
    As the title says the AI has the genetic algorithm as its main learning method.
    To simplify we used only 2 inputs for Sonic, that is right and jump. The constraints are fitting for this algorithm, like for example: If Sonic dies the current genome gets negative points, if he doesn't do anything for 1000 frames the it stops the current genomes controll, gets negative points and also starts the next genome etc. The genomes are a random sequence so most likely the agent will play dumb (will die to first enemy), but will learn to play with every new generation. In this project our main way to create new generations is through crossover and mutation.
  </p>
  </div>
  <br>
  <br>
  <h2 align = "center">
  Classes
  </h2>
  <div>
  <p> There are three classes used for this project </p>
  <ul>
  <li><i>GenAlgo.py</i> which has all the defined fuctions for the program to work.</li>
  <li><i>genome.py</i> which is a data class to store the sequence of actions and fitness score of the specific genome.</li>
  <li><i>MainSonic</i> is the the class or "main method" where we execute all the functions and create the game loop together with the constraints.</li>
  </ul>
  </div>
  
  <br>
  <br>
  
  <h2 align = "center">
  Gameplay
  </h2>
  

