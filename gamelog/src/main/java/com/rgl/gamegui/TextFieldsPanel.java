package com.rgl.gamegui;

import javax.swing.*;
import java.awt.*;

public class TextFieldsPanel extends JPanel {
    private JTextField titleField, platformField, youtubeField, commentsField, referenceField, coverImagePathField;

    public TextFieldsPanel() {
        setLayout(new GridLayout(6, 2));  // Use grid layout to arrange labels and text fields

        titleField = new JTextField();
        platformField = new JTextField();
        youtubeField = new JTextField();
        commentsField = new JTextField();
        referenceField = new JTextField();
        coverImagePathField = new JTextField();
        coverImagePathField.setEditable(false);  // Make this field non-editable

        // Add labels and text fields to the panel
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

    // Getter methods to access the text fields
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
