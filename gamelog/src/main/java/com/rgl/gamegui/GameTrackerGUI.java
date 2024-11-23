package com.rgl.gamegui;

import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;

import java.awt.*;
import java.awt.event.*;
import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;

import com.rgl.gamedata.GameInfo;
import com.rgl.helpers.ResourceExtractor;

/**
 * Implements the graphical user interface (GUI) for the Game Tracker application.
 * 
 * Provides fields and controls for adding, updating, and deleting game information,
 * as well as a dropdown menu for selecting games. The GUI is integrated with 
 * the GameManager to manage game data and update the UI accordingly.
 */

public class GameTrackerGUI extends JFrame {
    // Define UI components

    /**
     * Dropdown for selecting a game from the list.
     */
    private JComboBox<String> gameDropdown;

    /**
     * The text fields used for entering game details (title, platform, YouTube link, comments, reference).
     */
    private JTextField titleField, platformField, youtubeField, commentsField, referenceField, coverImagePathField;
    
    /**
     * Checkboxes to mark the status of the game.
     */
    private JCheckBox completedCheckBox, runAgainCheckBox;

    /**
     * Manages the games, adds and updates them
     */
    private GameManager gameManager;  
    
    private File selectedCoverFile;

    /**
     * Constructs the Game Tracker GUI, initializes components, and loads game data.
     */
    public GameTrackerGUI() {
        // Copy index.html from resources to the target directory
        ResourceExtractor.copyResourcesToTarget("index.html", "script.js");

        // Initialize the GameManager to handle the games
        gameManager = new GameManager();
        
        // Set up the window title, size, and layout
        setTitle("Game Tracker");
        setSize(400, 550);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BoxLayout(getContentPane(), BoxLayout.Y_AXIS));

        // Initialize the UI components
        initializeComponents();

        // Load and populate the dropdown with the list of games
        gameManager.loadGames();

        // Populate the dropdown with game titles
        populateGameDropdown();
    }

    // Initializes UI components such as text fields, buttons, and dropdown
    private void initializeComponents() {
        // Initialize text fields for input
        titleField = new JTextField();
        platformField = new JTextField();
        youtubeField = new JTextField();
        commentsField = new JTextField();
        referenceField = new JTextField();
        coverImagePathField = new JTextField();
        coverImagePathField.setEditable(false);

        // Initialize checkboxes for game status
        completedCheckBox = new JCheckBox("Completed");
        runAgainCheckBox = new JCheckBox("Run Again");

        // Create the dropdown for game titles
        gameDropdown = new JComboBox<>();

        // Add action listener to update fields when a game is selected
        gameDropdown.addActionListener(e -> updateUIFromSelectedGame());
        
        // Add UI components to the frame
        add(new JLabel("Select Game:"));
        add(gameDropdown);
        add(new JLabel("Game Title:"));
        add(titleField);
        add(new JLabel("Platform:"));
        add(platformField);
        add(new JLabel("Comments"));
        add(commentsField);
        add(new JLabel("YouTube Link:"));
        add(youtubeField);
        add(new JLabel("Reference:"));
        add(referenceField);
        add(new JLabel("Cover Image Path:"));
        add(coverImagePathField);
        add(completedCheckBox);
        add(runAgainCheckBox);

        add(createSubmitButton("Upload Cover", e -> uploadCoverButtonActionPerformed()));

        // Add Submit buttons with actions
        add(createSubmitButton("Submit New Game", e -> addNewGame()));
        add(createSubmitButton("Save Changes", e -> saveGameChanges()));

        // Delete button
        add(createSubmitButton("Delete Game", e -> deleteGame()));

        // Button to open HTML file in browser
        add(createSubmitButton("Open HTML", e -> openBrowser("http://localhost:8080/index.html")));
    }

    
    /**
     * Creates a submit button and attaches the provided action listener.
     *
     * @param text           the button label.
     * @param actionListener the action listener to attach.
     * @return the created JButton.
     */
    private JButton createSubmitButton(String text, ActionListener actionListener) {
        JButton button = new JButton(text);
        button.addActionListener(actionListener);
        return button;
    }

    /**
     * Populates the dropdown with the list of games from GameManager.
     */
    private void populateGameDropdown() {
        // Clear the dropdown and add a default option
        gameDropdown.removeAllItems();
        gameDropdown.addItem("<Choose a Game or Add New>");

        // Add each game's title to the dropdown
        for (GameInfo game : gameManager.getGames()) {
            gameDropdown.addItem(game.getGameTitle());
        }
    }

    /**
     * Updates the UI fields when a game is selected from the dropdown.
     */
    private void updateUIFromSelectedGame() {
        String selectedTitle = (String) gameDropdown.getSelectedItem();
        if ("<Choose a Game or Add New>".equals(selectedTitle)) {
            clearFields(); // Clear fields if the user selects the default option
            return;
        }

        // Retrieve the selected game from GameManager
        GameInfo selectedGame = gameManager.getGameByTitle(selectedTitle);
        if (selectedGame != null) {
            // Populate the fields with the selected game's details
            titleField.setText(selectedGame.getGameTitle());
            platformField.setText(selectedGame.getSystem());
            youtubeField.setText(selectedGame.getYoutubeLink());
            referenceField.setText(selectedGame.getReference());
            commentsField.setText(selectedGame.getComments());
            coverImagePathField.setText(selectedGame.getCoverImagePath());
            completedCheckBox.setSelected(selectedGame.getGameCompleted());
            runAgainCheckBox.setSelected(selectedGame.getRunback());
        }
    }

    /**
     * Handles the addition of a new game.
     */
    private void addNewGame() {
        // Collect inputs and create a new Game object
        String title = titleField.getText().trim();

        if (title.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Game title cannot be empty.", "Error", JOptionPane.ERROR_MESSAGE);
            return; // Don't proceed if the title is empty
        }

        // Check if the game title already exists
        for (GameInfo game : gameManager.getGames()) {
            if (game.getGameTitle().equalsIgnoreCase(title)) {
                JOptionPane.showMessageDialog(this, "A game with this title already exists.", "Error", JOptionPane.ERROR_MESSAGE);
                return; 
            }
        }

        String platform = platformField.getText();
        boolean completed = completedCheckBox.isSelected();
        String comments = commentsField.getText();
        String youtubeLink = youtubeField.getText();
        String reference = referenceField.getText();
        boolean runAgain = runAgainCheckBox.isSelected();
        
        // Get the cover file path (if any)
        String coverFilePath = (selectedCoverFile != null) ? selectedCoverFile.getAbsolutePath() : "";

        // Add the game with the cover path (empty if none selected)
        if (gameManager.addGame(title, platform, completed, comments, youtubeLink, reference, runAgain, coverFilePath)) {
            populateGameDropdown(); // Update the dropdown list
            clearFields(); // Clear the form for next input
        } else {
            JOptionPane.showMessageDialog(this, "Failed to add new game.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    /**
     * Saves changes made to an existing game.
     */
    private void saveGameChanges() {
        // Get the selected game from the dropdown
        String selectedTitle = (String) gameDropdown.getSelectedItem();
        GameInfo selectedGame = gameManager.getGameByTitle(selectedTitle);
    
        // If the selected game exists, update its details
        if (selectedGame != null) {
            String newTitle = titleField.getText();
            
            // Convert cover image path string to File
            File coverFile = new File(coverImagePathField.getText());
    
            // Ensure the file exists and is valid before passing to updateGame
            if (coverFile.exists() && coverFile.isFile()) {
                
                // Check if the cover file has changed
                if (!coverFile.getPath().equals(selectedGame.getCoverImagePath())) {
                    // Delete the old cover image if it exists
                    File oldCoverFile = new File(selectedGame.getCoverImagePath());
                    if (oldCoverFile.exists() && oldCoverFile.isFile()) {
                        boolean deleted = oldCoverFile.delete();  // Attempt to delete the old file
                        if (!deleted) {
                            JOptionPane.showMessageDialog(null, "Failed to delete the old cover image.", "Error", JOptionPane.ERROR_MESSAGE);
                            return;
                        }
                    }
    
                    // Copy the new cover image to the data/cover directory
                    File targetDirectory = new File("data/cover");
                    if (!targetDirectory.exists()) {
                        targetDirectory.mkdirs();  // Create the directory if it doesn't exist
                    }
    
                    // Keep the original file name
                    String originalFileName = coverFile.getName();
                    File newCoverFile = new File(targetDirectory, originalFileName);
    
                    // Handle file name conflict: if the file already exists, add a suffix
                    int counter = 1;
                    while (newCoverFile.exists()) {
                        // Append a number to the original name to avoid conflict
                        String nameWithoutExtension = originalFileName.substring(0, originalFileName.lastIndexOf('.'));
                        String extension = originalFileName.substring(originalFileName.lastIndexOf('.'));
                        newCoverFile = new File(targetDirectory, nameWithoutExtension + "_" + counter + extension);
                        counter++;
                    }
    
                    // Copy the file to the target directory
                    try {
                        Files.copy(coverFile.toPath(), newCoverFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
                        // Update the cover image path with the new file's path in the data/cover folder
                        selectedGame.setCoverImagePath(newCoverFile.getPath());
                    } catch (IOException e) {
                        e.printStackTrace();
                        JOptionPane.showMessageDialog(null, "Error copying cover image.", "Error", JOptionPane.ERROR_MESSAGE);
                        return;
                    }
                }
    
                // Now update other details and save
                gameManager.updateGame(selectedGame, newTitle, platformField.getText(), youtubeField.getText(), referenceField.getText(),
                                       commentsField.getText(), completedCheckBox.isSelected(), runAgainCheckBox.isSelected(), selectedGame.getCoverImagePath());
                populateGameDropdown();  // Refresh dropdown
            } else {
                JOptionPane.showMessageDialog(null, "Cover image file is invalid or doesn't exist.", "Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }
    
    private void uploadCoverButtonActionPerformed() {
        // Open a file chooser to select the cover image
        JFileChooser fileChooser = new JFileChooser();
        fileChooser.setFileFilter(new FileNameExtensionFilter("Image files", "jpg", "png"));
        int result = fileChooser.showOpenDialog(this);
        
        if (result == JFileChooser.APPROVE_OPTION) {
            selectedCoverFile = fileChooser.getSelectedFile(); // Get the selected file
            coverImagePathField.setText(selectedCoverFile.getAbsolutePath()); // Update the path field
            System.out.println("Selected Cover File: " + selectedCoverFile.getAbsolutePath()); // Debug print
        }
    }

    /**
     * Deletes the selected game.
     */
    private void deleteGame() {
        String selectedTitle = (String) gameDropdown.getSelectedItem();
        GameInfo selectedGame = gameManager.getGameByTitle(selectedTitle);

        if (selectedGame != null) {
            int confirm = JOptionPane.showConfirmDialog(this, "Are you sure you want to delete this game?", "Confirm Delete", JOptionPane.YES_NO_OPTION);
            if (confirm == JOptionPane.YES_OPTION) {
                gameManager.deleteGame(selectedGame);
                populateGameDropdown(); // Update the dropdown to remove the deleted game
                clearFields(); // Clear the fields
            }
        } else {
            JOptionPane.showMessageDialog(this, "No game selected for deletion.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }


    /**
     * Clears all the input fields and checkboxes.
     */
    private void clearFields() {
        titleField.setText("");
        platformField.setText("");
        youtubeField.setText("");
        commentsField.setText("");
        coverImagePathField.setText("");
        referenceField.setText("");
        selectedCoverFile = null;
        
        completedCheckBox.setSelected(false);
        runAgainCheckBox.setSelected(false);
    }

    /**
     * Opens a browser to the provided URL.
     *
     * @param url the URL to open.
     */
    private static void openBrowser(String url) {
        if (Desktop.isDesktopSupported()) {
            try {
                Desktop.getDesktop().browse(new URI(url));
            } catch (IOException | URISyntaxException ex) {
                ex.printStackTrace();
            }
        } else {
            System.out.println("Desktop is not supported. Cannot open the browser.");
        }
    }
}