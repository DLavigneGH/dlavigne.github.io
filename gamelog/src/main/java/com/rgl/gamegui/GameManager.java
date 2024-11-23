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
     * The list is initially empty and can be populated by loading game data
     * from the JSON file using {@link #loadGames()}.
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
     * This method retrieves all game information from the JSON file and sorts
     * the list of games based on the game title.
     */
    public void loadGames() {
        games = JsonHandler.loadGamesInfo();
        Collections.sort(games, (game1, game2) -> game1.getGameTitle().compareTo(game2.getGameTitle()));
    }

    /**
     * Adds a new game to the list and saves it to the JSON file.
     * If a cover file is provided, the method will handle the file copy to 
     * the target directory. The cover image path will be saved in the JSON file.
     * 
     * @param title       the title of the game.
     * @param platform    the platform of the game (e.g., PC, NES).
     * @param completed   true if the game is completed, false otherwise.
     * @param comments    additional comments about the game.
     * @param youtubeLink a YouTube link related to the game.
     * @param reference   reference or metadata for the game.
     * @param runAgain    true if the game is worth replaying, false otherwise.
     * @param coverFilePath the path to the cover image (optional).
     * @return true if the game was added successfully, false if the title is empty or already exists.
     */
    public boolean addGame(String title, String platform, boolean completed, String comments, 
    String youtubeLink, String reference, boolean runAgain, String coverFilePath) {
        try {
        // If a cover file path is provided (not empty), handle the file copy
        if (coverFilePath != null && !coverFilePath.isEmpty()) {
        File coverFile = new File(coverFilePath);

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

        // Proceed with creating the new game using the cover file path (which will be relative)
        GameInfo newGame = new GameInfo(title, platform, completed, comments, youtubeLink, reference, runAgain, coverFilePath);
        games.add(newGame);

        // Serialize the gameList to JSON
        JsonHandler.saveGamesInfo(games);

        return true;

        } catch (Exception e) {
        JOptionPane.showMessageDialog(null, "Failed to save cover image: " + e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        return false;
        }
}

    /**
     * Updates an existing game and saves the changes to the JSON file.
     * The method handles updating all details of a game, including the cover
     * image if provided. If the cover image is different, it will be copied
     * to the target directory and the path will be updated.
     * 
     * @param selectedGame the game object to update.
     * @param title        the new title of the game.
     * @param platform     the new platform of the game.
     * @param youtubeLink  the new YouTube link.
     * @param reference    the new reference for the game.
     * @param comments     new comments about the game.
     * @param completed    true if the game is completed, false otherwise.
     * @param runAgain     true if the game is worth replaying, false otherwise.
     * @param coverImagePath the new cover image path (optional).
     */
    public void updateOrSaveGame(GameInfo selectedGame, String title, String platform, String youtubeLink, 
    String reference, String comments, boolean completed, boolean runAgain, String coverImagePath) {
    
    // If selectedGame is null, it's a new game, so create a new GameInfo object
    if (selectedGame == null) {
        selectedGame = new GameInfo(title, platform, completed, comments, youtubeLink, reference, runAgain, coverImagePath);
        games.add(selectedGame);
    } else {
        // Otherwise, update the existing game
        selectedGame.setGameTitle(title);
        selectedGame.setSystem(platform);
        selectedGame.setYoutubeLink(youtubeLink);
        selectedGame.setReference(reference);
        selectedGame.setComments(comments);
        selectedGame.setGameCompleted(completed);
        selectedGame.setRunAgain(runAgain);
    }

    // Handle cover image if a new file path is provided
    if (coverImagePath != null && !coverImagePath.isEmpty()) {
        File coverFile = new File(coverImagePath);
        
        // Ensure the file exists and is valid
        if (coverFile.exists() && coverFile.isFile()) {
            String targetPath = "data/cover/" + coverFile.getName();
            File targetFile = new File(targetPath);
            try {
                // Ensure the directory exists
                targetFile.getParentFile().mkdirs();
                
                // Copy the cover image and update cover path in game object
                Files.copy(coverFile.toPath(), targetFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
                selectedGame.setCoverImagePath(targetPath); 
                
            } catch (IOException e) {
                JOptionPane.showMessageDialog(null, "Failed to update cover image: " + e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
                return;
            }
        } else {
            JOptionPane.showMessageDialog(null, "Cover image file is invalid or doesn't exist.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }
    } else {
        // If no cover image is provided, ensure it's cleared
        selectedGame.setCoverImagePath("");  
    }

    // Save the updated game list to JSON
    JsonHandler.saveGamesInfo(games);
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
     * Deletes a game from the list and updates the JSON file.
     * This method will also delete the associated cover image if it exists.
     * 
     * @param game the game to delete.
     * @return true if the game was successfully deleted, false otherwise.
     */
    public boolean deleteGame(GameInfo game) {
        // Remove the cover image if it exists
        String coverImagePath = game.getCoverImagePath();
        if (coverImagePath != null && !coverImagePath.isEmpty()) {
            File coverImageFile = new File(coverImagePath);
            if (coverImageFile.exists()) {
                boolean deleted = coverImageFile.delete();
                if (!deleted) {
                    System.out.println("Failed to delete cover image: " + coverImagePath);
                    return false;
                }
            }
        }
        boolean removed = games.remove(game);
        JsonHandler.saveGamesInfo(games);
        return removed;
    }
}
