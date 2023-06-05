# Marvel Snap Keyboard Adapter

The Marvel Snap Keyboard Adapter is a Python repository containing a project aimed at adapting the controls of a game called Marvel Snap for keyboard input. This project is currently under development and is designed to work specifically with a screen resolution of 1900 by 1200 pixels.

## Description

The goal of this adaptation project is to provide players with an alternative input method for Marvel Snap, enabling them to play the game using a keyboard instead of the default controller (mouse). By leveraging the Python programming language and its libraries, the project aims to enhance the accessibility and convenience of the game for a wider range of players.

The repository houses the necessary Python scripts, modules, and resources required to implement the keyboard adapter. Allowing players to perform actions such as movement and interactions within the Marvel Snap game battles.

While the project is still in progress, the initial implementation supports the screen resolution of 1900 by 1200 pixels. Development efforts are focused on ensuring compatibility with different resolutions and aspect ratios. Future updates may expand the project to support additional screen resolutions commonly used by players.

Contributions from the open-source community are welcomed and encouraged. Developers can actively participate in improving the keyboard adapter project by submitting bug reports, feature requests, or even contributing code to enhance its functionality and compatibility.

With the Marvel Snap Keyboard Adapter project, players will have the freedom to enjoy the game using a keyboard, providing a versatile and accessible alternative to traditional control schemes.

## How to use Marvel Snap Keyboard Adapter

Still need to be written


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