package com.rgl.jsonutility;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.rgl.gamedata.GameInfo;

import java.io.*;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Handles reading and writing game data to and from a JSON file.
 * 
 * Manages a persistent directory for storing the `gameTable.json` file 
 * and provides methods to save and load the list of games.
 */
public class JsonHandler {

    // Path to the persistent directory where the gameTable.json file will be stored
    private static final String PERSISTENT_DIR = "./data"; 
    private static final String FILE_PATH = Paths.get(PERSISTENT_DIR, "gameTable.json").toString();

    // Ensure the directory exists, make it if not
    static {
        try {
            Files.createDirectories(Paths.get(PERSISTENT_DIR)); 
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    /**
     * Saves the list of games to the JSON file in the persistent directory.
     *
     * @param games the list of games to save to the file.
     */
    public static void saveGamesInfo(List<GameInfo> games) {
        try (FileWriter writer = new FileWriter(FILE_PATH)) {
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            gson.toJson(games, writer);  // Converts the list to JSON and writes to the file
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Loads the list of games from the JSON file in the persistent directory.
     * If the file does not exist, it attempts to load data from resources and create the file.
     *
     * @return a list of games loaded from the file or resources.
     */
    public static List<GameInfo> loadGamesInfo() {
        Path path = Paths.get(FILE_PATH);
        if (!Files.exists(path)) {
            // If the file doesn't exist, load the initial data from resources and create the file
            return loadGamesFromResources();
        }
        try (FileReader reader = new FileReader(FILE_PATH)) {
            // Read from file and convert to Game[]
            Gson gson = new Gson();
            GameInfo[] gameArray = gson.fromJson(reader, GameInfo[].class); 
            return new ArrayList<>(List.of(gameArray));
        } catch (IOException e) {
            // Return an empty list if something goes wrong
            e.printStackTrace();
            return new ArrayList<>(); 
        }
    }

    
    /**
     * Loads the list of games from the resources if the persistent file does not exist.
     * This method is used to populate the data for the first time and save it to the persistent directory.
     *
     * @return a list of games loaded from the resources.
     */
    private static List<GameInfo> loadGamesFromResources() {
        InputStream resourceStream = JsonHandler.class.getClassLoader().getResourceAsStream("gameTable.json");
        if (resourceStream == null) {
            return new ArrayList<>();  // Return an empty list if the resource is not found
        }

        try (InputStreamReader reader = new InputStreamReader(resourceStream)) {
            Gson gson = new Gson();
            GameInfo[] gameArray = gson.fromJson(reader, GameInfo[].class);
            // Save the loaded games to the persistent directory
            saveGamesInfo(List.of(gameArray));  // Save it so it persists outside the JAR
            return new ArrayList<>(List.of(gameArray));
        } catch (IOException e) {
            e.printStackTrace();
            return new ArrayList<>();  // Return an empty list if something goes wrong
        }
    }

    /**
     * Finds and returns a game by its title.
     *
     * @param games the list of games to search through.
     * @param title the title of the game to find.
     * @return the game with the specified title, or null if not found.
     */
    public static GameInfo getGameByTitle(List<GameInfo> games, String title) {
        for (GameInfo game : games) {
            if (game.getGameTitle().equals(title)) {
                return game;
            }
        }
        return null;
    }

    /**
     * Updates the information of an existing game in the list.
     * If the game with the same title exists, it is updated with the new information.
     *
     * @param games       the list of games to update.
     * @param updatedGame the game object with updated information.
     */
    public static void updateGameInfo(List<GameInfo> games, GameInfo updatedGame) {
        for (int i = 0; i < games.size(); i++) {
            if (games.get(i).getGameTitle().equals(updatedGame.getGameTitle())) {
                games.set(i, updatedGame);
                break;
            }
        }
    }
}
