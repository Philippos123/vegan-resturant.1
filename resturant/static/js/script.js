document.addEventListener('DOMContentLoaded', function() {
    const modal = new bootstrap.Modal(document.getElementById('bookingModal'));
    
    document.querySelectorAll('.booking-item').forEach(item => {
        item.addEventListener('click', function() {
            const date = this.getAttribute('data-date');
            const time = this.getAttribute('data-time');
            const people = this.getAttribute('data-people');

            const location = "Eskilstuna Kungsgatan 36";
            const title = `Table at Swedish dishes`;
            
            // Update modal content with booking details
            document.getElementById('modalDate').textContent = `Date: ${date}`;
            document.getElementById('modalTime').textContent = `Time: ${time}`;

            
            // Generate the Google Calendar link with dynamic values
            const startTime = `${date}T${time.replace(':', '')}00Z`;
            const endTime = `${date}T${time.replace(':', '')}00Z`;
            
            const googleCalendarLink = `https://calendar.google.com/calendar/render?action=TEMPLATE&dates=${startTime}%2F${endTime}&details=Your%20Booking%20Details&location=${encodeURIComponent(location)}&text=${title}`;
            
            // Set the href attribute of the Google Calendar button
            document.getElementById('googleCalendarLink').setAttribute('href', googleCalendarLink);

            // Show the modal
            modal.show();
        });
    });
});