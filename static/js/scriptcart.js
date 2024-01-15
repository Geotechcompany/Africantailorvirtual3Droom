// Store selected images in an array
let selectedImages = [];

// Function to handle image selection
function selectImage(imageName) {
    const index = selectedImages.indexOf(imageName);

    if (index === -1) {
        // Image is not selected, add it to the array
        selectedImages.push(imageName);
    } else {
        // Image is already selected, remove it from the array
        selectedImages.splice(index, 1);
    }

    updateImageStyles();
}

// Function to update the styles of selected images
function updateImageStyles() {
    const imageCards = document.querySelectorAll('.img-card');

    imageCards.forEach((card) => {
        const imageName = card.querySelector('img').alt;

        if (selectedImages.includes(imageName)) {
            card.classList.add('selected');
        } else {
            card.classList.remove('selected');
        }
    });
}

// Function to add selected images to the cart
function addToCart() {
    // You can customize this function to handle adding items to the cart
    // For now, let's just log the selected images to the console
    console.log('Selected images:', selectedImages);
}
