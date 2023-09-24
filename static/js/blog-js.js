// Obtén referencias a los elementos HTML
const imageContainer = document.getElementById("image-container");
const imageInput = document.getElementById("image-input");
const changeImageButton = document.getElementById("change-image-button");

// Agrega un evento de clic al contenedor de imagen
imageContainer.addEventListener("click", () => {
    imageInput.click(); // Simula el clic en el input de tipo file
});

// Agrega un evento de cambio al input de tipo file
imageInput.addEventListener("change", (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
        // Cambia la imagen en el contenedor
        const reader = new FileReader();
        reader.onload = (event) => {
            const newImage = document.createElement("img");
            newImage.src = event.target.result;
            newImage.alt = "Nueva Imagen";
            newImage.style.maxWidth = "100%";
            newImage.style.height = "auto";
            imageContainer.innerHTML = ""; // Limpia el contenedor existente
            imageContainer.appendChild(newImage);
        };
        reader.readAsDataURL(selectedFile);
    }
});

// Agrega un evento de clic al botón de cambio de imagen
changeImageButton.addEventListener("click", () => {
    imageInput.click(); // Simula el clic en el input de tipo file
});
