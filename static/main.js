const contentsButton = document.querySelector(".contents-button");
const contentsPanel = document.querySelector("#contentsPanel");

contentsButton.addEventListener("click", function () {
  const isOpen = contentsButton.getAttribute("aria-expanded") === "true";

  contentsButton.setAttribute("aria-expanded", String(!isOpen));
  contentsPanel.hidden = isOpen;
});

document.addEventListener("click", function (event) {
  if (!event.target.closest(".contents-menu")) {
    contentsPanel.hidden = true;
    contentsButton.setAttribute("aria-expanded", "false");
  }
});

document.addEventListener("keydown", function (event) {
  if (event.key === "Escape") {
    contentsPanel.hidden = true;
    contentsButton.setAttribute("aria-expanded", "false");
  }
});
// Play one feedback video with sound when it scrolls into view; pause it when it leaves.
const scrollVideos = document.querySelectorAll("video[data-scroll-autoplay]");

if (scrollVideos.length && "IntersectionObserver" in window) {
  const scrollVideoObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      const video = entry.target;

      if (entry.isIntersecting && entry.intersectionRatio >= 0.5) {
        scrollVideos.forEach((otherVideo) => {
          if (otherVideo !== video) otherVideo.pause();
        });
        video.muted = false;
        video.defaultMuted = false;
        video.play().catch(() => {});
      } else {
        video.pause();
      }
    });
  }, { threshold: [0, 0.5, 1] });

  scrollVideos.forEach((video) => scrollVideoObserver.observe(video));
}


// Turn the footer email field into an email update request to the ministry.
const subscribeForm = document.querySelector("#subscribeForm");

if (subscribeForm) {
  subscribeForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const email = document.querySelector("#subscriberEmail").value.trim();
    const subject = encodeURIComponent("Wings for Christ email updates");
    const body = encodeURIComponent(`Please add this address to the Wings for Christ email updates: ${email}`);
    window.location.href = `mailto:stevesrobinson98@gmail.com?subject=${subject}&body=${body}`;
  });
}

