# Marvel Snap Keyboard Adapter

The Marvel Snap Keyboard Adapter is a Python repository containing a project aimed at adapting the controls of a game called Marvel Snap for keyboard input. This project is currently under development and is designed to work specifically with a screen resolution of 1900 by 1200 pixels.

## Description

The goal of this adaptation project is to provide players with an alternative input method for Marvel Snap, enabling them to play the game using a keyboard instead of the default controller (mouse). By leveraging the Python programming language and its libraries, the project aims to enhance the accessibility and convenience of the game for a wider range of players.

The repository houses the necessary Python scripts, modules, and resources required to implement the keyboard adapter. Allowing players to perform actions such as movement and interactions within the Marvel Snap game battles.

While the project is still in progress, the initial implementation supports the screen resolution of 1900 by 1200 pixels. Development efforts are focused on ensuring compatibility with different resolutions and aspect ratios. Future updates may expand the project to support additional screen resolutions commonly used by players.

Contributions from the open-source community are welcomed and encouraged. Developers can actively participate in improving the keyboard adapter project by submitting bug reports, feature requests, or even contributing code to enhance its functionality and compatibility.

With the Marvel Snap Keyboard Adapter project, players will have the freedom to enjoy the game using a keyboard, providing a versatile and accessible alternative to traditional control schemes.

## How to use Marvel Snap Keyboard Adapter

This section will provide you with informations about how to use and programs you must install to correctly use Marvel Snap Keyboard Adapter

### Configuring your computer

Before using Marvel Snap Keyboard Adapter you must download and install Python 3 (https://www.python.org/downloads/) to be sure Python is installed, open the Command Prompt and type "python --version" the output should be "Python 3.xx.xx" where xx.xx can be any number.
After installing Python you must install some dependencies libraries. To do this run all the following command in Command Prompt:

- pip install pyautogui
- pip install keyboard

After all the dependencies are installed, your computer is ready to run Marvel Snap Keyboard Adapter!
*Note: A script will be developed to automatically install all dependencies*

### Starting Marvel Snap Keyboard Adapter

To start Marvel Snap Keyboard Adapter you must:

1. Download this code (Code > Download ZIP);
2. Unzip the code anywhere you want;
3. Open the Command Prompt in the code you unzipped the code (Open the folder in File Explorer and write "cmd" in the address bar);
4. Run the following command exactly as it is written here: python "DxeKeyboard for MarvelSnap.py"
*Note: Steps 1 and 2 are required only for the first time you start Marvel Snap Keyboard Adapter*

After this 4 steps, Marvel Snap Keyboard Adapter is ready to be used.
At this point, use your mouse to start a match, the Marvel Snap Keybord Adapter is expecting you to have 4 cards in your hand at this point (3 from initial hand + 1 card you draw at the start of the turn)
*Note2: The command prompt needs to stay open while you run this application, if you close the command prompt, the application will also stops*
*Note3: I'm studying a better way to execute the application (maybe a .exe?), but for now you need to use cmd*

### Using Marvel Snap Keyboard Adapter

Marvel Snap Keyboard Adapter allows you to use the numbers in your keyboard to select and play your cards into any desired terrain.

#### Playing Cards

Think about this scenario: You have 4 cards in your hand, and you want to play the second card into the first terrain. 
With Marvel Snap Keyboard Adapter you just gotta press "2" (selecting the second card) and then press "1" (select the first terrain) and you are done! Second card played into First Terrain!!

More examples:
- Card number 6 into third terrain: Press "6" then "3";
- Card number 1 into second terrain: Press "1" then "2";
- Card number 3 into first terrain: Press "3" then "1";

#### Ending your Turn

To end your turn you just need to press "Space" key after you play your cards, Marvel Snap Keyboard Adapter will automatically click the "End Turn" button for you.

*Note: While using Marvel Snap Keyboard Adapter never use your mouse to End your Turn, as this will cause the application to malfunction. Check "Actions that will make Marvel Snap Keyboard Adapter malfunction" section for more info*

#### Snap

Snaping is easy, just press "S" key. SNAAAAAP!

#### Retreating

Not in a good situation? Bad hand and opponent just snapped? Just press "F" key, you will retreat right away!
*Note: you will retreat and confirm the retreat! Be sure what you are doing before pressing F*

#### Undoing all your play

Played some cards but changed your mind? Want to cancel everything and start your turn again? Press "esc" key, this will undo all your play.
*Note: This key will undo **all** your play, not only the last card played*

#### Moving cards between terrains

This feature is not supported (for now). Check "Limitations" section for others limitations information.

#### Starting a new match

When you finish a match, every navigation should be done using your mouse (as Marvel Snap Keyboard Adapter have no support for menu navigation)
When you start a new game, you must press the "R" key, by doing it you will tell the application that you are starting a new match, the application will expect you to have 4 cards in your hand again.

#### Fixing miss clicks

Some times the application can get a little lost, this happens when the number of cards in your hands is different from the number of cards the application expects you to have (Check "Actions that will make Marvel Snap Keyboard Adapter malfunction" for more infomation).
When this happens, the application will start to miss all the clicks.
To correct it, press "E" key and then the number of cards you have in your hand.

Example: You have 4 cards in your hand, and you want to play the second card into the first terrain. You press "2" but the third card is clicked. 
1. Press "Esc" to cancel the play;
2. Press "E";
3. Press "4" (Because in this example, you have 4 cards in your hand);

## Actions that will make Marvel Snap Keyboard Adapter malfunction

Basically any card that changes the number of cards in your hand will be a problem.
This happens because Marvel Snap Keyboard Adapter keeps track on how much cards you have on your hand to correctly calculate where it should click to select a card to play, but it cannot identify if you draw or discard any cards.

If Marvel Snap Keyboard Adapter start to miss all the clicks, at the start of your turn (before playing any card) press "e" key and than the number corresponding to the cards on your hand to fix it.

### Cards

The following cards/cards effects will make Marvel Snap Keyboard Adapter harder to use (not impossible!).

- Cards that makes you discard cards (Eg. Blade, Gambit, Sword Master);
- Cards that makes you draw cards (Eg. Mantis, Agent 13, Adam Warlock);
- Cards that can return to your hand (Eg. Deadpool, SabreTooth, Kitty Pride);
- Cards that makes other cards return to your hand (Eg. Beast, Falcon);
- Cards played by the opponent that makes you draw/discard/play cards (Eg. Doc. Octopus, Moon Knight, Maximus);

### Actions

The following actions will make Marvel Snap Keyboard Adapter harder to use (not impossible!).

- ANY action using your mouse (Play a card, end turn, undo a move), moving cards are ok;
- Try to play a card which you do not have enough Energy;

## Limitations

Here is a list of limitations the project have TODAY (some may be implemented/fixed in future updates)

- Only battle is supported (no menu interactions);
- Only 1900x1200 resolution is supported (for now);
- It is not possible to move cards (this action can be done with your mouse without any impact);
- You cannot undo your last move, if you change your mind you must use "Esc" key to undo all your play or finish your play with the mouse and then use "e" key to edit you hand;
- You cannot "Deselect" a card.