package com.rgl.gamegui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener;

public class ButtonsPanel extends JPanel {
    private JButton uploadCoverButton, submitNewGameButton, saveChangesButton, deleteGameButton, openHtmlButton;

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

    // Getter methods to access buttons
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

    // Method to add ActionListener to buttons
    public void addButtonActionListener(JButton button, ActionListener actionListener) {
        button.addActionListener(actionListener);
    }
}
