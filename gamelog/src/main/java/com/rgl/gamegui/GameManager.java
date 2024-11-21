package com.rgl.gamegui;

import com.rgl.gamedata.GameInfo;
import com.rgl.jsonutility.JsonHandler;
import javax.swing.JOptionPane;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

/**
 * Manages the list of games and provides functionality to add, update, 
 * delete, and retrieve game information.
 * 
 * Responsible for interacting with the JSON file through the JsonHandler 
 * class to persist game data.
 */
public class GameManager {

    private List<GameInfo> games; // List to store game objects

    /**
     * Initializes the list of games.
     */
    public GameManager() {
        games = new ArrayList<>();
    }

    /**
     * Retrieves the list of games.
     *
     * @return the list of games.
     */
    public List<GameInfo> getGames() {
        return games;
    }

    /**
     * Loads games from the JSON file and sorts them alphabetically by title.
     */
    public void loadGames() {
        games = JsonHandler.loadGamesInfo();
        Collections.sort(games, (game1, game2) -> game1.getGameTitle().compareTo(game2.getGameTitle()));
    }

    /**
     * Adds a new game to the list and saves it to the JSON file.
     *
     * @param title       the title of the game.
     * @param platform    the platform of the game (e.g., PC, NES).
     * @param completed   true if the game is completed, false otherwise.
     * @param comments    additional comments about the game.
     * @param youtubeLink a YouTube link related to the game.
     * @param reference   reference or metadata for the game.
     * @param runAgain    true if the game is worth replaying, false otherwise.
     * @return true if the game was added successfully, false if the title is empty or already exists.
     */
    public boolean addGame(String title, String platform, boolean completed, String comments, String youtubeLink, String reference, boolean runAgain) {
        if (title.isEmpty()) {
            JOptionPane.showMessageDialog(null, "Please enter a game title.", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }
        if (games.stream().anyMatch(game -> game.getGameTitle().equalsIgnoreCase(title))) {
            JOptionPane.showMessageDialog(null, "A game with this title already exists. Please choose a different title.", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }
        GameInfo newGame = new GameInfo(title, platform, completed, comments, youtubeLink, reference, runAgain);
        games.add(newGame);
        JsonHandler.saveGamesInfo(games);
        return true;
    }

    /**
     * Retrieves a game by its title.
     *
     * @param title the title of the game to retrieve.
     * @return the game object if found, null otherwise.
     */
    public GameInfo getGameByTitle(String title) {
        return games.stream().filter(game -> game.getGameTitle().equals(title)).findFirst().orElse(null);
    }

    /**
     * Updates the details of an existing game and saves the changes to the JSON file.
     *
     * @param game       the game object to update.
     * @param title      the new title of the game.
     * @param platform   the new platform of the game.
     * @param youtubeLink the new YouTube link.
     * @param reference  the new reference for the game.
     * @param comments   new comments about the game.
     * @param completed  true if the game is completed, false otherwise.
     * @param runAgain   true if the game is worth replaying, false otherwise.
     */
    public void updateGame(GameInfo game, String title, String platform, String youtubeLink, String reference, String comments, boolean completed, boolean runAgain) {
        game.setGameTitle(title);
        game.setSystem(platform);
        game.setYoutubeLink(youtubeLink);
        game.setReference(reference);
        game.setComments(comments);
        game.setGameCompleted(completed);
        game.setRunAgain(runAgain);
        JsonHandler.saveGamesInfo(games);
    }

    /**
     * Deletes a game from the list and updates the JSON file.
     *
     * @param game the game to delete.
     */
    public void deleteGame(GameInfo game) {
        games.remove(game);
        JsonHandler.saveGamesInfo(games);
    }
}
