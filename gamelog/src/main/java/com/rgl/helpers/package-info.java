/**
 * Contains utility classes for supporting various application functionalities.
 * <p>
 * This package includes:
 * <p>
 * - FileUtils: For file operations such as deletion and copying.
 *   Provides methods to delete files and copy files to a target directory with handling
 *   for duplicate filenames.
 * <p>
 * - HtmlOpener: Handles opening HTML files in the system's default web browser.
 *   It provides functionality to extract an HTML resource from the application's
 *   classpath to the execution directory and open it in the browser.
 * <p>
 * - ResourceExtractor: Extracts resource files from the application classpath to the
 *   target directory. Currently used to copy the `index.html` file to the execution
 *   directory, ensuring it is available for the application to serve or open.
 * <p>
 * - SimpleHttpServer: Starts a simple HTTP server that serves files from the application's
 *   execution directory. The server listens on port 8080 and serves files located in the
 *   root directory of the application, returning a 404 response if a file is not found.
 */

package com.rgl.helpers;