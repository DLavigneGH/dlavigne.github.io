package com.rgl.gamegui;

import javax.swing.*;
import java.awt.*;

/**
 * A panel containing checkboxes for managing game status options.
 * This panel is used in the Game Tracker application to collect or display 
 * boolean information about whether a game has been completed or should be played again.
 */
public class CheckboxesPanel extends JPanel {

    private JCheckBox completedCheckBox, runAgainCheckBox;

    /**
     * Constructs a new {@code CheckboxesPanel} with checkboxes for game status options.
     * The panel uses a horizontal flow layout to display checkboxes for "Completed" and "Run Again" options.
     */
    public CheckboxesPanel() {
        setLayout(new FlowLayout(FlowLayout.LEFT));

        completedCheckBox = new JCheckBox("Completed");
        runAgainCheckBox = new JCheckBox("Run Again");

        add(completedCheckBox);
        add(runAgainCheckBox);
    }

    // Getter methods
    public JCheckBox getCompletedCheckBox() {
        return completedCheckBox;
    }

    public JCheckBox getRunAgainCheckBox() {
        return runAgainCheckBox;
    }
}
