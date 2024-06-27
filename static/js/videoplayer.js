document.addEventListener('DOMContentLoaded', function () {
    const video = document.getElementById('video');
    const playPauseButton = document.getElementById('playPause');
    const seekBar = document.getElementById('seekBar');
    const currentTimeDisplay = document.getElementById('currentTime');
    const durationDisplay = document.getElementById('duration');

    // Play/Pause the video
    playPauseButton.addEventListener('click', function () {
        if (video.paused) {
            video.play();
            playPauseButton.textContent = 'Pause';
        } else {
            video.pause();
            playPauseButton.textContent = 'Play';
        }
    });

    // Update seek bar and time displays
    video.addEventListener('timeupdate', function () {
        const value = (100 / video.duration) * video.currentTime;
        seekBar.value = value;
        
        const currentMinutes = Math.floor(video.currentTime / 60);
        const currentSeconds = Math.floor(video.currentTime % 60);
        const durationMinutes = Math.floor(video.duration / 60);
        const durationSeconds = Math.floor(video.duration % 60);

        currentTimeDisplay.textContent = `${currentMinutes}:${currentSeconds < 10 ? '0' + currentSeconds : currentSeconds}`;
        durationDisplay.textContent = `${durationMinutes}:${durationSeconds < 10 ? '0' + durationSeconds : durationSeconds}`;
    });

    // Seek video
    seekBar.addEventListener('input', function () {
        const time = video.duration * (seekBar.value / 100);
        video.currentTime = time;
    });

    // Update duration display when video metadata is loaded
    video.addEventListener('loadedmetadata', function () {
        const durationMinutes = Math.floor(video.duration / 60);
        const durationSeconds = Math.floor(video.duration % 60);

        durationDisplay.textContent = `${durationMinutes}:${durationSeconds < 10 ? '0' + durationSeconds : durationSeconds}`;
    });
});
