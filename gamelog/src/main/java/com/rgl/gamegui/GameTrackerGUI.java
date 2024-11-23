package com.rgl.gamegui;

import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;

import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;

import com.rgl.gamedata.GameInfo;

/**
 * Implements the graphical user interface (GUI) for the Game Tracker application.
 * 
 * Provides fields and controls for adding, updating, and deleting game information,
 * as well as a dropdown menu for selecting games. The GUI is integrated with 
 * the GameManager to manage game data and update the UI accordingly.
 */

 public class GameTrackerGUI extends JFrame {

    private GameManager gameManager;

    // Dropdown
    private JComboBox<String> gameDropdown;
    
    // Panels
    private TextFieldsPanel textFieldsPanel;
    private CheckboxesPanel checkboxesPanel;
    private ButtonsPanel buttonsPanel;

    public GameTrackerGUI() {

        // Initialize the GameManager
        gameManager = new GameManager();
        gameManager.loadGames();

        // Initialize the panels
        textFieldsPanel = new TextFieldsPanel();
        checkboxesPanel = new CheckboxesPanel();
        buttonsPanel = new ButtonsPanel();

        // Set up the window title, size, and layout
        setTitle("Game Tracker");
        setSize(400, 420);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BoxLayout(getContentPane(), BoxLayout.Y_AXIS));

        // Add components to the frame
        add(new JLabel("Select Game:"));
        gameDropdown = new JComboBox<>();
        add(gameDropdown);
        add(textFieldsPanel);
        add(checkboxesPanel);
        add(buttonsPanel);

        // Populate dropdown
        populateGameDropdown();

        // Button actions
        buttonsPanel.addButtonActionListener(buttonsPanel.getUploadCoverButton(), e -> uploadCoverButtonActionPerformed());
        buttonsPanel.addButtonActionListener(buttonsPanel.getSubmitNewGameButton(), e -> addNewGame());
        buttonsPanel.addButtonActionListener(buttonsPanel.getSaveChangesButton(), e -> saveGameChanges());
        buttonsPanel.addButtonActionListener(buttonsPanel.getDeleteGameButton(), e -> deleteGame());
        buttonsPanel.addButtonActionListener(buttonsPanel.getOpenHtmlButton(), e -> openBrowser("http://localhost:8080/index.html"));

        // Add action listener to update fields when a game is selected
        gameDropdown.addActionListener(e -> updateUIFromSelectedGame());
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
            System.out.println("Adding to dropdown: " + game.getGameTitle());  // Debug print
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
        if (selectedGame == null) {
            System.out.println("Selected game not found: " + selectedTitle); // Debug print
            return;
        }
        if (selectedGame != null) {
            // Populate the fields with the selected game's details
            textFieldsPanel.getTitleField().setText(selectedGame.getGameTitle());
            textFieldsPanel.getPlatformField().setText(selectedGame.getSystem());
            textFieldsPanel.getYoutubeField().setText(selectedGame.getYoutubeLink());
            textFieldsPanel.getCommentsField().setText(selectedGame.getComments());
            textFieldsPanel.getReferenceField().setText(selectedGame.getReference());
    
            // Convert the relative cover image path to the absolute path
            String relativeCoverPath = selectedGame.getCoverImagePath();
            if (!relativeCoverPath.isEmpty()) {
                // Convert the relative path to an absolute path
                File coverFile = new File(relativeCoverPath);
                textFieldsPanel.getCoverImagePathField().setText(coverFile.getAbsolutePath());
            } else {
                textFieldsPanel.getCoverImagePathField().setText(""); // Clear the field if no cover is selected
            }
    
            checkboxesPanel.getCompletedCheckBox().setSelected(selectedGame.getGameCompleted());
            checkboxesPanel.getRunAgainCheckBox().setSelected(selectedGame.getRunback());
        }
    }

    /**
     * Handles the addition of a new game.
     */
    private void addNewGame() {
        // Collect data from the panels
        String title = textFieldsPanel.getTitleField().getText();
        String platform = textFieldsPanel.getPlatformField().getText();
        boolean completed = checkboxesPanel.getCompletedCheckBox().isSelected();
        String comments = textFieldsPanel.getCommentsField().getText();
        String youtubeLink = textFieldsPanel.getYoutubeField().getText();
        String reference = textFieldsPanel.getReferenceField().getText();
        boolean runAgain = checkboxesPanel.getRunAgainCheckBox().isSelected();
        String coverFilePath = textFieldsPanel.getCoverImagePathField().getText();
    
        if (gameManager.addGame(title, platform, completed, comments, youtubeLink, reference, runAgain, coverFilePath)) {
            populateGameDropdown();  // Update the dropdown list
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
            String newTitle = textFieldsPanel.getTitleField().getText();
    
            // Convert cover image path string to File
            File coverFile = new File(textFieldsPanel.getCoverImagePathField().getText());
    
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
                        // Update the cover image path with the relative path in the data/cover folder
                        selectedGame.setCoverImagePath("data/cover/" + newCoverFile.getName());  // Relative path for JSON
                    } catch (IOException e) {
                        e.printStackTrace();
                        JOptionPane.showMessageDialog(null, "Error copying cover image.", "Error", JOptionPane.ERROR_MESSAGE);
                        return;
                    }
                }
    
                // Now update other details and save
                gameManager.updateGame(selectedGame, newTitle, textFieldsPanel.getPlatformField().getText(), textFieldsPanel.getYoutubeField().getText(), textFieldsPanel.getReferenceField().getText(),
                textFieldsPanel.getCommentsField().getText(), checkboxesPanel.getCompletedCheckBox().isSelected(), checkboxesPanel.getRunAgainCheckBox().isSelected(), "data/cover/" + coverFile.getName());
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
            File selectedCoverFile = fileChooser.getSelectedFile(); // Get the selected file
            textFieldsPanel.getCoverImagePathField().setText(selectedCoverFile.getAbsolutePath()); // Update the path field
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

        textFieldsPanel.getTitleField().setText("");
        textFieldsPanel.getPlatformField().setText("");
        textFieldsPanel.getYoutubeField().setText("");
        textFieldsPanel.getCommentsField().setText("");
        textFieldsPanel.getReferenceField().setText("");
        textFieldsPanel.getCoverImagePathField().setText("");
        checkboxesPanel.getCompletedCheckBox().setSelected(false);
        checkboxesPanel.getRunAgainCheckBox().setSelected(false);
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