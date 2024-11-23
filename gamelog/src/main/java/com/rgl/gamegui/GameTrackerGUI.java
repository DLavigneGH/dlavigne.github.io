package com.rgl.gamegui;

import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;

import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

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

    private GameManager gameManager;
    private JComboBox<String> gameDropdown;
    private TextFieldsPanel textFieldsPanel;
    private CheckboxesPanel checkboxesPanel;
    private ButtonsPanel buttonsPanel;

    /**
     * Constructs a new {@code GameTrackerGUI} instance, initializing the user interface
     * components and linking them to the {@code GameManager}.
     * Copies required resources, loads games, and sets up the GUI layout.
     */
    public GameTrackerGUI() {
        ResourceExtractor.copyResourcesToTarget("index.html", "script.js");
        gameManager = new GameManager();
        gameManager.loadGames();
        textFieldsPanel = new TextFieldsPanel();
        checkboxesPanel = new CheckboxesPanel();
        buttonsPanel = new ButtonsPanel();

        // Set up the window and layout
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

        populateGameDropdown(); // Populate dropdown with games

        // Add button actions
        buttonsPanel.addButtonActionListener(buttonsPanel.getUploadCoverButton(), e -> uploadCoverButtonActionPerformed());
        buttonsPanel.addButtonActionListener(buttonsPanel.getSubmitNewGameButton(), e -> addNewGame());
        buttonsPanel.addButtonActionListener(buttonsPanel.getSaveChangesButton(), e -> saveGameChanges());
        buttonsPanel.addButtonActionListener(buttonsPanel.getDeleteGameButton(), e -> deleteGame());
        buttonsPanel.addButtonActionListener(buttonsPanel.getOpenHtmlButton(), e -> openBrowser("http://localhost:8080/index.html"));

        // Add action listener to update fields when a game is selected
        gameDropdown.addActionListener(e -> updateUIFromSelectedGame());
    }

    // UI-related methods
    /**
     * Populates the dropdown menu with the titles of games managed by the {@code GameManager}.
     */
    private void populateGameDropdown() {
        gameDropdown.removeAllItems();
        gameDropdown.addItem("<Choose a Game or Add New>");
        for (GameInfo game : gameManager.getGames()) {
            gameDropdown.addItem(game.getGameTitle());
        }
    }

    /**
     * Updates the user interface fields to reflect the details of the selected game.
     * If no game is selected, clears the fields.
     */
    private void updateUIFromSelectedGame() {
        String selectedTitle = (String) gameDropdown.getSelectedItem();
        if ("<Choose a Game or Add New>".equals(selectedTitle)) {
            clearFields();
            return;
        }

        GameInfo selectedGame = gameManager.getGameByTitle(selectedTitle);
        if (selectedGame != null) {
            textFieldsPanel.getTitleField().setText(selectedGame.getGameTitle());
            textFieldsPanel.getPlatformField().setText(selectedGame.getSystem());
            textFieldsPanel.getYoutubeField().setText(selectedGame.getYoutubeLink());
            textFieldsPanel.getCommentsField().setText(selectedGame.getComments());
            textFieldsPanel.getReferenceField().setText(selectedGame.getReference());

            String relativeCoverPath = selectedGame.getCoverImagePath();
            if (!relativeCoverPath.isEmpty()) {
                File coverFile = new File(relativeCoverPath);
                textFieldsPanel.getCoverImagePathField().setText(coverFile.getAbsolutePath());
            } else {
                textFieldsPanel.getCoverImagePathField().setText("");
            }

            checkboxesPanel.getCompletedCheckBox().setSelected(selectedGame.getGameCompleted());
            checkboxesPanel.getRunAgainCheckBox().setSelected(selectedGame.getRunback());
        }
    }

    // Button action handlers
    /**
     * Handles the addition of a new game by validating input fields and
     * updating the {@code GameManager}.
     */
    private void addNewGame() {
        String title = textFieldsPanel.getTitleField().getText();

        if (title.trim().isEmpty()) {
            JOptionPane.showMessageDialog(this, "Title is a required field.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        String platform = textFieldsPanel.getPlatformField().getText();
        boolean completed = checkboxesPanel.getCompletedCheckBox().isSelected();
        String comments = textFieldsPanel.getCommentsField().getText();
        String youtubeLink = textFieldsPanel.getYoutubeField().getText();
        String reference = textFieldsPanel.getReferenceField().getText();
        boolean runAgain = checkboxesPanel.getRunAgainCheckBox().isSelected();
        String coverFilePath = textFieldsPanel.getCoverImagePathField().getText();

        if (gameManager.addGame(title, platform, completed, comments, youtubeLink, reference, runAgain, coverFilePath)) {
            populateGameDropdown();
            clearFields();
        } else {
            JOptionPane.showMessageDialog(this, "Failed to add new game.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }
    /**
     * Saves changes to the currently selected game by updating the {@code GameManager}.
     */
    private void saveGameChanges() {
        String selectedTitle = (String) gameDropdown.getSelectedItem();
        GameInfo selectedGame = gameManager.getGameByTitle(selectedTitle);

        if (selectedGame != null) {
            String newTitle = textFieldsPanel.getTitleField().getText();
            String platform = textFieldsPanel.getPlatformField().getText();
            String youtubeLink = textFieldsPanel.getYoutubeField().getText();
            String reference = textFieldsPanel.getReferenceField().getText();
            String comments = textFieldsPanel.getCommentsField().getText();
            boolean completed = checkboxesPanel.getCompletedCheckBox().isSelected();
            boolean runAgain = checkboxesPanel.getRunAgainCheckBox().isSelected();
            String coverImagePath = textFieldsPanel.getCoverImagePathField().getText();

            gameManager.updateOrSaveGame(selectedGame, selectedTitle, newTitle, platform, youtubeLink, reference, comments, completed, runAgain, coverImagePath);
            populateGameDropdown();
        }
    }

    /**
     * Deletes the currently selected game after user confirmation.
     */
    private void deleteGame() {
        String selectedTitle = (String) gameDropdown.getSelectedItem();
        GameInfo selectedGame = gameManager.getGameByTitle(selectedTitle);
    
        if (selectedGame != null) {
            int confirm = JOptionPane.showConfirmDialog(this, "Are you sure you want to delete this game?", "Confirm Delete", JOptionPane.YES_NO_OPTION);
            if (confirm == JOptionPane.YES_OPTION) {
                if (gameManager.deleteGame(selectedGame)) {
                    populateGameDropdown();
                    clearFields();
                } else {
                    JOptionPane.showMessageDialog(this, "Failed to delete the game.", "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        } else {
            JOptionPane.showMessageDialog(this, "No game selected for deletion.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    /**
     * Handles the upload of a cover image by showing a file chooser dialog and updating the appropriate field.
     */
    private void uploadCoverButtonActionPerformed() {
        JFileChooser fileChooser = new JFileChooser();
        fileChooser.setFileFilter(new FileNameExtensionFilter("Image files", "jpg", "png"));
        int result = fileChooser.showOpenDialog(this);

        if (result == JFileChooser.APPROVE_OPTION) {
            File selectedCoverFile = fileChooser.getSelectedFile();
            textFieldsPanel.getCoverImagePathField().setText(selectedCoverFile.getAbsolutePath());
        }
    }

    // Utility methods
    /**
     * Clears all text fields and checkboxes in the user interface.
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
     * Opens a browser window to the specified URL.
     *
     * @param url The URL to open.
     */
    private static void openBrowser(String url) {
        if (Desktop.isDesktopSupported()) {
            try {
                Desktop.getDesktop().browse(new URI(url));
            } catch (IOException | URISyntaxException ex) {
                ex.printStackTrace();
            }
        }
    }
}