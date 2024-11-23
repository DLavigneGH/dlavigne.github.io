package com.rgl.gamegui;

import javax.swing.*;
import java.awt.*;

/**
 * A panel containing text fields for inputting game-related information.
 * This panel is used in the Game Tracker application to collect or display details
 * about a game, such as the title, platform, YouTube link, comments, reference, and cover image path.
 */
public class TextFieldsPanel extends JPanel {

    /**
     * Constructs a new {@code TextFieldsPanel} with labels and text fields for game information.
     * The panel uses a grid layout with six rows and two columns, displaying labels alongside the corresponding text fields.
     * The cover image path field is non-editable.
     */
    private JTextField titleField, platformField, youtubeField, commentsField, referenceField, coverImagePathField;

    public TextFieldsPanel() {
        setLayout(new GridLayout(6, 2));

        titleField = new JTextField();
        platformField = new JTextField();
        youtubeField = new JTextField();
        commentsField = new JTextField();
        referenceField = new JTextField();
        coverImagePathField = new JTextField();
        coverImagePathField.setEditable(false);

        add(new JLabel("Game Title:"));
        add(titleField);
        add(new JLabel("Platform:"));
        add(platformField);
        add(new JLabel("YouTube Link:"));
        add(youtubeField);
        add(new JLabel("Comments:"));
        add(commentsField);
        add(new JLabel("Reference:"));
        add(referenceField);
        add(new JLabel("Cover Image Path:"));
        add(coverImagePathField);
    }

    // Getter methods
    public JTextField getTitleField() {
        return titleField;
    }

    public JTextField getPlatformField() {
        return platformField;
    }

    public JTextField getYoutubeField() {
        return youtubeField;
    }

    public JTextField getCommentsField() {
        return commentsField;
    }

    public JTextField getReferenceField() {
        return referenceField;
    }

    public JTextField getCoverImagePathField() {
        return coverImagePathField;
    }
}
