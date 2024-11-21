package com.rgl.helpers;

import java.io.InputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

/**
 * Extracts resource files from the application classpath to the target directory.
 * 
 * Currently used to copy the `index.html` file to the execution directory, 
 * ensuring it is available for the application to serve or open.
 */

public class ResourceExtractor {

    /**
     * Copies the resource file (`index.html`) to the target directory.
     */
    public static void copyIndexHtmlToTarget() {
        InputStream in = ResourceExtractor.class.getClassLoader().getResourceAsStream("index.html");

        if (in == null) {
            System.out.println("Resource not found: index.html");
            return;
        }

        try {
            // Define the output path in the target folder (root)
            String outputPath = Paths.get(System.getProperty("user.dir"), "index.html").toString();
            
            // Ensure the directory exists
            Files.createDirectories(Paths.get(System.getProperty("user.dir")));

            // Create the output stream to write to the target folder
            try (FileOutputStream out = new FileOutputStream(outputPath)) {
                byte[] buffer = new byte[1024];
                int length;
                while ((length = in.read(buffer)) > 0) {
                    out.write(buffer, 0, length);
                }
            }

            System.out.println("index.html copied to: " + outputPath);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
