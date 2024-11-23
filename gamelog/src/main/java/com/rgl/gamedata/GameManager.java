package com.rgl.gamedata;

import com.rgl.helpers.FileUtils;
import com.rgl.jsonutility.JsonHandler;

import javax.swing.JOptionPane;
import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

/**
 * Manages the list of games and provides functionality to add, update, 
 * delete, and retrieve game information.
 */
public class GameManager {
    private List<GameInfo> games;

    public GameManager() {
        games = new ArrayList<>();
    }

    public List<GameInfo> getGames() {
        return games;
    }

    public void loadGames() {
        games = JsonHandler.loadGamesInfo();
        Collections.sort(games, (game1, game2) -> game1.getGameTitle().compareTo(game2.getGameTitle()));
    }

    public boolean addGame(String title, String platform, boolean completed, String comments, 
                           String youtubeLink, String reference, boolean runAgain, String coverFilePath) {
        try {
            String coverPath = null;

            if (coverFilePath != null && !coverFilePath.isEmpty()) {
                File coverFile = new File(coverFilePath);
                File targetDir = new File("data/cover");
                
                File copiedFile = FileUtils.copyFileToDirectory(coverFile, targetDir);
                coverPath = "data/cover/" + copiedFile.getName();
            }

            GameInfo newGame = new GameInfo(title, platform, completed, comments, youtubeLink, reference, runAgain, coverPath);
            games.add(newGame);
            JsonHandler.saveGamesInfo(games);
            return true;

        } catch (IOException e) {
            JOptionPane.showMessageDialog(null, "Failed to save cover image: " + e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }
    }

    public GameInfo getGameByTitle(String title) {
        return games.stream()
                    .filter(game -> game.getGameTitle().equals(title))
                    .findFirst()
                    .orElse(null);
    }

    public void updateGame(GameInfo game, String title, String platform, String youtubeLink, String reference, 
                           String comments, boolean completed, boolean runAgain, String coverImagePath) {
        game.setGameTitle(title);
        game.setSystem(platform);
        game.setYoutubeLink(youtubeLink);
        game.setReference(reference);
        game.setComments(comments);
        game.setGameCompleted(completed);
        game.setRunAgain(runAgain);

        if (coverImagePath != null && !coverImagePath.isEmpty()) {
            try {
                File coverFile = new File(coverImagePath);
                File targetDir = new File("data/cover");

                File copiedFile = FileUtils.copyFileToDirectory(coverFile, targetDir);
                game.setCoverImagePath("data/cover/" + copiedFile.getName());
            } catch (IOException e) {
                JOptionPane.showMessageDialog(null, "Failed to update cover image: " + e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            }
        }

        JsonHandler.saveGamesInfo(games);
    }

    public void deleteGame(GameInfo game) {
        if (game.getCoverImagePath() != null && !game.getCoverImagePath().isEmpty()) {
            File coverFile = new File(game.getCoverImagePath());
            FileUtils.deleteFile(coverFile);  // Use FileUtils to delete the cover image
        }
        games.remove(game);
        JsonHandler.saveGamesInfo(games);
    }
}
