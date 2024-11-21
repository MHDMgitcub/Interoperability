// Fetch the JSON file from the same folder
fetch('scriptlog.json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Display each entry in the JSON data
        const entriesDiv = document.getElementById("entries");

        // Clear existing content
        entriesDiv.innerHTML = '';

        // Loop through each entry in the JSON data
        for (const date in data) {
            if (data.hasOwnProperty(date)) {
                const ranIn = data[date].ran_in;
                // Create a new paragraph for each entry
                const entryParagraph = document.createElement("p");
                entryParagraph.innerText = `✅ ${date}: ${ranIn}`;
                
                // Append the paragraph to the entriesDiv
                entriesDiv.appendChild(entryParagraph);
            }
        }
    })
    .catch(error => {
        console.error('Error fetching JSON:', error);
        const errorParagraph = document.createElement("p");
        errorParagraph.innerText = 'Error fetching data.';
        document.getElementById("entries").appendChild(errorParagraph);
    });