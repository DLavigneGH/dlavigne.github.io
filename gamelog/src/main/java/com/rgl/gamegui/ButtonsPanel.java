package com.rgl.gamegui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener;

/**
 * A panel containing buttons for managing game-related actions in the Game Tracker application.
 * This panel includes buttons for uploading covers, submitting new games, saving changes,
 * deleting games, and opening an HTML view.
 */
public class ButtonsPanel extends JPanel {
    private JButton uploadCoverButton, submitNewGameButton, saveChangesButton, deleteGameButton, openHtmlButton;

    /**
     * Constructs a new {@code ButtonsPanel} and initializes buttons for various game management actions.
     * The panel uses a centered flow layout to arrange the buttons.
     */
    public ButtonsPanel() {
        setLayout(new FlowLayout(FlowLayout.CENTER));

        // Create buttons
        uploadCoverButton = new JButton("Upload Cover");
        submitNewGameButton = new JButton("Submit New Game");
        saveChangesButton = new JButton("Save Changes");
        deleteGameButton = new JButton("Delete Game");
        openHtmlButton = new JButton("Open HTML");

        // Add buttons to the panel
        add(uploadCoverButton);
        add(submitNewGameButton);
        add(saveChangesButton);
        add(deleteGameButton);
        add(openHtmlButton);
    }

    /**
     * Adds an {@code ActionListener} to a specified button.
     *
     * @param button          The {@code JButton} to which the {@code ActionListener} will be added.
     * @param actionListener  The {@code ActionListener} that will handle the button's action events.
     */
    public void addButtonActionListener(JButton button, ActionListener actionListener) {
        button.addActionListener(actionListener);
    }

    // Getter methods
    public JButton getUploadCoverButton() {
        return uploadCoverButton;
    }

    public JButton getSubmitNewGameButton() {
        return submitNewGameButton;
    }

    public JButton getSaveChangesButton() {
        return saveChangesButton;
    }

    public JButton getDeleteGameButton() {
        return deleteGameButton;
    }

    public JButton getOpenHtmlButton() {
        return openHtmlButton;
    }
}
