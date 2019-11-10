Intro:
This project was a group university project which made use of popular programs such as Git and Pycharm to develop a working chatbot in which we name Sven. Based around the game Minecraft, this chatbot enables responses to questions about crafting recipes, thier descriptions and other standard chat responses all incorporated within both discord and the Minecraft chat itself, hosted on a server.

Original task:
At the start of our development we indivdually devised which parts we should partake in to contribute to the project as a whole. My first task was input refactoring, the goal was to take a sentence from a text input and cut it down into a very simplified 2D array of the word, the amount of times it occured within the sentence and the type of word it was, to allow us to remove unncessary words that would not be assiciated to any type of response. This code would also remove unimportant characters such as ',' which had no real meaning within the sentence. I used a numpy array as the documentation for it was simple and it followed strict data type and size parameters similar to an SQL database meaning if incorrect data was somehow added it would not allow it to be added to the array. Furthermore to identify word type of every word in a dictionary I decided to used NLTK and WordNet, a corpus reader which allowed me to search said database and retrive each word type. This I then simplified further as the standard NLTK text system of referencing was too complex for the project as it contained multiple variation of types like nouns which would be insignificant to the final solution, by using a hand typed dictionary as seen at the start of the inputRefactor.py 

All code in ChatBot/inputRefactor.py was written by myself however, he code was reformatted slightly by https://github.com/Vendari 

/bossbar set minecraft:1 visible true


Short Summary:
My contributions to the project were:
-Using Scrum methodology with the website 'Trello' to keep track of overall progress as well as setting additional tasks.
-Using Python (Pycharm) to develop an input refactor to modify the input by parsing each word individually into an simplified interpretable 2d Numpy array with its word, amount of times the word occurs and type of word (noun). This was done by referencing a corporus using NLTK.
-Using Python and SSH on a server to install Minecraft Bukkit and link the program using the plugin RaspberryJuice which allows python to communicate using server ports.


Overall:
During my project I was able to; enhance my skills with GitHub being able to work side by side with other programmers, learn how to use Pycharm as the most popular IDE, work as a team effectively by program in modules rather than linearly, develop my object oriented skills in python allowing code to communicate more efficiently as well as develop my Agile skills using methods like the Kanban board, paired programming and Scrum meetings.
