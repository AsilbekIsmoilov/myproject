document.addEventListener('DOMContentLoaded', () => {
  const commentItems = document.querySelectorAll('.comment-item');
  const audioPlayer = new Audio();
  let activeComment = null;

  const playPauseBtn = document.querySelector('.play-pause');
  const playPauseIcon = playPauseBtn.querySelector('img');

  const backwardBtn = document.querySelector('.backward');
  const forwardBtn = document.querySelector('.forward');
  const seekBar = document.querySelector('.seek-bar');
  const timeDisplay = document.querySelector('.time-display');
  const speedSelect = document.querySelector('.speed-select');
  const volumeRange = document.querySelector('.volume-range');

  let isSeeking = false;

  commentItems.forEach(item => {
    item.addEventListener('click', () => {
      const src = item.getAttribute('data-src');
      if (!src) return;

      audioPlayer.pause();
      audioPlayer.src = src;
      audioPlayer.load();
      audioPlayer.volume = volumeRange.value;
      audioPlayer.play();

      playPauseIcon.src = '/static/img/pause.png';
      playPauseIcon.alt = 'Pause';

      if (activeComment) activeComment.classList.remove('active');
      item.classList.add('active');
      activeComment = item;

      item.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
  });

  playPauseBtn.addEventListener('click', () => {
    if (audioPlayer.paused) {
      audioPlayer.play();
      playPauseIcon.src = '/static/img/pause.png';
      playPauseIcon.alt = 'Pause';
    } else {
      audioPlayer.pause();
      playPauseIcon.src = '/static/img/play.png';
      playPauseIcon.alt = 'Play';
    }
  });

  backwardBtn.addEventListener('click', () => {
    audioPlayer.currentTime = Math.max(0, audioPlayer.currentTime - 10);
  });

  forwardBtn.addEventListener('click', () => {
    audioPlayer.currentTime = Math.min(audioPlayer.duration, audioPlayer.currentTime + 10);
  });

  volumeRange.addEventListener('input', () => {
    audioPlayer.volume = volumeRange.value;
  });

  speedSelect.addEventListener('change', () => {
    audioPlayer.playbackRate = speedSelect.value;
  });

  audioPlayer.addEventListener('timeupdate', () => {
    if (!isSeeking) {
      seekBar.value = audioPlayer.currentTime;
      updateTimeDisplay();
    }
  });

  audioPlayer.addEventListener('loadedmetadata', () => {
    seekBar.max = audioPlayer.duration;
    updateTimeDisplay();
  });

  seekBar.addEventListener('input', () => {
    isSeeking = true;
  });

  seekBar.addEventListener('change', () => {
    audioPlayer.currentTime = seekBar.value;
    isSeeking = false;
  });

  audioPlayer.addEventListener('ended', () => {
    playPauseIcon.src = '/static/img/play.png';
    playPauseIcon.alt = 'Play';

    if (activeComment) {
      activeComment.classList.remove('active');
      activeComment = null;
    }
  });

  function updateTimeDisplay() {
    const format = t => {
      const m = Math.floor(t / 60).toString().padStart(2, '0');
      const s = Math.floor(t % 60).toString().padStart(2, '0');
      return `${m}:${s}`;
    };
    const current = format(audioPlayer.currentTime);
    const total = isNaN(audioPlayer.duration) ? '00:00' : format(audioPlayer.duration);
    timeDisplay.textContent = `${current} / ${total}`;
  }
});

document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".error-circle").forEach(el => {
    const value = parseInt(el.textContent.trim());
    const type = el.dataset.errorType;
    if (!isNaN(value) && value >= 1 && ["25", "10", "2"].includes(type)) {
      el.classList.add("red-bg");
    }
  });
});

window.addEventListener('DOMContentLoaded', () => {
  document.body.classList.add('page-loaded');
});
