setTimeout(() => {
    const flashes = document.querySelectorAll('.flash-message');

    flashes.forEach((flash) => {
        flash.style.transition = "0.5s";
        flash.style.opacity = "0";

        setTimeout(() => {
            flash.remove();
        }, 500);
    });

}, 3000);

console.log("testing JS")
