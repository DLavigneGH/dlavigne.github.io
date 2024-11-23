## Table of Contents
- [Gamelog project](#gamelog-project)
  - [Overview](#overview)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Documentation](#documentation)
  - [Changelog](#changelog)

# Gamelog project

## Overview

I wanted to learn Java, and as a retro gamer, I created a project to manage a personal game log.   

This app allows users to add, view, and modify games, keeping track of their game collection easily.  

There is also a HTML file if you want to look at your collection!  

## Features

Add New Games: Fill out fields to register new games, which are saved in a JSON file.
Dynamic Dropdown List: Newly added games appear in a dropdown for easy selection.
Edit Game Information: Modify existing game details as needed.
HTML Table Generation: Automatically generates an index.html file displaying your game collection in a table format.

**IMPORTANT:** To fetch the JSON data properly from the index HTML, a simple HTTP server is ran from the App. If you close it, you will not see your table. 

Keep the App open and close it when you are done

## Requirements

Project done using Java version "23"

## Installation

Download the gamelog jar file and execute it.

## Usage

You will see a `Select Game` dropdown field at the top with all other fields being empty. The first time you boot the App you simply need to add your first game!

Upon pressing `Submit New Game`, your game should appear in the list and you can select it and change its information and save via `Save Changes`.

A folder `data` will be added with `gameTable.json` containing your games and their information.

You can delete any game entry with `Delete Game`.

The App should prevent you from entering duplicated games or empty names

If you want to see your collection, use the `Open HTML` button.
As mentioned in the IMPORTANT note above, the App launches a HTTP server to serve the index and the gameTable. If you close the App you will not see your table.

`Youtube` field was just for me because I stream my games so I put videos on Youtube.

## Documentation

You can read the Javadoc [here](https://dlavignegh.github.io/dlavigne.github.io/gamelog/target/reports/apidocs/index.html)

## Changelog

v1.0 - First version done and uploaded to GitHub
v1.1 - Search Field and table sorting
v1.2 - Ability to add image covers for your games and see as popup in the HTML table
