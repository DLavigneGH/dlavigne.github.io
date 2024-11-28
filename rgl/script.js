let games = [];  // Original full array of games
let currentGames = [];  // Currently displayed (filtered) games
let isFilterApplied = false;  // Flag to track if filter is applied

// Sorting states for title and platform
let sortTitleAscending = true;      // Track sorting order for titles
let sortPlatformAscending = true;   // Track sorting order for platforms

// Fetch the JSON file and initialize the games
fetch('https://dlavignegh.github.io/dlavigne.github.io/rgl/data/gameTable.json')
    .then(response => response.json())
    .then(data => {
        games = data;  // Store the full games array
        currentGames = [...games];  // Initialize currentGames as a copy of the full array
        displayGames(currentGames);  // Display all games initially
    })
    .catch(error => console.error('Error loading the JSON file:', error));

// Function to display games in the table
function displayGames(gameList) {
    const tableBody = document.getElementById('gamesTable').getElementsByTagName('tbody')[0];
    tableBody.innerHTML = '';  // Clear existing rows

    gameList.forEach(game => {
        const row = document.createElement('tr');

        // Create table data cells for each game property
        row.innerHTML = `
            <td>${game.gameTitle}</td>
            <td>${game.system}</td>
            <td><input type="checkbox" ${game.gameCompleted ? 'checked' : ''} disabled></td>
            <td>${game.comments}</td>
            <td><a href="${game.youtubeLink}" target="_blank">${game.youtubeLink}</a></td>
            <td>${game.referencedBy}</td>
            <td><input type="checkbox" ${game.runAgain ? 'checked' : ''} disabled></td>
        `;

        // If the game has a cover image, add an image tag for the popup functionality
        if (game.coverImagePath) {
            const coverImageUrl = 'https://dlavignegh.github.io/dlavigne.github.io/rgl/' + game.coverImagePath.replace(/^.*[\\\/]/, 'data/cover/');  // Convert path to URL
            const coverImagePopup = document.createElement('span');
            coverImagePopup.classList.add('cover-popup');
            coverImagePopup.setAttribute('data-image-url', coverImageUrl);
            coverImagePopup.textContent = '🎮';  // Icon to indicate the cover image

            // Add event listener for the popup when hovering over the game title
            row.cells[0].appendChild(coverImagePopup);
        }

        tableBody.appendChild(row);
    });
}

// Popup management variables
let popup; // Track the popup

// To show the popup when hovering over the title
document.addEventListener('mouseover', function(event) {
    if (event.target.classList.contains('cover-popup')) {
        const imageUrl = event.target.getAttribute('data-image-url');
        
        // Create and show the popup only if it doesn't already exist
        if (!popup) {
            popup = document.createElement('div');
            popup.classList.add('popup');
            popup.innerHTML = `<img src="${imageUrl}" alt="Cover Image" />`;
            document.body.appendChild(popup);
        }
        
        // Position the popup near the cursor
        popup.style.position = 'absolute';
        popup.style.top = `${event.pageY + 10}px`;
        popup.style.left = `${event.pageX + 10}px`;
    }
});

document.addEventListener('mouseout', function(event) {
    if (event.target.classList.contains('cover-popup') && popup) {
        document.body.removeChild(popup);
        popup = null;  // Reset the popup variable
    }
});

// Optional: Update popup position on mouse movement
document.addEventListener('mousemove', function(event) {
    if (popup) {
        popup.style.top = `${event.pageY + 10}px`;
        popup.style.left = `${event.pageX + 10}px`;
    }
});

// Filter games by title based on the search input
function filterGamesByTitle() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const filteredGames = games.filter(game => 
        game.gameTitle.toLowerCase().includes(searchTerm)  // Filter titles that include the search term
    );

    displayGames(filteredGames);
}

// Toggles sorting by game title (A-Z/Z-A)
function toggleSortByName() {
    const gamesToSort = isFilterApplied ? currentGames : games;

    const sortedGames = [...gamesToSort].sort((a, b) => {
        return sortTitleAscending
            ? a.gameTitle.localeCompare(b.gameTitle)  // A-Z
            : b.gameTitle.localeCompare(a.gameTitle); // Z-A
    });

    sortTitleAscending = !sortTitleAscending;
    document.getElementById('sortByNameButton').textContent = sortTitleAscending ? 'A-Z' : 'Z-A';

    displayGames(sortedGames);
}

// Toggles sorting by platform (A-Z/Z-A)
function toggleSortByPlatform() {
    const gamesToSort = isFilterApplied ? currentGames : games;

    const sortedGames = [...gamesToSort].sort((a, b) => {
        return sortPlatformAscending
            ? a.system.localeCompare(b.system)  // A-Z
            : b.system.localeCompare(a.system); // Z-A
    });

    sortPlatformAscending = !sortPlatformAscending;
    document.getElementById('sortByPlatformButton').textContent = sortPlatformAscending ? 'A-Z' : 'Z-A';

    displayGames(sortedGames);
}

// Filters by completed games based on checkbox state
function filterCompletedCheckbox() {
    const isChecked = document.getElementById('filterCompletedCheckbox').checked;
    
    isFilterApplied = true;

    if (isChecked) {
        currentGames = games.filter(game => game.gameCompleted);
    } else {
        currentGames = games.filter(game => !game.gameCompleted);
    }
    document.getElementById('filterRunAgainCheckbox').checked = false;
    displayGames(currentGames);
}

// Filters by 'Run Again' games based on checkbox state
function filterRunAgainCheckbox() {
    const isChecked = document.getElementById('filterRunAgainCheckbox').checked;
    
    isFilterApplied = true;  // Indicate that a filter is applied

    if (isChecked) {
        currentGames = games.filter(game => game.runAgain);
    } else {
        currentGames = games.filter(game => !game.runAgain);
    }

    document.getElementById('filterCompletedCheckbox').checked = false;
    displayGames(currentGames);
}

// Resets the Completed filter (uncheck the checkbox and show both completed and not completed games)
function resetCompletedFilter() {
    document.getElementById('filterCompletedCheckbox').checked = false;
    // Reset to show both completed and not completed games
    currentGames = [...games];
    displayGames(currentGames);
}

// Reset the Runback filter (uncheck the checkbox and show both run-again and not run-again games)
function resetRunbackFilter() {
    document.getElementById('filterRunAgainCheckbox').checked = false;
    // Reset to show both run-again and not run-again games
    currentGames = [...games];
    displayGames(currentGames);
}

// Resets all filters and sorting
function resetFilter() {
    document.getElementById('searchInput').value = '';

    document.getElementById('filterCompletedCheckbox').checked = false;
    document.getElementById('filterRunAgainCheckbox').checked = false;

    sortTitleAscending = true;
    sortPlatformAscending = true;

    document.getElementById('sortByNameButton').textContent = 'A-Z';
    document.getElementById('sortByPlatformButton').textContent = 'A-Z';

    isFilterApplied = false;

    currentGames = [...games];
    displayGames(currentGames);
}
