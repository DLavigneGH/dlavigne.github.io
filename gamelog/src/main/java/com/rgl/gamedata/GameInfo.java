package com.rgl.gamedata;

/**
 * Represents a game with its associated details.
 * 
 * Stores information such as the game's title, platform, completion status,
 * comments, YouTube link, reference, and whether the user wants to run it again.
 * Provides getter and setter methods to manage these properties.
 */

public class GameInfo {
    private String gameTitle;
    private String system;
    private String comments;
    private String youtubeLink;
    private String referencedBy;
    private String coverImagePath;

    private boolean gameCompleted;
    private boolean runAgain;

    /**
     * Constructs a new Game object with the specified details.
     * 
     * @param gameTitle    the title of the game
     * @param system       the platform or system on which the game is played (e.g., PC, NES)
     * @param gameCompleted whether the game has been completed (true if completed, false otherwise)
     * @param comments     any additional comments or notes about the game
     * @param youtubeLink  a link to a relevant YouTube video about the game
     * @param referencedBy a reference to the source or person that suggested or referenced the game
     * @param runAgain     whether the game is worth playing again (true if it is, false otherwise)
     */
    public GameInfo(String gameTitle, String system, boolean gameCompleted, String comments, String youtubeLink, String referencedBy, boolean runAgain, String coverImagePath) {
        this.gameTitle = gameTitle;
        this.system = system;
        this.gameCompleted = gameCompleted;
        this.comments = comments;
        this.youtubeLink = youtubeLink;
        this.referencedBy = referencedBy;
        this.runAgain = runAgain;
        this.coverImagePath = coverImagePath;

    }

    // Getters and setters
    public String getGameTitle() {
        return gameTitle;
    }

    public void setGameTitle(String gameTitle) {
        this.gameTitle = gameTitle;
    }

    public String getYoutubeLink() {
        return youtubeLink;
    }

    public void setYoutubeLink(String youtubeLink) {
        this.youtubeLink = youtubeLink;
    }

    public String getSystem() {
        return system;
    }

    public void setSystem(String system) {
        this.system = system;
    }

    public String getReference() {
        return referencedBy;
    }

    public void setReference(String referencedBy) {
        this.referencedBy = referencedBy;
    }

    public boolean getGameCompleted() {
        return gameCompleted;
    }

    public void setGameCompleted(boolean gameCompleted) {
        this.gameCompleted = gameCompleted;
    }

    public boolean getRunback() {
        return runAgain;
    }

    public void setRunAgain(boolean runAgain) {
        this.runAgain = runAgain;
    }

    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }

    public String getCoverImagePath() {
        return coverImagePath;
    }
    
    public void setCoverImagePath(String coverImagePath) {
        this.coverImagePath = coverImagePath;
    }
}
