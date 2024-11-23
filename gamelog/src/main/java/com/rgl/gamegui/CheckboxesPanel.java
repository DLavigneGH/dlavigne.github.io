package com.rgl.gamegui;

import javax.swing.*;
import java.awt.*;

public class CheckboxesPanel extends JPanel {
    private JCheckBox completedCheckBox, runAgainCheckBox;

    public CheckboxesPanel() {
        // Set up a horizontal layout for the checkboxes
        setLayout(new FlowLayout(FlowLayout.LEFT));

        completedCheckBox = new JCheckBox("Completed");
        runAgainCheckBox = new JCheckBox("Run Again");

        // Add checkboxes to the panel
        add(completedCheckBox);
        add(runAgainCheckBox);
    }

    // Getter methods to access the checkboxes
    public JCheckBox getCompletedCheckBox() {
        return completedCheckBox;
    }

    public JCheckBox getRunAgainCheckBox() {
        return runAgainCheckBox;
    }
}
