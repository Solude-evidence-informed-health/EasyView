// Função para ajustar o estilo responsivo
function adjustHeaderStyle() {
    var productName = document.getElementById("product-name");
    var uploadButton = document.getElementById("upload-button");
    if (window.innerWidth <= 600) {
        productName.style.fontSize = "18px";
        uploadButton.style.fontSize = "14px";
    } else {
        productName.style.fontSize = "24px";
        uploadButton.style.fontSize = "16px";
    }
};

// Chamar a função ao carregar a página e ao redimensionar a janela
window.addEventListener("load", adjustHeaderStyle);
window.addEventListener("resize", adjustHeaderStyle);

document.addEventListener("DOMContentLoaded", function(event) {
            const currentLocation = window.location.pathname;
            console.log('currentLocation', currentLocation); // '/about
            const navItems = document.getElementsByName('nav-item');

            function highlightActiveLink() {
                console.log('number of navItems', navItems.length)
                for (let i = 0; i < navItems.length; i++) {
                    const item = navItems[i];
                    const href = item.getAttribute('href');
                    const isCurrentPage = href === currentLocation;

                    if (isCurrentPage) {
                        console.log('item', item)
                        item.classList.add("active");
                    } else {
                        item.classList.remove("active");
                    }
                }
            }

            highlightActiveLink();

            window.addEventListener('popstate', highlightActiveLink);
        });
