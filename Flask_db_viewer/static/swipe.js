document.addEventListener("DOMContentLoaded", function () {
    let touchStartX = 0;
    let touchEndX = 0;

    document.addEventListener("touchstart", function (event) {
        touchStartX = event.changedTouches[0].screenX;
    });

    document.addEventListener("touchend", function (event) {
        touchEndX = event.changedTouches[0].screenX;
        handleSwipe();
    });

    function handleSwipe() {
        let swipeThreshold = 50; // Minimum swipe distance
        let currentPath = window.location.pathname;
        let recipeIdMatch = currentPath.match(/^\/(\d+)(\/clock)?$/); // Matches "/18" or "/18/clock"

        if (recipeIdMatch) {
            let recipeId = recipeIdMatch[1];
            let isClockPage = recipeIdMatch[2] === "/clock";

            if (touchStartX - touchEndX > swipeThreshold) {
                // Left swipe → Go from recipe details to clock page
                if (!isClockPage) {
                    window.location.href = `/${recipeId}/clock`;
                }
            } else if (touchEndX - touchStartX > swipeThreshold) {
                // Right swipe → Go from clock page back to recipe details
                if (isClockPage) {
                    window.location.href = `/${recipeId}`;
                }
            }
        }
    }
});