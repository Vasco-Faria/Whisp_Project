$.ajaxSetup({
    beforeSend: function beforeSend(xhr, settings) {
        function getCookie(name) {
            let cookieValue = null;


            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i += 1) {
                    const cookie = jQuery.trim(cookies[i]);

                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }

            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        }
    },
});
$(document).on("click", ".js-toggle-modal", function(e) {
    e.preventDefault()
    $(".js-modal").toggleClass("hidden")
})
.on("click", ".js-submit", function(e) {
    e.preventDefault()
    const text = $(".js-post-text").val().trim()
    const $btn = $(this)

    if(!text.length) {
        return false
    }

    $btn.prop("disabled", true).text("Posting!")
    $.ajax({
        type: 'POST',
        url: $(".js-post-text").data("post-url"),
        data: {
            text: text
        },
        success: (dataHtml) => {
            $(".js-modal").addClass("hidden");
            $("#posts-container").prepend(dataHtml);
            $btn.prop("disabled", false).text("New Post");
            location.reload();
            $(".js-post-text").val('')
        },
        error: (error) => {
            console.warn(error)
            $btn.prop("disabled", false).text("Error");
        }
    });
})
.on("click", ".js-follow", function(e) {
    e.preventDefault();
    const action = $(this).attr("data-action")

    $.ajax({
        type: 'POST',
        url: $(this).data("url"),
        data: {
            action: action,
            username: $(this).data("username"),
        },
        success: (data) => {
            $(".js-follow-text").text(data.wording)
            if(action == "follow") {
                
                console.log("DEBUG", "unfollow")
                $(this).attr("data-action", "unfollow")
            } else {
                
                console.log("DEBUG", "follow")
                $(this).attr("data-action", "follow")
            }
        },
        error: (error) => {
            console.warn(error)
        }
    });
})

const videos = document.querySelectorAll('.auto-play-video');

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.play(); 
        } else {
            entry.target.pause(); 
        }
    });
});

videos.forEach(video => {
    observer.observe(video);
});

$(document).ready(function() {
    $('#like-button').on('click', function(event) {
        event.preventDefault();
        var post_id = $(this).data('post-id');
        var url = '/like/' + post_id + '/';

        $.get(url, function(data) {
            var likeButton = $('#like-button');
            var likeText = $('#like-text');
            var likeCount = $('#like-count');

            if (data.liked) {
                likeText.text('Unlike');
                likeCount.text(data.like_count);
            } else {
                likeText.text('Like');
                likeCount.text(data.like_count);
            }
        });
    });
});