package com.rgl;

import com.rgl.gamegui.GameTrackerGUI;
import com.rgl.helpers.SimpleHttpServer;

/**
 * Main entry point for the Game Tracker application.
 * 
 * This class initializes and starts the HTTP server on a separate thread 
 * and then launches the graphical user interface (GUI) for managing game data.
 */

public class Main {
    /**
     * The main method that starts the HTTP server and launches the Game Tracker GUI.
     *
     * It starts the HTTP server on a separate thread to ensure the GUI remains responsive.
     * Once the server is running, it then makes the GameTrackerGUI visible for the user to interact with.
     * 
     * @param args command-line arguments (not used in this application).
     */    
    public static void main(String[] args) {
        // Start the HTTP server in a new thread so it doesn't block the GUI
        new Thread(() -> {
            try {
                SimpleHttpServer.startServer();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }).start();

        // Launch the GUI
        new GameTrackerGUI().setVisible(true);
    }
}
