let games = [];  // Original full array of games
let currentGames = [];  // Currently displayed (filtered) games
let isFilterApplied = false;  // Flag to track if filter is applied

// Sorting states for title and platform
let sortTitleAscending = true;      // Track sorting order for titles
let sortPlatformAscending = true;   // Track sorting order for platforms

// Fetch the JSON file and initialize the games
fetch('http://localhost:8080/data/gameTable.json')
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
        tableBody.appendChild(row);
    });
}
// Function to filter games by title based on the search input
function filterGamesByTitle() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const filteredGames = games.filter(game => 
        game.gameTitle.toLowerCase().includes(searchTerm)  // Filter titles that include the search term
    );

    displayGames(filteredGames);  // Display the filtered list
}

// Function to toggle sorting by game title (A-Z/Z-A)
function toggleSortByName() {
    const gamesToSort = isFilterApplied ? currentGames : games;

    const sortedGames = [...gamesToSort].sort((a, b) => {
        return sortTitleAscending
            ? a.gameTitle.localeCompare(b.gameTitle)  // A-Z
            : b.gameTitle.localeCompare(a.gameTitle); // Z-A
    });

    sortTitleAscending = !sortTitleAscending;
    document.getElementById('sortByNameButton').textContent = sortTitleAscending ? 'A-Z' : 'Z-A';

    displayGames(sortedGames);  // Display the sorted games
}

// Function to toggle sorting by platform (A-Z/Z-A)
function toggleSortByPlatform() {
    const gamesToSort = isFilterApplied ? currentGames : games;

    const sortedGames = [...gamesToSort].sort((a, b) => {
        return sortPlatformAscending
            ? a.system.localeCompare(b.system)  // A-Z
            : b.system.localeCompare(a.system); // Z-A
    });

    sortPlatformAscending = !sortPlatformAscending;
    document.getElementById('sortByPlatformButton').textContent = sortPlatformAscending ? 'A-Z' : 'Z-A';

    displayGames(sortedGames);  // Display the sorted games
}

// Function to reset the Completed filter (uncheck the checkbox and show both completed and not completed games)
function resetCompletedFilter() {
    document.getElementById('filterCompletedCheckbox').checked = false;
    // Reset to show both completed and not completed games
    currentGames = [...games];  // Show all games
    displayGames(currentGames);
}

// Function to reset the Runback filter (uncheck the checkbox and show both run-again and not run-again games)
function resetRunbackFilter() {
    document.getElementById('filterRunAgainCheckbox').checked = false;
    // Reset to show both run-again and not run-again games
    currentGames = [...games];  // Show all games
    displayGames(currentGames);
}

// Function to filter by completed games based on checkbox state
function filterCompletedCheckbox() {
    const isChecked = document.getElementById('filterCompletedCheckbox').checked;
    
    isFilterApplied = true;  // Indicate that a filter is applied

    if (isChecked) {
        currentGames = games.filter(game => game.gameCompleted);  // Show completed games
    } else {
        currentGames = games.filter(game => !game.gameCompleted);  // Show not completed games
    }
    document.getElementById('filterRunAgainCheckbox').checked = false;
    displayGames(currentGames);
}

// Function to filter by 'Run Again' games based on checkbox state
function filterRunAgainCheckbox() {
    const isChecked = document.getElementById('filterRunAgainCheckbox').checked;
    
    isFilterApplied = true;  // Indicate that a filter is applied

    if (isChecked) {
        currentGames = games.filter(game => game.runAgain);  // Show run again games
    } else {
        currentGames = games.filter(game => !game.runAgain);  // Show games not marked for run again
    }

    document.getElementById('filterCompletedCheckbox').checked = false;
    displayGames(currentGames);
}

// Function to reset all filters and sorting
function resetFilter() {
    document.getElementById('filterCompletedCheckbox').checked = false;
    document.getElementById('filterRunAgainCheckbox').checked = false;

    sortTitleAscending = true;
    sortPlatformAscending = true;

    document.getElementById('sortByNameButton').textContent = 'A-Z';
    document.getElementById('sortByPlatformButton').textContent = 'A-Z';

    isFilterApplied = false;  // No filter applied

    currentGames = [...games];  // Reset to full game list
    displayGames(currentGames);  // Show all games
}
