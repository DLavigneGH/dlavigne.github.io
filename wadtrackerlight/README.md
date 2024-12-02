## Table of Contents
- [Classic DooM WAD Randomizer and Tracker](#classic-doom-wad-randomizer-and-tracker)
  - [Overview](#overview)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Issues](#issues)
  - [Changelog](#changelog)

# Classic DooM WAD Randomizer and Tracker

## Overview

Here is a python App to randomize Classic DooM WAD downloads from www.doomworld.com/idgames. It can also track what you have played.

## Features

This opens a Selenium Webdriver session to `www.doomworld.com/idgames` in the background and presses the `Random File` button. The Webdriver will look for the `filename path` of the WAD visible on this page, and will do an API call to get information of that file (id, title, filename, author, etc.) (See idGames Archive Public API [documentation](https://www.doomworld.com/idgames/api/) for more info)

An example of api call made from the App would be: <br>
```https://www.doomworld.com/idgames/api/api.php?action=get&file=levels/doom2/Ports/megawads/cchest3.zip&out=json```<br>
Click [here](https://www.doomworld.com/idgames/api/api.php?action=get&file=levels/doom2/Ports/megawads/cchest3.zip&out=json) to see the response.

You can save that response to a JSON file with a button from the App, if you wish to keep track of what you play or do other data manipulation (create tables, etc.)

## Requirements

This was made with python "3.13" and EXE comes with all dependencies.

## Installation

Download the wadrandomizer.exe file and launch it.

## Usage

![Randomizer](.doc/randomizer.png)

Upon starting the App (there is a <10 seconds loading) you will be greeted with an empty UI.
The only available option is to click `Randomize`.

If Randomize was successful, the UI will start to populate with the WAD information that that was found for you.
It doesn't allow filtering, meaning you will get any WAD from the database (heretic, deathmatch, doom, doom2, megawads, etc.)

A `Download WAD` button will be available to download the WAD.

You can save the information to a JSON file with the button `Save to JSON`.
This will create a file next to the EXE which can be used to track your WADs you have played! This button is optional so if you don't feel like playing the WAD you got you can just randomize a new one immediately!

## Issues

Sometimes launching doesn't work; you will get an error popup about certificate. Just relaunch the App.

## Changelog

v1.0 - First version done and uploaded to GitHub<br>
