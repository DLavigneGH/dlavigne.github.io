package com.rgl.gamegui;

import com.rgl.gamedata.GameInfo;
import com.rgl.jsonutility.JsonHandler;
import javax.swing.JOptionPane;
import java.util.List;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;
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
    public boolean addGame(String title, String platform, boolean completed, String comments, 
    String youtubeLink, String reference, boolean runAgain, String coverFilePath) {
        try {
        // If a cover file path is provided (not empty), handle the file copy
        if (coverFilePath != null && !coverFilePath.isEmpty()) {
        File coverFile = new File(coverFilePath); // This is the selected file path

        // Get the directory where the JAR is located
        String jarDir = new File(GameManager.class.getProtectionDomain().getCodeSource().getLocation().toURI()).getParent();

        // Build the absolute path for the cover file in the "data/cover" directory
        String coverPath = jarDir + File.separator + "data" + File.separator + "cover" + File.separator + coverFile.getName();
        File targetFile = new File(coverPath);

        // Ensure the directories exist
        targetFile.getParentFile().mkdirs();

        // Copy the file to the target directory
        Files.copy(coverFile.toPath(), targetFile.toPath(), StandardCopyOption.REPLACE_EXISTING);

        // Store the relative path for JSON saving (relative to the "data" folder)
        coverFilePath = "data/cover/" + coverFile.getName();
        }

        System.out.println("Cover File Path: " + coverFilePath);  // Debugging step

        // Proceed with creating the new game using the cover file path (which will be relative)
        GameInfo newGame = new GameInfo(title, platform, completed, comments, youtubeLink, reference, runAgain, coverFilePath);
        games.add(newGame);

        // Serialize the gameList to JSON (assuming you have a method for this)
        JsonHandler.saveGamesInfo(games);;  // Call your method to save the game list to JSON

        return true;

        } catch (Exception e) {
        JOptionPane.showMessageDialog(null, "Failed to save cover image: " + e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        return false;
        }
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
    public void updateGame(GameInfo game, String title, String platform, String youtubeLink, String reference, String comments, boolean completed, boolean runAgain, String coverImagePath) {
        game.setGameTitle(title);
        game.setSystem(platform);
        game.setYoutubeLink(youtubeLink);
        game.setReference(reference);
        game.setComments(comments);
        game.setGameCompleted(completed);
        game.setRunAgain(runAgain);
    
        // Handle cover image update if a new file is selected
        if (coverImagePath != null && !coverImagePath.isEmpty()) {
            File coverFile = new File(coverImagePath);
            String absolutePath = coverFile.getAbsolutePath();
            game.setCoverImagePath(absolutePath);  // Set the absolute path in the GameInfo object
    
            try {
                File targetFile = new File(absolutePath);  // Use absolute path
                targetFile.getParentFile().mkdirs(); // Ensure the directory exists
    
                // Copy the new cover image to the correct location
                Files.copy(coverFile.toPath(), targetFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
    
                // Update the cover image path in the GameInfo object
                game.setCoverImagePath(targetFile.getPath());  // No need to do this twice
    
            } catch (IOException e) {
                JOptionPane.showMessageDialog(null, "Failed to update cover image: " + e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
                return;
            }
        } else {
            // If no cover image is provided, ensure it's cleared or set to default path
            game.setCoverImagePath("");  // Clear the cover image path if not selected
        }
    
        // Save the updated game data to JSON
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
