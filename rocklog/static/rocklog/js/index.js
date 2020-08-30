// Globals required for YouTube API
var player
var done = false

var PROTOCOL = `${window.location.protocol}//`

function makeNewPlayer(id) {
  player = new YT.Player('player', {
    height: '390',
    width: '640',
    videoId: id,
    events: {
      'onReady': onPlayerReady
    }
  })
}

function onPlayerReady(event) {
  event.target.playVideo()
}

function stopVideo() {
  player.stopVideo()
}

function toggleStarYellow(icon) {
  icon.hasClass('stared') ? icon.removeClass('stared') : icon.addClass('stared')
}

function isRowBeingClosed(elem) {
  return elem.hasClass("active")
}

function appendPlayerToRowBody(rowBody) {
  rowBody.find(".video-container").append($("#player"))
}

function pauseVideo(player) {
  try {
    player.pauseVideo()
  } catch (e) {}
}

function destroyPreviousPlayer(player) {
  try {
    player.destroy()
  } catch (e) {}
}

function fetchVideoAndAppend(rowBody, player, artist, song) {
  $.ajax({
    url: encodeURI(PROTOCOL + window.location.host + "/videoid/" + artist + "/" + song),
    success: function(id) {
      appendPlayerToRowBody(rowBody)
      destroyPreviousPlayer(player)
      makeNewPlayer(id)
    }
  })
}

function saveSongRequest(songId, icon) {
  $.ajax({
    url: encodeURI(PROTOCOL + window.location.host + "/toggle_save/" + songId),
    success: function(data) {
      toggleStarYellow(icon)
    }
  })
}

(function ($) {

  // On document ready
  $(function () {
    var documentRoot = $("#document_root").attr("content")
    var rows = $(".collapsible-header")
    var stars = $(".star-icon")

    rows.click(function(e) {
      var rowElem = $(this)
      var song = rowElem.find(".song").html()
      var artist = rowElem.find(".artist").html()
      var rowBody = rowElem.next()

      if (isRowBeingClosed(rowElem)) {
        pauseVideo(player)
      } else {
        fetchVideoAndAppend(rowBody, player, artist, song)
      }
    })

    stars.click(function(e) {
      e.stopPropagation()

      var icon = $(this)
      var songId = $(this).parent().attr("id")

      saveSongRequest(songId, icon)
    })

    // For the collections
    $('.collapsible').collapsible({
      accordion: false
    })

    $('.parallax').parallax()
  })

})(jQuery)
