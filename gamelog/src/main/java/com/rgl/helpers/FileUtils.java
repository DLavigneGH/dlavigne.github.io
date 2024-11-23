package com.rgl.helpers;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;

/**
 * Utility class for file operations such as deletion and copying.
 * Provides methods to delete files and copy files to a target directory with handling
 * for duplicate filenames.
 */
public class FileUtils {

    /**
     * Deletes the specified file if it exists.
     *
     * @param file The file to be deleted.
     * @return {@code true} if the file was successfully deleted, {@code false} if the file does not exist or deletion failed.
     */
    public static boolean deleteFile(File file) {
        if (file.exists()) {
            return file.delete();
        }
        return false;
    }

    /**
     * Copies the specified source file to the target directory.
     * If a file with the same name already exists in the target directory, a numeric suffix is added to the new file's name to avoid overwriting.
     *
     * @param sourceFile      The file to be copied.
     * @param targetDirectory The directory to which the file will be copied.
     * @return The {@code File} object representing the copied file in the target directory.
     * @throws IOException If an I/O error occurs during the copying process.
     */
    public static File copyFileToDirectory(File sourceFile, File targetDirectory) throws IOException {
        if (!targetDirectory.exists()) {
            targetDirectory.mkdirs(); // Ensure the directory exists
        }

        String originalFileName = sourceFile.getName();
        File newFile = new File(targetDirectory, originalFileName);

        int counter = 1;
        while (newFile.exists()) {
            String nameWithoutExtension = originalFileName.substring(0, originalFileName.lastIndexOf('.'));
            String extension = originalFileName.substring(originalFileName.lastIndexOf('.'));
            newFile = new File(targetDirectory, nameWithoutExtension + "_" + counter + extension);
            counter++;
        }

        Files.copy(sourceFile.toPath(), newFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
        return newFile;
    }
}
