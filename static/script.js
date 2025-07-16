 // side bar
 const sidebar = document.getElementById("sidebar");
  const hamburger = document.querySelector(".hamburger");

  function toggleSidebar() {
    sidebar.classList.toggle("show");
  }

  document.addEventListener("click", function (event) {
    const isClickInsideSidebar = sidebar.contains(event.target);
    const isClickOnHamburger = hamburger.contains(event.target);

    if (!isClickInsideSidebar && !isClickOnHamburger && sidebar.classList.contains("show")) {
      sidebar.classList.remove("show");
    }
  });

  function closeSidebarOnScroll() {
    if (sidebar.classList.contains("show")) {
      sidebar.classList.remove("show");
    }
  }

  window.addEventListener("scroll", closeSidebarOnScroll);
  window.addEventListener("touchmove", closeSidebarOnScroll);  // for finger scroll
  window.addEventListener("wheel", closeSidebarOnScroll);      // for mouse scroll

// video player