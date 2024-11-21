package com.rgl.helpers;

import java.awt.Desktop;
import java.io.*;
import java.nio.file.*;

/**
 * Handles opening HTML files in the system's default web browser.
 * 
 * Provides functionality to extract an HTML resource from the application's
 * classpath to the execution directory and open it in the browser.
 */
public class HtmlOpener {
    /**
     * Extracts an HTML file from the application's resources and opens it in the default web browser.
     *
     * This method extracts the specified HTML file from the resources folder, copies it to the
     * execution directory (if not already present), and then opens it in the default browser.
     * 
     * @param resourceName the name of the HTML resource to open.
     */
    public static void openHtmlFromResources(String resourceName) {
        try {
            // Extract the HTML file from resources and copy to execution directory
            Path htmlFile = extractResourceToExecutionDirectory(resourceName);
            
            // Open the HTML file in the default browser
            Desktop.getDesktop().browse(htmlFile.toUri());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    
    /**
     * Extracts an HTML resource file from the classpath and copies it to the execution directory.
     * If the file already exists in the execution directory, it is not overwritten.
     *
     * @param resourceName the name of the HTML resource to extract.
     * @return the path to the extracted HTML file.
     * @throws IOException if an I/O error occurs while extracting the file.
     */
    private static Path extractResourceToExecutionDirectory(String resourceName) throws IOException {
        // Get the directory where the JAR file was executed
        Path executionDir = Paths.get("").toAbsolutePath();
        
        // Create the destination path for the HTML file
        Path htmlFile = executionDir.resolve(resourceName);
        
        // Check if file already exists to avoid overwriting
        if (Files.exists(htmlFile)) {
            System.out.println("HTML file already exists at: " + htmlFile);
        } else {
            // Extract the resource from classpath
            InputStream resourceStream = HtmlOpener.class.getClassLoader().getResourceAsStream(resourceName);
            if (resourceStream == null) {
                throw new FileNotFoundException("Resource not found: " + resourceName);
            }

            // Save the resource (HTML) to the execution directory
            Files.copy(resourceStream, htmlFile, StandardCopyOption.REPLACE_EXISTING);
            System.out.println("Extracted HTML file to: " + htmlFile);
        }

        return htmlFile;
    }
}
