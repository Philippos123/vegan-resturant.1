document.addEventListener("DOMContentLoaded", function () {
    "use strict";

    const modalElement = document.getElementById("bookingModal");
    
    // Only initialize the modal if the element exists
    if (modalElement) {
        const modal = new bootstrap.Modal(modalElement);

        document.querySelectorAll(".booking-item").forEach(function (item) {
            item.addEventListener("click", function () {
                const date = item.getAttribute("data-date");
                const time = item.getAttribute("data-time");
                const people = item.getAttribute("data-people");

                const location = "Eskilstuna Kungsgatan 36";
                const title = "Table at Swedish dishes";

                const googleCalendarLink =
                    "https://calendar.google.com/calendar/render?action=TEMPLATE&dates=%2F" +
                    "&details=Your%20Booking%20Details&location=" +
                    encodeURIComponent(location) +
                    "&text=" + encodeURIComponent(title);

                // Set the href attribute of the Google Calendar button
                document.getElementById("googleCalendarLink").setAttribute("href", googleCalendarLink);

                // Show the modal
                modal.show();
            });
        });
    }
});